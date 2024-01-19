from textual.app import ComposeResult
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import Static, Button


def button_example(id: str) -> ComposeResult:
    yield Horizontal(
        VerticalScroll(
            Static("Standard Buttons", classes="header"),
            Button("Default"),
            Button("Primary!", variant="primary"),
            Button.success("Success!"),
            Button.warning("Warning!"),
            Button.error("Error!"),
        ),
        VerticalScroll(
            Static("Disabled Buttons", classes="header"),
            Button("Default", disabled=True),
            Button("Primary!", variant="primary", disabled=True),
            Button.success("Success!", disabled=True),
            Button.warning("Warning!", disabled=True),
            Button.error("Error!", disabled=True),
        ),
        id=id,
    )
