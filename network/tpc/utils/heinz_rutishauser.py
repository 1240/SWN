# -*- coding: cp1251 -*-

__author__ = '1240'

t = []
exp = []
three = []
operation = ['+', '-', '*', '/', ')']  # ��������, ��� ������� ������� ���������
l = 0
c = 0


class element:
    val = None
    lev = None

    def __init__(self, el, l):
        self.val = el
        self.level(l)

    def level(self, l):
        if self.val in operation:
            self.lev = l - 1
        else:
            self.lev = l + 1


# ��������� ���������, ������������ � ������
def calc(three):
    print three
    global c
    a = int(three[0])
    b = int(three[2])
    if three[1] == '+':
        c = a + b
    elif three[1] == '-':
        c = a - b
    elif three[1] == '*':
        c = a * b
    elif three[1] == '/':
        c = (a + 0.0) / b

#������� ������, ��������� ���������, �������� ������� t, exp
def find_max(exp, three):
    maxlev = max(t)
    i = 0
    while i < len(exp):
        if exp[i].lev == maxlev:
            three.append(exp[i].val)
            three.append(exp[i + 1].val)
            three.append(exp[i + 2].val)
            calc(three)
            #�������� ������ ���� ������ �� �� �������� � ��������� ������� �� 1
            exp[i].val = c
            exp[i].lev = maxlev - 1
            t[i] = exp[i].lev
            #������� ������, ����������� ������ � ��������� ����� ������
            del exp[i + 3], t[i + 3], exp[i + 2], t[i + 2], exp[i + 1], t[i + 1], exp[i - 1], t[i - 1]
            break
        i += 1


formula = "1 + ( 2 * 3 ) - 4 - 2"

expression = formula.split()
print(expression)
#��������� ������� t, exp
for el in expression:
    el = element(el, l)
    l = el.lev
    t.append(l)
    exp.append(el)
#���������� ���������
while len(exp) > 1:
    three = []
    find_max(exp, three)
print exp[0].val

