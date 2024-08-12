print('''                                
   /$$                                                                          
  | $$                                                                          
 /$$$$$$    /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$ /$$   /$$  /$$$$$$   /$$$$$$ 
|_  $$_/   /$$__  $$ /$$__  $$ |____  $$ /$$_____/| $$  | $$ /$$__  $$ /$$__  $$
  | $$    | $$  \__/| $$$$$$$$  /$$$$$$$|  $$$$$$ | $$  | $$| $$  \__/| $$$$$$$$
  | $$ /$$| $$      | $$_____/ /$$__  $$ \____  $$| $$  | $$| $$      | $$_____/
  |  $$$$/| $$      |  $$$$$$$|  $$$$$$$ /$$$$$$$/|  $$$$$$/| $$      |  $$$$$$$
   \___/  |__/       \_______/ \_______/|_______/  \______/ |__/       \_______/                                                                                                                                                       
                                                                         
 /$$           /$$                           /$$                                
|__/          | $$                          | $$                                
 /$$  /$$$$$$$| $$  /$$$$$$  /$$$$$$$   /$$$$$$$                                
| $$ /$$_____/| $$ |____  $$| $$__  $$ /$$__  $$                                
| $$|  $$$$$$ | $$  /$$$$$$$| $$  \ $$| $$  | $$                                
| $$ \____  $$| $$ /$$__  $$| $$  | $$| $$  | $$                                
| $$ /$$$$$$$/| $$|  $$$$$$$| $$  | $$|  $$$$$$$                                
|__/|_______/ |__/ \_______/|__/  |__/ \_______/                                                                                                         
      ''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You find yourself in a crossroad. Would you go left or right? Type 'left' or 'right' ").lower()

if(direction == "right"):
    print("Game over")
else:
    river_action = input("You've come to a lake. There's a lake in the middle. Would you swim or wait? Type 'swim' or 'wait' ").lower()
    if(river_action == "swim"):
        print("Game over")
    else:
        door_option = input("You see three doors, red, yellow and blue. Which one do you enter? Type 'red', 'yellow', or 'blue': ").lower()
        if door_option == 'red' or door_option == 'blue':
            print("Game over")
        else:
            print("You win!")