# Calculator - Easy

## Problem

You have found an old calculator lying around (I mean **really** old). Its
buttons and screen work, but it doesn't seem to do anything when you press the
`=` button. You've figured out that it has an onboard computer but its memory
got wiped a long time ago, and have taken it upon yourself to restore it to its
former glory. Let's start by writing support for the **addition** and
**subtraction** of **integers**. Each integer could be **positive** or
**negative** (starting with a `-`). Input is fed to the calculator as a
sequence of integers, joined by addition (`+`) or subtraction (`-`) operations
in **infix** notation (meaning the operator appears between its operands). Your
input file is a list of valid inputs to your calculator, each on their own line.
Each line will match the following regular expression `-?[0-9]+([-+]-?[0-9]+)*`.
Output the answers to each expression in order, separated by spaces.

### Example 1

#### Input

```
1-19-14-11+22
11+6+7+7-20
6+14-22-16+23
23+8-1-13+18
15+17-10-5+10
```

#### Output

```
-21 11 5 35 27
```
