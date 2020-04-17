# Candles - Hard

## Summary
Alice and Bob are preparing a birthday cake for Camilla. The cake is
ready, and Bob bought **N** candles to put on the cake, however these candles
are not all of the same length, and Alice believes it's unacceptable. Camilla
turns **K** years old today, and Alice and Bob have to prepare at least **K**
candles of the same length according to the rules, as soon as possible, so the
birthday party isn't ruined.

## Problem
Alice and Bob can cut existing candles with insane precision,
including fractional numbers. For example, they can cut a candle of length 9
into five candles of lengths ¾, 1⅓, 1⅔, 1¾, 3½ . What's the max possible length
of the candles Alice and Bob can achieve in order to have at least K candles of
that length? Provide the answer with five decimal point precision.

The input consists of two lines. The first line contains two integer numbers:
initial number of candles N and the minimal number of candles K that has to be
of the same length.  The next line has N positive integers - the corresponding
lengths of every candle.

### Example 1

#### Input
```
2 5
10 7
```

#### Output
```
3.33333
```
