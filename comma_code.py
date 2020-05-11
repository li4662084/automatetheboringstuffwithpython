spam = ['apples', 'bananas', 'tofu', 'cats']
# 定义函数comma_code.
def comma_code(list):
    # 添加一个字符变量。
    string = ''
    # 除最后一个外遍历列表中的其他所有元素。
    for i in range(len(list) - 1):
        # 在字符串内添加相应的元素以及逗号、空格。
        string += list[i] + ', '
    # 最后在末尾添加and和最后一个元素。
    # 确保列表中包含元素，如果不包含不输出。
    if len(list) >0:
        string += 'and ' + list[-1]
    else:
        pass
    return string

print(comma_code(spam))