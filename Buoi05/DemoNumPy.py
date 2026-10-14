# Cài numpy trước
import numpy as np

# Tạo mảng điểm 11 SV
scores = np.array([7.7, 9.9, 2.9, 5.3, 7.8, 9.8, 10, 9,8,10,11])
print(scores)

print("Số phần tử:", scores.size)
print("Số chiều:", scores.ndim)
print("Kích thước:", scores.shape)
print("Kiểu DL:", scores.dtype)

# Tính điểm TB, độ lệch chuẩn, trung vị
print("DTB:", np.mean(scores))
print("Độ lệch chuẩn:", np.std(scores))
print("Trung vị:", np.median(scores)) # Giá trị nằm ở giữa sau SX
print("Min:", np.min(scores))

# Tìm các diem > 7.0
score_above_7 = scores[scores >= 7]
print(score_above_7)