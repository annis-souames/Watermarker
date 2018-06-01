""" 
@TODO : use pathlib and turn extension to png instead jpg.png
@TODO : add more modes
@TODO : add error checks
"""



from PIL import Image
import argparse
import os

def watermark_corner(input_image_path,
                                output_image_path,
                                watermark_image_path):
    #Main image
    base_image = Image.open(input_image_path).convert("RGBA")
    #Watermark image
    watermark = Image.open(watermark_image_path).convert("RGBA")
    width, height = base_image.size
    #Creating a temporary BG image
    bg = Image.new("RGBA",base_image.size,(0,0,0,255))
    #pasting watermark in the temp img
    bg.paste(watermark,(0,0))
    #changing the alphaness of the temp image
    bg.putalpha(50)
    #Overlaying both image together
    result = Image.alpha_composite(base_image,bg)
    #result.show()
    result.save(output_image_path)

def watermark_full(input_image_path,
                     watermark_image_path,
                     output_image_path):
    """ A full background watermark effect"""
    #Main image
    base_image = Image.open(input_image_path).convert("RGBA")
    #Watermark image
    watermark = Image.open(watermark_image_path).convert("RGBA").resize(base_image.size)
    width, height = base_image.size
    #changing the alphaness of the watermark
    watermark.putalpha(10)
    #Overlaying both image together
    result = Image.alpha_composite(base_image,watermark)
    #result.show()
    result.save(output_image_path)

def apply_watermark(original,  wm, mode):
    files = os.listdir(original)
    print files
    for f in files:
        path = original + "/" + f
        print path
        save_path = "watermarked/" + f + ".png"
        if mode == "full":
            watermark_full(path,wm,save_path)
        if mode == "corner":
            watermark_corner(path,wm,save_path)


 
parser = argparse.ArgumentParser()
parser.add_argument("mode", help = "Print directory")
parser.add_argument("path", help = "Path of the folder containing images to apply the watermark on" )
parser.add_argument("wm", help = "path of the watermark")

 
if __name__ == '__main__':
    args = parser.parse_args()
    if args.mode == "full":
        apply_watermark(original = args.path, wm = args.wm, mode = args.mode)

    