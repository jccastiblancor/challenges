# Albern Coordinates - Hard

## Summary
Albern mapping is a way of turning a two-word phrase into a coordinate pair & size. The first word determines the x position & width, while the second word determines the y position and height.

A word can be mapped to a coordinate position by summing the products of each letter's position in the alphabet and its position in the word.

Sizes are much simpler - simply take the length of the word.

For example, to find the Albern Coordinates of the phase "*long cat*":
```
//  L          O          N          G
x = (1 * 12) + (2 * 15) + (3 * 14) + (4 * 7)
  = 112

width = 4

//  C         A         T
y = (1 * 3) + (2 * 1) + (3 * 20)
  = 65

height = 3
```

## Problem

Find the longest chain of Albern coordinates in `input.html`, and enter the contents of the last element in this chain.
