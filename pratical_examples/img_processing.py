import time
import os
import concurrent.futures
from PIL import Image, ImageFilter


image_dir = "download\\"
image_names = [os.path.join(image_dir, image_name) for image_name in os.listdir(image_dir)]


def blur_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    size = (1200, 1200)
    img.thumbnail(size)

    filename = os.path.basename(img_name)
    img.save(f"processed/{filename}")
    print(f"img {filename} was processed")


if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(blur_image, image_names)
    
    end = time.perf_counter()

    print(f"Finished in {end - start} seconds")
