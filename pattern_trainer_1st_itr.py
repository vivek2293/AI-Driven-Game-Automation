from PIL import Image
import cv2
import numpy as np

# Pattern matcher for aim circle
def match_image(pattern_url, image_url):
    tar = cv2.imread(pattern_url)
    tar_gray = cv2.cvtColor(tar, cv2.COLOR_BGR2GRAY)


    # Convert to HSV Color Space:
    image = cv2.imread(image_url)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


    # Define a Green Color Range:
    lower_green = np.array([50, 218, 183]) 
    upper_green = np.array([175, 255, 255])

    # Create and apply the mask:
    mask = cv2.inRange(hsv_image, lower_green, upper_green)
    green_areas = cv2.bitwise_and(image, image, mask=mask)

    # Grayscale and blur to remove noise:
    gray_image = cv2.cvtColor(green_areas, cv2.COLOR_BGR2GRAY)

    # Template Matching:
    result = cv2.matchTemplate(gray_image, tar_gray, cv2.TM_CCOEFF_NORMED)


    threshold = 0.3
    loc = np.where(result >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0] + tar.shape[1], pt[1] + tar.shape[0]), (0, 0, 255), 2)
    
    return image


# Display detections
result_images = []
for i in range(1, 7):
    img = match_image("./images/aim_complete.png", "./Aim_train/"+str(i)+".png")
    result_images.append(img)

for idx, result_image in enumerate(result_images, start=1):
    cv2.imshow(f"Matching Result {idx}", result_image)

cv2.waitKey(0)
cv2.destroyAllWindows()