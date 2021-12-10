import time, sys
indent = 0
indentIncreasing = True

try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()

# def collatz(number):
#     num = int(number)
#     if num % 2 == 0:
#         print(num // 2)
#         return num // 2
#     else:
#         print(3 * num + 1)
#         return 3 * num + 1
#
# print('Enter a number bro')
# num = input()
