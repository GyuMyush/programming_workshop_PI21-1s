from io import IOBase
import json
from statistics import mean

def fact(x):
    if type(x) != int:
        return "Ошибка! Число должно быть целым!"
    if x == 1:
        return 1
    return fact(x-1) * x



def filter_even(li):
    if type(li) != list:
        return "Ошибка! Параметром функции должен быть список!"
    if len(li) == 0:
        return "Ошибка! Список пустой!"
    if len(list(filter(lambda x: type(x) != int, li))) != 0:
        return "Ошибка! В списке присутствуют значения, не соотвествующие целочисленному типу!"
    return list(filter(lambda x: x % 2 == 0, li)) 




def square(li):
    if type(li) != list:
        return "Ошибка! Параметром функции должен быть список!"
    if len(li) == 0:
        return "Ошибка! Список пустой!"
    if len(list(filter(lambda x: type(x) != int, li))) != 0:
        return "Ошибка! В списке присутствуют значения, не соотвествующие целочисленному типу!"
    return list(map(lambda x: x ** 2, li))



def bin_search(li, element):

    if type(element) != int and type(element) != float:
        return "Ошибка! Второй параметр функции должен быть числом!"
    if type(li) != list:
        return "Ошибка! Первый параметр функции должен быть списком!"
    if len(li) == 0:
        return "Ошибка! Первый параметр (список) пустой!"
    if len(list(filter(lambda x: type(x) != int and type(x) != float, li))) != 0:
        return "Ошибка! В списке присутствуют не числовые значения!"
    if(li != sorted(li)):
        return "Ошибка! Список не отсортирован по возрастанию!"         

    low = -1
    high = len(li)

    while high > low+1:
        mid = (low+high)//2

        if(li[mid] == element):
            return mid

        if(li[mid] < element):
            low = mid 
        else:
            high = mid 
            
    if(li[mid] != element):
        return -1



def is_palindrome(string):
    if type(string) != str:
        return "Ошибка! Параметр функции должен быть строкой!"
    if len(string) == 0:
        return "Ошибка! Параметр функции не должен быть пустой строкой!"
    string = string.replace(" ", "")
    string = string.lower()
    string = "".join(list(filter(lambda x: x.isalpha(), string)))
    left = 0
    right = len(string)-1 
    count_equality = 0
    while left != right:
        if(string[left] == string[right]):
            count_equality+=1
        else:
            return "NO"
        if left > right:
            break
        left+=1
        right-=1
    return "YES"
        
 

def calculate(path2file):

    if type(path2file) != str:
        return "Ошибка! Параметр функции должен быть строкой!"
    if len(path2file) == 0:
        return "Ошибка! Параметр функции не должен быть пустой строкой!"

    file = open(path2file,'r')

    if not isinstance(file, IOBase): 
        return "Ошибка! Открыт должен быть файл!"

    if not file.name.endswith(".txt"):
        return "Ошибка! Файл должен быть с расширением TXT!"
        
    operations_list = ["+", "-", "*", "//", "%", "**"]  
    result_list = []

    count_iter = 1

    for _str in file.readlines():

        split_list = _str.split("    ")

        if len(split_list) != 3:
            return "Ошибка файл не соответствует формату, указанному в ТЗ"

        if not split_list[0] in operations_list:
            return "Ошибка! Математическая операция не найдена в строке " + str(count_iter)

        try:
            check = int(split_list[1])
        except:
             return "Ошибка! Значение №1 не является целым числом в строке " + str(count_iter)

        try:
            check = int(split_list[2])
        except:
             return "Ошибка! Значение №2 не является целым числом в строке " + str(count_iter)          


        result_operate = eval(split_list[1] + split_list[0] + split_list[2])
        result_list.append(str(result_operate))

        count_iter+=1


    if count_iter == 1:
        return "Ошибка! Файл пуст!"

    result_str = ",".join(result_list)

    f_result = open('output1.txt','w')
    f_result.write(result_str)
    f_result.close()

    file.close()

    return result_str



def substring_slice(path2file_1, path2file_2):

    if type(path2file_1) != str:
        return "Ошибка! Параметр функции №1 должен быть строкой!"
    if len(path2file_1) == 0:
        return "Ошибка! Параметр функции №1 не должен быть пустой строкой!"

    if type(path2file_2) != str:
        return "Ошибка! Параметр функции №2 должен быть строкой!"
    if len(path2file_2) == 0:
        return "Ошибка! Параметр функции №2 не должен быть пустой строкой!"

    file1 = open(path2file_1,'r')
    file2 = open(path2file_2,'r')

    if not isinstance(file1, IOBase): 
        return "Ошибка! Открыт должен быть файл!"
    if not isinstance(file2, IOBase): 
        return "Ошибка! Открыт должен быть файл!"

    if not file1.name.lower().endswith(".txt"):
        return "Ошибка! Файл №1 должен быть с расширением TXT!"
    if not file2.name.lower().endswith(".txt"):
        return "Ошибка! Файл №2 должен быть с расширением TXT!"
        
    str_list_file1 = file1.readlines()
    str_list_file2 = file2.readlines() 

    if len(str_list_file1) == 0:
        return "Ошибка! Файл №1 пуст!"
    if len(str_list_file2) == 0:
        return "Ошибка! Файл №2 пуст!"

    if len(str_list_file1) != len(str_list_file2):
        return "Ошибка! Количество строк в файлах не совпадает!"

    result_list = []
    count_iter = 0

    for _str in str_list_file1:

        split_list = str_list_file2[count_iter].split(" ")

        if len(split_list) != 2:
            return "Ошибка файл №2 не соответствует формату, указанному в ТЗ"

        try:
            check = int(split_list[0])
            if(check<0):
                raise ""
        except:
             return "Ошибка! Значение №1 в файле №2 не является целым положительным числом (т.е. индексом) в строке " + str(count_iter + 1)

        try:
            check = int(split_list[1])
            if(check<0):
                raise ""
        except:
             return "Ошибка! Значение №2 в файле №2 не является целым положительным числом (т.е. индексом) в строке " + str(count_iter + 1)          

        if int(split_list[0]) > int(split_list[1]):
            return "Ошибка! Значение №1 должно быть меньше или равно значения №2 в файле №2 в строке " + str(count_iter + 1) 

        if int(split_list[0]) > len(_str):
            return "Ошибка! Значение №1 в файле №2 должно быть меньше длины строки в файле №1. Строка: " + str(count_iter + 1)
        if int(split_list[1]) > len(_str):
            return "Ошибка! Значение №2 в файле №2 должно быть меньше длины строки в файле №1. Строка: " + str(count_iter + 1)


        result_operate = _str[int(split_list[0]):int(split_list[1]) + 1]
        result_list.append(str(result_operate))

        count_iter+=1



    result_str = " ".join(result_list)

    f_result = open('output2.txt','w')
    f_result.write(result_str)
    f_result.close()

    file1.close()
    file2.close()

    return result_str



def decode_ch(sting_of_elements):

    if type(sting_of_elements) != str:
        return "Ошибка! Параметр функции должен быть строкой!"
    if len(sting_of_elements) == 0:
        return "Ошибка! Параметр функции не должен быть пустой строкой!"

    try:
        periodic_table = json.load(open('periodic_table.json',"r", encoding = "utf-8"))
    except:
        return "Ошибка чтения JSON"

    check   = 0 
    list_ch = [] 
    str_ch  = ""
    count = 1
    for ch in sting_of_elements:

        if ch.isupper():
            check += 1
            if check == 2:
                list_ch.append(str_ch)
                check = 1
                str_ch = ""
        str_ch += ch
        if count == len(sting_of_elements):
            list_ch.append(str_ch)    
        count += 1

    result_str_ch = ""
    for ch in list_ch:
        try:
            result_str_ch += periodic_table.get(ch)
        except:
            return "Элемент " + ch + " не найден в периодической таблице!"

    return result_str_ch 



class Student:
    def __init__(self, name, surname, grades = [3,4,5]):

        if type(name) != str or type(surname) != str:
            print("При инициализации класса произошла ошибка! На вход необходимо подавать name и surname строкового типа!")
            return

        if type(grades) != list:
            print("При инициализации класса произошла ошибка! На вход необходимо подавать grades типа список!")
            return

        if len(grades) == 0:
            print("При инициализации класса произошла ошибка! Список оценок grades не может быть пустым!")
            return
            
        self.name     = name 
        self.surname  = surname
        self.fullname = name + " " + surname
        self.grades   = grades
    
    def greeting(self):
        return "Hello, I am Student"

    def mean_grade(self):
        return round(mean(self.grades), 2)

    def is_otlichnik(self):
        if self.mean_grade() >= 4.5:
            return "YES"
        else:
            return "NO"

    def __add__(self, other):
        if isinstance(other, Student):
            return self.name + " is friends with " + other.name
        else:
            return "Второй объект не является экземпляром класса Student!"

    def __str__(self):
        if hasattr(self, "fullname"): 
            return self.fullname
      


class MyError(Exception):
    def __init__(self, msg = ""):
        if type(msg) != str:
            self.msg = "При инициализации класса произошла ошибка! На вход необходимо подавать строку!"
            return
        if msg == "": 
            self.msg = None
        else:
            self.msg = msg

    def __str__(self):
        if self.msg != None:
            return "MyError, " + self.msg 
        else:
            return "Вызван класс исключений MyError"
