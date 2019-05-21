### CTCI solution ####
### Author : Prashant Kumar ####

## we will use list to simplify our task
## and make the string again we will check 
# the length of the string at last


def string_compression(inpstr: str)-> str:
    '''Returns the compressed version of the string'''
    finallst = []
    consecutivecnt = 0
    for i in range(len(inpstr)):
        consecutivecnt +=1
        if (i+1) >= len(inpstr) or inpstr[i] != inpstr[i+1]:
            finallst.append(inpstr[i])
            finallst.append(str(consecutivecnt))
            consecutivecnt = 0 
    finalstr = "".join(finallst)
    # Finaly check the length of both the strings
    if len(finalstr) >=  len(inpstr):
        return inpstr
    else:
        return finalstr




print(string_compression('aabccddddddd'))
