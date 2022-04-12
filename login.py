while 1:
    userName = "mustafa"
    password = "12345asd"

    print("")
    kullaniciAdi=input("Giriş yapmak için kullanıcı adınızı girin: ")
    sifre=input("Giriş yapmak için şifrenizi girin: ")

    if kullaniciAdi == userName and sifre == password:
        print("Sisteme başarılı bir şekilde giriş yapıldı.")
        break
    elif kullaniciAdi != userName and sifre == password:
        print("Kullanıcı adı yanlış! Kontrol edip tekrar deneyin.")
    elif kullaniciAdi == userName and sifre != password:
        print("Şifreniz yanlış! Kontrol edip tekrar deneyin.")
    elif kullaniciAdi == password and sifre == userName:
        print("Yerlerini karıştırmış olabilirsin :) ")
    else:
        print("Kullanıcı adı veya şifreniz yanlış! Kontrol edip tekrar deneyin.")
