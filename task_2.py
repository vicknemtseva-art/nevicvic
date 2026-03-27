s = 25
byte = 4
str = 50
kn = 100
mb = 1.44*1024*1024
x = s*byte*str*kn
z = mb / x
books = int (mb // x)
print("Количество книг, помещающихся на дискету:", books)
