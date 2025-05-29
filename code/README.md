# INFORMATION

Information about how to run all parts of the pipeline are explained in the "how to" section from the [README](https://github.com/JelteHeldens/MaskedGS-people-removal/blob/main/README.md#how-to) in the root folder.

This README contains a quick summary of the files present here:
  - <b>frames</b>: Contains code needed to extract frames from video input, and code to subsample frames to reduce image amount.
  - <b>masked-gaussian-splatting</b>: Contains the masked Gaussian Splatting code.
  - <b>masks</b>: Contains the code to generate masks, dilate them, and later resize them for the actual Gaussian Splatting reconstruction.
