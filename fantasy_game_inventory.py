# Fantasy Game Inventory
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        print(k, v)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

# List to Dictionary Function for Fantasy Game Inventory
def addToInventory(inventory, addedItems):
    # your code goes here
    # 遍历所有addedItems中的元素。
    for item in addedItems:
        # 检查元素是否在inventory中。
        if item in inventory.keys():
            # 已存在的元素Value加一。
            inventory[item] += 1
        # 元素不在inventory中，直接赋值。
        else:
            inventory[item] = 1
    # 注意需要返回value给函数。
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)