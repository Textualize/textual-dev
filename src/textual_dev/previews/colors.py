from textual._color_constants import COLOR_NAME_TO_RGB
from textual.app import App, ComposeResult
from textual.color import Color
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.design import ColorSystem
from textual.widget import Widget
from textual.widgets import Button, Footer, Label, Static, TabbedContent

try:
    from textual.lazy import Lazy
except ImportError:

    def Lazy(widget: Widget) -> Widget:  # type: ignore
        return widget


class ThemeColorButtons(VerticalScroll):
    def compose(self) -> ComposeResult:
        for color_name in ColorSystem.COLOR_NAMES:
            yield Button(color_name, id=color_name)


class ColorBar(Static):
    pass


class ColorItem(Horizontal):
    pass


class ColorGroup(Vertical):
    pass


class Content(Vertical):
    pass


class ColorsView(VerticalScroll):
    pass


class ColorTabs(TabbedContent):
    pass


class NamedColorsView(ColorsView):
    def compose(self) -> ComposeResult:
        with ColorGroup(id=f"group-named"):
            for name, rgb in COLOR_NAME_TO_RGB.items():
                color = Color(*rgb)
                with ColorItem() as ci:
                    ci.styles.background = name
                    yield ColorBar(name, classes="text")
                    yield ColorBar(f"{color.hex6}", classes="text")
                    yield ColorBar(f"{color.rgb}", classes="text text-left")


class ThemeColorsView(ColorsView):
    def compose(self) -> ComposeResult:
        LEVELS = [
            "darken-3",
            "darken-2",
            "darken-1",
            "",
            "lighten-1",
            "lighten-2",
            "lighten-3",
        ]

        for color_name in ColorSystem.COLOR_NAMES:
            with ColorGroup(id=f"group-{color_name}"):
                yield Label(f'"{color_name}"')
                for level in LEVELS:
                    color = f"{color_name}-{level}" if level else color_name
                    with ColorItem(classes=color):
                        yield ColorBar(f"${color}", classes="text label")
                        yield ColorBar("$text-muted", classes="muted")
                        yield ColorBar("$text-disabled", classes="disabled")


class ColorsApp(App[None]):
    CSS_PATH = "colors.css"

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Footer()
        with ColorTabs("Theme Colors", "Named Colors"):
            yield Content(ThemeColorButtons(), ThemeColorsView(), id="theme")
            yield Lazy(NamedColorsView())

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query(ColorGroup).remove_class("-active")
        group = self.query_one(f"#group-{event.button.id}", ColorGroup)
        group.add_class("-active")
        group.scroll_visible(top=True, speed=150)


if __name__ == "__main__":
    ColorsApp().run()
