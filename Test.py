
def is_even(n: int) -> bool:
    return n % 2 == 0

def main():
    try:
        s = input("Enter an integer: ").strip()
        n = int(s)
    except ValueError:
        print("Not an integer.")
        return
    print(f"{n} is {'even' if is_even(n) else 'odd'}")

if __name__ == "__main__":
    main()
