import math
import numpy as np
import string
print("enter input values, enter 1 for second value for single number operations")
a = int(input("enter number a: "))
b = int(input("enter number b: "))
def add(a ,b):
    print(a+b)
def sub(a ,b):
    print(a-b)
def mul(a ,b):
    print(a*b)
def divi(a ,b):
    print(a//b)
def modu(a ,b):
    print(a%b)
def root(a):
    print(math.sqrt(a))
def perc(a ,b):
    print((a/b)*100)
def sine(a):
    m = np.arcsin(a)
    print(m)
def cose(a):
    m = np.arccos(a)
    print(m)
def tan(a):
    m = np.arctan(a)
    print(m)
def loga(a ,b):
    print(math.log(a ,b))
def fact(a):
   print(math.factorial(a))
def exp(a ,b):
    print(a**b)

#getting operation type
print("enter type of operation: (simple{s}/complex{c})")
type = input("enter type:")
type = str.lower(type)
if type == "s":
    print("SELECT ANY ONE OPTION:-"
      "\n 1.ADD"
      "\n 2.SUB"
      "\n 3.MUL"
      "\n 4.DIV"
      "\n 5.MOD"
      "\n 6.ROOT"
      "\n 7.PERCENTAGE")
    option = int(input("enter option code: "))
    if option == 1:
        add (a ,b)
    if option == 2:
        sub(a ,b)
    if option == 3:
        mul(a ,b)
    if option == 4:
        divi(a ,b)
    if option == 5:
        modu(a ,b)
    if option == 6:
        root(a)
    if option == 7:
        perc(a ,b)
    if option>7:
       print("error, enter valid operation code")
else:
    print("enter the type of operation:"
          "\n 1.sin^-1"
          "\n 2.cos^-1"
          "\n 3.tan^-1"
          "\n 4.log"
          "\n 5.exponent"
          "\n 6.factorial")
    opt = int(input("enter the operation code:"))
    if opt == 1:
        sine(a)
    if opt == 2:
        cose(a)
    if opt == 3:
        tan(a)
    if opt == 4:
        loga(a ,b)
    if opt == 5:
        exp(a ,b)
    if opt == 6:
        fact(a)
    if opt>6:
       print("error, enter valid operation code")

