# ByteSwap MicroPython Utility Module

A MicroPython `viper` utility module to swap two bytes in a `bytearray`. Designed for use with RGB565 displays that have byte order issues.

## Usage Example

```python
from byteswap import byteswap

data = bytearray(b'\xF8\x00\xAA\xBB')
print(data)  # b'\xF8\x00\xAA\xBB'
byteswap(data, len(data))
print(data)  # b'\x00\xF8\xBB\xAA'
```

## License

This project is provided under the [Public Domain License](https://spdx.org/licenses/CC0-1.0.html). Feel free to use, modify, and distribute it according to the terms of the license.