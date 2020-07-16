def msgToNum(msg):
    iki = ["a","b","c","ç"]
    üç = ["d","e","f"]
    dört = ["g","h","ı","i"]
    beş = ["j","k","l"]
    altı = ["m","n","o","ö"]
    yedi = ["p","q","r","s","ş"]
    sekiz = ["t","u","ü","v"]
    dokuz = ["w","x","y","z"]
    sıfır = [" "]

    mesaj = ""
    
    
    
    for i in msg:
        if i in iki:
            kd = int(iki.index(i)+1)
            mesaj = mesaj + (str(2) * kd)

        elif i in üç:
            kd = int(üç.index(i)+1) 
            mesaj = mesaj + (str(3) * kd)  

        elif i in dört:
            kd = int(dört.index(i)+1)
            mesaj = mesaj + (str(4) * kd)

        elif i in beş:
            kd = int(beş.index(i)+1)
            mesaj = mesaj + (str(5) * kd)

        elif i in altı:
            kd = int(altı.index(i)+1)
            mesaj = mesaj + (str(6) * kd)

        elif i in yedi:
            kd = int(yedi.index(i)+1)
            mesaj = mesaj + (str(7) * kd)

        elif i in sekiz:
            kd = int(sekiz.index(i)+1)
            mesaj = mesaj + (str(8) * kd)

        elif i in dokuz:
            kd = int(dokuz.index(i)+1)
            mesaj = mesaj + (str(9) * kd)

        elif i in sıfır:
            mesaj = mesaj + str(0)
        mesaj = mesaj + "-"
    mesaj = mesaj[:-1]
    return mesaj


def numToMsg(num):
    iki = ["a","b","c","ç"]
    üç = ["d","e","f"]
    dört = ["g","h","ı","i"]
    beş = ["j","k","l"]
    altı = ["m","n","o","ö"]
    yedi = ["p","q","r","s","ş"]
    sekiz = ["t","u","ü","v"]
    dokuz = ["w","x","y","z"]
    sıfır = [" "]
    
    ilk = None
    kd = 1 
    yazı = ""
    
    for i in num:
        if ilk == None:
            ilk = i
            

        else:
            if i == ilk:
                kd += 1
            else:
                #print(kd,"Sayı:",ilk)
                
                if ilk == "0":
                    yazı += " "

                elif ilk == "2":
                    yazı += iki[kd-1]

                elif ilk == "3":
                    yazı += üç[kd-1]

                elif ilk == "4":
                    yazı += dört[kd-1]

                elif ilk == "5":
                    yazı += beş[kd-1]

                elif ilk == "6":
                    yazı += altı[kd-1]

                elif ilk == "7":
                    yazı += yedi[kd-1]

                elif ilk == "8":
                    yazı += sekiz[kd-1]

                elif ilk == "9":
                    yazı += dokuz[kd-1]
                
                ilk = i
                kd = 1
                
    
    #print(kd,"Sayı:",ilk)

    if ilk == "-":
        yazı += " "

    elif ilk == "2":
        yazı += iki[kd-1]

    elif ilk == "3":
        yazı += üç[kd-1]

    elif ilk == "4":
        yazı += dört[kd-1]

    elif ilk == "5":
        yazı += beş[kd-1]

    elif ilk == "6":
        yazı += altı[kd-1]

    elif ilk == "7":
        yazı += yedi[kd-1]

    elif ilk == "8":
        yazı += sekiz[kd-1]

    elif ilk == "9":
        yazı += dokuz[kd-1]

    return yazı

#print(msgToNum("deneme bir iki üç"))
#print(numToMsg(msgToNum("deneme bir iki üç")))



