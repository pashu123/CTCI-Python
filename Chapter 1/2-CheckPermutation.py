### CTCI solution ####
### Author : Prashant Kumar ####

## We will assume only character through a - z is present
## In first pass we will keep count of the character in first 
## String and then in second pass we will decrement the count of
## every character. if the final resultant list count is 0 then 
## then we will output the result


def check_permutation(originalstr : str, permstr:str)-> bool:
    '''Input two strings, returns boolean value
        checking the permutation between two'''
    if len(originalstr) != len(permstr):
        return False

    countlist = [0] * 26

    for i,j in zip(originalstr,permstr):
        countlist[ord(i)-97] += 1
        countlist[ord(j)-97] -= 1
    
    for i in countlist:
        if i != 0:
            return False
    
    return True


print(check_permutation('hello','olleh'))
# True

print(check_permutation('mynameis','nisameym'))
#True

print(check_permutation('permutation','holaitsis'))
#False