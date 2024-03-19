sectret_message = input().split(" ")
decoded_message = []

for word in sectret_message :
    chair_code = ''
    text_part = ''
    while not word.isalpha() :
        chair_code += word[0 :1]
        word = word[1 :]
    new_word = list(word)
    new_word[0], new_word[-1]=new_word[-1],new_word[0]
    word = ''.join(new_word)
    text_part = word
    letter = chr(int(chair_code))
    decoded_message.append(letter + text_part)
print(' '.join(decoded_message))