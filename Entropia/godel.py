numbers = [1, 2, 3]
combinations = []

for i in numbers:
    for j in numbers:
        for k in numbers:
            for l in numbers:
                combination = [i, j, k, l]
                combinations.append(combination)

print(combinations)
adds = []

for i in combinations:
    adds.append(2**i[0] + 3**i[1] + 5**i[2] + 7**i[3])

g = adds.index(185)
print(adds.pop(g), combinations.pop(g))

g = adds.index(185)
print(adds.pop(g), combinations.pop(g))