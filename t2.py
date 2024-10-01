import math

reference_point = (3, 3)
points = [(2, 8), (3, 7), (4, 6), (3, 5), (5, 3), (7, 4), (8, 2), (6, 1), (1, 2), (6, 9)]

distances = [(p, math.dist(reference_point, p)) for p in points]
closest = min(distances, key=lambda x: x[1])
farthest = max(distances, key=lambda x: x[1])



print(f"Closest: {closest[0]}, Distance: {closest[1]:.2f}")
print(f"Farthest: {farthest[0]}, Distance: {farthest[1]:.2f}")













# import math

# # พิกัดของจุดอ้างอิง
# reference_point = (3, 3)

# # พิกัดของจุดต่าง ๆ
# points = [
#     (2, 8),
#     (3, 7),
#     (4, 6),
#     (3, 5),
#     (5, 3),
#     (7, 4),
#     (8, 2),
#     (6, 1),
#     (1, 2),
#     (6, 9)
# ]

# # ฟังก์ชันคำนวณระยะทางระหว่างจุดสองจุด
# def calculate_distance(p1, p2):
#     return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# # คำนวณระยะทางสำหรับแต่ละจุดและเก็บผลลัพธ์ในลิสต์
# distances = []
# for point in points:
#     distance = calculate_distance(reference_point, point)
#     distances.append((point, distance))

# # หาจุดที่ใกล้ที่สุดและไกลที่สุด
# closest_point = min(distances, key=lambda x: x[1])
# farthest_point = max(distances, key=lambda x: x[1])

# # แสดงผลลัพธ์
# print("Distances from reference point (3, 3):")
# for point, distance in distances:
#     print(f"Point {point}: Distance = {distance:.2f}")

# print(f"\nClosest point: {closest_point[0]} with distance {closest_point[1]:.2f}")
# print(f"Farthest point: {farthest_point[0]} with distance {farthest_point[1]:.2f}")



# import math

# reference_point = (3, 3)
# points = [(2, 8), (3, 7), (4, 6), (3, 5), (5, 3), (7, 4), (8, 2), (6, 1), (1, 2), (6, 9)]

# # คำนวณระยะทาง
# distances = [(p, math.dist(reference_point, p)) for p in points]

# # หาระยะทางที่ใกล้สุดและไกลสุด
# min_distance = min(distances, key=lambda x: x[1])[1]
# max_distance = max(distances, key=lambda x: x[1])[1]

# # หาจุดที่มีระยะทางใกล้สุดและไกลสุด
# closest_points = [p for p, d in distances if d == min_distance]
# farthest_points = [p for p, d in distances if d == max_distance]

# แสดงผลลัพธ์
# print(f"Closest points: {closest_points}, Distance: {min_distance:.2f}")
# print(f"Farthest points: {farthest_points}, Distance: {max_distance:.2f}")