import string
import random


def gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.punctuation
    s4 = string.digits

    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    random.shuffle(s)
    passlen = int(input("Enter Password Length : "))
    print("".join(s[0:passlen]))

gen()