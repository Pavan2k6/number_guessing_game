import random
x = random.randint(1,100)
attempts = 0

while True:
    y = int(input("Enter the number: "))
    attempts += 1

    if y == x:
        print("correct")
        print("You guessed in " + str(attempts) + " attempts")
        break

    elif y > x:
        print("high")

    else:
        print("low")
      
