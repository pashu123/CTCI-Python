### CTCI solution ####
### Author : Prashant Kumar ####

#We will make use of list to solve this problem
#Because python strings in immutable, python list are mutable
# and hence in place urlification can be done or custom mutable 
# string classes can be made to make the problem easier.

def urlify(original:list,truelen:int)->list:
    scount = 0
    for i in range(truelen):
        if original[i] == ' ':
            scount += 1
    print(scount)
    index = (truelen + 2 * scount)
    print(index)
    for i in reversed(range(truelen)):
        if original[i] == ' ':
            original[index - 1] = '0'
            original[index - 2] = '2'
            original[index - 3] = '%'
            index -= 3
        else:
            original[index - 1] = original[i]
            index -= 1
    
    return original


print(urlify(['M','r',' ','J','o','h','n',' ','S','m','i','t','h',' ',' ',' ',' '],13))



