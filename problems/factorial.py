def factorial(n: int) -> int:
    # Base Case
    if n <= 1:
        return 1
    # Recurcive Case
    else:
        return n * factorial(n-1)


def factorial(n: int) -> int:
    return 1 if n <= 1 else n * factorial(n-1)


