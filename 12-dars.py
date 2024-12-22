n = int(input("1-Sonni kiritng:"))
k = int(input("2-Sonni kiritng:"))
for i in range (k):
    print(n)


a = int(input("1-Sonni kiritng:"))
b = int(input("2-Sonni kiritng:"))
for i in range (a, b+1):
    print(i)


a = int(input("1-Sonni kiritng:"))
b = int(input("2-Sonni kiritng:"))
for i in range (b, a-1, -1):
    print(i)


a = int(input("Konfertni kilosini  kiritng:"))
for i in range(1, 11):
    print(f"{i}, kilo kanferni narhi {i * a}")


a = int(input("Konfertni kilosini  kiritng:"))
for i in range(1, 10):
    print(f"{i/10:.1f}, kilo kanferni narhi {i/10 * a:.1f}")


a = int(input("Konfertni kilosini  kiritng:"))
for i in range(1, 6):
    print(f"{i/5:.1f}, kilo kanferni narhi {i/5 * a:.1f}")


a = int(input("1-Sonni kiritng:"))
b = int(input("2-Sonni kiritng:"))
s = 0
for i in range (a, b+1):
    s = s+i
print(f"Yig`indisi{s}")


a = int(input("1-Sonni kiritng:"))
b = int(input("2-Sonni kiritng:"))
s = 1
for i in range (a, b+1):
    s = s*i
print(f"Ko`paytmasi{s}")


a = int(input("1-Sonni kiritng:"))
b = int(input("2-Sonni kiritng:"))
s = 1
for i in list(range(a, b+1)):
    s += i**2
print(f"Kvadrati{s}")