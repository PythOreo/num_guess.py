from random import choice
comp = choice(range(1, 50))
x = 0
def print_msg(msg): 
    print(msg)   
while True:
    try: 
        player = int(input("Please input a num in the range of 50: ")) 
        if player > comp: 
            print_msg("Your choice is bigger")
            x += 1
        elif player < comp: 
            print_msg("Your choice is smaller") 
            x += 1
        else: 
            x += 1
            print(f"Bingo! You choosed the correct num in {x} tries")
            break
    except ValueError: 
        print("Please input a number")

    

    