sequence = list()
result = list()
max_value = 4000000
n = 0
while True:
    if n == 0:
        sequence.append(1)
    if n == 1:
        sequence.append(2)
    if n > 1:
        sequence.append(sequence[n - 2] + sequence[n - 1])

    if sequence[n] > max_value:
        sequence.pop(n)
        break

    if sequence[n] % 2 == 0:
        result.append(sequence[n])

    n += 1

print(sum(result))
