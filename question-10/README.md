## Binary Array Partition Problem
Given an array Z of 0s and 1s, divide the array into 3 non-empty parts, such that all of these parts represent the same binary value.

If it is possible, return any [i, j], such that

`Z[0], Z[1]`, ..., `Z[i]` is the first part;
`Z[i+1], Z[i+2]`, ..., `Z[j-1]` is the second part, and
`Z[j], Z[j+1]`, ..., `Z[Z.length - 1]` is the third part.
All three parts have equal binary value.
If it's not possible return `[-1, -1]`.

Example Inputs and Outputs
Example 1
Input: Z = `[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]`
Output: Partition indices: `[2, 7]`

Example 2
Input: Z = `[1,0,1,0,1]`
Output: Partition indices: `[0, 3]`

Example 3
Input: Z = `[1,1,0,1,1]`
Output: Partition indices: `[-1, -1]`