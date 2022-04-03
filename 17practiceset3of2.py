# WAP TO FILL IN A LETTER TEMPLATE GIVEN BELOW WITH NAME AND DATE
# LETTER=DEAR</NAME/>
# YOU ARE SELECTED
# </DATE/>

a=input(" enter your name \n, " )
b=input("enter today's date ")

print("DEAR!", a)
print("YOU ARE SELECTED!")
print("DATE : ",b)


# ANOTHER METHOD

letter=''' Dear! <|NAME|>
Greetings from ABC COMPANY, I AM HAPPY TO TELL YOU ABOUT YOUR SELCTION! 
You are selected! 
Best Wishes And Regards! 
Yukti 
Date : <|DATE\>'''

name= input('Enter Your Name \n')
date= input('Enter Date ')
letter= letter.replace("<|NAME|>",name)
letter= letter.replace("<|DATE\>",date)
print(letter)

