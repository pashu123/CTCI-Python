### CTCI solution ####
### Author : Prashant Kumar ####

## we will use python list and assume that character 
## through a-z is given in the string we will also make
## sure that we are using on and off state i.e 0 and 1 to 
## store the entire count

def palindromeperm(originalstr:str) -> bool:
    '''Returns whether any permutation of the
        string can be made to look like a palindrome'''
    
    count_list = [0]*26
    for i in originalstr:
        count_list[ord(i)-97] ^= 1
    error_check = 0
    for j in count_list:
        if j == 1:
            error_check += 1
        if error_check > 1:
            return False
    
    return True



# True
print(palindromeperm('tactcoa'))
# False
print(palindromeperm('hello'))


