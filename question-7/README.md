

## Question 

If it is possible, return any [i, j], such that
* Z[0], Z[1], ..., Z[i] is the first part;
* Z[i+1], Z[i+2], ..., Z[j-1] is the second part, and
* Z[j], Z[j+1], ..., Z[Z.length - 1] is the third part.
* All three parts have equal binary value.



Examples : 


indexs: [0,1,2,3,4]
Input : [1,0,1,0,1]


Output : [0,3]



| Part                                  | Sub-Binary (i=0,j=3)           |     value      |   
| --------------------------------------| -------------------------------|----------------|
| Z[0], Z[1], ..., Z[i]                 | [1,0,1,0,1,0][:0 + 1]          |     [1]        |
| Z[i+1], Z[i+2], ..., Z[j-1]           | [1,0,1,0,1,0][0 + 1: 3]        |     [0,1]      |
| Z[j], Z[j+1], ..., Z[Z.length - 1]    | [1,0,1,0,1,0][3:]              |     [0,1]      |







---
---
---




indexs: [0,1,2,3,4,5]

Input : [1,0,1,0,1,0]