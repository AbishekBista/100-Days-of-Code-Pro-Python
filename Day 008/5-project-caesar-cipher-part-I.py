print('''

 _____                            
/  __ \                           
| /  \/ __ _  ___  ___  __ _ _ __ 
| |    / _` |/ _ \/ __|/ _` | '__|
| \__/\ (_| |  __/\__ \ (_| | |   
 \____/\__,_|\___||___/\__,_|_|                                                          
 _____ _       _                  
/  __ (_)     | |                 
| /  \/_ _ __ | |__   ___ _ __    
| |   | | '_ \| '_ \ / _ \ '__|   
| \__/\ | |_) | | | |  __/ |      
 \____/_| .__/|_| |_|\___|_|      
        | |                       
        |_|                       

      ''')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, text, shift):
    output_word = ""
    for letter in text:
        if letter in alphabet:
            index_of_letter = alphabet.index(letter)
            if direction == 'encode':
                new_position = (index_of_letter + shift) % 26
            elif direction == 'decode':
                new_position = index_of_letter - shift
            
            output_word += alphabet[new_position]
        else:
            output_word += letter
    
    print(output_word)

wanna_play = True

while wanna_play == True:
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt: ")
    if direction != 'encode' and direction != 'decode':
       print("Wrong option entered. Exiting...")
       break
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    
    caesar(direction, text, shift)
    
    play_again = input("Do you wanna play again? Type 'yes' to play again. Otherwise type 'no': ")
    
    if play_again == 'no':
        print('Exiting...')
        wanna_play = False
    elif play_again == 'yes':
        continue
    else:
        print('You typed a wrong option. Exiting...')
        break
