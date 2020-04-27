#!/usr/bin/env python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImageProcessor:
    def load(self, path):
        img_array = mpimg.imread(path, cmap='rgba')
        print("image {}x{} loaded".format(*img_array.shape))
        return img_array

    def display(self, array):
        plt.imshow(array, cmap='gray')
        plt.show()


if __name__ == '__main__':
    ip = ImageProcessor()
    img = ip.load('../resources/42AI.png')
    print(type(img))
    print(img)
    ip.display(img)
    img = ip.load('../resources/stinkbug.png')
    # img_grey = [[[c, c, c] for c in line] for line in img]
    print(type(img))
    print(img)
    ip.display(img)
    # ip.display(img_grey)
    img = ip.load('../resources/stinkbug.jpg')
    print(type(img))
    print(img)
    ip.display(img)
