import cv2
import numpy as np
# Load an image using OpenCV
import csv
image = cv2.imread("D:\\CET\\Extrs\\Photos\\Cat1.jpg")

listx=[]
listy=[]

# Get the dimensions of the image
rows, cols = image.shape[:2]
print(rows,cols)

threshold_value=150
  

  # Loop through each pixel and set the red channel to maximum
  
for i in range(rows):
    for j in range(cols):
        if (sum(image[i, j]) / 3>=threshold_value):
            image[i, j, 0] = 255  # Set the red channel to maximum
            image[i, j, 1] = 255  # Set the green channel to maximum
            image[i, j, 2] = 255  # Set the blue channel to maximum
            listx.append(i)  # X coodinates
            listy.append(j)  # Y coordinates
        else:
            image[i, j, 0] = 0  # Set the red channel to minimum
            image[i, j, 1] = 0  # Set the green channel to minimum
            image[i, j, 2] = 0  # Set the blue channel to minimum

#insert values to numpy and then change the give an image with reduced white spots
kernel = np.ones((3, 3), np.uint8)
image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
# Resize the image to the new dimensions for display 

new_height=300
new_width=300
resized_image = cv2.resize(image, (new_width, new_height))

#create a new csv file and store the values of the dimnesions of the image to the file
with open("dimensions.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([rows, cols]) #write the dimensions to a csv file
csvfile.close()

cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()