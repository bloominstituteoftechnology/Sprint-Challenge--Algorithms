# name = input('Enter your name: ')
# print('Your name is: ',name)

# if name == 'Hamid':
#     print('Welcome Admin')
# else:
#     print('Sorry your not the admin')

def recursive_fib(n):
    if n < 1:
        print("Incorrect input.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return recursive_fib(n - 1) + recursive_fib(n - 2)

n = input(int())
recursive_fib(n)