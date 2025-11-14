def addmultiplenumbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def isiteven(num):
    if isinstance(num, int) and num % 2 == 0:
        return True
    return False


def isitaninteger(num):
    return isinstance(num, int)


def main():
    print("Hello learners!")
    
    
    print(addmultiplenumbers([1, 2, 3]))            
    print(multiplymultiplenumbers([2, 3, 4]))       
    print(isiteven(5))                               
    print(isitaninteger(10))                         


if __name__ == "__main__":
    main()