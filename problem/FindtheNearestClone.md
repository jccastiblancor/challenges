In this challenge, there is a connected undirected graph where each of the nodes
is a color. Given a color, find the shortest path connecting any two nodes of
that color. Each edge has a weight of 1. If there is not a pair or if the color 
is not found, print -1.

For example, given *graph_nodes=5*, and 4 edges *g_from=[1,2,2,3]* and 
*g_to=[2,3,4,5]* and colors for each node are *arr=[1,2,3,1,3]* we can draw 
the following graph:

![](https://s3.amazonaws.com/hr-assets/0/1529952915-a96eba7baa-nearestcloneexample.png)

Each of the nodes is labeled [node]/[color] and is colored appropriately. 
If we want the shortest path between color 3, blue, we see there is a direct 
path between nodes 3 and 5. For green, color 1, we see the path length 2 from 
1->2->4. There is no pair for node 4 having color 2, red.

##Function Description

Complete the findShortest function in the editor below. It should return 
an integer representing the length of the shortest path between two nodes 
of the same color, or **-1** if it is not possible.

findShortest has the following parameter(s):

- *g_nodes*: an integer, the number of nodes
- *g_from*: an array of integers, the start nodes for each edge
- *g_to*: an array of integers, the end nodes for each edge
- *ids*: an array of integers, the color id per node
- *val*: an integer, the id of the color to match
##Input Format

The first line contains two space-separated integers n and m, the number of nodes
and edges in the graph.
Each of the next m lines contains two space-separated integers *g_from[i]* and 
*g_to[i]*, the nodes connected by an edge.
The next line contains n space-seperated integers,*ids[i]* , representing the 
color id of each node from 1 to n.
The last line contains the id of the color to analyze.

**Note:** The nodes are indexed from 1 to n.

##Constraints

- 1<=n<=10<sup>6</sup>
- 1<=m<=10<sup>6</sup>
- 1<=*ids[i]*<=10<sup>8</sup>

##Output Format

Print the single integer representing the smallest path length or **-1**.

##Sample Input 0
````
4 3
1 2
1 3
4 2
1 2 1 1 
1
````
##Sample Output 0
````
1
```` 
##Explanation 0

![](https://s3.amazonaws.com/hr-assets/0/1529953948-1e4fee4daf-nearestclonesample0.png)

In the above image the distance between the closest nodes having color label  is 1.

##Sample Input 1
````
4 3
1 2
1 3
4 2
1 2 3 4
2
````
##Sample Output 1
````
-1
```` 
##Explanation 1

![](https://s3.amazonaws.com/hr-assets/0/1530566003-c7e0b27b06-nearestclonesample1.png)

##Sample Input 2
````
5 4
1 2
1 3
2 4
3 5
1 2 3 3 2
2
````
##Sample Output 2
````
3
````
##Explanation 2

![](https://s3.amazonaws.com/hr-assets/0/1530566304-daec2771f0-nearestclonesample2.png)