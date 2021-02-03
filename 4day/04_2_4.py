#-*- coding: euc-kr -*-
character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
    }

for key in character:
    if type(character[key]) is dict:
        for item in character[key]:
            print("{0} : {1}".format(item, character[key][item])) 

    elif type(character[key]) is list:
        for i in character[key]:
            print("{0} : {1}".format(key, i))

    else : 
        print("{0} : {1}".format(key, character[key])) 
