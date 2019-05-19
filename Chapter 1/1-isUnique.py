### CTCI solution ####
### Author : Prashant Kumar ####

# We will implement this with the help of python list 
# Making sure that count of character through a-z is present in the 
# list. So the time complexity would be O(n) and space complexity O(1).

def is_unique(s : str):
    ''' Takes a string input to determine
    whether the character present in it
    are unique'''

    count_list = [0] * 26
    
    for char in s:
        if count_list[ord(char)-97] == 1:
            return False
        else:
            count_list[ord(char)-97] = 1

    return True


# False
print(is_unique('hello'))

#True
print(is_unique('hola'))
