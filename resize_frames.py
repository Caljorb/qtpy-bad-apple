import cv2
import numpy as np
import scipy as sp
import scipy.signal

NUM_FRAMES = 6572

def generate_kernel(parameter):
    kernel = np.array([0.25 - parameter / 2.0, 0.25, parameter,
                     0.25, 0.25 - parameter /2.0])
    return np.outer(kernel, kernel)

def reduce(image):
    kernel = generate_kernel(.4)

    y, x = image.shape
    while y > 5 and x > 5:
        image = sp.signal.convolve2d(image, kernel, 'same')
        image = image[::2, ::2]
        y, x = image.shape

    return image

def display(image):
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():

    # for i in range(NUM_FRAMES):
    for i in range(1, NUM_FRAMES+1):
        frame_in = './frames_in/output_{:04d}.jpg'.format(i)
        frame = cv2.imread(frame_in, cv2.IMREAD_GRAYSCALE)
        frame = reduce(frame)

        frame_out = './frames_out/output_{:04d}.jpg'.format(i)
        cv2.imwrite(frame_out, frame)
        # display(frame)

if __name__ == "__main__":
    main()
