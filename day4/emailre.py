#-*- coding:utf-8-*-
import re

def is_email(addr):
    re_email = re.compile(r'^[\w\d\.]+@[\w\d]+\.\w+$')
    return re_email.match(addr)

assert is_email('someone@gmail.com')
assert is_email('bill.gates@microsoft.com')
assert not is_email('bob#example.com')
assert not is_email('mr-bob@example.com')
print('ok')

def name_of_email(addr):
    re_email = re.compile(r'^(<([\w\d\s]+)>\s+)?([\w\d\.]+)@[\w\d]+\.\w+$')
    m = re_email.match(addr)
    if m:
        if m.group(1):
            return m.group(2)
        else:
            return m.group(3)

print(name_of_email('<Tom Paris> tom@voyager.org'))
print(name_of_email('tom@voyager.org'))
