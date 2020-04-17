# Types - Hard

## Summary

You are developing a type system for a simple programming language, called *Lang*.  Here is an
example program:

```
(type even (int -> bool))
(type odd  (int -> bool))

(func (even n) (if (= n 0) true  (odd  (- n 1))))
(func (odd n)  (if (= n 0) false (even (- n 1))))

(type fib (int -> int))
(type helper (int int int -> int))

(func (fib n) (helper 0 1 (+ n 1)))
(func (helper n a b) (if (= n 0) a (helper (- n 1) a (+ a b))))
```

*Lang* has the following types:

* `int`, representing the integers (..., `-1`, `0`, `1`, `2`, etc),
* `bool` for booleans (`true` and `false`).
* `(P1 P2 ... PN -> R)` for any types `P1`, `P2`, ..., `PN` and `R`.  Representing a function
taking `N` arguments, and returning a value of type `R`.

A *Lang* program consists of a sequence of statements, each on their own line (Empty lines are
ignored).  A statement can be one of the following:

* A `type` declaration, of the form `(type NAME TYPE)` which introduces a new variable, with the
given name and type.
* A `func`tion definition, of the form `(func (NAME V1 V2 ... VN) BODY)` which supplies the
implementation of a function previously declared with the given name.  `BODY` is an expression
(explained below).  In a well-formed program, the function will have been declared with `N`
parameters, whose names are given by `V1`, `V2`, ..., `VN` and the type of its body will match
the return type in its declaration too.

Expressions in *Lang* are one of the following:

* An integer literal, like `-1`,  `0`, `1`, `2` etc.
* A variable name, which can refer to a parameter of the function the expression is defined in, or
any function declared before the expression in the program.
* A conditional of the form `(if c a b)` which evaluates to `a` if `c` evaluates to `true` and
evaluates to `b`  if `c` evaluates to `false`.
* A function call of the form `(f e1 e2 ... en)` where `f` is a variable name and `ei` is an
expression for `1 <= i <= n`.

## Problem

Type checking is great but we want to make the lives of *Lang* programmers even simpler still.  Why
should they have to declare types at all?  We can figure things out from context, using **type
inference**.  The language needs to change in certain ways to support this, we'll call our new
language *Lang++*.  It differs from *Lang* in the following ways:

* **No more `type` declarations**.  We don't need them anymore, because all types will be inferred.
* **Functions accessible before definition**.  Because the language no longer has type
declarations, there is no way to declare a function's signature before using it, so now a
function can be referenced earlier in the program than when it was defined.
* **The `any` type**.  Sometimes, there is not enough context in the program to infer a precise
type.  In that case, we can say the expression has type `any`.

The list of possible type errors has also changed in *Lang++:*

* We still have **undefined identifier** and **if condition mismatch** like before,
* but we no longer have **missing type declaration**.
* **Arity mismatch**.  In *Lang* there were two kinds of arity mismatch error:  A function
definition could disagree with the type declaration or a call-site could.  In *Lang++ *we do not
have a type declaration to act as a source of truth, so we say there is an arity mismatch if one
reference to a function (definition or call-site) disagrees with another in the number of
parameters it passes.
* **Type mismatch**.  Again, because we no longer have type declarations, in *Lang++*, parameter
type and return type mismatches are all folded into one:  If we have conflicting information
about the type of an expression (e.g. it is a variable, and it is being passed as a `bool`
parameter to one function and an `int` parameter to another function), then it is considered a
type error.
* **If branch mismatch**. Our type system requires that the “then” and “else” cases of an if
expression have the same type.  If they cannot be made to agree on their type, this is considered
a type error.
* **Infinite Types**.  It is possible to construct types that are “infinite” for example the
function `(func (inf) inf)` has a type `(-> (-> (-> ...)))`, because it returns it self.  We have
no good way to represent a type like this, so we treat it as an error.

Note that *Lang* has the following built-in identifiers:

```
(type true  bool)
(type false bool)
(type +     (int int -> int))
(type -     (int int -> int))
(type =     (int int -> bool))
(type <     (int int -> bool))
```

Your input will be a *Lang++* program.  Like before, your output will be a sequence of responses
each separated from the next by a space.  There should be one response for **each function
definition**, in the order they are encountered in the program.  The response will be `Err` if one
of the mentioned type errors is discovered whilst checking the function or the **most general
type** for the function otherwise.  Consult the examples for an explanation of “most general type”.

### Example 1

#### Input

```
(func (even n) (if (= n 0) true  (odd  (- n 1))))
(func (odd n)  (if (= n 0) false (even (- n 1))))

(func (fib n) (helper 0 1 (+ n 1)))
(func (helper n a b) (if (= n 0) a (helper (- n 1) a (+ a b))))
```

#### Output

```
(int -> bool) (int -> bool) (int -> int) (int int int -> int)
```

#### Notes:

How did this get inferred?

* `even` is a function that takes one parameter, so its type must have this
  shape: `(any -> any)`.
    * Its parameter `n`, is passed as a parameter to `=` which we know takes
      `int`s, so it must be an `int`.
    * The “then” branch of the if expression returns a `bool`, so that must be
      the return type of the function overall.
    * So `even` has type `(int -> bool)`.
* `odd`'s type is worked out similarly to `even`'s.
* `fib` takes one parameter, so its type has to have this shape: `(any -> any)`.
    * Its first parameter is passed to `+` so must be an `int`.
    * Its return type must be the same as `helper`'s.
    * So far we know that `fib` has type `(int -> any)`.  We need to look at
      `helper` to figure out the return type.
* `helper` takes three parameters so has shape `(any any any -> any)`.
    * Looking at the invocation of `helper` in `fib` we already know that all of
      its parameters are `int` type (the first two had integer literals passed
      in, and the second had the result of an addition, which is an `int`).
    * The “then” branch of the if expression returns the second parameter, which
      is an `int`, so helper's return type must be `int`.
    * `helper` has type `(int int int -> int)` **and** `fib` has type `(int ->
      int)`.

When it comes to **most general types** consider this example:

```
(func (id x) x)
```

This function could be assigned the type `(int -> int)` or `(bool -> bool)`, or even `((int bool ->
int) -> (int bool -> int))`, but **its most general type is `(any -> any)`**.  The most general
type imposes the fewest constraints whilst remaining correct.  Suppose the program continued as
follows:

```
(func (foo x) (> (id x) 0))
```

Now `id` has type `(int -> int)`, and `foo` has type `(int -> bool)`.  If the program continued:

```
(func (bar x) (&& (id x) x))
```

`id` can no longer be assigned a type (this is a limitation of our type system)!  But because we
discovered that in the definition of `bar`, the expected output for this program would be:

```
(int -> int) (int -> bool) Err
```
