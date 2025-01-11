num = int(input("ENTER THE NUM: \n"))

prime = True

for i in range(2,num):
    if(num%i==0):
        prime = False
        break

if prime:
    print("THE NUMBER YOU HAVE ENTERED IS PRIME NUMBER....")
else:
        print("THE NUMBER YOU HAVE ENTERED IS NOT A PRIME NUMBER....")
