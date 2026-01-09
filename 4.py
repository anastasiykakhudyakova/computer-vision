"""
Задание #4
сделать сегментацию на основе суперпиксельной сегментации на основе SLIC, SEEDS, LSC
"""
import cv2
import numpy as np

def seeds_segmentation(image, n_segments=100):
    h, w = image.shape[:2]
    seeds = cv2.ximgproc.createSuperpixelSEEDS( w,  h, 3,  n_segments, num_levels=5, prior=1, histogram_bins=5,)
    seeds.iterate(image, 10)  # На каждой итерации SEEDS уточняет границы суперпикселей
    labels = seeds.getLabels()
    mask = seeds.getLabelContourMask(thick_line=False)
    return labels, mask

def lsc_segmentation(image, n_segments=100):
    h, w = image.shape[:2]

    # вычисление среднего размера суперпикселя
    region_size = int(np.sqrt((w * h) / n_segments))
    lsc = cv2.ximgproc.createSuperpixelLSC(image, region_size=region_size, ratio=0.075)
    lsc.iterate(10)
    labels = lsc.getLabels()
    mask = lsc.getLabelContourMask()
    return labels, mask

def display_results(image, labels, mask, algorithm_name):
    colored_mask = np.zeros_like(image)
    for label in range(np.max(labels) + 1):
        colored_mask[labels == label] = np.random.randint(50, 200, 3)

    contours_img = image.copy()
    if len(mask.shape) == 2:
        contours_img[mask > 0] = [255, 255, 255]

    cv2.imshow("original", image)
    cv2.imshow("mask", colored_mask)
    cv2.imshow("countours", contours_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    image = cv2.imread("Tosha.png")
    print("1. SEEDS сегментация")
    print("2. LSC сегментация")
    choice = input("Выберите метод (1 или 2): ")
    if choice == "1":
        labels, mask = seeds_segmentation(image)
        display_results(image, labels, mask, "SEEDS")

    elif choice == "2":
        labels, mask = lsc_segmentation(image)
        display_results(image, labels, mask, "LSC")

main()
