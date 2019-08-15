a = raw_input("Prima dari : ") #mendapatkan input dari user
b = raw_input("Sampai : ") #mendapatkan input dari user

print "bilangan prima dimulai dari", a
print "berakhir di", b

a = int(a) #merubah a menjadi integer
b = int(b) #merubah b menjadi integer
for n in range(a,b+1): #menelusuri bilangan
    prima = True #anggap n adalah prima
    for i in range(2,n): #i adalah bilangan antara 2 sampai n-1
        if n % i ==0: #jika i membagi n
   prima = False #  maka bukan prima
            break #keluar dari perulangan
    if prima: #jika prima = True
        print n, #tampilkan n