import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn= input("Did you mean %s instead? Enter Y if yes or N if no." %get_close_matches(w,data.keys())[0])
        if yn== "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N":
            return " we didnot understand the entry"

    else:
        return "The word doesn't exist. Please double check in."


word= input("enter the word:")
output = translate(word)
if type (output)== list:
    output= translate(word)
    for item in output:
        print(item)
else:
    print(output)
