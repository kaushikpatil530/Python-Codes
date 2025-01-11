sub1 = int(input ( " ENTER SUB1 MARKS HERE :" ))
sub2 = int(input ( " ENTER SUB2 MARKS HERE :" ))
sub3 = int(input ( " ENTER SUB3 MARKS HERE :" ))

if ( sub1 < 33 or sub2 <33 or sub3 < 33 ):
    print(" SORRY...!  YOU ARE FAIL")

elif(sub1+sub2+sub3/3 < 40):
    print(" SORRY...!  YOU ARE FAIL")

else:
    print("CONGRATS....  YOU ARE PASS")