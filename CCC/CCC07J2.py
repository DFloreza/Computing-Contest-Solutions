# define the emoticon list
eList = ["CU", ":-)", ":-(", ";-)", ":-P", "(~.~)", "TA", "CCC", "CUZ", "TY", \
"YW"]

# define the translation list
tList = ["see you", "I'm happy", "I'm unhappy", "wink", "stick out my tongue", \
"sleepy", "totally awesome", "Canadian Computing Competition", "because", "thank-you", \
"you're awesome"]

txt = input()

while txt != "TTYL":
    if txt not in eList:
        print(txt)
    else: 
        # proceed as normal
        # find the index of the inputted text
        translateIndex = eList.index(txt)
        newText = tList[translateIndex] 
        print(newText)
    
    txt = input()

if txt == "TTYL":
    print("talk to you later")
