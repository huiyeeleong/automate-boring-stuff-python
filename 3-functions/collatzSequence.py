def collatz(number):
    if number % 2 == 0:
        print(number // 2)
    else:
        print(3 * number + 1)
try:
    while True:
        userPrompt = int(input("Please input any number: "))
        collatz(userPrompt)
        
except ValueError:
    print('Error: Invalid argument')

