### CTCI solution ####
### Author : Prashant Kumar ####


## There can be two situation when the string is of same
## length (replace) and when the string is of different length



def one_edit_away(string1:str , string2:str)-> bool:
    '''Checks if one string can be converted into another 
    with just one edit'''
    if len(string1) == len(string2):
        return checkreplace(string1,string2)
    elif (len(string1) + 1) == len(string2):
        return checkedit(string1,string2)
    elif (len(string2) + 1) == len(string1):
        return checkedit(string2,string1)
    else:
        return False



def checkreplace(str1,str2):
    ''' Checks max of one difference between strings'''
    found_diff = False
    for i,j in zip(str1,str2):
        if i != j:
            if found_diff:
                return False
            found_diff = True
    return True

def checkedit(str1,str2):
    index1 = 0
    index2 = 0
    while len(str1) < index1 and len(str2) < index2:
        if str1[index1] != str2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    
    return True


print(one_edit_away('hola','hila'))

print(one_edit_away('myname','holais'))



