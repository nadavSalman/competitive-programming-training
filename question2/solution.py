


'''
D. AB-Strings
There are two strings s and t, consisting only of letters a and b. 
You can make the following operation several times: choose a prefix of s, a prefix of t and swap them. 
Prefixes can be empty, also a prefix can coincide with a whole string.

Your task is to find a sequence of operations 
after which one of the strings consists only of 'a' letters and the other consists only of 'b' letters. 
The number of operations should be minimized.


nput : 

The first line contains a string s (1 ≤ |s| ≤ 2·105).

The second line contains a string t (1 ≤ |t| ≤ 2·105).

Here |s| and |t| denote the lengths of s and t, respectively. 
It is guaranteed that at least one of the strings contains 
at least one a letter and at least one of the strings contains at least one b letter.

Output : 

The first line should contain a single integer n (0 ≤ n ≤ 5·105) — the number of operations.
Each of the next n lines should contain two space-separated integers ai, bi — the lengths of prefixes of s and t to swap, respectively.

Example :
Input :
s = bab
t = bb

output : 
2
1 0 - Swap the prefix of the first string with length 1 and the prefix of the second string with length 0. -> s = ab , t = bbb
1 3 - Swap the prefix of the first string with length 1 and the prefix of the second string with length 3. -> s = bbbb t = a

------------------------------
>>> s
'≤'
>>> ord(s)
8804
>>> 

'''


def str_prefix(str,prefix):
    return str[0:prefix]

'''
s na
s_prefix and t_prefix are integer for the prefix.
'''
def swap_by_prefix(s,t,s_prefix,t_prefix):
    s_str_prefix = str_prefix(s,s_prefix)
    print('s prefix : ',s_str_prefix)
    t_str_prefix = str_prefix(t,t_prefix)
    print('t prefix :',t_str_prefix)

    print('t prefix + the rest of s = ',t_str_prefix + s[s_prefix:s.__len__() + 1])#+1 to include the last char
    print('s prefix + the rest of t = ',s_str_prefix + t[s_prefix:t.__len__() + 1])

    s = t_str_prefix + s[s_prefix:s.__len__()]
    t = s_str_prefix + t[s_prefix:t.__len__()]
    print('--------')
    print()

    #print(t_str_prefix + s[s_prefix:s.__len__()],s_str_prefix + t[s_prefix:t.__len__()])



def main():
    s = 'bab'
    t = 'bb'
    swap_by_prefix(s,t,2,0)
    print('s = ',s,' , t = ',t)


    # result_of_wsaping = swap_by_prefix(s,t,1,0)
    # print('t = ',result_of_wsaping[0],' , s = ',result_of_wsaping[1])

if __name__ == "__main__":
    main()