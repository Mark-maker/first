import random
battleship=[]
for i in range(5):
    battleship.append(['O']*5)
def printboard():
    for i in battleship:
        print (" ".join(i).replace("'",""))
ship_row=random.randrange(0,5)
ship_column=random.randrange(0,5)

def play():
    chances=5
    while True:
        printboard()
        row=input("Enter guess row: ")
        col=input("Enter guess coloumn: ")
        if row==ship_row and col==ship_column:
            print("Oh My God .. You sunk my Ship, You win....!!")
        else:
            if int(row)>4 or int(col)>4:
                print ("You've gone out of the sea dear")
            elif battleship[int(row)][int(col)]=="X":
                print ("Oops..! You've selected it already")
                chances+=1
            else:
                print ("Sry babz you gotta try again.. {} chances left".format(chances))
                battleship[int(row)][int(col)]="X"
            if chances==0:
                print ("Game Over..!!")
                break
        chances-=1
play()
