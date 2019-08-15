def segitigaTree():
    centre=35
    inicial=1
    level=9 #input("Tinggi dari piramid? \n\t")
    for height in range (inicial,level+1):
        for index in range (1,centre-height):
            sys.stdout.write (' ')
        sys.stdout.write (str(inicial))
        for index in range (inicial+1,height):
            sys.stdout.write (str(index))
        for index in range (height,inicial,-1):
            sys.stdout.write (str(index))
        if height>1:
            sys.stdout.write ('1')
        sys.stdout.write ('\n')
segitigaTree()