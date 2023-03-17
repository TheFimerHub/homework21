import time
def printing(txt):
    print('')
    print('\x1b[1mProgram:\x1b[0m')
    for char in txt:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print('')