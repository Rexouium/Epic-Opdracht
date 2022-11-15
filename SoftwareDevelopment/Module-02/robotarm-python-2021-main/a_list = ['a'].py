Buy_list = ['Items: ']
print("Items: Banana, Orange, Cheese, Burger")

Item_To_Buy = input("Name the item here")

Buy_list.append(Item_To_Buy)

def test_list():
    return Buy_list

result = test_list()

print(result)