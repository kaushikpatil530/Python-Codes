#a = input("Enter your name : \n")
#print(" Good morning, " + a)




letter  = ''' Dear <|Name|> ,
                   you Are Selected !
                   <|Date|>  '''


name = input(" Enter Name Here : \n")
date = input(" Enter Date Here : \n")


letter = letter.replace(" <|Name|>", name)
letter = letter.replace(" <|Date|>",date)

print(letter)