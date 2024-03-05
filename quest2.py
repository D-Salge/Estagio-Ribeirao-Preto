def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        while fib[-1] < n:
            fib.append(fib[-1] + fib[-2])
        return fib

def pertence_fibonacci(n):
    fib = fibonacci(n)
    if n in fib:
        return True
    else:
        return False

n = int(input("Informe um numero: "))
if pertence_fibonacci(n):
    print("O numero informado pertence a sequencia de Fibonacci.")
else:
    print("O numero informado nao pertence a sequencia de Fibonacci.")
