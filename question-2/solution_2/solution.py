import os


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


'''
Return prefix of a string.
'''
def str_prefix(str,prefix):
    """[summary]

    Args:
        str ([type]): [description]
        prefix ([type]): [description]

    Returns:
        [type]: [description]
    """
    return str[0:prefix]

def swap_by_prefix(s,t,s_prefix,t_prefix):
    """swap the given prefixes  for the given strings.

    Args:
        s (string): s string
        t (string): t string
        s_prefix (integer): s prefix
        t_prefix (integer): t prefix

    Returns:
        [tuple]: The function return tuple with two elements  : (s after swap with t prefix,t after wsap with s prefix).
    """
    #print('s prefix : ',s_prefix,' , t prefix : ',t_prefix)
    s_str_prefix = str_prefix(s,s_prefix)
    #print('s prefix : ',s_str_prefix)
    t_str_prefix = str_prefix(t,t_prefix)
    #print('t prefix : ',t_str_prefix)
    s_after_wsap = t_str_prefix + s[s_prefix:s.__len__()]
    #print('s_afte_wsap -> ',s_after_wsap)
    t_after_swap = s_str_prefix + t[t_prefix:t.__len__()]
    #print('t_afte_wsap -> ',t_after_swap)
    return (s_after_wsap,t_after_swap)

def contain_one_type_of_char(str):
    """[summary]

    Args:
        str ([type]): [description]

    Returns:
        [type]: [description]
    """
    if str.__len__() > 0:
        first_char = str[0]
        for character in str:
            if character != first_char:
                return False       
    return True

def f(s,t,si,ti):
    #print('f entry ...')
    if contain_one_type_of_char(s) and contain_one_type_of_char(t):
        print('solution found')
    elif si < s.__len__() and ti < t.__len__():
        # print('si < s.__len__() and ti < t.__len__()')
        if contain_one_type_of_char(str_prefix(s,si)) and contain_one_type_of_char(str_prefix(t,ti)):
            # print('contain_one_type_of_char(str_prefix(s,si)) and contain_one_type_of_char(str_prefix(t,ti))')
            
            
            
            for i1 in range(si + 1,s.__len__()):
                new_s , new_t = swap_by_prefix(s,t,si,ti)
                print(new_s,new_t,i1,ti)
                f(new_s,new_t,i1,ti)
            

            
            for i2 in range(ti + 1,s.__len__()):
                new_s , new_t = swap_by_prefix(s,t,si,ti)
                print(new_s,new_t,si,i2)
                f(new_s,new_t,si,i2)

            #f(new_s,new_t,si + 1,ti + 1)



db_solution = []
def solution1(s,t,si,ti,visited):
    #print(s,t,si,ti,visited)
    if contain_one_type_of_char(s) and contain_one_type_of_char(t):
        db_solution.append(visited.copy())
        
        if visited.__len__() < 6:
            pass
            #print(visited)
        #print('solution found - ',visited)
    elif si <= s.__len__() and ti <= t.__len__() and ((si,ti) not in visited):
        # print('si < s.__len__() and ti < t.__len__()')
        if contain_one_type_of_char(str_prefix(s,si)) and contain_one_type_of_char(str_prefix(t,ti)):
            # print('contain_one_type_of_char(str_prefix(s,si)) and contain_one_type_of_char(str_prefix(t,ti))')
            new_s , new_t = swap_by_prefix(s,t,si,ti)
            visited.append((si,ti))
            #print(visited)
            #print('~~~~~~~~~~~~~~~~~~~~~')
            curent_entry_trrget = []
            for new_s_index in range(s.__len__() + 1):
                for new_t_index in range(t.__len__() + 1): 
                    entry = (new_s_index,new_t_index)
                    curent_entry_trrget.append(entry)
                    # print(entry)
                    # visited.append(entry)
                    solution1(new_s,new_t,new_s_index,new_t_index,visited.copy())
            #print('~~~~~~')
            #print(curent_entry_trrget)
            #print('~~~~~~')
            #print('~~~',curent_entry_trrget,'~~~')



def faind_minimun_in_all_solution(solutions):    
    min_sol = (-1,-1)
    
    if db_solution.__len__() >= 1:
        min_sol = db_solution[0]

    for sol in db_solution:
        if sol.__len__() < min_sol.__len__():
            min_sol = sol


    return min_sol
        














def faind_minimum_sequence(s_str,t_str,s_prefix,t_prefix,l):
    if contain_one_type_of_char(s_str) and contain_one_type_of_char(t_str):
        print('number of operations : ',l.__len__())
        print('operations : ',l)
    for index1 in range(s_prefix,s_str.__len__()):
        for index2 in range(t_prefix,t_str.__len__()):
            print(s_str,t_str,index1,index2)
            swap_by_prefix(s_str,t_str,index1,index2)
            faind_minimum_sequence(s_str,t_str,index1,index2,l.copy())




# def collect_all_solutions(db):
    
    
    

'''
important linsks :
- https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
- https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference
'''
def main():
    print('Hi there black kiti')
    print(os.getcwd(),'| question2/solution/solution.py')
    s = 'aa'
    t = 'aba'
    solution1(s,t,0,0,[])
    # print(faind_minimun_in_all_solution(db_solution))
    
    min_sol = db_solution[0]
    
    for sol in db_solution:
        if sol.__len__() < min_sol.__len__():
            min_sol = sol.copy()

    print(min_sol)
    #print(db_solution)
    # s = 'b'
    # t = 'aba'
    #solution1(s,t,0,0,[])
    #swap(0,1) -> s = ab t = ba
    #swap(1,1) -> s = bb t = aa

    # swap_by_prefix('aaabba','ababba',1,3), ('abaaabba','abba')

    # s = 'aaabba'
    # t = 'ababba'



    # print('s = ',s,' , t = ',t)

    # s,t = swap_by_prefix(s,t,1,3)# re asaing s and t.

    # print('s = ',s,' , t = ',t)
    





    # print('prefix(bab,-1) -> ',str_prefix(s,-1))
    # print('prefix(bab,4) -> ',str_prefix(s,4))
    # print('prefix(bab,0) -> ',str_prefix(s,0))
    # print('prefix(bab,3) -> ',str_prefix(s,3))
    # print('prefix(bab,2) -> ',str_prefix(s,2))
    #swap_by_prefix(s,t,2,0)

    # result_of_wsaping = swap_by_prefix(s,t,1,0)
    # print('t = ',result_of_wsaping[0],' , s = ',result_of_wsaping[1])

if __name__ == "__main__":
    main()





def sambusak():
    return 1