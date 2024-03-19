import re

text_to_receive = input()
pattern_for_hidden_eggs = r"[#@]{1,}([a-z]{3,})[#@]{1,}[^a-zA-Z0-9]*/{1,}(\d+)\/{1,}"

matches = re.findall(pattern_for_hidden_eggs, text_to_receive)

if matches:
    for color, amount in matches:
        print(f"You found {amount} {color} eggs!")