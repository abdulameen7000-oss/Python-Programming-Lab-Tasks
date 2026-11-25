#Implement a Python program that counts how many times each word appears in a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print("Word Frequency:")
for word, frequency in count.items():
    print(word, ":", frequency)