### CTCI solution ####
### Author : Prashant Kumar ####


## Checks whether the string is rotated version of itself
## Assume in used the kmp algo

def string_rot(origstr,rotstr):
    
    if len(origstr) != len(rotstr):
        return False
    
    if rotstr in origstr+origstr:
        return True
    else:
        return False



# Return True
print(string_rot('waterbottle','erbottlewat'))