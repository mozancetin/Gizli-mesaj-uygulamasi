from çevirici import *
import pyperclip
while(True):
    print("""*********************************************************
Gizli Mesaj Yollama Programına Hoşgeldiniz. (v1.0)

1 | Program Hakkında Bilgi
2 | Mesajdan Numara Formuna Çeviri
3 | Numara Formundan Mesaja Çeviri

Çıkmak için "q" ya basın.

*********************************************************""")
    print("\n")
    secenek = input("Seçiminiz: ")
    print(50*"\n")
    if secenek == "q":
        break
    elif int(secenek) == 1:
        print("""*************************************************************************************

Bu program, küçük harfler ile girdiğiniz metinleri eski tuşlu
telefonların tuş takımına göre kodlar. Mesela 'a' harfi eski
tuşlu telefonlarda 2 rakamına 1 kez basarak oluşturulurdu.
Bunu 'Mesajdan Numara Formuna Çeviri' özelliği ile yapar.

Aynı zamanda bu numara formuna çevirdiğimiz mesajları da
'Numara Formundan Mesaja Çeviri' özelliği ile tekrar görüntüleyebiliriz.

-----------------------------------------

Programı Yapan: Mustafa Ozan Çetin

Github: /mozancetin

Sponsor: https://goyomod.com/

-----------------------------------------
*************************************************************************************""")
        input("\n\n 2. Kısım için enter'a basın. (1/2)")
        print(20*"\n")
        print("""*************************************************************************************

Test etmek için 'Mesajdan Numara Formuna Çeviri' seçerek 'deneme' yazın.
Yazınızın bir dizi sayı ve '-' lerden oluşan bir biçime geldiğini
göreceksiniz. O sayı dizini sizin panonuza kopyalanmış olacak.
Şimdi 'Numara Formundan Mesaja Çeviri' özelliğini seçerek 'yapıştır'
seçeneğine basalım. Bu sefer az önce panoya kopyaladığımız sayı dizini
bizim ilk başta yazmış olduğumuz 'deneme' yazısını ortaya çıkaracak.

Unutma bu program eğlence amaçlı yazılmıştır ve çok kolay bir şifreleme
yöntemi olduğu için hiçbir güvenlik sağlamaz.

NOT: Program sadece küçük harfleri ve 29 harfli Türk Alfabesi dışında
birkaç harfi kabul eder. (Örneğin x)

İyi eğlenceler :)

-----------------------------------------

Programı Yapan: Mustafa Ozan Çetin

Github: /mozancetin

Sponsor: https://goyomod.com/

-----------------------------------------
*************************************************************************************""")
        input("\n\nDevam etmek için enter'a basın.")
    elif int(secenek) == 2:
        print("""*********************************************************
Mesajdan Numara Formuna Çeviri

1 | Yapıştır
2 | Kendin Yaz

Çıkmak için "q" ya bas.

*********************************************************""")
        secenek2 = input("Seçiminiz: ")
        print(50*"\n")
        if secenek2 == "q":
            print(50*"\n")
            continue
                
        elif int(secenek2) == 1:
            msg = pyperclip.paste()
            print("Mesajınız: '{}'".format(msg))
            secenek3 = input("Doğru mu? (E/H)\n")
            
            if secenek3 == "e" or secenek3 == "E":
                print(50*"\n")
                text = msgToNum(msg)
                print("Mesajın dönüştürüldü: ", text)
                print("Panoya kopyalanıyor.")
                pyperclip.copy(text)
                print("Panoya kopyalandı. İstediğiniz yere ctrl+v yaparak yapıştırabilirsiniz.")
                msg = None
                text = None
                input("\nDevam etmek için enter'a basın.")
            elif secenek3 == "h" or secenek3 == "H":
                print(50*"\n")
                print("İstediğiniz metini kopyalarak tekrar deneyiniz.")
                msg = None
                input("\nDevam etmek için enter'a basın.")
            else:
                print(50*"\n")
                print("Yanlış bir tuşa bastınız. Lütfen tekrar deneyiniz.")
                msg = None
                input("\nDevam etmek için enter'a basın.")
                
        elif int(secenek2) == 2:
            msg = input("Mesajını Yaz (Küçük harfler ile): ")
            print(50*"\n")
            text = msgToNum(msg)
            print("Mesajın dönüştürüldü: ", text)
            print("Panoya kopyalanıyor.")
            pyperclip.copy(text)
            print("Panoya kopyalandı. İstediğiniz yere ctrl+v yaparak yapıştırabilirsiniz.")
            msg = None
            text = None
            input("\nDevam etmek için enter'a basın.")
    elif int(secenek) == 3:
        print("""*********************************************************
Numara Formundan Mesaja Çeviri

1 | Yapıştır
2 | Kendin Yaz

Çıkmak için "q" ya bas.

*********************************************************\n""")
        secenek4 = input("Seçiminiz: ")
        print(50*"\n")
        if secenek4 == "q":
            print(50*"\n")
            continue

        elif int(secenek4) == 1:
            num = pyperclip.paste()
            print("Yapıştırdığınız numara formu: " + num)
            print("\n")
            secenek5 = input("Doğru mu? (E/H)\n")
            
            if secenek5 == "e" or secenek5 == "E":
                print(50*"\n")
                encoded_text = numToMsg(num)
                print("Gizli Mesaj: " + encoded_text)
                encoded_text = None
                num = None
                input("\nDevam etmek için enter'a basın.")
            elif secenek5 == "h" or secenek5 == "H":
                print(50*"\n")
                print("İstediğiniz metini kopyalarak tekrar deneyiniz.")
                num = None
                input("\nDevam etmek için enter'a basın.")
            else:
                print(50*"\n")
                print("Yanlış bir tuşa bastınız. Lütfen tekrar deneyiniz.")
                num = None
                input("\nDevam etmek için enter'a basın.")

        elif int(secenek4) == 2:
            num = input("Numara Formunu Girin: ")
            print(50*"\n")
            encoded_text = numToMsg(num)
            print("Gizli Mesaj: " + encoded_text)
            encoded_text = None
            num = None
            input("\nDevam etmek için enter'a basın.")
            

    print(50*"\n")
