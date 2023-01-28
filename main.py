"""""""""""""""""""""""

LESSON 1

"""""""""""""""""""""""
"""
print('Hello World')

favourite_number = 7
average = 4.81
print("Любимое число:", favourite_number)
print("Оценка:", average)

name = "Антон"
age = 15
print(name)
print(age)
print(name, age)
name = "Антон"
surname = "Коцин"
age = 15
print(name, surname, age)
name = "Anton"
surname = "Kotsin"
age = 15
print(name, surname, age)

print(5/2)
print(5//2)
print(10 % 2)

name = "Инжинирум"
name = name + 1
print(name)

name = input()
age = input()
print("Тебя зовут:", name)
print("Твой возраст:", age)


name = input('Please, enter your name')
surname = input('Enter your surname')
age = int(input('How old are you?'))
print('Hello', name, surname)
print('Happy B-day')
age = age + 1 # age += 1
print('You are', age, 'years old')

print(5 < 2)
print(5 > 2)
print(5 <= 2)
print(5 >= 2)
print(5 == 2)
print(5 != 2)

a = int(input())
b = int(input())
print(a+b)

a = float(input())
b = float(input())
print(a+b)

r = input()
print(r,r,r)

str1 = input()
str2 = input()
str3 = input()
print(str3)
print(str2)
print(str1)

metr = int(input())
rash = int(input())
print((metr*rash+100)*2)

print('Привет')
name = input('Как тебя зовут?')
surname = input('Какая у тебя фамилия?')
city = input('В каком городе ты живешь?')
country = input('В какой стране ты живешь?')
passport = input('Скажи номер паспорта')
age = input('Сколько тебе лет?')
print('Информация о тебе:', name, surname, city, country, passport, age + 'лет')

import math
g = 10
speed = int(input())
ugol = int(input())
print('Дальность:', (speed**2 * math.sin(ugol)**2) / g)
"""

"""""""""""""""""""""""

LESSON 2

"""""""""""""""""""""""

"""
ques1 = input('Ты человек?')
ques2 = input('ты изучаешь программирование?')
if ques1 == 'да':
    print('Ваш ответ принят')
elif ques1 == 'нет':
    print('Ваш ответ принят')
else:
    print('Ошибка')
if ques2 == 'да':
    print('Ваш ответ принят')
elif ques1 == 'нет':
    print('Ваш ответ принят')
else:
    print('Ошибка')


print('Привет')
name = input('Введи свое имя:')
surname = input('Введи свою фамилию:')
age = int(input('Введи свой возраст:'))
if age > 18:
    print('Ты уже взрослый')
else:
    print('Ты несовершеннолетний')


ch1 = int(input('Число1: '))
ch2 = int(input('Число2: '))
oper = input('Оператор: ')
if oper == "/":
    if ch1 == 0:
        print('Ошибка')
else:
    print(ch1/ch2)
if oper == "*":
    print(ch1 * ch2)
if oper == "+":
    print(ch1 + ch2)
if oper == "-":
    print(ch1 - ch2)
else:
    print('Ошибка')


a = input()
b = input()
c = input()
if a == "красный" and b == "жёлтый" and c == "зелёный" or a == "3" and b == "2" and c == "1":
    print("ПОЕХАЛИ")
else:
    print("СТОЙ")



city1 = input('Введите город1:')
city2 = input('Введите город2:')
if city1 == 'Париж' and city2 == 'Берлин' or city1 == 'Берлин' and city2 == 'Париж':
    print('Такой вариант не подходит')
elif city1 != 'Париж' or city2 != 'Берлин':
    print('Хороший выбор')


#1-камень, 2-ножницы, 3- бумага
a = input()
b = input()
if a == '1' or a == 'Камень' and b == '2' or b == 'Ножницы':
    print('Камень победил')
elif a == '2' or a == 'Ножницы' and b == '3' or b == 'Бумага':
    print('Ножницы победили')
elif a == '3' or a == 'Бумага' and b == '1' or b == 'Камень':
    print('Бумага победила')



print('Обратный отсчет:')
i = 10
for i in range(10, 0, -1):
    print(i)
print('Поехали!')


a = int(input('Введите столбец: '))
for b in range(0,11,1):
   print(str(b) , '*' ,str(a), '= ' + str(b*a))


for i in range(1,10,2):
    print()
    for a in range(1,10,1):
        result=i*a
        result_1=(i+1)*a
        print(i,"*",a,"=",result," ",i+1,"*",a,"=",result_1)


for a in range(99, 60, -2):
    print(a)
for a in range(39, 1, -2):
    print(a)


a = int(input())
b = 0
while a % 2 == 0:
    a /= 2
    b += 1
if a == 1:
    print(b)
else:
    print("НЕТ")
"""


"""""""""""""""""""""""

LESSON 3

"""""""""""""""""""""""

"""
print('ура' in 'Муравей') #True
print('стар' not in 'Всем на старт!') #False

print(chr(125)) # char - character
print(ord('%')) # ord - order
print(chr(ord('a') + 3))

name=input()
for i in range(0,len(name):
   if name[i]=='p':
       print(i)

name=input()
if len(name)<4:
    print('НЕТ')
else:
    print (name[3])
    
name=input()
print(name[-1])

a = input()
b = input()
if a[-1] == b[0]:
    print('Верно')
else:
    print('Ошибка')

a = input()
while True:
    b = input()
    if a[-1] == b[0]:
        a=b
    else:
        break  

a = input()
while True:
    if len(a) < 8:
        print('Короткий')
        a = input()
    elif ('123' in a):
        print('Простой')
        a = input()
    else:
        print('ОК')
        break


list_of_meal = ['vegetables', 'chicken' , 'cola']
print(list_of_meal)
list_of_meal.pop()
print(list_of_meal)
list_of_meal.append('water')
print(list_of_meal)
print('#' * 30)
for i in range(len(list_of_meal)):
    print(list_of_meal[i])
print('#' * 30)
for item in list_of_meal:
    print(item)
print('#' * 30)

list_of_meal = ['vegetables', 'chicken', 'cola']
const_list_of_meal = ('vegetables', 'chicken', 'cola')
list_of_meal[1] = 'pork'
const_list_of_meal[1] = 'pork'  #ошибка


a = input("")
b = list(a)
while ("(" in b) == True:
    c1 = b.index("(")
    while b[c1] != ")":
        b.pop(c1)
    b.remove(")")
    if b[c1 - 1] == " ":
        b.pop(c1 - 1)
        print(''.join(b))
"""

"""""""""""""""""""""""

LESSON 4

"""""""""""""""""""""""

"""
data = input()
print(data, type(data))
data = data.split()
print(data, type(data))

a = input()
print(a.replace(' ', '\n'))

a = input().split()
for i in a:
    print('*' * int(i))

#1 пирамида
a = int(input('Введите высоту пирамиды:')) -1
b = 1
while a > -1:
        print(' ' * a + '*' * b)
        b += 2
        a -= 1

#2 пирамида
x = int(input('Введите высоту пирамиды:'))
k = 1
for i in range(x):
    print(' ' *(x-1-i), '*' * k )
    k += 2

#разьясн пирамиды 2
a = int(input()) -1
b = 1
while a > -1:
        print('_' * a + '*' * b)
        b += 2
        a -= 1

name = 'Inginirium'
for index in range(len(name)):
    print(name[index], end='')

name = 'Inginirium'
print('In' in name)
if'iri' in name:
    print('+')
else:
    print('-')

name = 'Inginirium'
for letter in name:
    print(letter, end='')

products = {'apple', 'orange', 'cola', 'apple'}
print(products)

products = {'apple', 'orange', 'cola', 'apple'}
companies = {'apple', 'google', 'facebook'}
print(products | companies)

products = {'apple', 'orange', 'cola', 'apple'}
companies = {'apple', 'google', 'facebook'}
print(products & companies)

products = {'apple', 'orange', 'cola', 'apple'}
companies = {'apple', 'google', 'facebook'}
print(products - companies)

products = {'apple', 'orange', 'cola', 'apple'}
companies = {'apple', 'google', 'facebook'}
print(products ^ companies)

products = set()
products.add('cola')
products.add('water')
products.remove('cola')
print(products)
print('cola' in products)

books = {'Harry Potter': 'J.K. Rowling', '1984': 'G. Orwell'}
books_list = ['J.K. Rowling', 'G. Orwell']
print(books_list[0])
print(books['Harry Potter'])
print(books_list[0] == books['Harry Potter'])

books = {
'Harry Potter': 'J.K. Rowling',
'1984': 'G. Orwell',
'War and Peace': 'L. Tolstoy'
if "Harry Potter' in books:
print('There is the "Harry Potter"!')
if 'KOLOBOK' not in books:
print('There is no "KOLOBOK"!')

books = {
'Harry Potter': 'J.K. Rowling',
'1984': 'G. Orwell',
'War and Peace': 'L. Tolstoy'
}
print(books.keys())
print(books.values())
print(books.items())

list_nums = [1, 2, 3, 3, 2 ,1]
tuple_nums = (1, 2, 3, 3, 2, 1)
set_nums = {1, 2, 3, 3, 2, 1}
dict_data = {'first': 1, 'second': 2, 'third': 3}
print(list_nums, type(list_nums), sep='\n')
print(tuple_nums, type(tuple_nums), sep='\n')
print(set_nums, type(set_nums), sep='\n')
print(dict_data, type(dict_data), sep='\n')

#1
morze = {'a': '•—', 'b': '—•••', 'c': '—•—•',
         'd': '—••', 'e': '•', 'f': '••—•',
         'g': '——•', 'h': '••••', 'i': '••',
         'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———',
         'p': '•——•', 'q': '——•—', 'r': '•—•',
         's': '•••', 't': '—', 'u': '••—',
         'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••','_': '_'}
text = input().lower().split()
a = []
for i in text:
    for j in i:
        print(morze[j], end=" ")
    print()


#2
dayBirth = {
    'янв': [],
    'фев': [],
    'мар': [],
    'апр': [],
    'май': [],
    'июн': [],
    'июл': [],
    'авг': [],
    'сен': [],
    'окт': [],
    'ноя': [],
    'дек': [],
}
for i in range(int(input())):
    about = input().split()
    name = about[0]
    month = about[2]
    dayBirth[month].append(name)
    dayBirth[month].sort()
for u in range(int(input())):
    m = input()
    print(dayBirth[m],end=' ')


#3
a=int(input())
d={}
for i in range(0,a):
    birthday=input().split(" ")
    d[birthday[-1]] = birthday[0]
c=int(input())
list=[]
for i in range(0,c):
    month=input()
    list.append(month)
for i in list:
    if i in d:
        print(d[i])

"""

"""""""""""""""""""""""

LESSON 5

"""""""""""""""""""""""

"""

a=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()


a, b = [int(i) for i in input().split()]
a, b = map(int, input().split())

n=int(input())
m=int(input())
a=[[int(i) for i in input().split()[:m]] for j in range(n)]
s=0
for i in range(n):
    s+=a[i][i]
print(s)

n=int(input())
a=[[int(i) for i in input().split()[:n]] for j in range(n)]
m=a[0][0]
for i in range(n):
    for j in range(n):
        if i > j and i < n-1-j or i>j and i>n-1-j:
            if a[i][j] > m:
                m=a[i][j]
print(m)

n=int(input())
m=int(input())
a=[[int(i) for i in input().split()[:m]] for j in range(n)]
x_1=int(input())
x_2=int(input())
for i in range(n):
    a[i][x_1], a[i][x_2] = a[i][x_2], a[i][x_1]
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()


a=[3,5,6,3,5,76,-8,0,10]
for i in range(len(a)-1):
    for j in range(len(a)- i - 1):
        if a[j+1] < a[j]:
            a[j+1], a[j] = a[j], a[j+1]
print(a)

a=[3,5,6,3,5,76,-8,0,10]
left, right = 0, len(a) - 1
while left <= right:
    for i in range(right, left, -1):
        if a[i-1] > a[i]:
            a[i-1], a[i] = a[i], a[i-1]
    left+=1
    for i in range(left, right):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    right-=1
print(a)

a=[3,5,6,3,5,76,0,10]
a_m=[0]*(max(a)+1)
for i in range(len(a)):
    a_m[a[i]]+=1
for i in range(len(a_m)):
    if a_m[i]:
        for k in range(a_m[i]):
            print(i, end=' ')
  
a=[3,5,6,3,5,76,-8,0,10]
for i in range(len(a)-1):
    for j in range(len(a)- i - 1):
        if a[j+1] < a[j]:
            a[j+1], a[j] = a[j], a[j+1]
    print(a)
"""

"""""""""""""""""""""""

LESSON 6

"""""""""""""""""""""""

"""

import random
k=0
a=random.randint(1,100)
b=int(input())
while b!=a:
    if b<a:
        k=k+1
        print('+',k)
        b=int(input())
    else:
        k=k+1
        print('-',k)
        b=int(input())
print('right',k+1)



import random

g_h=100
d_h=100
while True:
    print("дракон бьет")
    choise_g=int(input('1 or 2'))
    if choise_g==random.randint(1,2):
        print("отразил")
    else:
        print("вас ударили")
        g_h=g_h-50
    print("вы бьете")
    choise_g=int(input('1 or 2'))
    if choise_g==random.randint(1,2):
        print("отразил")
    else:
        print("вы ударили")
        d_h=d_h-50
    if d_h==0:
        print("вы победили")
        break
    if g_h==0:
        print("вы програли")
        break
        
#1 Задача
'''
n=int(input())
m=int(input())
a=[[int(i) for i in input().split()[:m]] for j in range(n)]
s=0
for i in range(n):
    s+=a[i][i]
print(s)
'''
'''
#2 Задача
n=int(input())
a=[[int(i) for i in input().split()[:n]] for j in range(n)]
m=a[0][0]
for i in range(n):
    for j in range(n):
        if i > j and i < n-1-j or i>j and i>n-1-j:
            if a[i][j] > m:
                m=a[i][j]
print(m)
'''
#3 Задача
'''
n=int(input())
m=int(input())
a=[[int(i) for i in input().split()[:m]] for j in range(n)]
x_1=int(input())
x_2=int(input())
for i in range(n):
    a[i][x_1], a[i][x_2] = a[i][x_2], a[i][x_1]
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
'''
#4 Задача
'''
n = int(input())
m = int(input())
a=[]
for i in range(n):
	t=[]
	for j in range(m):
		t.append(0)
	a.append(t)
size = 1
r=l=d=u=0
while(size <= n*m):
	k=r
	while(k < m - r and size <= n*m):
		a[r][k] = size
		size+=1
		k+=1
	r+=1

	k = d+1
	while(k  < n - d  and size <= n*m):
		a[k][m - d -1] = size
		size+=1
		k+=1
	d+=1

	k = m - l - 2
	while(k >= l and size <= n*m):
		a[n - l- 1][k] = size
		size+=1
		k-=1
	l+=1

	k = n-u-2
	while(k >= u + 1 and size <= n*m):
		a[k][u] = size
		size+=1
		k-=1
	u+=1
for i in a:
	for j in i:
		print(str(j).ljust(3, ' '), end='')
	print()
'''

"""

"""""""""""""""""""""""

LESSON 7

"""""""""""""""""""""""

"""
text = input("Введите текст, который хотите зашифровавать: ")
k = int(input("Укажите ключ: "))
def ceaser(user, key):
    res, n = [], ""
    dictionary, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    for i in range(len(user)):
        if user[i] in dictionary:
            n = dictionary
        elif user[i] in dictionary_upper:
            n = dictionary_upper
        else:
            res.append(user[i])
        if user[i] in n:
            for j in range(len(n)):
                if 0 <= j + key < len(n) and user[i] == n[j]:
                    res.append(n[j + key])
                elif j + key >= len(n) and user[i] == n[j]:
                    res.append(n[(1 - j - key) % (len(n) - 1)])
                elif j + key < 0 and user[i] == n[j]:
                    res.append(n[(j + key) % len(n)])
    return ''.join(res)
print(ceaser(text, k))


a = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц",
     "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
b = input()
key = int(input())
def Caesar(b, key):
    text = ' '
    for i in b:
        index = a.index(i)
        newindex = index + key
        text += a[newindex]
    return (text)
print(Caesar(b, key), sep='')

def mult(a, b):
    if a > b:
        a,b = b,a
    else:
        return a**b
a,b=10,2
for i in range(1,10):
    b=a
    b=mult(a,b)
print(a,b)
"""

"""""""""""""""""""""""

LESSON 8

"""""""""""""""""""""""

"""
from tkinter import *
root = Tk()
root.title('Приложеие')
root.geometry('500x200')
Label(text='Изображение').pack()
Entry(text='Ввод').pack()
Button(text='кнопка').pack()
root.mainloop()


l1.pack(side=TOP)
l2.pack(side=BOTTOM)
l3.pack(side=RIGHT)
l4.pack(side=LEFT)

from tkinter import *
def button_1():
    l.config(text=int(int(a.get())*2))
root=Tk()
root.title('Приложение')
root.geometry ('500x300')
a = Entry(root, width=15, bg='gray', fg='cyan', font='consolas')
a.pack()
Button(root, text='умножить на 2', width=15, height=2, bg= 'white', command=button_1).pack()
l = Label(root, width=15, bg='gray', fg='cyan', font='consolas')
l.pack()
root.mainloop()

from tkinter import *
def button_1():
    l.config(text=int(int(a.get())**2))
def button_2():
    l.config(text=int(int(a.get())**3))

root=Tk()
root.title('Приложение')
root.geometry('500x300')
a=Entry(root, width=15,bg='white',fg='cyan',font='consolas')
a.pack()
b1=Button(root, text='возвести в квадрат', width=15, height=2,bg='red', command=button_1)
b2=Button(root, text='возвести в куб', width=15, height=2,bg='red', command=button_2)
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
l = Label(root, width=15,bg='white', fg='cyan', font='consolas')
l.pack()

root.mainloop()

#фантазии
from tkinter import *
def button_1():
    a.config(text=str(a.get()))
root = Tk()
root.title('Приложение')
root.geometry ('500x300')
Label(text='Введите фамилию').pack()
a = Entry(root, width=15, bg='gray', fg='cyan', font='consolas')
a.pack()
Button(root, text='Ввести', width=15, height=2, bg= 'white', command=button_1).pack()
root.mainloop()


from tkinter import *
def button_1():
    l.config(text=int(int(a.get())**2))
def button_2():
    l.config(text=int(int(a.get())**3))

root=Tk()
root.title('Приложение')
root.geometry('500x300')
a=Entry(root, width=15,bg='white',fg='cyan',font='consolas')
a.pack()
b1=Button(root, text='возвести в квадрат', width=15, height=2,bg='red', command=button_1)
b2=Button(root, text='возвести в куб', width=15, height=2,bg='red', command=button_2)
b1.pack(side=LEFT)
b2.pack(side=RIGHT)
l = Label(root, width=15,bg='white', fg='cyan', font='consolas')
l.pack()

root.mainloop()
"""


"""""""""""""""""""""""

LESSON 9

"""""""""""""""""""""""


"""

from tkinter import *
from tkinter import messagebox
def button_1():
    messagebox.showinfo('Результат', int(a.get())*2)
root=Tk()
root.title('Приложение')
root.geometry('500x300')
a=Entry(root, width=10,  bg='gray', fg='cyan', font='consolas')
a.pack()
Button(root, text='Посчитать', width=10, height=2, bg='red',command=button_1).pack()
root.mainloop()


class tkinter.messagebox.Message(master=None, **options)
tkinter.messagebox.showinfo(title=None, message=None, **options)
tkinter.messagebox.showwarning(title=None, message=None, **options)
tkinter.messagebox.showerror(title=None, message=None, **options)
tkinter.messagebox.askquestion(title=None, message=None, **options)
tkinter.messagebox.askokcancel(title=None, message=None, **options)
tkinter.messagebox.askretrycancel(title=None, message=None, **options)
tkinter.messagebox.askyesno(title=None, message=None, **options)
tkinter.messagebox.askyesnocancel(title=None, message=None, **options)


#калькулятор
from tkinter import *
def button_1():
    l.config(text=int(int(a.get()) + int(x.get())))
def button_2():
    l.config(text=int(int(a.get()) - int(x.get())))
def button_3():
    l.config(text=int(int(a.get()) * int(x.get())))
def button_4():
    l.config(text=int(int(a.get()) / int(x.get())))
def button_5():
    l.config(text=int(int(a.get()) // int(x.get())))
def button_6():
    l.config(text=int(int(a.get()) % int(x.get())))
root=Tk()
root.title('Приложение')
root.geometry('500x300')
a=Entry(root, width=15,bg='white',fg='cyan',font='consolas')
a.pack()
x=Entry(root, width=15,bg='white',fg='cyan',font='consolas')
x.pack()
Button(root, text='+', width=15, height=2, bg= 'white', command=button_1).pack()
Button(root, text='-', width=15, height=2, bg= 'white', command=button_2).pack()
Button(root, text='*', width=15, height=2, bg= 'white', command=button_3).pack()
Button(root, text='/', width=15, height=2, bg= 'white', command=button_4).pack()
Button(root, text='//', width=15, height=2, bg= 'white', command=button_5).pack()
Button(root, text='%', width=15, height=2, bg= 'white', command=button_6).pack()
l = Label(root, width=15,bg='white', fg='cyan', font='consolas')
l.pack()
root.mainloop()


from tkinter import *
import random
from tkinter import messagebox

size=5
size_include=2
mas = [0] * size
print(mas)
for i in range(size): 
    mas[i] = [0] *size_include
print(mas)
iterator=0
def button_1():
    global iterator
    a=random.randint(1,5)
    b=int(Line.get())
    l.config(text=a)
    l2.config(text=f"осталось {5-iterator} ")
    if iterator==4:
        cal.destroy()
    mas[iterator][0]=a
    mas[iterator][1]=b
    iterator+=1
    if a==b:
        messagebox.showinfo('Результат','угадали' )
    else:
        messagebox.showinfo('Результат','не угадали' )


cal=Tk()
cal.title('игра')
cal.geometry('500x500')
Line=Entry(cal, width=20,bg='white',fg='black',font='consolas', text='Введите первое число')

Line.pack()

start=Button(cal, text='Start', width=15, height=2,bg='white', command=button_1)
exit_button = Button(cal, text="Exit", command=cal.destroy)


l=Label(cal, width=15,bg='white', fg='black', font='consolas')
l.pack()
l2=Label(cal, width=15,bg='white', fg='black', font='consolas')
l2.pack()

start.pack()
exit_button.pack()
cal.mainloop()
print(mas)

"""
"""""""""""""""""""""""

LESSON 10

"""""""""""""""""""""""
"""


a=[3,2,1,10,30,23]
print(a)
b=a
b.sort()
print(b)
if b == a:
    print("Все хорошо")
else:
    print("Ошибка")

n=int(input())
m=int(input())
a=[[int(i) for i in input().split()[:m]] for j in range(n)]
x_1=int(input())
x_2=int(input())
for i in range(n):
    a[i][x_1], a[i][x_2] = a[i][x_2], a[i][x_1]
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()



import random
n=4
m=4
a=[0]*n
for i in range(n):
    a[i]=[0]*m
print(a)
for i in range(n):
    for j in range(m):
        a[i][j]=random.randint(1,5)
print(a)

import random
n=4
m=4
p=4
a=[0]*n
for i in range(n):
    a[i]=[0]*m
for i in range(n):
    for j in range(m):
        a[i][j]=[0]*p

for i in range(n):
    for j in range(m):
        for k in range(p):
            a[i][j][k]=random.randint(1,5)
print(a)


import random
n=4
m=4
a=[0]*n
for i in range(n):
    a[i]=[0]*m
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
print('*'*10)
for i in range(n):
    for j in range(m):
        a[i][j]=random.randint(1,5)
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
S1=0
S2=1

print('*'*10)
for i in range(n):
    a[i][S1], a[i][S2] = a[i][S2], a[i][S1]

for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()



#фулл каменцы из 5 штук
a = input()
b = input()

if a == '1' or a == 'Камень' and b == '2' or b == 'Ножницы':
    print('Камень победил')
elif a == '1' or a == 'Камень' and b == '3' or b == 'Бумага':
    print('Бумага победила')
elif a == '1' or a == 'Камень' and b == '4' or b == 'Ром':
    print('Камень победил')
elif a == '1' or a == 'Камень' and b == '5' or b == 'Пират':
    print('Пират победил')

elif a == '2' or a == 'Ножницы' and b == '1' or b == 'Камень':
    print('Камень победил')
elif a == '2' or a == 'Ножницы' and b == '3' or b == 'Бумага':
    print('Ножницы победили')
elif a == '2' or a == 'Ножницы' and b == '4' or b == 'Ром':
    print('Ножницы победили')
elif a == '2' or a == 'Ножницы' and b == '5' or b == 'Пират':
    print('Пират победил')

elif a == '3' or a == 'Бумага' and b == '1' or b == 'Камень':
    print('Бумага победила')
elif a == '3' or a == 'Бумага' and b == '2' or b == 'Ножницы':
    print('Ножницы победили')
elif a == '3' or a == 'Бумага' and b == '4' or b == 'Ром':
    print('Ром победил')
elif a == '3' or a == 'Бумага' and b == '5' or b == 'Пират':
    print('Бумага победила')

elif a == '4' or a == 'Ром' and b == '2' or b == 'Ножницы':
    print('Ножницы победили')
elif a == '4' or a == 'Ром' and b == '1' or b == 'Камень':
    print('Камень победил')
elif a == '4' or a == 'Ром' and b == '3' or b == 'Бумага':
    print('Ром победил')
elif a == '4' or a == 'Ром' and b == '5' or b == 'Пират':
    print('Ром победил')

elif a == '5' or a == 'Пират' and b == '1' or b == 'Камень':
    print('Пират победил')
elif a == '5' or a == 'Пират' and b == '2' or b == 'Ножницы':
    print('Пират победил')
elif a == '5' or a == 'Пират' and b == '3' or b == 'Бумага':
    print('Бумага победила')
elif a == '5' or a == 'Пират' and b == '4' or b == 'Ром':
    print('Ром победил')

if a == b:
    print('ничья')


a = input()
b = input()

if a == 'камень' and b == 'ножницы' or a == 'камень' and b == 'ром':
    print('первый')
elif a == 'ножницы' and b == 'бумага' or a == 'ножницы' and b == 'ром':
    print('первый')
elif a == 'бумага'and b == 'камень'  or a == 'бумага'and b == 'пират' :
    print('первый')
elif a == b:
    print('ничья')
else:
    print('второй')
    

password = ("1234")
password1 = ("Заводись")
enter = int(input())
enter1 = input()

if password != enter and enter1 != password1:
    print("Доступ запрещен")
else:
    print("Добро пожаловать")
"""


"""""""""""""""""""""""

LESSON 11

"""""""""""""""""""""""

"""

import random
n=int(input('строки'))
m=int(input('столбцы'))
arr=[0]*n
print(arr)
for i in range(len(arr)):
    arr[i]=[0]*m
print(arr)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j]=random.randint(0,10)
sum=0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        sum+=arr[i][j]
print(sum)
print(sum/(n*m))
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=' ')
    print()




import random
arr=[]
arr_orig=[1,2,3,4,5,6]
for i in range(0,6):
    element=random.choice(arr_orig)
    arr.append(element)
    arr_orig.remove(element)
    
print(arr)
arr.sort()
print(arr)


for letter in 'Hello,i m gleb':
if letter != 'l':
print(letter, end='')
"""

"""""""""""""""""""""""

LESSON 12

"""""""""""""""""""""""

"""

from tkinter import *
root = Tk()
canvas=Canvas(root, width=200, height=200,
bg='white')
canvas.pack()
root.mainloop()

from tkinter import *
root=Tk()
canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()
canvas.create_line(10, 10, 150, 150)
root.mainloop()


from tkinter import *
root=Tk()
canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()
canvas.create_rectangle(15, 15, 190, 110)
root.mainloop()

from tkinter import *
root=Tk()
canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()
canvas.create_oval(15, 15, 190, 110)
root.mainloop()

from tkinter import *
root=Tk()
canvas=Canvas(root, width=200, height=200, bg='white')
canvas.pack()
canvas.create_polygon(15, 15, 190, 110, 50, 120, fill='yellow', outline='black')
root.mainloop()

from tkinter import *
def change():
    canvas.itemconfig(square, fill='blue’)
    print(canvas.itemcget(square, 'fill'))
side = 200
canvas_width, canvas_height = 300, 300
x, y=20, 20
root=Tk()
canvas=Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()
square = canvas.create_rectangle(x, y, x+side, y+side, fill='yellow')
Button(text='1244', command=change).pack()
root.mainloop()

from tkinter import *
colors=['white', 'gray', 'brown', 'yellow', 'blue', 'red','green', 'pink', 'magenta', 'black']
def get_next(item):
    curr = colors.index(canvas.itemcget(item, 'fill'))
    if curr != len(colors) - 1:
        return curr + 1
    return 0
def change_square():
    canvas.itemconfig(square, fill=colors[get_next(square)])
def change_roof():
    canvas.itemconfig(roof, fill=colors[get_next(roof)])
def change_sun():
    canvas.itemconfig(sun, fill=colors[get_next(sun)])
side = 200
canvas_width, canvas_height = 500, 500
x, y=150, 300
root=Tk()
canvas=Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()
square = canvas.create_rectangle(x, y, x+side, y+side, fill=colors[2], outline='white')
roof =canvas.create_polygon(x, y, x+side, y, x+side//2, y-side//2, fill=colors[1], outline='white')
sun = canvas.create_oval(canvas_width -  side//2, 0, canvas_width, side//2, fill=colors[3], outline='white')
Button(text='Основание', command=change_square).pack()
Button(text='Крыша', command=change_roof).pack()
Button(text='Солнце', command=change_sun).pack()
root.mainloop()

from tkinter import *
from tkinter import messagebox
def button_1():
    messagebox.showinfo('Результат', int(a.get())*2)
root=Tk()
root.title('Приложение')
root.geometry('500x300')
a=Entry(root, width=10,  bg='gray', fg='cyan', font='consolas')
a.pack()
Button(root, text='Посчитать', width=10, height=2, bg='white', command=button_1).pack()
root.mainloop()

from tkinter import *
from tkinter import messagebox
def button_1():
    messagebox.showinfo('Результат', int(a.get())+int(b.get()))
def button_2():
    messagebox.showinfo('Результат', int(a.get())-int(b.get()))
def button_3():
    messagebox.showinfo('Результат', int(a.get())*int(b.get()))
def button_4():
    messagebox.showinfo('Результат', int(a.get())/int(b.get()))
def button_5():
    messagebox.showinfo('Результат', int(a.get())//int(b.get()))
def button_6():
    messagebox.showinfo('Результат', int(a.get())%int(b.get()))
root=Tk()
root.title('Приложение')
root.geometry('500x500')
a=Entry(root, width=10,  bg='gray', fg='cyan', font='consolas')
a.pack()
b=Entry(root, width=10,  bg='gray', fg='cyan', font='consolas')
b.pack()
Button(root, text='+', width=10, height=2, bg='white',
	 command=button_1).pack()

Button(root, text='-', width=10, height=2, bg='white',
	 command=button_2).pack()

Button(root, text='*', width=10, height=2, bg='white',
	 command=button_3).pack()

Button(root, text='/', width=10, height=2, bg='white',
	 command=button_4).pack()

Button(root, text='//', width=10, height=2, bg='white',
	 command=button_5).pack()

Button(root, text='%', width=10, height=2, bg='white',
	 command=button_6).pack()
root.mainloop()


from tkinter import *

def set_value(formula):
    if formula == '':
        lbl['text']='0'
    else:
        lbl['text']=str(eval(formula))
def logicalc(operation):
    if operation == "C":
        set_value('')
    elif operation == "DEL":
        set_value(lbl['text'][0:-1])
    elif operation == "X^2":
        set_value(str((eval(lbl["text"]))**2))
    elif operation == "=":
        set_value(lbl["text"])
    else:
        if lbl['text'] == "0":
            lbl["text"] = ""
        lbl["text"] = lbl['text']+operation

root = Tk()
root["bg"] = "black"
root.geometry("485x550+200+200")
root.title("Калькулятор")
root.resizable(False, False)
lbl = Label(text='0', font=("Consolas", 21, "bold"), bg="black", foreground="white")
lbl.place(x=11, y=50)
btns = [
"C", "DEL", "*", "=",
"1", "2", "3", "/",
"4", "5", "6", "+",
"7", "8", "9", "-",
"(", "0", ")", "X^2"
]
x = 10
y = 140
for bt in btns:
    com = lambda x=bt: logicalc(x)
    Button(text=bt, bg="white",font=("Consolas", 15),command=com).place(x=x, y=y,width=115,height=79)
    x += 117
    if x > 400:
        x = 10
        y += 81
root.mainloop()


from roman import *

def roman_to_int(s:str)->int:
    res=0
    d={'CM':900, 'CD':400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV':4,
        'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for k in d:
        res+=d[k]*s.count(k)
        s=s.replace(k, '')
    return res

def int_to_roman(num:int)->str:
    info=['I', 'X', 'C', 'M']
    #      0    1    2    3
    weird_number=''# 58 LVIII XXXXXIIIIIIII
    i=0
    while num != 0:
        n=num%10
        weird_number=info[i]*n+weird_number
        num//=10
        i+=1
    res=weird_number
    res=res.replace('IIIIIIIII','IX')
    res=res.replace('IIIII', 'V')
    res=res.replace('IIII', 'IV')
    res=res.replace('XXXXXXXXX','XC')
    res=res.replace('XXXXX','L')
    res=res.replace('XXXX','XL')
    res=res.replace('CCCCCCCCC','CM')
    res=res.replace('CCCCC','D')
    res=res.replace('CCCC','CD')
    return res

t = ['IV', 'LVIII', 'MCMXCIV', 'XCIX', 'LXXX', 'LXIX']
print(t)
for i in t:
    print(i, '->' ,roman_to_int(i))

a=[4, 58, 1994, 26, 99, 69, 80]
for i in a:
    print(i, '->',int_to_roman(i))
    

"""

"""""""""""""""""""""""

LESSON 13

"""""""""""""""""""""""

"""


"""

columns=('id', 'name', 'lastname', 'age',
'height', 'weight')
data = [
(1, 'Ivan', 'Ivanov', 14, 160, 50),
(2, 'Sasha', 'Sidorov', 15, 210, 40),
(3, 'Masha', 'Poradina', 30, 178, 70),
(4, 'Timur', 'Korolev', 44, 160, 120) ]

def read_from_file(filename):
    with open(filename, 'r') as file:
        columns = tuple(file.readline().split(','))
        data = []
        for line in file:
            line = line.split(',')
            data.append((int(line[0]), line[1],
line[2], int(line[3]), int(line[4]), int(line[5])))
    return columns, data

def write_to_file(filename):
    with open(filename, 'w') as file:
        file.write(','.join(columns)+'\n')
        for line in data:
            line=[str(i) for i in line]
            file.write(','.join(line)+'\n')



read_from_file('data.csv')