coordA = int(input())
coordB = int(input())
r = int(input())
coordX = int(input())
coordY = int(input())
if r <= 0:
    print('Sua amplitude esta baixa, nao conseguimos te localizar no radar')
else:
    if r + 2 > int(((coordX - coordA)**2 + (coordY - coordB)**2)**0.5):
        print('Esferas do dragao detectadas')
    else:
        print('Esferas fora do radar')