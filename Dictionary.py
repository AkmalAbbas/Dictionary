import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

# Getting meaning of word
def Translate(word):
    word = word.lower()
    if word.lower() in data:
        return data[word]

    elif len(get_close_matches(word , data.keys())) > 0:
        yn = input(f"Did you mean {get_close_matches(word,data.keys())[0]} instead? Enter Y if yes N if No : ")
        if yn.lower() == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn.lower() == "n":
            return "Words doesnot exist"
        else:
            return "We dont understand sorry"
    else:
        print("Words doesnot exist")

word = input("Enter word to search : ")
output = Translate(word)

if type(output) == list:
    for item in output:
        print(item,end='\n')
else:
    print(output)