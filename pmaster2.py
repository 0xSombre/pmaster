import socket
import os
import sys

print("""
0- çıkış
1- ip doğrulama
2- web ip öğrenme
3- mac adresi öğrenme
""")

soru = input("işlem seçiniz: ")

if soru == "1":
    ip = input("ip adresini giriniz: ")
    try:
       socket.inet_aton(ip)
       print("Bu ip adresi vardır")
    except socket.error:
       print("Bu ip adresi yoktur")

elif soru == "2":
    url = input("url giriniz: ")
    print("İpv4 adresi:",socket.gethostbyname(url))
elif soru == "3":
    tekrarla = 0  
    while tekrarla == 0:  
        intp = raw_input("192.168.1.")  
        komut = "nbtstat -a 192.168.1." + intp 
        os.system(command)  
        raw_input()  
        os.system("CLS")
elif soru == "0":
    keyboardInterrupt()
else:
    print("hatalı kelime")
