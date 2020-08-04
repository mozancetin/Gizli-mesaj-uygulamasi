def Encrypt(msg, key):

    msg = str(msg)
    encryption = ""
    for i in msg:
        encryption += chr(int(ord(i)) + int(key))
    return encryption


def Decrypt(msg, key):

    msg = str(msg)
    decryption = ""
    for i in msg:
        decryption += chr(int(ord(i)) - int(key))
    return decryption

        
def Brute_Force(msg):
    key = 0
    while(True):
        message = Decrypt(msg, key)
        print("This could be your message. If it doesn't make sense, keep looking: " + message)
        verification = str(input("Keep Looking/Stop? (K/S)\n"))
        if verification == 's' or verification == 'S':
            return message
        elif verification == 'k' or verification == 'K':
            print(50*"\n")
            key += 1
        else:
            print("Wrong answer option. Try again...")

Brute_Force(Encrypt("deneme",15))
