# SPDX-License-Identifier: CC0-1.0

@micropython.viper
def byteswap(data: ptr8, length: int):
 i = 0
 while i < length:
  temp = data[i]
  data[i] = data[i + 1]
  data[i + 1] = temp
  i += 2