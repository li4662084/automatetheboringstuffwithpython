tableData = [['apples', 'organges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    # 建立一个列表存储每一行的打印宽度。
    colWidths = []
    # 建立一个变量用于存储每行的最大宽度。
    colWidth = 0
    # 遍历每一行。
    for i in range(len(tableData)):
        # 遍历每一行中的元素。
        for j in range(len(tableData[i])):
            # 找出每行元素的最大长度
            if len(tableData[i][j]) > colWidth:
                colWidth = len(tableData[i][j])
        # 将每行最大长度存储在列表中。
        colWidths.append(colWidth)
    # 通过遍历每一个元素，再遍历每一行，打印列表数据。
    for j in range(len(tableData[0])):
        for i in range(len(tableData)):
            print(tableData[i][j].rjust(colWidths[i]),end='')
        print('')

printTable(tableData)