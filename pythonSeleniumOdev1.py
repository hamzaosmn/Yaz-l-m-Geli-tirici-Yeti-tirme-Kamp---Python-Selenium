# string(str) => metinsel veri tipi

İsim = "Hamza"

# integer(int), float and complex => numerik(sayısal) veri tipleri

x = 10       # int => tam sayı veri tipi

y = 9.9      # float => ondalıklı sayı veri tipi

z = 5j       # complex => ileri düzey matematik işlemleri için kullanılan veri tipi

# list => liste veri tipi

ogrenciListesi = ["Ahmet","Ayşe","Mehmet","Fatma"]

# tuple => listeye benzeyen bir veri tipi

tuple1 = ("Ahmet", 10, 5.2,'abc')

# boolen => mantıksal veri tipi (True or False)

x = 10
y = 15

print(x > y)
print(x < y)

# dictionary => key-value ciftlerinden oluşan ilişkisel diziler gibi çalışan veri tipi

dict1 = {'name':'Hamza', 'code': 1122, 'deptName':'Civil Engineering'}

###########################################################################################################################################

# Kodlama.io sitesindeki kategori ve eğitmen => list

Kategori = ["Tümü","Proglamla"]                        
Eğitmen = ["Engin Demiroğ", "Halit Enes Kalaycı"]      

# Kodlama.io sitesindeki kurs isimleri, açıklamalar ve başlıklar => str

stringOrnek1 = "Yazılım Geliştiric iYetiştirme Kampı "
stringOrnek2 = "Genel Duyuru"
stringOrnek3 = "Kamp Programı"

# Kodlama.io sitesindeki '27% tamamlandı've '330 Yorum' gibi kısımlardaki sayısal yerler => int

tamamlandiYuzdesi = 27
yorumSayisi = 330

###########################################################################################################################################

# Kodlama.io sitesindeki notifications kısmında şart blokları kullanılmış.

answer = input("onayTiki açılsın mı:")

if answer == "Evet":
    print("send email")
elif answer == "Hayır":
    print("don't send email")





