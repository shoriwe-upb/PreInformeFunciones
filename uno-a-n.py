def one_to_n(n):
    number = 1
    while number <= n:
        if number % 2 != 0:
            print(number)
        number += 1


def main():
    to_number = int(input("numero: "))
    one_to_n(to_number)


if __name__ == "__main__":
    main()
