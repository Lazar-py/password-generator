import random

print('Welcome to the PyPassword Generator!')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letterNum = int(input('How many letters would you like in your password?\n'))
shuffledLetters = random.sample(letters, letterNum)
numberNum = int(input('How many numbers would you like in your password?\n'))
shuffledNumbers = random.sample(numbers, numberNum)
symbolNum = int(input('How many symbols would you like in your password?\n'))
shuffledSymbols = random.sample(symbols, symbolNum)

combinedList = []
combinedList.extend(shuffledLetters + shuffledNumbers + shuffledSymbols)
random.shuffle(combinedList)
print(''.join(combinedList))
