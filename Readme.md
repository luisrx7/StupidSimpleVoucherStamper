# Stupid Simple Voucher Stamper

## Use Case

The purpose of this tool is to create a list of codes generated from an initial string and stamp these codes onto an image. After that you can aggregate the stamped images into bigger image and print these images.

## Installation
```bash
git clone 
cd StupidSimpleVoucherStamper
pip install -r requirements.txt
```
## Usage

### Generate Codes
Edit run.py and change the following variables:
```python
    # The string that will be used to generate the codes
    initial_string = "ABC123"
    # The number of codes that will be generated
    count = 100
    # The name of the input image
    initial_image = "sample.jpg"
    # The lebgth of the code
    code_length = 8
```
### Stamp Codes
Replace input/sample.jgp with your image

Edit run.py and chenge the following arguments of the stamp_codes function:
```python
    # The name of the input image
    initial_image = "sample.jpg"
    # The font size of the code
    font_size = 20
    # The font color (R,G,B) of the code
    font_color = (0, 0, 0)
    # The font of the code
    font = "arial.ttf"
    # The position of the code (pixels) in the image
    x = 0
    y = 0
```

### Aggregate Images
Edit run.py and change the following arguments of the aggregate_images function:
```python
    # The offset (pixels) between the images
    padding = 10 
    # The number of images per row
    rows = 5
    # Tthe number of images per column
    columns = 5
```

### Runnig the script
```bash
#After you have installed the requirements and edited run.py to your needs you can run the script with the following command:
python3 run.py
```