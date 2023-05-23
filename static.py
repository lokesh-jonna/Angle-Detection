import cv2
from skimage.transform import hough_line, hough_line_peaks
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


def edge_detection(img, blur_ksize=5, threshold1=100, threshold2=200):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gaussian = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 0)
    img_canny = cv2.Canny(img_gaussian, threshold1, threshold2)

    return img_canny


image = edge_detection(cv2.imread('lo.png'))

h, theta, d = hough_line(image)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
ax = axes.ravel()

ax[0].imshow(image)
ax[0].set_title('Input image')
ax[0].set_axis_off()

ax[1].imshow(image, cmap=cm.gray)
for _, angle, dist in zip(*hough_line_peaks(h, theta, d)):
    y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
    y1 = (dist - image.shape[1] * np.cos(angle)) / np.sin(angle)
    ax[1].plot((0, image.shape[1]), (y0, y1), '-r')
ax[1].set_xlim((0, image.shape[1]))
ax[1].set_ylim((image.shape[0], 0))
ax[1].set_axis_off()
ax[1].set_title('Detected lines')

plt.tight_layout()
plt.show()

angle = []
dist = []
for _, a , d in zip(*hough_line_peaks(h, theta, d)):
    angle.append(a)
    dist.append(d)

angle = [a*180/np.pi for a in angle]
print(angle[0])
