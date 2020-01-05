import math
#### Tugas nya Azizah
#### 02181031
print ('\n Hello, what  is your name?')
name = input()
print('\n Hello,' ,name ,"Keep Smile and Learn Coding")

print("\n welcome to Python 3.x")

print("\n Program Menghitung Luas dan volume bola")
print(50*"+")

### menghitung luas permukaan bola
print("\n______Hitung Luas Permukaan Bola______")
r = int(input("Masukan nilai jari-jari : "))
pi =22/7

LuasPB = 4 * pi * math.pow(r, 2)
print("\n Luas permukaan bola adalah : {0:.2f}".format(LuasPB ) )


###menghitung volume bola
print("\n____Hitung Volume Bola_____")
r = int(input("Masukan nilai jari-jari : "))

volume = 4/3 * math.pi * math.pow(r, 3)
print("\n Volume bola adalah: {0:.2f}".format( volume ) )

print("Thank you," ,name ,"For using my program")
input("\n\n Press enter key to exit")
print(50*"+")



