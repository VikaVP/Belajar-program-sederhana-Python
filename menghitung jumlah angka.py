def Hitungvowel():
    kalimat= raw_input("Masukan kalimat : ")
    vokal= ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O' ]
    vok = 0
    for i in kalimat():
        if i in vokal :
            vok += 1
    vokal = len(kalimat)
   
print ("Jumlah huruf = ")