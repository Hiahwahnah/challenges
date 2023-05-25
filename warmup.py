# Prompt user to enter a number and then a word and print that word that number of times

num = int(input("Enter a number: "))
word = input("Enter a word: ")

# for loop to spice it up by making every other letter capital and then lowercase
output = ""
for i, letter in enumerate(word):
    if i % 2 == 0:
        output += letter.lower()
    else:
        output += letter.upper()

output = (output + " ") * num
print(output.strip())