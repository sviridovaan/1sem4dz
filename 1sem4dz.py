#Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по 
# прямой между дольками (то есть разломить шоколадку на два 
# прямоугольника)

a = int(input("Введите количество долек, которое необходимо отломить\n"))
b = int(input("Введите количество ячеек шоколадки по вертикали\n"))
c = int(input("Введите количество ячеек шоколадки по горизонтали\n"))
if b%a == 0 or c%a == 0 or b*b == a or c*c == a or b == a or c == a:
    print ("Шоколадку можно разломить на два прямоугольника")
else :
    print ("Шоколадку нельзя разделить на 2 прямоугольника")