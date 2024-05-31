
class TooTiny(Exception):
    pass

class TooYoung(Exception):
    pass

class TooOld(Exception):
    pass

age = 35

try:
    if age < 7:
        raise TooTiny("Too tiny to cast the vote....")
    elif age < 18:
        raise TooYoung("Too young to cast the vote....")
    elif age > 100:
        raise TooOld("Too very old to cast the vote....")
    else:
        print("You can cast your valuable vote.....")
except TooTiny as t:
    print("Exception caught.....")
    print(t)
except TooYoung as y:
    print("Exception caught.....")
    print(y)
except TooOld as o:
    print("Exception caught.....")
    print(o)
finally:
    print("Voting completed.....")