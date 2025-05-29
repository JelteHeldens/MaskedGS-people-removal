import os
from PIL import Image

#Folder declaration
input_directory = './data/classroom/colmap/images'
mask_directory = './data/classroom/masks'
output_directory = "./data/classroom/colmap/masks"
os.makedirs(output_directory, exist_ok=True)

i = 0
for filename in os.listdir(input_directory):
    if filename.endswith('.jpg'):
        input_path = os.path.join(input_directory, filename)
        input_name = os.path.splitext(filename)[0]  # '001' from '001.jpg'

        #Determine correlated mask name
        mask_filename = input_name + '.jpg.png'
        mask_path = os.path.join(mask_directory, mask_filename)

        #Check if mask exists
        if os.path.exists(mask_path):
            with Image.open(input_path) as img:
                img_size = img.size
            with Image.open(mask_path) as mask_img:
                resized_mask = mask_img.resize(img_size, Image.NEAREST)
                output_path = os.path.join(output_directory, mask_filename)
                resized_mask.save(output_path)
            i += 1
        else:
            print("Mask doesn't exist for:",filename)

print(i,"masks resized for",output_directory)

