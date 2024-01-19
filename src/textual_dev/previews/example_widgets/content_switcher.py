from textual.app import ComposeResult
from textual.containers import VerticalScroll, Container, Horizontal
from textual.widgets import Button, ContentSwitcher, DataTable, Markdown

MARKDOWN_EXAMPLE = """# Three Flavours Cornetto

The Three Flavours Cornetto trilogy is an anthology series of British
comedic genre films directed by Edgar Wright.

## Shaun of the Dead

| Flavour | UK Release Date | Director |
| -- | -- | -- |
| Strawberry | 2004-04-09 | Edgar Wright |

## Hot Fuzz

| Flavour | UK Release Date | Director |
| -- | -- | -- |
| Classico | 2007-02-17 | Edgar Wright |

## The World's End

| Flavour | UK Release Date | Director |
| -- | -- | -- |
| Mint | 2013-07-19 | Edgar Wright |
"""


def content_switcher_example(id: str) -> ComposeResult:
    table: DataTable = DataTable(id="data-table")
    table.add_columns("Book", "Year")
    table.add_rows(
        [
            (title.ljust(35), year)
            for title, year in (
                ("Dune", 1965),
                ("Dune Messiah", 1969),
                ("Children of Dune", 1976),
                ("God Emperor of Dune", 1981),
                ("Heretics of Dune", 1984),
                ("Chapterhouse: Dune", 1985),
            )
        ]
    )

    yield Container(
        Horizontal(
            Button("DataTable", id="data-table"),
            Button("Markdown", id="markdown"),
            id="buttons",
        ),
        ContentSwitcher(
            table,
            VerticalScroll(Markdown(MARKDOWN_EXAMPLE), id="markdown"),
            initial="data-table",
            id="content-switcher-example",
        ),
        id=id,
    )
