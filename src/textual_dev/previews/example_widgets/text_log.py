from rich.syntax import Syntax
from textual.widgets import TextLog

CODE = '''\
def loop_first_last(values: Iterable[T]) -> Iterable[tuple[bool, bool, T]]:
    """Iterate and generate a tuple with a flag for first and last value."""
    iter_values = iter(values)
    try:
        previous_value = next(iter_values)
    except StopIteration:
        return
    first = True
    for value in iter_values:
        yield first, False, previous_value
        first = False
        previous_value = value
    yield first, True, previous_value\
'''


def text_log_example(id: str):
    log = TextLog(highlight=True, markup=True, id=id)
    log.write(Syntax(CODE, "python", indent_guides=True))
    yield log
