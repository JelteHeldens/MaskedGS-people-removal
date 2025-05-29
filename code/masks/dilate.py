import os
import cv2
import numpy as np

#Folder declaration
input_folder = "./data/classroom/original_masks"
output_folder = "./data/classroom/masks"
os.makedirs(output_folder, exist_ok=True)

kernel_size = 20
kernel = np.ones((kernel_size, kernel_size), np.uint8)

i = 0
for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)

    #Load mask in grayscale
    mask = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    #Invert for dilation, then re-invert
    inverted = cv2.bitwise_not(mask)
    dilated = cv2.dilate(inverted, kernel, iterations=1)
    final_mask = cv2.bitwise_not(dilated)

    #Save dilated mask
    cv2.imwrite(output_path, final_mask)
    i+=1

print("Dilated",i,"images.")
