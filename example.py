# -*- coding: utf-8 -*-
"""color_code module examples"""
from color_codes import ColorCodes, Values


def main():
    """"Create a ColorCode object and use with print()."""
    bright_green = ColorCodes(
            Values.Color.green,
            Values.Target.foreground,
            Values.Intensity.bright,
            underline=False, bold=False
    )

    print(
            "{}This text is green. "
            "{}And the color on this text has been reset.".format(
                bright_green.get_code(),
                bright_green.reset_code
            )
    )
    print("")
    print("The escape sequence used to change "
          "the text color is: {}".format(bright_green.code))
    return None


if __name__ == '__main__':
    main()
