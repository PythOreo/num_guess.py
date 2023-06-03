from random import choice
comp = choice(range(1, 50))
tries = 0  
while True:
    try: 
        player = int(input("Please input a num in the range of 50: "))
        tries += 1
        if player > comp: 
            print("Your choice is bigger")
        elif player < comp: 
            print("Your choice is smaller") 
        else: 
            print(f"Bingo! You choosed the correct num in {tries} tries")
            break
    except ValueError: 
        print("Please input a number")

    

    
