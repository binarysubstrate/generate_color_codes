# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import, print_function, unicode_literals)

import unittest

from color_codes import ColorCodes, Values


class TestCodeGeneration(unittest.TestCase):
    def test_get_code_pass(self):
        bright_green = ColorCodes(
                Values.Color.green,
                Values.Target.foreground,
                Values.Intensity.bright,
                underline=False, bold=False
        )
        self.assertEqual(bright_green.get_code(), '\x1b[92m')
        return None

    def test_bold_pass(self):
        bright_green_bold = ColorCodes(
                Values.Color.green,
                Values.Target.foreground,
                Values.Intensity.bright,
                underline=False, bold=True
        )
        self.assertEqual(
                bright_green_bold.code,
                '\x1b[92;1m'.__repr__()
        )
        return None

    def test_underline_pass(self):
        bright_green_underline = ColorCodes(
                Values.Color.green,
                Values.Target.foreground,
                Values.Intensity.bright,
                underline=True, bold=False
        )
        self.assertEqual(
                bright_green_underline.code,
                '\x1b[92;4m'.__repr__()
        )
        return None


if __name__ == '__main__':
    unittest.main()
