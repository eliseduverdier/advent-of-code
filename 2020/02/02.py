#/usr/bin/py

def check_passwords(passwords):
    for line in passwords:
        rule, password = line.split(':')



def maxlength(string, letter):
    count = 0
    for l in string:
        if l == letter:
            count += 1

passwords = open('./02.txt', 'r')
check_passwords(passwords)
