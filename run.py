import generator
import stamp
import aggregate


def main():

    initial_string = "test"
    count = 100
    initial_image = "sample.jpg"
    code_length = 6

    generator.generate_codes(initial_string,count=count,code_length=code_length)
    stamp.stamp_codes(initial_image,font_size=20,font_color=(0,0,0),font="arial.ttf",x=0,y=0)
    aggregate.process_images(padding = 50,columns = 2,rows = 3)

main()