from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from rich import print



def Draw_in_img(img0,text,font_size=20,font_color=(0,0,0),font="arial.ttf",x=0,y=0):
    img = img0.copy()
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("calibri.ttf", font_size)
    draw.text((x, y),text,(0,0,0),font=font)
    return img

def stamp_codes(filename_init_image,filename_codes="codes.txt",output_folder="output\\stamped_images\\",font_size=20,font_color=(0,0,0),font="arial.ttf",x=0,y=0):
    initial_image = Image.open(f"input\\{filename_init_image}")
    with open(filename_codes) as f:
        codes = f.readlines()
        for i,code in enumerate(codes):
            code = code.strip()
            img = Draw_in_img(initial_image,code,x=60,y=370,font_size=font_size,font_color=font_color,font=font)
            print(f"Saving {code} - {i+1}/{len(codes)}")
            img.save(f"{output_folder}{i}.jpg")


if __name__ == "__main__":
    stamp_codes(filename_init_image="sample.jpg")