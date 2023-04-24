from typing import Union

from toga_gtk.libs import Gtk, Pango

from .base import SimpleProbe


class FontProbe(SimpleProbe):
    """Probe to verify attributes of the GTK font backend.
    Uses a label widget to hold the font being tested.
    """

    native_class = Gtk.Label

    @property
    def _native_font(self) -> Pango.FontDescription:
        """Convenience property to get the native font object from GTK for use by other properties"""
        sc = self.native.get_style_context()
        return sc.get_property("font", sc.get_state())

    @property
    def family(self) -> Union[str, None]:
        """
        :return: The font family name, or None if not previously set
        """
        return self._native_font.get_family()

    @property
    def size(self) -> int:
        """Retrieves the size of the font and converts it to points if necessary

        :return: The size of the font in points
        """
        font_size = self._native_font.get_size()
        is_points = not self._native_font.get_size_is_absolute()
        return font_size if is_points else int(font_size / Pango.SCALE)

    @property
    def weight(self) -> Pango.Weight:
        return self._native_font.get_weight()

    @property
    def style(self) -> Pango.Style:
        return self._native_font.get_style()
