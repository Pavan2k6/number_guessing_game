low = 1
high = 100

while True:
    y = (low + high)//2
    print("computer guess: ",y)

    feedback = input("L,H,C :")

    if feedback == 'C':
        print("correctly guessed!!")
        break
    elif feedback == 'H':
        high = y - 1
    elif feedback == "L":
        low = y + 1
    
        