import asyncio
from typing import Callable

import pytest


async def wait_for_predicate(
    predicate: Callable[[], bool],
    timeout_secs: float = 2,
    poll_delay_secs: float = 0.001,
) -> None:
    """Wait for the given predicate to become True by evaluating it every `poll_delay_secs`
    seconds. Fail the pytest test if the predicate does not become True after `timeout_secs`
    seconds.

    Args:
        predicate (Callable[[], bool]): The predicate function which will be called repeatedly.
        timeout_secs (float): If the predicate doesn't evaluate to True after this number of
            seconds, the test will fail.
        poll_delay_secs (float): The number of seconds to wait between each call to the
            predicate function.
    """
    time_taken = 0.0
    while True:
        result = predicate()
        if result:
            return
        await asyncio.sleep(poll_delay_secs)
        time_taken += poll_delay_secs
        if time_taken > timeout_secs:
            pytest.fail(
                f"Predicate {predicate} did not return True after {timeout_secs} seconds."
            )
