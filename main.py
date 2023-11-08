import matplotlib.pyplot as plt

def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fib)
    return fibonacci_sequence

N = int(input("Введите количество чисел Фибоначчи: "))
fibonacci_sequence = generate_fibonacci(N)

x = list(range(1, N + 1))
y = fibonacci_sequence

plt.plot(x, y, marker='o')
plt.xlabel('Номер числа Фибоначчи')
plt.ylabel('Значение числа Фибоначчи')
plt.title(f'Зависимость величины числа Фибоначчи от его номера')
plt.grid(True)
plt.show()
