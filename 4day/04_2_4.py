#-*- coding: euc-kr -*-
character = {
    "name": "���",
    "level": 12,
    "items": {
        "sword": "�Ҳ��� ��",
        "armor": "Ǯ�÷���Ʈ"
    },
    "skill": ["����", "���� ����", "���� ���� ����"]
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
