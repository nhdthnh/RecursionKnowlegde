import time
# Đệ quy
def tower_of_hanoi_recursive(n, source, target, auxiliary):
    # Trường hợp cơ bản: Nếu chỉ có 1 đĩa, di chuyển trực tiếp từ cột source sang target
    if n == 1:
        return f'Move disk 1 from {source} to {target}\n'
    # GĐ 1: Di chuyển n-1 đĩa từ source sang auxiliary, sử dụng target làm cột trung gian
    steps = tower_of_hanoi_recursive(n - 1, source, auxiliary, target)
    # GĐ 2: Di chuyển đĩa thứ n từ source sang target
    steps += f'Move disk {n} from {source} to {target}\n'
    # GĐ 3: Di chuyển n-1 đĩa từ auxiliary sang target, sử dụng source làm cột trung gian
    steps += tower_of_hanoi_recursive(n - 1, auxiliary, target, source)
    return steps  # Trả về chuỗi các bước

# Không đệ quy
def tower_of_hanoi_iterative(n):
    total_moves = 2**n - 1  # Tổng số bước di chuyển cần thiết
    moves = []  # List để lưu các bước di chuyển
    # Vòng lặp để tính toán các bước di chuyển
    for move in range(1, total_moves + 1):
        # Xác định đĩa nào đang được di chuyển
        disk = 1
        temp_move = move
        while temp_move % 2 == 0:
            temp_move //= 2
            disk += 1
        # Xác định cột nguồn và cột đích cho đĩa hiện tại
        if disk % 2 == 1:  # Đĩa lẻ
            if (move // 2**disk) % 3 == 0:
                source, target = 'A', 'C'
            elif (move // 2**disk) % 3 == 1:
                source, target = 'C', 'B'
            else:
                source, target = 'B', 'A'
        else:  # Đĩa chẵn
            if (move // 2**disk) % 3 == 0:
                source, target = 'A', 'B'
            elif (move // 2**disk) % 3 == 1:
                source, target = 'B', 'C'
            else:
                source, target = 'C', 'A'
        # Thêm bước di chuyển vào danh sách
        moves.append(f'Move disk {disk} from {source} to {target}')
    return '\n'.join(moves)

# Thực hiện và đo thời gian
n = 3  # Có thể thay đổi giá trị này
result_recursive_hanoi = tower_of_hanoi_recursive(n, 'A', 'C', 'B')
print(f"Tháp Hà Nội (đệ quy) cho {n} đĩa:\n{result_recursive_hanoi}")
result_iterative_hanoi = tower_of_hanoi_iterative(n)
print(f"Tháp Hà Nội (không đệ quy) cho {n} đĩa:\n{result_iterative_hanoi}")
