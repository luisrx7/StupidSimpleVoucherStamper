from PIL import Image
import os
from rich import print


def process_images(input_folder = "output\\stamped_images\\",output_folder = "output\\grouped_images\\",padding = 50,columns = 2,rows = 3):

    # clear output folder
    for filename in os.listdir(output_folder):
        os.remove(output_folder+filename)


    files = os.listdir(input_folder)
    # sort files by creation date
    files.sort(key=lambda x: os.path.getmtime(os.path.join(input_folder, x)))
    #divide files into groups of 6
    #get image size
    images_size = Image.open(input_folder+files[0]).size

    files = [files[i:i+6] for i in range(0, len(files), 6)]




    # iterate over the groups of 6 images
    for i,files_group in enumerate(files):
        # create a new image with the size of 6 images (2x3 grid) with an offset of 50 pixels between them  with a white background
        new_im = Image.new('RGB', (images_size[0]*columns+padding*columns, images_size[1]*rows+padding), (255, 255, 255))
        # iterate over the 6 images
        for j,file in enumerate(files_group):
            # open the image
            im = Image.open(f"{input_folder}{file}")
            # calculate the position of the image
            x = (j%columns)*(images_size[0]+padding)
            y = (j//columns)*(images_size[1]+padding)
            # paste the image in the new image
            new_im.paste(im, (x,y))
        print(f"Saving {i+1}/{len(files)}")
        # save the new image
        new_im.save(f"{output_folder}{i}.jpg")
        # new_im.show()

if __name__ == "__main__":
    process_images()