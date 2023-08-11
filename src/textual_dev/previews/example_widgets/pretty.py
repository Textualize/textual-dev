from textual.containers import Container
from textual.app import ComposeResult
from textual.widgets import Pretty

DATA = {
    "title": "Back to the Future",
    "releaseYear": 1985,
    "director": "Robert Zemeckis",
    "genre": "Adventure, Comedy, Sci-Fi",
    "cast": [
        {"actor": "Michael J. Fox", "character": "Marty McFly"},
        {"actor": "Christopher Lloyd", "character": "Dr. Emmett Brown"},
    ],
}


def pretty_example(id: str) -> ComposeResult:
    yield Container(Pretty(DATA), id=id)
