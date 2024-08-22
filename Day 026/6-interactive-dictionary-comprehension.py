sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_list = sentence.split()

result = {word:len(word) for word in word_list}
print(result)
