def is_prime(number):
    number = abs(number)
    if number == 0:
        return False
    half = number / 2
    step = 2
    while step <= half:
        if number % step == 0:
            return False
        step += 1
    return True


def main():
    number = int(input("Number: "))
    if is_prime(number):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    main()
