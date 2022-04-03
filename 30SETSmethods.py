#1 METHOD (ADDING VALUES TO AN EMPTY SET)
a=set()
print(type(a))
b={1,2,3,4,9}

# ADDING VALUES TO AN EMPTY SET
a.add(4)
a.add(9)
a.add(0)
a.add(23)
a.add(4)
a.add(23)  
print(a)  #WILL NOT PRINT REPETITIVE VALUES

#it can't add list
# a.add([7,6,2])

#it can't add dictionary
# a.add({7,6,2})

# BUT it can add tuple
a.add((7,6,2))
print(a)


# 2 METHOD (WILL PRINT LENGTH OF SET)
print(len(a))
  #WILL PRINT LENGTH OF SET

#3 METHOD (#WILL REMOVE THE PARTICULAR NO)
a.remove(9)  #WILL REMOVE THE PARTICULAR NO 
print(a)

#4 METHOD
print(a.pop())  #removes an arbitrary element(element not choosen by us) and returns the removed element. Raises keyerror if set is empty.
                 
#5 METHOD
# a.clear()   #WILL CLEAR THE WHOLE SET
# print(a)

#6 METHOD
print(a.union(b))    # GIVE ALL ELEMENTS OF BOTH SETS


#7 METHOD
print(a.intersection(b))   # gives common element

#5 METHOD
a.clear()   #WILL CLEAR THE WHOLE SET
print(a)
