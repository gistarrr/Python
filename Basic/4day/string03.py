#-*- coding: euc-kr -*-
number = int(input("���� �Է�> "))

if number %2 == 0:
    print("\n".join([
        "�Է��� ���ڿ��� {}�Դϴ�.",
        "{}��(��) ¦���Դϴ�."
    ]).format(number, number))

else : 
    print("\n".join([
        "�Է��� ���ڿ��� {}�Դϴ�.",
        "{}��(��) Ȧ���Դϴ�."
    ]).format(number, number))