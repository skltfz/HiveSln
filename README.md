# HiveSln
This puzzle is funny, lets play it by using python ...
 
First of all, what is Hive puzzle. In fact, i have no idea what name it is. I bought it very long time ago when I am young in a trip. Obviously it is not easy to solve

Until currently I figured out this puzzle is able to solved by outer 12 blocks first, and in fact, given the 6 angles are found. Whatever it is found accidently or luckily, human brain can solved the rest of the blocks pretty handy. Just a lot of accumulation required.

The rules of this puzzle is simple, any diagonal & adjacent lines sums are equals to 38. And there are 1-19 blocks.

This solution is about using a relative smart way to select the desire blocks and validate if they can be the final answer eventually.

The reason is if you brute focus 19 blocks there will be 19 permutations in 19 chooses i.e. 19! = 1.216451e+17 combinations. You never want to iterate that many times 

By thinking carefully, that 6 angle's blocks should be the very good start points, in fact is there is also 19!/13! = 19535040 combinations.

Fortunately python is quite fast (or at least my laptop is quite fast)

So the rationale is: getting that 6 angles (actually, by doing carefully there are 30504 combinations, by filter out the duplication it became 5084 combinations, and then adding the inner 7 blocks rules, eventually the program can find the answer (in premise that you need to write the condition right, the inner rules are pretty tedious I have to say, but I don't know how to simplify it, since it is really hardcore additions only lol)
