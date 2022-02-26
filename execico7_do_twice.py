def do_twice(f, x):
    f(x)
    f(x)
def print_spam(x):
    print(x)
do_twice(print_spam, 'Bem vindo')