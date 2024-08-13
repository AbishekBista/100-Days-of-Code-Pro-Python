input_heights = input("Enter a list of heights: ")

heights_list = input_heights.split()
sum = 0
for heights in heights_list:
    sum += int(heights)

average_height = int(sum / len(heights_list))

print(f"The average height is {average_height}")
