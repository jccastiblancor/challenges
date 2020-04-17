# Calculator - Hard

## Problem

You have found an old calculator lying around (I mean **really** old). Finally
to make this calculator extra special, you're going to implement **equation
solving**. You noticed a button on the calculator annotated with the letter `X`,
you're going to use this to let people input formulae with **variables** in
them.

Your calculator will now accept **an integer** (call it *Y*) then a space,
followed by **a formula** in **prefix notation** (like before) mentioning the
variable `X` **exactly once**, in the place of a number. It will output the
**integer** value that `X` must take to make the formula evaluate to *Y*, if
such an integer exists. If it's impossible to find such an integer, output `Err`
instead.

For example, if we wanted to solve the equation `231 = (1 + 2) * (X + 4) * (5 +
6)`, we would input `231 * * + 1 2 + X 4 + 5 6` into the calculator.

Again, your input is a list of calculator inputs, each on their own line, and
the expected output is a list of your calculator's outputs, in order of input,
separated by spaces.

### Example 1

#### Input

```
231 * * + 1 2 + X 4 + 5 6
413 * * - + 2 + 9 7 9 3 * X 3
-22 - + 2 + 4 * 3 - - 6 4 9 X
15 - - X - - 1 7 7 * 5 - 3 2
-51 - * 5 0 + X * + 0 9 - 5 0
-305 * 5 + + - 6 * 7 9 0 - X 9
-120 - - + X + 0 1 1 * 7 * 3 6
-10 - * 8 2 + 9 - * - 4 1 8 X
18 * + - 1 9 + 3 3 * X - 6 9
114 - - * 9 + 6 8 * + 2 1 3 X
```

#### Output

```
3 Err 7 7 6 5 6 7 3 3
```
