import cv2
import numpy as np
from matplotlib import pyplot as plt


def plot_many_images(images, titles, rows=1, columns=2):

	"""Plots each image in a given list in a grid format using Matplotlib."""

	for i, image in enumerate(images):

		plt.subplot(rows, columns, i+1)

		plt.imshow(image, 'gray')

		plt.title(titles[i])

		plt.xticks([]), plt.yticks([])  # Hide tick marks

	plt.show()

def pre_process_image(img, skip_dilate=False):

	"""Uses a blurring function, adaptive thresholding and dilation to expose the main features of an image."""

	# Gaussian blur with a kernal size (height, width) of 9.

	# Note that kernal sizes must be positive and odd and the kernel must be square.

	proc = cv2.GaussianBlur(img.copy(), (9, 9), 0)

	# Adaptive threshold using 11 nearest neighbour pixels

	proc = cv2.adaptiveThreshold(proc, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

	# Invert colours, so gridlines have non-zero pixel values.

	# Necessary to dilate the image, otherwise will look like erosion instead.

	proc = cv2.bitwise_not(proc, proc)
	if not skip_dilate:
		kernel = np.array([[0., 1., 0.], [1., 1., 1.], [0., 1., 0.]])
		proc = cv2.dilate(proc, kernel)
		return proc


def show_image(img):

	"""Shows an image until any key is pressed."""

	cv2.imshow('image', img)  # Display the image

	cv2.waitKey(0)  # Wait for any key to be pressed (with the image window active)

	cv2.destroyAllWindows()  # Close all windows

img=cv2.imread('sudoku.jpg',cv2.IMREAD_GRAYSCALE)

ret, threshold1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

threshold2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

processed=pre_process_image(img)

show_image(processed)
