##############   INDICES    ################
a="YUKTI"
print(a[4])

##############    SLICING    ###############
a="YUKTI  BISHT" #SPACE ALSO COUNTS
print(a[1:8])

##############    CONCATENATION  ##################
d="HI!! "
a="YUKTI "
b="BISHT "

# CONCATENATING TWO STRINGS
c=d+a+b
print(c)
print(type(a))

x='bisht'
print(x[:2]) #will take lowest index automatically

y='yukti'
print(y[3:]) #will exclude character till no

##### NEGATIVE INDICES   #####
q="YUKTI"
print(q[-5:-2])

####### SLICING WITH SKIP VALUE  #######
a="YUKTI"
print(a[1:4:2])


#####   HOW TO GET RANDOM NUMBER  ####
a='YUKTI'
print(a[0:1],a[3:5:])
# print(a[3:])