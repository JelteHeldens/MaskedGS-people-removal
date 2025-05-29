import os
import cv2

#Folder declaration
video_path = ""
output_folder = ""
os.makedirs(output_folder, exist_ok=True)

vidcap = cv2.VideoCapture(video_path)
success,image = vidcap.read()
count = 0
while success:
    cv2.imwrite(output_folder+"/frame%d.jpg" % count, image)     # save frame as JPEG file
    success,image = vidcap.read()
    #print('frame: ', count, success)
    count += 1
    
print(count,"frames saved.")
