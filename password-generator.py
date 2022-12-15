import random
def salasana(luku):
    i = 0
    length = 8
    lista = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","V","W","X","Y","Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    if luku != "":
        if type(luku) == int:
            if luku >= 0:
                length = luku
    
    while i < length:
        print(lista[random.randint(0, 61)], end ="")
        i+=1
    print("")
    
pituus = int(input("Choose the length of the password: "))
salasana(pituus)
