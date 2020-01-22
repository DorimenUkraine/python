import first_main_conception

print('Top level in second_main_conception.py')

first_main_conception.function1()

if __name__ == '__main__':
    print('second_main_conception.py is being run directly')
else:
    print('second_main_conception.py has been imported')