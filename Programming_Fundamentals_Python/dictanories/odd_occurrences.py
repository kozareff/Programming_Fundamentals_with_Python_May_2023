words = input().split(" ")
dictonary = {}

for word in words:
    word_lower = word.lower()

    if word_lower not in dictonary:
        dictonary[word_lower] = 0
    dictonary[word_lower] += 1

for key, value in dictonary.items():
    if value % 2 != 0:
        print(key, end=" ")