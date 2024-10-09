def bin_search(mass, mark, left, right):
    # если нету
    if left > right:
        return -1

    mid = (left + right) // 2

    if mass[mid] == mark:
        return mid
    elif mass[mid] < mark:  # если слева
        return bin_search(mass, mark, mid + 1, right)
    else:  # справа
        return bin_search(mass, mark, left, mid - 1)

def fun(mass, mark):
    return bin_search(mass, mark, 0, len(mass) - 1)

mass = [2, 3, 6, 9, 16, 20, 26, 54, 78, 84, 95, 99, 100]
print("Which number from that array [2, 3, 6, 9, 16, 20, 26, 54, 78, 84, 95, 99, 100] should I find?")

mark = int(input())

result = fun(mass, mark)
if result != -1:
    print(f"Number found at that position: {result}")
else:
    print("Number not found.")
