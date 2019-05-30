# we will first use the hashtable approach


from linkedlist import SinglyLinkedList


def removedups(ll):
    '''remove duplicates from the linked list'''
    dupdict = {}

    for i in ll:

        if i.data not in dupdict:
            i.next = i.next.next
            dupdict[i.data] = 1


    return ll



a = SinglyLinkedList()
a.insert_head(2)
a.insert_head(2)
a.insert_head(5)
a.insert_last(3)
a.insert_head(5)
a.insert_last(3)


print(a)

a = removedups(a)
print(a)