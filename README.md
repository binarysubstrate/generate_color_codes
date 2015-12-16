## What it is
generate_color_codes provides a class that is instantiated with color
and formatting preferences. The resulting instance methods and attributes
can be used to modify terminal formatting or referenced directly.

Although the ColorCodes class is easily implemented, it also
serves as a demo for the assembly of a ANSI escape sequences.

## Dependencies
Both Python 2.7 and Python 3.x are supported. There are no dependencies.


#### Platform Support
ANSI escape sequences aren't supported by Windows, but may work
on Windows with application terminals such as with PyCharm.

#### Windows Alternatives
* [colorama](https://github.com/tartley/colorama) is a good cross-platform package for producing terminal color.
* [ansicon](https://github.com/adoxa/ansicon) provides ANSI escape sequences for Windows console programs.


## Examples
Create a ColorCodes instance:

```python
from color_codes import ColorCodes, Values

bright_green = ColorCodes(
        Values.Color.green,
        Values.Target.foreground,
        Values.Intensity.bright,
        underline=False, bold=False)
```

Use the ColorCodes get_code() method to change the
color of console text:

```python
from color_codes import ColorCodes, Values

print(
        "{}This text is green. "
        "{}And the color on this text has been reset.".format(
            bright_green.get_code(),
            bright_green.reset_code
        )
)
```

Use the `code` property to print the generated escape sequence:

```python
print(bright_green.code)
```

Note that escape sequence can be used directly. You may wish to
simply generate sequence(s) manually and use that code directly:

```python
print("{}This text is also green.".format('\x1b[92m'))
```
