import random
import time
# Đệ quy
def quick_sort_recursive(arr):
    if len(arr) <= 1:
            return arr
        # Chọn phần tử "pivot" làm trung tâm để chia danh sách
    pivot = arr[len(arr) // 2]  # Chọn phần tử ở giữa danh sách làm pivot
    # Phân chia danh sách thành 3 phần:
    # - Các phần tử nhỏ hơn pivot
    left = [x for x in arr if x < pivot]
    # - Các phần tử bằng pivot
    middle = [x for x in arr if x == pivot]
    # - Các phần tử lớn hơn pivot
    right = [x for x in arr if x > pivot]
    # Gọi đệ quy để sắp xếp các phần bên trái và bên phải, sau đó ghép lại
    return quick_sort_recursive(left) + middle + quick_sort_recursive(right)

# Không đệ quy
def quick_sort_iterative(arr):
    stack = [arr]
    result = []
    while stack:
        current = stack.pop()
        if len(current) <= 1:
            result.extend(current)
            continue
        pivot = current[len(current) // 2]
        left = [x for x in current if x < pivot]
        middle = [x for x in current if x == pivot]
        right = [x for x in current if x > pivot] 
        stack.append(right)
        stack.append(middle)
        stack.append(left)
    return result

# Thực hiện và đo thời gian
array_size = 5  # Có thể thay đổi kích thước mảng
arr = random.sample(range(10000), array_size)  # Tạo mảng ngẫu nhiên
print("Mảng đã cho : " + str(arr))

sorted_recursive = quick_sort_recursive(arr)
sorted_iterative = quick_sort_iterative(arr)
print(f"Đệ quy: {sorted_recursive}")
print(f"Không đệ quy: {sorted_iterative}")


