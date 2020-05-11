# 创建一个函数collatz。
def collatz(number):
    # 如果number是偶数，执行number // 2。
    if number % 2 == 0:
        n = number // 2
        print(n)
        return n
    # 如果number是奇数，执行3 * number + 1。
    elif number % 2 == 1:
        n = 3 * number + 1
        print(n)
        return n
# 要求用户输入一个数字。
num = input('Enter number: \n')
# 尝试对输入的内容进行取整操作。
try:
    num = int(num)
    # 利用while循环执行函数collatz。
    while True:
        num = collatz(num)
        # 当collatz结果为1时跳出循环。
        if num == 1:
            break
# 当用户输入的是非整数时，给出提示。
# (如果想根据不同错误提供不同信息可以在except后加入相应的错误代码）
except: # 如 except ValueError。
    print('Please input a integer number!')


