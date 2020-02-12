def do_twice(f, num):
    f(num)
    f(num)

def print_spam(val):
    print(val)

#do_twice(print_spam, 5)

def print_twice(param):
    print(param, param)

#print_twice("Hello")

do_twice(print_twice, "spam")

def do_four(f, num):
    for i in range(4):
        f(num)

do_four(print_spam, 4)

#Fermat’s Last Theorem
def check_fermat(a, b, c, n):
    if n > 2:
        if a**n + b**n == c**n:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work.")

check_fermat(1,2,3,3)