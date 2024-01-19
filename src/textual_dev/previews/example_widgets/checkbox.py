from textual.app import ComposeResult
from textual.containers import VerticalScroll, Container
from textual.widgets import Checkbox


def checkbox_example(id: str) -> ComposeResult:
    yield Container(
        VerticalScroll(
            Checkbox("Arrakis :sweat:"),
            Checkbox("Caladan"),
            Checkbox("Chusuk"),
            Checkbox("[b]Giedi Prime[/b]"),
            Checkbox("[magenta]Ginaz[/]"),
            Checkbox("Grumman", True),
            Checkbox("Kaitain", id="initial_focus"),
            Checkbox("Novebruns", True),
        ),
        id=id,
    )
