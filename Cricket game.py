import random
print("CRICKET GAME")
d=random.randint(1,50)
c=0
print("Target:",d)
while (True):
    a=int(input("Enter the number: "))
    b=random.randint(1,7)
    if a==b:
        print("You Loose")
        break
    if a>6:
        print("ERROR")
        continue
    if a!=b:
        c=c+a
        print("Your score is :",c)
    if c>=d:
        print("Congrulations")
        print("YOU WON")
        break