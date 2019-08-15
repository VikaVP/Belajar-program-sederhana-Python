n = 0
i = int(input("Masukan angka : "))
for k in range (1,i+1):
    print (k),
    if k == i :
        print ('='),
    else :
        print ('+'),
    n = n + k
    
print (n)