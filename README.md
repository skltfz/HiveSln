# HiveSln - by SKLTFZ

This puzzle is funny, lets play it by using python ...
![alt text](https://github.com/skltfz/HiveSln/blob/main/hive-sumallto38.png?raw=true)
The rules of this puzzle is simple, sum of any diagonal & adjacent lines nodes are equals to 38. And there are 19 nodes.

First of all, what is Hive puzzle. In fact, i have no idea what name it is. My parent bought it very long time ago in a oversea trip. Obviously it is not easy to solve for a 1x yrs old guy. I googled in and it named 數字蜂窩 in chinese (while it is 100% sure mine is not bought at China lol)

Recently, I figured out this puzzle is able to solved by outer 12 nodes first, and in fact, given the 6 edge's angles are found. Whatever it is found by any reason (intuition? genius? luck? not sure), human brain can solved the rest of the nodes pretty easily by doing additions.

The problem is that you cannot validate it without getting to the last piece of node right... Then I am started to curious how many actual combinations there are

If you brute force 19 nodes, then the number of combinations equals to 19 into 19 permutations, so you need to do 19! = 1.216451e+17 iterations. You never want to iterate that many times (I dont think you can :D...)

What is the solution? It is implemented to find the first 6 edge angles first because

1. it is easier to validate
2. it has 19!/13! = 19535040 combinations
   By getting these 6 angle nodes with validation passed. The outer 12 nodes are show.

However there is still 5084 combinations. Next we getting the center node by validating the 3 diagonal lines nodes (fiveCheck), finally getting the rest of inner nodes by fourCheck

Finally, the interesting part is: there are actually 2 possible solutions (should I say only? in fact I thought there is only 1 until the program told me the truth... LOL) :) Enjoy the truth to be revealed

To run the program:

install python, and possible impossible numpy by using pip then execute the hiveSln.py by

py hiveSln.py or pythons hiveSln.py
