#Roads and libraries
##Problem
The Ruler of HackerLand believes that every citizen of the country should have access to a library. Unfortunately, HackerLand was hit by a tornado that destroyed all of its libraries and obstructed its roads! As you are the greatest programmer of HackerLand, the ruler wants your help to repair the roads and build some new libraries efficiently.

HackerLand has n cities numbered from 1 to n . The cities are connected by m
bidirectional roads. A citizen has access to a library if:

*Their city contains a library.

*They can travel by road from their city to a city containing a library.

The following figure is a sample map of HackerLand where the dotted lines denote obstructed roads:

![img1](https://s3.amazonaws.com/hr-challenge-images/0/1481983010-b779ad2b2b-torque1.png)

The cost of repairing any road is c<sub>road</sub> dollars,
and the cost to build a library in any city is c<sub>lib</sub> dollars.
If in the above example c<sub>road</sub>=2  and c<sub>lib</sub>=3 , 
we would build 5 roads at a cost of 5x2=10 and 2 libraries for a cost of 6. 
We don't need to rebuild one of the roads in the cycle 1 -> 2 -> 3 -> 1.

You are given q queries, where each query consists of a map of HackerLand 
and value of c<sub>lib</sub> and c<sub>road</sub>. For each query, 
find the minimum cost of making libraries accessible to all the citizens 
and print it on a new line.

##Function Description

Complete the function roadsAndLibraries. 
It must return the minimal cost of providing libraries to all, as an integer.

roadsAndLibraries has the following parameters:

* n: integer, the number of cities
* c<sub>lib</sub>: integer, the cost to build a library
* c<sub>road</sub>: integer, the cost to repair a road
* cities: 2D array of integers where each *cities[i]* contains two integers
 that represent cities connected by an obstructed road.

##Input Format

The first line contains a single integer q, that denotes the number of queries.

The subsequent lines describe each query in the following format:
- The first line contains four space-separated integers that describe the 
respective values of n, m, c<sub>lib</sub>  and c<sub>road</sub>, the number 
of cities, number of roads, cost of a library and cost of a road.
- Each of the next  m lines contains two space-separated integers, *u[i]*  and
*v[i]*, that describe a bidirectional road that connects cities *u[i]* and *v[i]*.

##Constraints
- 1 <=1<=10
- 1 <=n<=10<sup>5</sup>
- 0 <=m<=min(10<sup>5</sup>,nx(n-1)/2)
- 1 <=c<sub>road</sub>,c<sub>lib</sub><=10<sup>5</sup>
- 1 <=*u[i]*, *v[i]*<=n
- Each road connects two distinct cities.

##Output Format

For each query, print an integer that denotes the minimum cost to make libraries accessible to all the citizens on a new line.

##Sample Input
````
2
3 3 2 1
1 2
3 1
2 3
6 6 2 5
1 3
3 4
2 4
1 2
2 3
5 6
````

##Sample Output

````
4
12
````

##Explanation

Perform the following q=2 queries:

1. HackerLand contains  cities connected by  bidirectional roads. 
The price of building a library is  and the price for repairing a road is .

![img1](https://s3.amazonaws.com/hr-challenge-images/0/1479708586-328d4ff060-torque.png)

The cheapest way to make libraries accessible to all is to:

- Build a library in city **1** at a cost of **x=2**.
- Repair the road between cities **1** and **2** at a cost of **y=1**.
- Repair the road between cities **2** and **3** at a cost of **y=1**.

This gives a total cost of **2+1+1=4** . Note that the road between cities 3 and 1
 does not need to be repaired each is connected to city 2.
1. In this scenario it is optimal to build a library in each city because the
 cost of building a library (c<sub>lib</sub>=2) is less than the cost of repairing
  a road (c<sub>road</sub>=5).
  
![img1](https://s3.amazonaws.com/hr-challenge-images/0/1479709794-c1d435eec9-torque3.png)

There are **6** cities, so the total cost is **6x2=12**.