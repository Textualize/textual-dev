from textual.app import ComposeResult
from textual.containers import Container, Horizontal
from textual.widgets import RadioSet, RadioButton


def radio_button_example(id: str) -> ComposeResult:
    yield Container(
        RadioSet(
            RadioButton("Battlestar Galactica"),
            RadioButton("Dune 1984"),
            RadioButton("Dune 2021", id="focus_me"),
            RadioButton("Serenity", value=True),
            RadioButton("Star Trek: The Motion Picture"),
            RadioButton("Star Wars: A New Hope"),
            RadioButton("The Last Starfighter"),
            RadioButton("Total Recall :backhand_index_pointing_right: :red_circle:"),
            RadioButton("Wing Commander"),
        ),
        id=id,
    )


def radio_set_example(id: str) -> ComposeResult:
    yield Container(
        Horizontal(
            RadioSet(
                RadioButton("Battlestar Galactica"),
                RadioButton("Dune 1984"),
                RadioButton("Dune 2021"),
                RadioButton("Serenity", value=True),
                RadioButton("Star Trek: The Motion Picture"),
                RadioButton("Star Wars: A New Hope"),
                RadioButton("The Last Starfighter"),
                RadioButton(
                    "Total Recall :backhand_index_pointing_right: :red_circle:"
                ),
                RadioButton("Wing Commander"),
                id="focus_me",
            )
        ),
        Horizontal(
            RadioSet(
                "Amanda",
                "Connor MacLeod",
                "Duncan MacLeod",
                "Heather MacLeod",
                "Joe Dawson",
                "Kurgan, [bold italic red]The[/]",
                "Methos",
                "Rachel Ellenstein",
                "Ramírez",
            )
        ),
        id=id,
    )
