# Question - 4
 
 [Question source](https://codeforces.com/problemset/problem/1443/B) 

## B. Saving the City

Bertown is a city with n buildings in(if there were no mines under the building, then nothing happens).(if there were no mines under the building, then nothing happens). a straight line.

The city's security service discovered that some buildings were mined. A map was compiled, which is a string of length n, where the i-th character is "1" if there is a mine under the building number i and "0" otherwise.

    .ing happens).

For manual activation of one mine, the sapper takes a coins. He can repeat this operation as many times as you want.
Also, a sapper can place a mine under a building if it wasn't there. For such an operation, he takes b coins. He can also repeat this operation as many times as you want.

The sapper can carry out operations in any order.

You want to blow up all the mines in the city to make it safe. Find the minimum number of coins that the sapper will have to pay so that after his actions there are no mines left in the city.

### Input :
The first line contains one positive integer t (1≤t≤105) — the number of test cases. Then t test cases follow.
Each test case begins with a line containing two integers a and b (1≤a,b≤1000) — the cost of activating and placing one mine, respectively.

The next line contains a map of mines in the city — a string consisting of zeros and ones.

### Output : 
For each test case, output one integer — the minimum number of coins that the sapper will have to pay.

input : 
2
1 1
01000010
5 1
01101110

output : 
2
6

Note
In the second test case, if we place a mine under the fourth building and then activate it, then all mines on the field are activated. The cost of such operations is six, b=1 coin for placing a mine and a=5 coins for activating.


solution explain :

option 1 :
Try all operation combination that blow up all the mines in the city that and return the minimum number of coins required for that sequence of operation.

input : map of mines in the city -> "0010101....011110"
run throu the mines-map :
    - for each cell perform the following action :
        * Do nathing.
        - If there is a mine :
            * manual activation of the mine.
        - If there is no mine :
            * place a mine under a building.

continu this procedure recursivly and return the minimum number of coins .








metrix :
 time complexiy :