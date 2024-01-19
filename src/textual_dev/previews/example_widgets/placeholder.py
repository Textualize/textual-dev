from textual.app import ComposeResult
from textual.containers import Container, Horizontal, VerticalScroll
from textual.widgets import Placeholder


def placeholder_example(id: str) -> ComposeResult:
    yield Container(
        VerticalScroll(
            Container(
                Placeholder("This is a custom label for p1.", id="p1"),
                Placeholder("Placeholder p2 here!", id="p2"),
                Placeholder(id="p3"),
                Placeholder(id="p4"),
                Placeholder(id="p5"),
                Placeholder(),
                Horizontal(
                    Placeholder(variant="size", id="col1"),
                    Placeholder(variant="text", id="col2"),
                    Placeholder(variant="size", id="col3"),
                    id="c1",
                ),
                id="bot",
            ),
            Container(
                Placeholder(variant="text", id="left"),
                Placeholder(variant="size", id="topright"),
                Placeholder(variant="text", id="botright"),
                id="top",
            ),
            id="content",
        ),
        id=id,
    )
