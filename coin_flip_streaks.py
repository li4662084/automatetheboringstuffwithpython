import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    results = []
    for i in range(100):
        result = random.randint(0, 1)
        if result == 0:
            results.append('H')
        elif result == 1:
            results.append('T')
    # Code that checks if there is a streak of 6 heads or tails in a row.
    # 指定计数器count，以及两个字符参数为None。
    count = 0
    current = None # current代表前一个元素。
    checker = None # checker代表目前的元素。
    for i in range(100):
        current = checker
        checker = results[i]
        # 如果相邻两个字符相等，计数加一。
        if current == checker:
            count += 1
        # 如果相邻两个字符不相等，计数归零。
        elif current != checker:
            count = 0
        # 当计数等于6时，出现Streak，并跳出循环。
        if count == 6:
            numberOfStreaks += 1
            break


print('Chance of streak: %s%%' % (numberOfStreaks / 100))