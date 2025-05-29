# Masked Gaussian Splatting for people removal pipeline

![pipeline](https://github.com/user-attachments/assets/86f04433-8f27-4bcf-86f1-4f274b310e17)

## Disclaimer

This GitHub page provides code and data used in a thesis. Everything here is for educational purpose only.

The Gaussian Splatting is based on the [original Gaussian Splatting by graphdeco-inria](https://github.com/yzslab/gaussian-splatting/tree/dynamic_mask),
the adaptation made here is build off of work by user [yzslab](https://github.com/yzslab/gaussian-splatting/tree/dynamic_mask).
Besides the code available on this GitHub page, [COLMAP](https://github.com/colmap/colmap) is required.

The data available on this page is captured by me. The people in these datasets have given me
their permission to use these images for the purpose of the thesis. Because of this, the
datasets won’t be publicly available for a long time. Please refrain from using this data, even
for educational purposes, to respect the privacy and wishes of the people present in them.

## Information

This technique contains a pipeline designed for the removal of dynamic elements for scene reconstruction using Gaussian Splatting, focussed on humans.
Besides the code present in this repository, [COLMAP](https://github.com/colmap/colmap) is required. It is based on segmentation masks from DeepLabV3+,
COLMAP and an adapted version of Gaussian Splatting.

In case there are any issues with the submodules, please refer to the [original Gaussian Splatting by graphdeco-inria](https://github.com/yzslab/gaussian-splatting/tree/dynamic_mask).
The version used is from oct 30, 2024 (comit: 54c035f7834b564019656c3e3fcc3646292f727d).

No outputs from the total pipeline are stored in this repository, as the file size of the reconstructions exceed the maximum GitHub file size. One dataset, "classroom",
is made fully ready for reconstruction. To run this see the [Executing reconstruction](https://github.com/JelteHeldens/MaskedGS-people-removal/edit/main/README.md#executing-reconstruction) step of the "How to" section.

## How to

### OPTIONAL: Video input processing

In case the desired input is a video, use [get_frames.py](https://github.com/JelteHeldens/MaskedGS-people-removal/blob/main/code/frames/get_frames.py) to extract the frames from the video.

Afterwards, to reduce the amount of frames, [frames_sample.py](https://github.com/JelteHeldens/MaskedGS-people-removal/blob/main/code/frames/frames_sample.py) can be used. The recommended amount
 of images is around 125 to 190.)


### Segmentation mask creation

The first step in this pipeline is the creation of the segmentation masks. To generate these masks, simply run [deeplab.py](https://github.com/JelteHeldens/MaskedGS-people-removal/blob/main/code/masks/deeplab.py)
, after changing the paths of course. Then run [dilate.py](https://github.com/JelteHeldens/MaskedGS-people-removal/blob/main/code/masks/dilate.py), to dilate the masks.

### COLMAP reconstruction

After the first step, COLMAP can be performed on the input images and correlated masks. Simply launch COLMAP, or run it from the command line,
using the input images, masks and a workspace folder as arguments.

### Masked Gaussian Splatting reconstruction

#### Preperation

After completion, the COLMAP workspace folder contains a "sparse" folder and "database.db" file.
Move these two files in to a seperate folder named "distorted". Now copy the images to the folder that contains the "distorted" folder, (ideally do this in the workspace folder to not overwrite anything
as this step also creates an "images" folder) and rename it to "input".
 Now navigate to the [masked-gaussian-splatting](https://github.com/JelteHeldens/MaskedGS-people-removal/tree/main/code/masked-gaussian-splatting) folder.
 Here, run [convert.py](https://github.com/JelteHeldens/MaskedGS-people-removal/blob/main/code/masked-gaussian-splatting/convert.py) as follows:

 ```bash
python convert.py -s <path/to/folder/containing/disorted/and/input> --skip_matching
```

To run the masked Gaussian Splatting reconstruction, the masks have to be resized first to match the resultion of their correlated image in the newly created
"images" folder from the convert.py step. To do this run [resize.py](https://github.com/JelteHeldens/MaskedGS-people-removal/blob/main/code/masks/resize.py) after,
again, changing the paths.

#### Executing reconstruction

If the conversion is run, and the masks are resized, masked Gaussian Splatting can be executed. To create a reconstruction using masks run:

 ```bash
python train.py -s <path/to/folder/containing/disorted/and/input> --resolution 2 --masks <path/to/resized/masks>
```

You can use the same command without the masks argument to do a mask-less reconstruction for comparion (the resolution argument is of course optional)

#### Evaluation

Finally, if you want images from the reconstruction rendered from the same camera positions as the input images, you can run this command:

 ```bash
python render.py --model_path <path/to/output/folder/from/reconstruction> --source_path <path/to/folder/containing/disorted/and/input>
```

This will provide you with rendered images as well as ground truth images for comparison.
