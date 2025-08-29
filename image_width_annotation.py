import cv2
import matplotlib.pyplot as plt

image = cv2.imread('jigsaw.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width, _ = image_rgb.shape

arrow_start = (0, 20)
arrow_end = (width-1, 20)

cv2.arrowedLine(image_rgb, arrow_start, arrow_end,(255, 255, 0), 3, tipLength=0.05)    
cv2.arrowedLine(image_rgb, arrow_end, arrow_start,(255, 255, 0), 3, tipLength=0.05)    

font = cv2.FONT_HERSHEY_SIMPLEX
height_value_position = ((arrow_start[0] + arrow_end[0])//2 - 80, arrow_start[1] - 10)
cv2.putText(image_rgb, f'Width: {height}', height_value_position,font, 0.8, (255, 255, 0), 2, cv2.LINE_AA)

plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.axis('off')
plt.title('Image with width')
plt.show()