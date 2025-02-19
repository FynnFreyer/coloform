# Coloform

Similar to [`colorama` by Jonathan Hartley](https://github.com/tartley/colorama/) this project aims to provide a simple interface for coloring terminal output, contrary to `colorama` it doesn't try to provide support for Windows.
If you need Windows support, or run this on something other than a mainstream terminal emulator, this is probably not for you.

## Concept

Usage is very similar to `colorama`, you have objects for foreground, background, styles and cursor.
These are prefixed with `Rich`, to differentiate them from the `colorama` objects (if for some reason you have to, like me, have both packages available).

Coloramas `Cursor` is unchanged and available for convenience.

```python
from coloform import Fore, Back, Style

print(f'Look ma, {Style.UNDERLINE}more styles{Style.RESET_UNDERLINE}, than we ever {Style.STRIKE_OUT}wanted{Style.RESET_STRIKE_OUT} {Style.BLINK}needed{Style.RESET_BLINK}!')
print(f'Also, {Fore.HEX_1234FF}hex and rgb colors for fore-{Fore.RESET} and {Back.RGB_255_20_255}background{Back.RESET}')
print(f'Common {Fore.RED}aliases {Back.GREEN}just {Fore.RESET}work!{Style.RESET_ALL}')
```

Features loads of useless aliases (`Style.UNDERLINE == Style.UNDERLINED` etc.).

## Why

Because it's not the 90s anymore, and screw compatibility.
Also, I like to see bad UI design in terminals, and this is my contribution towards that.

## Thanks

Thanks to Sascha Peilicke for his documentation work around ANSI escape codes.

