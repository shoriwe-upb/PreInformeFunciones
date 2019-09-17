def is_prime(number):
    number = abs(number)
    half = number / 2
    step = 2
    while step <= half:
        if number % step == 0:
            return False
        step += 1
    return True


def primo_hermano(number):
    if number % 6 != 0:
        if is_prime(number + 1):
            return True
    return False


def main():
    number = int(input("Number: "))
    if primo_hermano(number):
        print("Es primo hermano")
    else:
        print("No es primo hermano")


if __name__ == "__main__":
    main()
