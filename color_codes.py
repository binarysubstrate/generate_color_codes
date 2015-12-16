# -*- coding: utf-8 -*-
"""Terminal formatting with ANSI escape sequences.

    On terminals that support ANSI escape sequences, generate codes to color
    and format output.

    The ColorCodes class provides an instance method get_code() for
    using directly within code. It also makes the sequence
    available for reference as an instance property
    called "code." See examples below.

    Values is a helper class to allow ColorCodes to be easily instantiated
    without having to use reference information. However, the
    Values class is not required. ColorCodes parameters may be
    entered as integers and booleans.

    ANSI escape sequences aren't supported by Windows, but may work
    on Windows with terminals included with applications such
    as PyCharm. Alternatives include:

        colorama is a good cross-platform package for
        producing terminal color.
        https://github.com/tartley/colorama

        ansicon  provides ANSI escape sequences for Windows  console
        programs. However, this is only useful on a  per-user basis,
        as opposed to being a solution for one's Windows users.
        https://github.com/adoxa/ansicon

    Examples:
        Create a ColorCodes instance:

            bright_green = ColorCodes(
                    Values.Color.green,
                    Values.Target.foreground,
                    Values.Intensity.bright,
                    underline=False, bold=False)

        Use the ColorCodes get_code() method to change the
        color of console text:

            print("{}This text is green.{} And this color "
                  "has been reset.".format(
                       bright_green.get_code(),
                       bright_green.reset_code))

        Use the "code" property to print the generated escape sequence:
            print(bright_green.code)

        The escape sequence can be used directly:
            print("{}This is also green text.".format('\x1b[92m'))

    References:
        https://en.wikipedia.org/wiki/ANSI_escape_code
        http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-048.pdf

"""
from __future__ import (absolute_import, print_function, unicode_literals)


class Values(object):
    """Map ANSI values to readable names."""

    class Color(object):
        """ANSI color table."""
        black = 0
        red = 1
        green = 2
        yellow = 3
        blue = 4
        magenta = 5
        cyan = 6
        white = 7

    class Target(object):
        """Background colors values are 10 more than foreground values."""
        foreground = 0
        background = 10

    class Intensity(object):
        """Normal color values begin at 30. Bright values begin at 90."""
        normal = 30
        bright = 90


class ColorCodes(object):
    """Terminal formatting with ANSI escape sequences.

    Instance Attributes:
        code: The escape sequence for the ColorCode instance
            for reference or "manual" use.

    Class Attributes:
        csi: The Control Sequence Initiator. The CSI begins with an escape
            character, "ESC," represented as ASCII decimal 27, hex 0x1B,
            or octal 033. This is followed by '[' for sequences of
            more than two characters.

        reset_code: The reset/normal escape sequence.

    """
    _escape = '\033'
    csi = _escape + '['
    _sgr_final_byte = 'm'
    reset_code = csi + '0' + _sgr_final_byte

    def __init__(self, color, target, intensity, underline=False, bold=False):
        """Object initialization

        Note that the Values class may be used when instantiating
        a ColorCodes object, instead of using literal integers and booleans.

        Args:
            color (int): Value from the ANSI color table.
            target (int): SGR code indicating either foreground or background.
            intensity (int): SGR code indicating normal or bright intensity.
            underline (bool): Include the SGR code for underline if True.
            bold (bool): Include the SRG code for bold if True.

        """
        self.color = color
        self.target = target
        self.intensity = intensity
        self.underline = underline
        self.bold = bold
        self.color_code = None
        self.sgr_code = ''

        self._initialize_instance()

    def _initialize_instance(self):
        """Orchestrator for escape sequence."""
        self._generate_color_value()
        self._generate_sgr_code()
        self._calculate_effects()
        self._add_final_byte()
        self.code = self.sgr_code.__repr__()
        return None

    def _generate_color_value(self):
        """The initial value is the sum of color, target, and intensity."""
        self.color_code = str(self.color + self.target + self.intensity)
        return None

    def _generate_sgr_code(self):
        """Generate initial SGR (Select Graphic Rendition) value."""
        # The SGR begins with a CSI (Control Sequence Initiator),
        # followed by the value generated for color,
        # target (foreground/background), and brightness.
        self.sgr_code += ColorCodes.csi
        self.sgr_code += self.color_code
        return None

    def _calculate_effects(self):
        """Add values to the SGR code for underline and bold if present."""
        if self.underline:
            self.sgr_code = "{0};{1}".format(
                    self.sgr_code,
                    str(4)
            )

        if self.bold:
            self.sgr_code = "{0};{1}".format(
                    self.sgr_code,
                    str(1)
            )
        return None

    def _add_final_byte(self):
        """Escape codes end with a final byte."""
        self.sgr_code += ColorCodes._sgr_final_byte
        return None

    def get_code(self):
        """Return the generated escape sequence. This value can
        be used directly in print() statements."""
        return self.sgr_code
