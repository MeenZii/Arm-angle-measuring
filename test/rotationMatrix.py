import cv2
import numpy as np

show_angle = 150 # suggested angle

# Angle to be rotated (in degrees)
angle = show_angle

# Center points (x2, y2) and rotation target points (x3, y3)
x0, y0 = (1050, 700)
x1, y1 = (450, 700)

# Converting angles to radians
angle_rad = np.radians(angle)

# Create a Rotation Transformation Matrix
rotation_matrix = np.array([[np.cos(angle_rad), -np.sin(angle_rad)],
                             [np.sin(angle_rad), np.cos(angle_rad)]])

# Apply Rotational Transformation
vector = np.array([x1 - x0, y1 - y0])
rotated_vector = np.dot(rotation_matrix, vector)

# Calculating the Position After Rotation
x1_rotated = int(rotated_vector[0] + x0)
y1_rotated = int(rotated_vector[1] + y0)

# check
print("x1_rotated:", x1_rotated)
print("y1_rotated:", y1_rotated)
print("x1:", x1)
print("y1:", y1)

img = np.zeros((1080, 2020, 3), dtype="uint8") + 255
cv2.line(img, (x0, y0), (x1, y1), (25, 0, 0), 10)  # origin
cv2.line(img, (x0, y0), (x1_rotated, y1_rotated), (0, 0, 255), 10)  # a rotating line

cv2.imshow("Test", img)
cv2.waitKey(0)
