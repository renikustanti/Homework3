#kuadrat
a = int(input("Masukan Nilai A = "))
y = int(input("Masukan Nilai Pangkat B = "))

def kuadrat(a,b):
    if y == 0:
        return 1
    else:
        return a * pangkat(a,b,-1)
print("%d dipangkat %d = %d" %(a,b,pangkat(a,b)))