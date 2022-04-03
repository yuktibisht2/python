mydict={
"key"   : "value",
"yukti" : "coder",
"list"  : [1,2,3],
  1     :  2,
"marks" : "100" ,
"another dict" : {1,2,3,1,2}
}
# 1 METHOD
print(mydict.keys())   #WILL PRINT "KEY"
print(type(mydict.keys())) #WILL GIVE "mydict" AS A TYPE
print(list(mydict.keys())) #WILL CONVERT "mydict" TYPE TO "LIST"

#2 METHOD
print(mydict.values())  # WILL PRINT "VALUES"
print(type(mydict.values()))  #WILL GIVE "mydict" AS A TYPE
print(list(mydict.values()))   #WILL CONVERT "mydict" TYPE TO "LIST"

#3 METHOD
print(mydict.items())    #PRINTS IN COMBINATION i.e.=key and value of a dictionary

#4 METHOD
updatemydict={                # UPDATES THE DICTIONARY BY ADDING KEY-VALUES PAIRS 
    "YUKTI" : "bisht"
}
mydict.update(updatemydict)
print(mydict)

#5 method
print(mydict.get("yukti")) #PRINTS VALUE ASSOCIATED WITH KEY "YUKTI"
print(mydict["yukti"]) #PRINTS VALUE ASSOCIATED WITH KET "YUKTI"

#NOW D/F B/W UPPER TWO PRINTS IS i.e. (.get) AND [] SYNTAX

print(mydict.get("yukti2")) #RETURNS NONE AS yukti2 IS NOT PRESENT IN DICTIONARY
print(mydict["yukti2"]) #THROWS AN ERROR AS yukti2 IS NOT PRESENT IN THE DICTIONARY