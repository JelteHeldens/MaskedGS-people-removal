import os
import torch
import torchvision.transforms as T
from torchvision.models.segmentation import deeplabv3_resnet101
from PIL import Image
import numpy as np
import cv2

#Folder declaration
input_folder = "./data/classroom/images_people"
output_folder = "./data/classroom/original_masks"
os.makedirs(output_folder, exist_ok=True)

#Use GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:",device)

#Load pretrained DeepLabV3+ model
model = deeplabv3_resnet101(pretrained=True).to(device).eval()

#Preprocessing
transform = T.Compose([
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225])
])

# Class index for 'person' in COCO is 15
PERSON_CLASS_ID = 15

# Loop over input images
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg')):
        input_path = os.path.join(input_folder, filename)
        image = Image.open(input_path).convert("RGB")
        image_tensor = transform(image).unsqueeze(0).to(device)

        #Run the model
        with torch.no_grad():
            output = model(image_tensor)['out'][0]
        prediction = output.argmax(0).byte().cpu().numpy()

        #Create binary mask for 'person' class
        mask = (prediction == PERSON_CLASS_ID).astype(np.uint8) * 255

        #Invert mask (black = person, white = background)
        inverted_mask = cv2.bitwise_not(mask)

        #Save masks
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg.png")
        cv2.imwrite(output_path, inverted_mask)
        print("Saved segmentation mask:", output_path)

print("Finito!")
