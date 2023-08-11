from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Select, Header, Footer, SelectionList

LINES = """I must not fear.
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.""".splitlines()


def select_example(id: str) -> ComposeResult:
    content = Select((line, line) for line in LINES)
    yield Container(Header(), content, id=id)


def selection_list_example(id: str) -> ComposeResult:
    yield Container(
        Header(),
        SelectionList[int](
            ("Falken's Maze", 0, True),
            ("Black Jack", 1),
            ("Gin Rummy", 2),
            ("Hearts", 3),
            ("Bridge", 4),
            ("Checkers", 5),
            ("Chess", 6, True),
            ("Poker", 7),
            ("Fighter Combat", 8, True),
        ),
        Footer(),
        id=id,
    )
