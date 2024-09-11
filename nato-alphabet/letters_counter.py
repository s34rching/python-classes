import re

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = [re.sub('[^a-zA-Z0-9 \n\.]', '', word) for word in sentence.split(" ")]

result = {word:len(word) for word in words}

print(result)
