import numpy as np
import argparse
from PIL import Image
import sys

class imageAnalyzer():

    def __init__(self, img):
        self.img = Image.open(img)
        self.img = np.asarray(self.img)

    def get_image_stats(self):
        print(self.dimensions())
        print(self.colors())
        print(self.byte_count())
        print(self.intensity())
        print(self.brightness())

    def dimensions(self):
        dims = np.shape(self.img)
        return f"Dimensions: {dims[0]} (height) x {dims[1]} (width)"

    def colors(self):
        l = len(np.shape(self.img))

        if l <= 2:
            return "color scheme: grayscale"
        else:
            return f"color scheme: {np.shape(self.img)[l-1]} color channels (RGB or other)"

    def byte_count(self):
        return f"bytes: {len(self.img.tobytes())}"

    def intensity(self):
        if "grayscale" in self.colors():
            return "image is in grayscale"

        return f"average intensity: {np.mean(self.img)}"

    def brightness(self):
        if "grayscale" in self.colors():
            return "image is in grayscale"
        else:
            return f"average brightness: {np.average(self.img[2])/255 * 100}"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="image to return statistics for")
    args = parser.parse_args()
    image = args.image

    stats = imageAnalyzer(image)
    stats.get_image_stats()

if __name__ == '__main__':
    main()