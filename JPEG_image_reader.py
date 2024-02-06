from PIL import Image
import os
import matplotlib.pyplot as plt
import math

class JPEGImageReader:
    def __init__(self, directory):
        self.directory = directory
        self.images = {}

    def read_images(self, num_images=None):
        print("Reading images...\n")
        image_files = os.listdir(self.directory)
        if num_images is not None:
            image_files = image_files[:num_images]
        # TODO: tutte le immagini aperte con open() non ci stanno, guarda di mantenere la bitmap, leggi comando dell'elaborato
        for filename in image_files:
            if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
                image_path = os.path.join(self.directory, filename)
                image = Image.open(image_path)
                self.images[filename] = image
        print("Images loaded.\n")
        return self.images

    '''def get_image(self, filename):
        return self.images.get(filename)'''

    def get_all_images(self):
        return self.images

    def show_images(self, num_images=None):
        if num_images is None:
            num_images = len(self.images)
        sqrt = math.sqrt(num_images)
        if sqrt.is_integer():
            num_rows = num_columns = int(sqrt)
        else:
            num_columns = math.floor(sqrt)
            num_rows = math.ceil(num_images/num_columns)
        fig, axes = plt.subplots(nrows=num_rows, ncols=num_columns, figsize=(15, 15))
        for i, (filename, image) in enumerate(list(self.images.items())[:num_images]):
            x = i // num_columns
            y = i % num_columns
            axes[x][y].imshow(image)
        plt.setp(axes, xticks=[], yticks=[], frame_on=False)
        plt.show()

    def close_images(self):
        for image in self.images.values():
            image.close()

# Example usage:
if __name__ == "__main__":
    directory_path = os.path.abspath("images")
    reader = JPEGImageReader(directory_path)
    reader.read_images(1000)
    all_images = reader.get_all_images()
    for filename, image in all_images.items():
        print(f"Filename: {filename}, Size: {image.size}")
    reader.show_images(100)
    reader.close_images()