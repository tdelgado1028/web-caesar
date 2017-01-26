alphabet = "abcdefghijklmnopqrstuvwxyz"

def alphabet_position(Char):

    for i in range(len(alphabet)):
        if Char == alphabet[i] or Char == alphabet[i].upper():
            return i

def rotate_character(Char, Rot):

    if Char.isalpha():
        encrypted = ""
        NewCharPos = alphabet_position(Char) + Rot

        if NewCharPos <26:
            encrypted += alphabet[NewCharPos]
        else:
            encrypted += alphabet[NewCharPos %26]


        if Char.isupper():
            return encrypted.upper()
        else:
            return encrypted

    return Char


def encrypt(Msg, Rot):
    FinalMsg = []

    for i in range (len(Msg)):
        for j in range(len(Msg[i])):

            FinalMsg.append(rotate_character(Msg[i][j], Rot))

    FinalMsg = "".join(FinalMsg)

    return FinalMsg
