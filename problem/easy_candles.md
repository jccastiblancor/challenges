# Candles - Easy

## Summary
Alice and Bob are preparing a birthday cake for Camilla. The cake is
ready, and Bob bought **N** candles to put on the cake, however these candles
are not all of the same length, and Alice believes it's unacceptable. Camilla
turns **K** years old today, and Alice and Bob have to prepare at least **K**
candles of the same length according to the rules, as soon as possible, so the
birthday party isn't ruined.

## Problem
Bob and Alice can make any of the candles *shorter* by removing some
part of it (that part is wasted and cannot be used afterwards). What's the max
possible length of these candles?

The input consists of two lines. The first line contains two integer numbers:
initial number of candles N and the minimal number of candles K that has to be
of the same length.  The next line has N positive integers - the corresponding
lengths of every candle.

### Example 1

#### Input
```
5 4
1 2 3 4 5
```

#### Output
```
2
```
