items=['A','B','C','D','E']

#Approach 1

#for item in items:
#    if item == 'B':
#        items.remove('B')
#    else:
#        print(item)

# A D E - list item getting skipped

#Approach 2 - Need to be followed

new_list=[]
for item in items:
    if item == 'B':
        continue
    else:
        print(item)
        new_list.append(item)

#A C D E

