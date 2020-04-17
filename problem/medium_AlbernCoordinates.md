# Albern Coordinates - Medium

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

Find the element in `input.html` whose coordinates & size match the Albern Coordinates of the phrase "*variable chinchilla*".

Then find the element whose coordinates & size match the Albern Coordinates of the phrase contained in that first element.

Repeat this until you are unable to find the next element in the chain. What is the contents of the final element you found?
