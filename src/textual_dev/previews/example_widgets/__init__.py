import random
from statistics import mean

from textual.app import ComposeResult
from textual.containers import Container, Center, Middle
from textual.widgets import (
    DirectoryTree,
    Footer,
    Header,
    Input,
    Label,
    ListView,
    ListItem,
    LoadingIndicator,
    Sparkline,
    Static,
    Tree,
    ProgressBar,
    TabbedContent,
    TabPane,
    Markdown,
    Tabs,
)

from .button import button_example
from .checkbox import checkbox_example
from .content_switcher import content_switcher_example
from .data_table import data_table_example
from .markdown import markdown_viewer_example, markdown_example
from .option_list import option_list_example
from .placeholder import placeholder_example
from .pretty import pretty_example
from .radio import radio_button_example, radio_set_example
from .select import select_example, selection_list_example
from .switch import switch_example

# from .text_log import text_log_example


def directory_tree_example(id: str) -> ComposeResult:
    yield Container(DirectoryTree("./"), id=id)


def footer_example(id: str) -> ComposeResult:
    yield Container(Footer(), id=id)


def header_example(id: str) -> ComposeResult:
    yield Container(Header(), id=id)


def input_example(id: str) -> ComposeResult:
    yield Container(
        Input(placeholder="First Name"), Input(placeholder="Last Name"), id=id
    )


def label_example(id: str) -> ComposeResult:
    yield Container(Label("Hello, world!"), id=id)


def list_item_example(id: str) -> ComposeResult:
    yield Container(
        ListView(
            ListItem(Label("One")),
            ListItem(Label("Two")),
            ListItem(Label("Three")),
        ),
        id=id,
    )

    yield Footer()


def loading_example(id: str) -> ComposeResult:
    yield Container(LoadingIndicator(), id=id)


def sparkline_example(id: str) -> ComposeResult:
    data = [random.expovariate(1 / 3) for _ in range(1000)]

    yield Container(
        Sparkline(data, summary_function=max),
        Sparkline(data, summary_function=mean),
        Sparkline(data, summary_function=min),
        id=id,
    )


def static_example(id: str) -> ComposeResult:
    yield Container(Static("Hello, world!"), id=id)


def tree_example(id: str) -> ComposeResult:
    tree: Tree[dict] = Tree("Dune")
    tree.root.expand()
    characters = tree.root.add("Characters", expand=True)
    characters.add_leaf("Paul")
    characters.add_leaf("Jessica")
    characters.add_leaf("Chani")
    yield Container(tree, id=id)


def progress_bar_example(id: str) -> ComposeResult:
    bar = ProgressBar(total=100, show_eta=False)
    bar.advance(50)
    yield Container(Center(Middle(bar)), id=id)


def tabbed_content_example(id: str):
    content = TabbedContent()
    content._tab_content = [
        TabPane("Leto", Markdown("# Leto"), id="leto"),
        TabPane("Jessica", Markdown("# Jessica"), id="jessica"),
        TabPane("Paul", Markdown("# Paul"), id="paulo"),
    ]
    # This does not work, reason why I used _tab_content above
    # content.add_pane(TabPane("Leto", Markdown("#Leto"), id="letoo"))
    # content.add_pane(TabPane("Jessica", Markdown(""), id="jessicoa"))
    # content.add_pane(TabPane("Paul", Markdown(""), id="paulo"))

    yield Container(content, id=id)


def tabs_example(id: str):
    yield Container(Tabs("First tab", "Second tab", "Third tab"), id=id)


__all__ = [
    "button_example",
    "checkbox_example",
    "content_switcher_example",
    "data_table_example",
    "directory_tree_example",
    "footer_example",
    "header_example",
    "input_example",
    "label_example",
    "list_item_example",
    "loading_example",
    "markdown_viewer_example",
    "markdown_example",
    "option_list_example",
    "placeholder_example",
    "pretty_example",
    "progress_bar_example",
    "radio_button_example",
    "radio_set_example",
    "select_example",
    "selection_list_example",
    "sparkline_example",
    "static_example",
    "switch_example",
    "tabbed_content_example",
    "tabs_example",
    "tree_example",
    # "text_log_example",
]
