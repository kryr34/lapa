from colorama import Fore, init

def test(func):
    def inner():
        (result, compare, passed) = func()
        if passed:
            print(Fore.GREEN + f'[ GOOD ] {func.__qualname__}');
        else:
            print(Fore.RED+
                  f'[ BAD  ] {func.__qualname__}\n' +
                  f'  result:\n{result}\n' +
                  f'  answer:\n{compare}');
    return inner
if __name__ == '__main__':
    print("This is decorator of test format, nothing excute.")
