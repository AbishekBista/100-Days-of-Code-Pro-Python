print("Welcome to the Love Calculator")

your_name = input("What is your name? ").lower()
their_name = input("What is their name? ").lower()

t_count = your_name.count('t') + their_name.count('t')
r_count = your_name.count('r') + their_name.count('r')
u_count = your_name.count('u') + their_name.count('u')
e_count = your_name.count('e') + their_name.count('e')

l_count = your_name.count('l') + their_name.count('l')
o_count = your_name.count('o') + their_name.count('o')
v_count = your_name.count('v') + their_name.count('v')
e_count_again = your_name.count('e') + their_name.count('e')

true_count = t_count + r_count + u_count + e_count
love_count = l_count + o_count + v_count + e_count_again

love_percentage = 10 * true_count + love_count

if love_percentage < 10 or love_percentage > 90:
    print(f"Your score is {love_percentage}, you go together like coke and mentos.")
elif love_percentage >=40 and love_percentage <= 50:
    print(f"Your score is {love_percentage}, you are alright together.")
else:
    print(f"Your score is {love_percentage}")

