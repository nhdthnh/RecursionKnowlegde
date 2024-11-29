def merge_sort(arr):
    # Kiểm tra nếu mảng chỉ có một phần tử hoặc rỗng
    if len(arr) <= 1:
        return arr
    # Chia mảng làm hai nửa và đệ quy sắp xếp
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Trộn hai nửa đã sắp xếp
    sorted_array = []
    i = j = 0
    # So sánh và gộp từng phần tử từ hai nửa vào mảng kết quả
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_array.append(left_half[i])
            i += 1
        else:
            sorted_array.append(right_half[j])
            j += 1
    # Thêm phần còn lại của mỗi nửa vào mảng kết quả
    sorted_array.extend(left_half[i:])
    sorted_array.extend(right_half[j:])
    
    return sorted_array

def merge_sort_iterative(arr):
    width = 1  # Kích thước của mảng con bắt đầu từ 1
    n = len(arr)
    while width < n:
        for i in range(0, n, 2 * width):
            # Xác định hai nửa mảng con để gộp
            left = arr[i:i + width]
            right = arr[i + width:i + 2 * width]
            # Bắt đầu quá trình trộn trực tiếp vào arr
            sorted_array = []
            i_left = i_right = 0
            
            # So sánh từng phần tử của hai mảng con và thêm vào mảng kết quả tạm thời
            while i_left < len(left) and i_right < len(right):
                if left[i_left] < right[i_right]:
                    sorted_array.append(left[i_left])
                    i_left += 1
                else:
                    sorted_array.append(right[i_right])
                    i_right += 1
            # Thêm các phần tử còn lại
            sorted_array.extend(left[i_left:])
            sorted_array.extend(right[i_right:])
            
            # Ghi mảng đã trộn lại vào arr
            arr[i:i + 2 * width] = sorted_array
        # Tăng kích thước của mảng con
        width *= 2
    return arr
test_array = [38, 27, 43, 3, 9, 82, 10]
# Kết quả khi sử dụng Merge Sort đệ quy
result_recursive = merge_sort(test_array.copy())
# Kết quả khi sử dụng Merge Sort không đệ quy
result_iterative = merge_sort_iterative(test_array.copy())
print("Kết quả Merge Sort đệ quy:", result_recursive)
print("Kết quả Merge Sort không đệ quy:", result_iterative)