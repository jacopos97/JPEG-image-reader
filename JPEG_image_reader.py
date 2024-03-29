from PIL import Image
import os
import matplotlib.pyplot as plt
import math
import time
from io import BytesIO

INPUT_IMAGES_RELATIVE_PATH = "images"
OUTPUT_IMAGES_RELATIVE_PATH = "images_bmp"
IMAGES_NUMBER = 5000


class JPEGImageReader:
    def __init__(self, directory) -> None:
        self.directory = directory
        self.images = []

    def read_images(self, num_images=None) -> None:
        image_files = os.listdir(self.directory)
        if num_images is not None and num_images <= len(image_files):
            image_files = image_files[:num_images]
        print("Reading images...")
        for filename in image_files:
            if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
                image_path = os.path.join(self.directory, filename)
                self.open_image(image_path)
        print("Images loaded.")

    def open_image(self, image_path) -> None:
        with open(image_path, 'rb') as file:
            image_data = file.read()
            image = Image.open(BytesIO(image_data))
            self.images.append(image.convert("1"))

    def get_all_images(self) -> []:
        return self.images

    def show_images(self, num_images=None) -> None:
        if num_images is None or num_images > len(self.images):
            num_images = len(self.images)
        sqrt = math.sqrt(num_images)
        if sqrt.is_integer():
            num_rows = num_columns = int(sqrt)
        else:
            num_columns = math.floor(sqrt)
            num_rows = math.ceil(num_images/num_columns)
        fig, axes = plt.subplots(nrows=num_rows, ncols=num_columns, figsize=(15, 15))
        for i, image in enumerate(self.images[:num_images]):
            x = i // num_columns
            y = i % num_columns
            axes[x][y].imshow(image)
        plt.setp(axes, xticks=[], yticks=[], frame_on=False)
        plt.show()

    def save_images(self, path) -> None:
        os.makedirs(path, exist_ok=True)
        output_path = os.path.join(path, "image")
        print("Saving images...")
        for i, image in enumerate(self.images):
            path = output_path + str(i+1) + ".bmp"
            image.save(path)
        print("Images saved.")

    def close_images(self) -> None:
        for image in self.images:
            image.close()


def clean_directory(path) -> None:
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")


if __name__ == "__main__":
    directory_path = os.path.abspath(INPUT_IMAGES_RELATIVE_PATH)
    reader = JPEGImageReader(directory_path)
    start_time = time.time()
    reader.read_images(IMAGES_NUMBER)
    execution_time = time.time() - start_time
    print("Time in seconds to read images: %s" % round(execution_time,5))
    #all_images = reader.get_all_images()
    #for filename, image in all_images.items():
        #print(f"Filename: {filename}, Size: {image.size}")
    #reader.show_images(100)
    save_path = os.path.abspath(OUTPUT_IMAGES_RELATIVE_PATH)
    clean_directory(save_path)
    start_time = time.time()
    reader.save_images(save_path)
    execution_time = time.time() - start_time
    print("Time in seconds to save images: %s" % round(execution_time,5))
    reader.close_images()
