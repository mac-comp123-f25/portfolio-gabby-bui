def countdown(n):
    if n == 0:
        print("Blast Off!")
    else:
        print(n)
        countdown(n - 1)

if __name__ == "__main__":
    countdown(10)