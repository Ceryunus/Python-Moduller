import datetime  # zaman
import math  # matematik
import os  # Dosya işlemleri
import random  # rastgele işlemler
import smtplib
# e posta gönerme
import ssl
from collections import Counter  # sayıcı :)
from email import encoders
from email.mime.base import MIMEBase
# mail 2. kısım
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *  # Gorsel Gui

import requests  # Veri çekmek için get ve post methodlarını barıdıran modül
from imap_tools import AND
# 3.kısım
from imap_tools import MailBox  # e-posta okuma

# os modülü(dosya işlemleri)

print(os.getcwd())  # şu an bulunduğum klasörün adi
print(os.listdir())  # şu an bulunduğum klasörün dizinindeki  diyer klasörler
print(os.listdir("C:/Users/Ts/PycharmProjects"))  # istediğim dizini gösrteriyor
print(
    os.chdir())  # normalde parmetresiz gönderdiğimiz komutlar hep calıstığımız klasörü gösrerir bu komut onun yerini deyistirmemizi sağlıyor

os.mkdir("C:/Users/Ts/PycharmProjects/deneme_kasoru")  # sadece kasör olusturur
print(os.listdir("C:/Users/Ts/PycharmProjects"))

os.rmdir("C:/Users/Ts/PycharmProjects/deneme_kasoru")  # klasör silme

# --------------------------------------------------------------------------------------------------------


# regex modülü (string işlemleri)

cumle = "Yunus emre nin isimi yunus emredir"
patern = "emre"

print(re.search(patern, cumle))  # ilk bulduğu yeri gösterior

durum = re.search(patern, cumle)  # class olduğu icin bir obje oluşturup sonradn istediğimiz bilgiyi gösterebiliyoruz
print(durum.span())
print(dir(durum))

for eslesme in re.findall(patern, cumle):  # tüm cümledeki emreyi buldu strin golarak döndürür
    print(eslesme)

for eslesme in re.finditer(patern, cumle):  # finditer ile span gibi functionlara eslesebiliyorum obje olarak döndürür
    print(eslesme.span(), eslesme.group())

# önemli !!!! Patren Oluştururken !
# \d Rakamlar                       base42          base\d\d
# \w harfler rakam                  R2-D2           \w\w\w\w\w
# \s 1 bolsuk                       Pimg Pong       Ping\sPong
# \D rakam değil                    base            \D\D\D\D
# \W karakter değil                 R2D2            \W\W\W\W
# \S bosluk değil                   PingPong        \S\S\S\S\S\S\S\S


# önemli !!!! Patren Oluştururken !
# []	A set of characters	"[a-m]"
# \	Signals a special sequence (can also be used to escape special characters)	"\d"
# .	Any character (except newline character)	"he..o"
# ^	Starts with	"^hello"
# $	Ends with	"world$"
# *	Zero or more occurrences	"aix*"
# +	One or more occurrences	"aix+"
# {}	Exactly the specified number of occurrences	"al{2}"
# |	Either or	"falls|stays"
# ()	Capture and group

cumle2 = "base42"
patern2 = r"base\d\d"
print(re.search(patern2, cumle2))

# --------------------------------------------------------------------------------------------------------

# random modülü

myList = [1, 3, "selam", "naber"]
print(random.random())  # 0 ile 1 arasında  random sayı üretir
print(random.uniform(1, 10))  # girilen 2 paremtre arası float bir değer döndürüyor
print(random.randint(1, 10))  # 2 değer arası int değer döndürür
print(random.choice(myList))  # bir liste arasından bir elemanı random olarak seciyor
print(random.sample(*[range(10)], k=5))  # listeden random 5 eleman secip gösteriyor

myList2 = [*range(10)]  #
print(myList2)  # rastgele kar bu listeyi demek
print(random.shuffle(myList2))  # fakat bunu tekrar listeye atmamalıyım cünkü none (boş bir değer dönüyor!
print(myList2)  #

# --------------------------------------------------------------------------------------------------------


# math modülü

print(round(7.6))  # virgüllü sayıyı normal yuvarlama
print(math.ceil(7.1))  # sayıyı hep üsteki tamsayıya yuarlar
print(math.floor(7.9))  # sayııy hep aşağıdaki tamsayıya yuvarlar
print(math.factorial(5))  # faktorial hesavı
print(math.pow(2, 3))  # üs almaya yarıyor 2 nin 3. kuvveti

# --------------------------------------------------------------------------------------------------------


# collection modülündeki Counter methodu sayaç işlevi görüyor

myList = [*range(10)]
Liste1 = random.sample(myList, k=4)
Liste2 = random.sample(myList, k=4)
Liste3 = random.sample(myList, k=4)
Liste4 = random.sample(myList, k=4)

listeListesi = [Liste1, Liste2, Liste3, Liste4]
listeToplam = Liste1 + Liste2 + Liste3 + Liste4
print(listeListesi)
print(listeToplam)

for index, liste in enumerate(
        listeListesi):  # 2 tane eleman döndürdüğü icin enumarete 1. eleman ile 2. eleman arasına virgül koydduk
    print(f"{index + 1}.Liste  {liste}")

kactane = Counter(
    listeToplam)  # bu fonnksiyonun adı sayaç yani bir listedeki eleman kac kere tekrarlandığını bize gösteriyor
print(kactane)

sarki = """Hazin geliyor hazin geliyor
Geceler ömrümden
Sevinçler derdimden
Yaşamak ölmekten hazin geliyor
Hazin geliyor hazin geliyor
Geceler ömrümden
Sevinçler derdimden
Yaşamak ölmekten hazin geliyor"""
sarkis = Counter(sarki.lower().split()).most_common(
    4)  # stringi lovere indirdim sonra kelimelere ayırıp en cok olab 4 tane kelimeyi ekran ayazdırdım

print(sarkis)

# --------------------------------------------------------------------------------------------------------


# datetime modülü(zaman işleri)

# datetime.date komutuyla yapılanlar
bugun = datetime.date.today()  # bugünün  tarihi veriyor
print(bugun)

dun = datetime.date(2021, 5, 8)  # belli tarihleri de kullanabiliyoruz
print(dun)

# datetime en büyük avantajı tarihler artasınada matematiksel işlemler yapabiliyorux
print(bugun - dun)

yarin = bugun + datetime.timedelta(days=1)  # 1 gün ekle tarihe dedik
print(yarin)

zamanaraligi = bugun - dun  # tarihler arsı zaman aralığını bulma !
print(zamanaraligi.days)

print(bugun.year, bugun.month, bugun.day)
print(bugun.__getattribute__("month"))  # dunder methoduyla da ulaşabiliyoruz

print(datetime.date.isocalendar(bugun))  # yıl , hafta ,  haftanın kacıncı günü
print(datetime.date.weekday(bugun))

print(datetime.date.ctime(bugun))

# datetime.time komutuyla yapılanlar

zaman = datetime.time(21, 15, 30)  # saat 21:15:30  olduğunu zaman deyişkenine atıyoruz
print(zaman)
print(zaman.hour, zaman.minute, zaman.second)

dt = datetime.datetime(2021, 5, 9, 11, 35, 5)  # hem tarih hem de zaman ın 1 seferde oluşturabilyoruz
print(dt)
print(dt.hour, dt.minute)


# --------------------------------------------------------------------------------------------------------


# decaratorler :bir function önceden veya sonradan calıştırmak istediğim komutlar olduğu zaman kullanılack !

# argümansız olanı:

def deco(f):
    def wrapper():
        print("başlama")
        f()
        print("bitis")

    return wrapper()


@deco
def yazdir():
    print("yunus")


# argümanlı olanı
def deco(f):
    def wrapper(*args):
        print("baslangic")
        f(*args)
        print("bitis")

    return wrapper


@deco
def toplama(a, b):
    print(a + b)


toplama(4, 6)


# argümanle + deco fonksiyonuna da argüman ekilyerek gönderme
def deco(msg1, msg2):
    def ara_fonksiyon(f):
        def wrapper(*args):
            print(msg1)

            f(*args)

            print(msg2)

        return wrapper

    return ara_fonksiyon


@deco("Decodan gönderilen 1. argüman", "decoodan gönderilen 2. argüman")
def toplama(a, b):
    print(a + b)


toplama(4, 5)

# decaratorler örneği : süre ölçme bir fonksiyon ne kadar sürede calışıyor gibi :X

import time


# baslangıc_zamani=time.time()
# print(type(baslangıc_zamani))
# bitis_zamani=time.time()
# print(bitis_zamani-baslangıc_zamani)
#
def sure_olc(f):
    def wrapper(*args):
        baslangıc_zamani = time.time()
        print(baslangıc_zamani)
        f(*args)
        bitis_zamani = time.time()
        print(bitis_zamani)
        print(bitis_zamani - baslangıc_zamani)

    return wrapper


@sure_olc
def fac(sayi):
    fact = 1
    while sayi > 1:
        fact *= sayi
        sayi -= 1
    print(f"faktoriyel : {fact}")


fac(100)

# --------------------------------------------------------------------------------------------------------


# request modülü

bolgeler_URL = "https://data.police.uk/api/forces"
print(requests.get(bolgeler_URL))  # 200 kodu döndürürse başarılı omuştır
response = requests.get(bolgeler_URL)
print(response.status_code)
print(response.url)
print(response.text)  # string olarak gösteriyor
print(response.json())  # liste olarak gösteriyor

# 1 parametre gönderme

# https://data.police.uk/api/crime-categories?date=2011-08
suc_katagorileri_URL = "https://data.police.uk/api/crime-categories"
payload = {
    "date": "2020-01"}  # linek parametre veriyoruz yukarıdaki commandli olan yerde göründüğü gibi ? işaretinden sonra olan yerler parametler olarak gözüküyor
response = requests.get(suc_katagorileri_URL, params=payload)
print(response.status_code)  # sorun olmadığını gördük 200 ü görünce
print(response.url)  # linkim güncellenmiş :S
print(response.json())

# 1 den fazl parametre gönderme

suc_URL = "https://data.police.uk/api/crimes-no-location"
payload = {
    "category": "all-crime",
    "force": "city-of-london",
    "date": "2020-01"
}
response = requests.get(suc_URL, params=payload)
print(response)  # 200 gördk yani calişti
print(response.json())

# --------------------------------------------------------------------------------------------------------

# tkinter modülü

master = Tk()
master.title("İlk Kez")
canvas = Canvas(master, height=600, width=850)  # pencere boyutu
# pack   place  grid arayüze  yerleştirme paketleri
canvas.pack()

frame_ust = Frame(master, bg='black')
frame_ust.place(relx=0.13, rely=0.15, relheight=0.2, relwidth=0.75)  # x_konum , y_konum , genişlik , uzunluk

frame_sol = Frame(master, bg='black')
frame_sol.place(relx=0.13, rely=0.36, relheight=0.55, relwidth=0.20)  # x_konum , y_konum , genişlik , uzunluk

frame_sag = Frame(master, bg='black')
frame_sag.place(relx=0.34, rely=0.36, relheight=0.55, relwidth=0.54)  # x_konum , y_konum , genişlik , uzunluk

ust_label = Label(frame_ust, bg="white", text=" Hatirlatma : ", height=1, font="bold")
ust_label.pack(padx=5, pady=10, side=LEFT)

E1 = Entry(frame_ust, bd=5)
E1.pack(padx=10, pady=10, side=RIGHT)

ust_label2 = Label(frame_ust, bg="white", text=" Entrybox : ", height=1, font="bold")
ust_label2.pack(padx=10, pady=10, side=RIGHT)

# dropdown,optionmenu,listbox menu olusturma
hatirlatma_opsiyonu = StringVar(frame_ust)
hatirlatma_opsiyonu.set("Seçenekler")  # default :

hatirlatma_acilirmenu = OptionMenu(

    frame_ust,
    hatirlatma_opsiyonu,
    "seçenek1",
    "seçenek2",
    "seçenek3"
)
hatirlatma_acilirmenu.pack(padx=5, pady=10, side=LEFT)

master.mainloop()

# --------------------------------------------------------------------------------------------------------

# ssl ile mail gönderme işelmi

kullanici = 'email'
sifre = "sifre"
alici = 'aliciEmaili'
mesaj = "deneme"
baslik = "Python gonderisi"

context = ssl.create_default_context()
port = 465
host = "smtp.gmail.com"

# basit kullanımı sadece e porstanını mesjınını gönderiyor
eposta_sunucus = smtplib.SMTP_SSL(host=host, port=port, context=context)
eposta_sunucus.login(kullanici, sifre)
eposta_sunucus.sendmail(kullanici, alici, mesaj)

# 2. yömtede mail

email_user = 'email'
email_password = "sifre"
email_send = 'alici'

subject = 'Deneme Python'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Merhaba Python'
msg.attach(MIMEText(body, 'plain'))

filename = 'pythonexedonüştürme.txt'
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_user, email_password)

server.sendmail(email_user, email_send, text)
server.quit()
print("bitti")

# e Posta okuma

posta_kutusu = MailBox('imap.gmail.com')
posta_kutusu.login("email", "sifre", initial_folder="INBOX")
kriter = AND(date_gte=datetime.date(2021, 1, 1), from_="alici")
for massage in posta_kutusu.fetch(kriter):
    print(massage.text)
