# Construct The Tree - Easy

## Problem

Given a **binary tree** as a string, print its node contents in a **pre-order
traversal**. A pre-order traversal is defined recursively by visiting the root,
traversing its left sub-tree and then its right sub-tree.  The tree is given in
**breadth-first order**, and when a node is not present, this is encoded by a
`#` in place of the node's value. Trailing `#   ` entries are omitted.  Node
values are guaranteed to be unique, when they exist.  Output the values in the
nodes that exist, in traversal order, separated by spaces.

### Example 1

#### Input

```
5 3 2 # 6 1 # # # 4 0
```

Represents the following tree:

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
5 3 6 2 1 4 0
```
