import random
numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = random.choice(numbers)
print(n)
result = []

for i in range(1, 20):
    for j in range(1, 20):
        if n % (i+j) == 0:
            if i != j:
                if i not in result or j not in result:
                    result.append(f'{i}{j}')
                    # result.append(j)
print(result)

