from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widgets import Button, ContentSwitcher

from textual_dev.previews.example_widgets import (
    option_list_example,
    button_example,
    checkbox_example,
    list_item_example,
    data_table_example,
    markdown_viewer_example,
    placeholder_example,
    pretty_example,
    directory_tree_example,
    footer_example,
    header_example,
    input_example,
    label_example,
    loading_example,
    markdown_example,
    radio_button_example,
    radio_set_example,
    select_example,
    selection_list_example,
    sparkline_example,
    static_example,
    switch_example,
    tree_example,
    content_switcher_example,
    progress_bar_example,
    tabbed_content_example,
    tabs_example,
    # text_log_example,
)

WIDGETS = {
    "Button": button_example,
    # "Checkbox": checkbox_example,
    # "ContentSwitcher": content_switcher_example,
    # "DataTable": data_table_example,
    # "DirectoryTree": directory_tree_example,
    # "Footer": footer_example,
    # "Header": header_example,
    # "Input": input_example,
    # "Label": label_example,
    # "ListItem": list_item_example,
    # # ListView missing
    # "Loading": loading_example,
    # "MarkdownViewer": markdown_viewer_example,
    # "Markdown": markdown_example,
    # "OptionList": option_list_example,
    # "Placeholder": placeholder_example,
    # "Pretty": pretty_example,
    # "ProgressBar": progress_bar_example,
    # "RadioButton": radio_button_example,
    # "RadioSet": radio_set_example,
    # "Select": select_example,
    # "SelectionList": selection_list_example,
    # "Sparkline": sparkline_example,
    # "Static": static_example,
    # "Switch": switch_example,
    # "TabbedContent": tabbed_content_example,
    # "Tabs": tabs_example,
    # "Tree": tree_example,
}


class WidgetButtons(Vertical):
    DEFAULT_CSS = """
    WidgetButtons {
        dock: left;
        width: 32;
        overflow-y: scroll;
    }

    WidgetButtons > Button {
        width: 100%;
    }
    """

    def compose(self) -> ComposeResult:
        for widget in WIDGETS.keys():
            yield Button(widget, id=widget)


class WidgetsApp(App[None]):
    """Demonstrates widget types."""

    CSS_PATH = "widgets.css"

    def compose(self) -> ComposeResult:
        yield WidgetButtons()

        first_button = list(WIDGETS.keys())[0]

        with ContentSwitcher(initial=first_button, id="main-switcher"):
            for widget_name, widget in WIDGETS.items():
                yield from widget(id=widget_name)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        widget_selection_button = event.button.id in WIDGETS.keys()

        selector = (
            "#main-switcher" if widget_selection_button else "#content-switcher-example"
        )
        self.query_one(selector).current = event.button.id


if __name__ == "__main__":
    WidgetsApp().run()
