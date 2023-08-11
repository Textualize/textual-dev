from textual.app import ComposeResult
from textual.containers import Horizontal, Container
from textual.widgets import Switch, Static


def switch_example(id: str) -> ComposeResult:
    focused_switch = Switch()
    focused_switch.focus()

    yield Container(
        Static("[b]Example switches\n", classes="label"),
        Horizontal(
            Static("off:     ", classes="label"),
            Switch(animate=False),
            classes="container",
        ),
        Horizontal(
            Static("on:      ", classes="label"),
            Switch(value=True),
            classes="container",
        ),
        Horizontal(
            Static("focused: ", classes="label"), focused_switch, classes="container"
        ),
        Horizontal(
            Static("custom:  ", classes="label"),
            Switch(id="custom-design"),
            classes="container",
        ),
        id=id,
    )
