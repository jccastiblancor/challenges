# Construct The Tree - Hard

## Summary

Given the **pre-order and in-order traversals** of a **binary tree**, T, print
its **breadth-first traversal**. The breadth first traversal works by visiting
the tree level-by-level (the level of a node in a tree is the length of the
shortest path from it to the root), starting at level 0 (i.e. the root) and
increasing from there. Nodes of the same level are visited in left-to-right
order.

Input is given over two lines, the first being the **pre-order traversal** and
the second being the **in-order traversal**. Node values are guaranteed to be
unique in each traversal. Output the values in the nodes that exist, in
traversal order, separated by spaces. If a node does not exist at a particular
position, indicate this by printing a `#`.  Trailing `#` entries should be
omitted.  For all levels apart from the root and the leaves, there must be
twice as many entries as non-`#` entries in the level above. This invariant does
not apply to the root which has no level above it, nor the leaves which may
have fewer elements because trailing # entries have been omitted.

### Example 1

#### Input

```
5 3 6 2 1 4 0
3 6 5 4 1 0 2
```

represent the pre- and in-order traversals for the following tree:

```
 __5__
/     \
3     2
 \   /
  6 1
   / \
  4   0
```

#### Output

```
5 3 2 # 6 1 # # # 4 0
```
