# Watermarker
A simple and effective batch watermark generator made with python
Watermarker is a simple tool which can apply watermark over a whole folder, it contains two modes : Full and corner
The full mode apply a watermark with the size of your original image and blend with the whole image, for example : 

The corner mode apply the watermark at the top corner of the image : 


All original images  must be in a folder and the watermark in the root folder of the repo or in subfolders

# How to use it:
Download the repo and launch your terminal (or command line) in the root folder, and call the main script : 
> pythton main.py [path] [watermark_path] [mode: full or corner]

- Replace `[path]` with the name of the folder containing all your images (such folder must remain in the root folder of the program)
- Replace `[watermark_path]` with with the path of the watermark image
- Replace `[mode]` with : Full or corner

**Dependencies :**  PIL

 
