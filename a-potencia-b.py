def pow(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result


def main():
    results = []
    for i in range(2):
        a = int(input(f"numero a{i + 1}: "))
        b = int(input(f"numero b{i + 1}: "))
        results.append(pow(a, b))
    if results[0] > results[1]:
        print(f"{results[0]} > {results[1]}")
    elif results[0] < results[1]:
        print(f"{results[0]} < {results[1]}")
    else:
        print(f"{results[0]} == {results[1]}")


if __name__ == "__main__":
    main()
