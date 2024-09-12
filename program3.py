
choose = input('f or c  ')

if choose == 'c':
    Celsius = float(input())
    def conv_to_f(c):
        c = 9/5 * Celsius + 32
        return c
    Fahrenheit = conv_to_f(Celsius)
    print(Fahrenheit)
else: 
    Fahrenheit = float(input())
    def conv_to_c(f):
        f = ((Fahrenheit - 32) * 5) / 9
        return f
    Celsius = conv_to_c(Fahrenheit)
    print(Celsius)