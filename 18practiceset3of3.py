# WAP TO DETECT DOUBLE SPACES IN A STRING

a='THIS STATEMENT INCLUDES  DOUBLE SPACE AND SINGLE SPACE TOO! THANKYOU FOR DETECTING!'
c=a.find("  ")
print(c)

b=a.find(" ")
print(b)