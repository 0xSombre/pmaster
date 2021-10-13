import socket

print("""
1- ip doğrulama
2- web ip öğrenme
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
else:
    print("lütfen tekrar deneyiniz")
