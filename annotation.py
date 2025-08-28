import cv2
import matplotlib.pyplot as plt

image = cv2.imread('jigsaw.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Converting Image from BGR 2 RGB

# Get Image dimensions
height, width, _ = image_rgb.shape

# Draw 2 recatngle across intersecting regions
# Rect1: Top left corner
rect1_width, rect1_height = 150, 150
top_left1 = (20, 20)  # 20 pixels padding
btm_right1 = (top_left1[0] + rect1_width, top_left1[1] + rect1_height)
cv2.rectangle(image_rgb, top_left1, btm_right1, (0, 255, 255), 3)   # Yellow rectangle

# Rect2: Bottom right corner
rect2_width, rect2_height = 200, 150
top_left2 = (width - rect2_width - 20, height - rect2_height - 20)  # 20 pixels padding
btm_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)
cv2.rectangle(image_rgb, top_left2, btm_right2, (255, 0, 255), 3)   # Magenta colour

# Draw circles at center of both the rectangles
center1_x = top_left1[0] + rect1_width // 2
center1_y = top_left1[1] + rect1_width // 2
center2_x = top_left2[0] + rect2_width // 2
center2_y = top_left2[1] + rect2_width // 2
cv2.circle(image_rgb, (center1_x, center1_y), 15, (0, 255, 0), -1)  # Filled green circle
cv2.circle(image_rgb, (center2_x, center2_y), 15,(0, 0, 255), -1)  # Filled red circle

# Draw line connecting the center of both the circles
cv2.line(image_rgb, (center1_x, center1_y), (center2_x, center2_y), (0, 255, 0), 3)

# Add text labels for regions
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb, 'Region 1', (top_left1[0], top_left1[0]-10), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Region 2', (top_left2[0], top_left2[0]-10), font, 0.7, (255, 0, 255), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Center 1', (center1_x - 40, center1_y + 40), font, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Center 2', (center2_x - 40, center2_y + 40), font, 0.6, (0, 0, 255), 2, cv2.LINE_AA)

# Add bidirectional arrow representing height
arrow_start = (width - 50, 20)  # Start near top right
arrow_end = (width - 50, height - 20)   # End near bottom right

# Draw arrow in both directions
cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.05)    # Downward arrow
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.05)    # Upward arrow

# Annnotate heigth value
height_value_position = (arrow_start[0] - 150, (arrow_start[1] + arrow_end[1])//2)
cv2.putText(image_rgb, f'Height: {height}', height_value_position, font, 0.8, (255, 255, 0), 2, cv2.LINE_AA)

# Display the edited image
plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.title('Annotated Image with Regions, Centers, Bi-directional Height arrows')
plt.axis('off')
plt.show()