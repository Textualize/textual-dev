from textual.containers import Container
from textual.app import ComposeResult
from textual.widgets import Footer, Header, OptionList
from textual.widgets.option_list import Option, Separator


def option_list_example(id: str) -> ComposeResult:
    yield Container(
        Header(),
        OptionList(
            Option("Aerilon", id="aer"),
            Option("Aquaria", id="aqu"),
            Separator(),
            Option("Canceron", id="can"),
            Option("Caprica", id="cap", disabled=True),
            Separator(),
            Option("Gemenon", id="gem"),
            Separator(),
            Option("Leonis", id="leo"),
            Option("Libran", id="lib"),
            Separator(),
            Option("Picon", id="pic"),
            Separator(),
            Option("Sagittaron", id="sag"),
            Option("Scorpia", id="sco"),
            Separator(),
            Option("Tauron", id="tau"),
            Separator(),
            Option("Virgon", id="vir"),
        ),
        Footer(),
        id=id,
    )
