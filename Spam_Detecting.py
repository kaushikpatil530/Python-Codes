text = input(" ENTER THE TEXT HERE : \n ")

if (" make a lot of money" in text):
    spam = True

elif (" pay money " in text):
    spam = True

elif(" click here " in text ):
    spam = True

else:
     spam = False 

if (spam == True) :
    print("THIS TEXT IS SPAM")

else:
    print("THIS TEXT IS NOT SPAM")