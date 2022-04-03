#wap to create dictionary of hindi words with values as their english translation. Provide an option to user to look up for.

mydict = {
    "YUKTI" : "TECHNIQUE/IDEA",
    'SUKSHM': 'SUBTLE',
    "DANGE" :  "riots",
    "PAKSHPATI" : "partiality",
    "PAKSHPAT" : "prejudice(incorrect view against something)",
    '''JHUKA HUA''' : "biased(bias is normally used in the same context as prejudice but is a view in favour of something)"
}
print("options are",mydict.keys())
a=input("Enter the hindi word to look up for\n")
# print("The meaning of your entered hindi word is : ",mydict[a])  if we write a word which is not present in key it will give error.
print("The meaning of your entered hindi word is : ",mydict.get(a)) #we wrote this to avoid error.


##################################################################
#                2 QUS [WAP TO INPUT 8 NO FROM USER AND DISPLAY ALL THE UNIQUE NO(ONCE)]
d1=int(input("enter 1 no\n"))
d2=int(input("enter 2 no\n"))
d3=int(input("enter 3 no\n"))
d4=int(input("enter 4 no\n"))
d5=int(input("enter 5 no\n"))
d6=int(input("enter 6 no\n"))
d7=int(input("enter 7 no\n"))
d8=int(input("enter 8 no\n"))
y={d1,d2,d3,d4,d5,d6,d7,d8}
print(y)

############# 3 QUESTION(WHAT WILL BE THE LENGTH OF FOLLOWING SET)
q=set()
q.add(20)
q.add(20.0)
q.add("20")  #LENGTH =2(bcz in set it takes 20 and 20.0 equal)
print(q)