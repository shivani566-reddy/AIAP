
def print_first_ten_multiples(number: int) -> None:
    for i in range(1, 11):
        print(number * i)


if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    print_first_ten_multiples(n)


