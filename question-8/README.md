
### Problem
Decode String
Part 1 - Decode String Simplified
The simplified version of "decode string" presents us with an alpha-numeric string where a number may come before any letter. Given such a string, decode the string so that each number/letter combinations is expanded.

Example 1
input: 4a output: aaaa

Example 2
input: a2b10c output: abbcccccccccc

Part 2 - Decode String (Standard Version)
Given an encoded string s, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note that k is guaranteed to be a positive integer.

Constraints

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets [].
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
Example 1
input: abcdefg output: abcdefg

Example 2
input: ab2[c]3[de4[f]] output: abccdeffffdeffffdeffff

Example 3
input: 2[2[2[a]]] output: aaaaaaaa