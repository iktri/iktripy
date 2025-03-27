binary = 10100110010011101001001001010111
c = str(binary)
print('Binary = ', binary)

# konversi IBM
sign = int(c[0])
x = 7
y = 0
exp = 0
while x >= 1:
    q = (c[x])
    exp += int(q) * (2 ** y)
    x -= 1
    y += 1
w = 8
r = -1
fr = 0
while w <= 31:
    m = (c[w])
    fr += int(m) * (2 ** r)
    w += 1
    r -= 1
v = exp - 64
ibm = (-1) ** sign * (16) ** v * (fr)
print('Hasil konversi IBM adalah ', ibm)

# konversi ieee
sign = int(c[0])
x = 8
y = 0
exp = 0
while x >= 1:
    q = (c[x])
    exp += int(q) * (2 ** y)
    x -= 1
    y += 1
w = 9
r = -1
fr = 0
while w <= 31:
    m = (c[w])
    fr += int(m) * (2 ** r)
    w += 1
    r -= 1
z = exp - 127
ieee = (-1) ** sign * (1 + fr) * (2 ** z)
print('Hasil konversi IEEE adalah ', ieee)