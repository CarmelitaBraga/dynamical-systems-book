#As was taught

def F2K():
    F = float(input("Enter temperature in degrees Fahrenheit: "))
    K = 5 * (F - 32)/ 9 + 273
    print(f'The temperature in Kelvin is {K} K.')

F2K()

#As I would do it

def F2K(tempF):
    return 5 * (tempF - 32)/ 9 + 273