
def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number //= 10
    print(total)



No = int(input(" Insert value "))
sum_of_digits(No)