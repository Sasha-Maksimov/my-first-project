

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)
print('-----------------')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
i = 0
while i < 5:
    print(i)
    i = i + 1

print('-----------------------')

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = list(set(a) & set(b))
print(c)

print('-------------------------')

i = input('ведите слово:')
if i == i[::-1]:
    print(True)
else:
    print(False)
print('-----------------------------')

a = [1, 3, 5, 2, 4, 6, 7, 8, 9,]
print(f' {a[0]}; {a[-1]}')

print('-----------------------------')

a = set(['Тимур', 'Адам', 'Кайрат', 'Глеб', 'Саня'])
b = set(['Глеб', 'Кайрат', 'Саня'])
print(set(a) - set(b))

print('---------------------')

a = 'мы уехали путешествовать по миру'
x = a.count('у')
b = a.count('у')
print(b)

print('------------------------------')

l = 19
p = 23
loc = l
l = p
p = loc
print(l, p)


print('----------------------------')


def a(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)


a(8)

print('---------------------------')

loc = {'a': 3, 'b': 1, 'd': 6, 'c': 5, 'f': 4, 'e': 2}
for i in sorted(loc.items(), key=lambda para: para[1]):
    print(i)
print()
for i in sorted(loc.items(), reverse=True, key=lambda para: para[1]):
    print(i)

print('-------------------------')

loc = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
for i in sorted(loc.items(), reverse=True, key=lambda para: para[1])[:3]:
    print(i)

print('-------------------')

a = [30, 25,  60, 70, 45, 90, 85, 135]
result = list(filter(lambda x: not x % 15, a))
print(result)


print("---------------------------------")

loc1 = input("ведите число:")
loc2 = input("ведите число:")
result = int(loc1) +- int(loc2)
print(result)

print("число a=")
a = int(input())

print("число b=")
b = int(input())

print("выбрать операцию")
print("+_a+b")
print("-_a-b")
d = input()
if d=="+":
    print(a+b)
if d=="-":
    print(a-b)

print("---------------------")

from pyowm import OWM

owm = OWM('b63de3bad15b7355f1d65d522da325ff')
mgr = owm.weather_manager()
place = input("Какой город/страна?:")
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"]
print(w)
print("температура в городе " + str(temp))
