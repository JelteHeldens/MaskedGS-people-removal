import os
import shutil

#Folder declaration
frame_folder = ""
output_folder = ""+"_"+str(sample)
os.makedirs(output_folder, exist_ok=True)

sample = 6

frame_files = sorted(os.listdir(frame_folder))
count = 0
for i in range(0, len(frame_files), sample):
    frame_file = frame_files[i]
    frame_path = os.path.join(frame_folder, frame_file)
    
    output_path = os.path.join(output_folder, frame_file)
    shutil.copy(frame_path, output_path)
    count += 1

print(count," frames sampled (every ",sample," frames).")
