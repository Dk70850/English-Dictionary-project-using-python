import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]        
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("did you mean %s instead? enter y if yes , or n if no." % get_close_matches(w, data.keys())[0])
        if yn == "y" :
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "n" :
            return "the word doesnt exist "
        else:
            return "we didnt understand your entry "        
    else:
        return "the word doesnt exist "    

word = input("enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)        