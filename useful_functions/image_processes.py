"""
Image processes.
"""

import os
import datetime

import cv2
import numpy as np


def change_img_size(original_img_path: str, result_img_path: str, img_size: tuple = (320,240)) -> None:
    """
    Open file and change its size.
    """

    # Open file from path
    img = cv2.imread(original_img_path)

    # Resize it
    simg = cv2.resize(img, img_size)
    print(simg.shape)

    # Save the updated image
    cv2.imwrite(result_img_path, simg)


def color_pixels_to_black(original_img_path: str, result_img_path: str, img_size: tuple = (320,240)) -> None:
    """
    Change all not totally white pixels of image to black, and save the result.
    """

    # Open file from path
    img = cv2.imread(original_img_path)
    print(simg.shape)

    # Resize it
    simg = cv2.resize(img, img_size)


    # Create a mask where any channel is not 255 (not pure white)
    mask = np.any(simg < 255, axis=-1)

    # Set all non-white pixels to black
    simg[mask] = [0, 0, 0]

    # Save the updated image
    cv2.imwrite(result_img_path, simg)


def generate_training_images(orig_dir: str, result_dir: str) -> None:
    """
    Get all the image files from 'dir' and turn them to clean black and white images,
    then saves to 'result_dir'.
    """

    # List all .png files in the directory
    files = [f for f in os.listdir(orig_dir) if f.lower().endswith('.png')]
    print(f"Number of PNG files in dir: {len(files)}")

    for file in files:
        # Read image
        img = cv2.imread(os.path.join(orig_dir, file))

        if img is None:
            print(f"Could not read image: {file}")
            continue

        print(img.shape)

        # Create mask for pixels that are almost white (all channels >= 254)
        almost_white_mask = np.all(img >= 254, axis=-1)

        # Create new image: white where almost white, black elsewhere
        result = np.zeros_like(img)
        result[almost_white_mask] = [255, 255, 255]

        # Save the results
        result_path = os.path.join(result_dir, f"y_{file}")
        cv2.imwrite(result_path, result)


def check_generation_results(result_dir: str):
    """
    Check every picture in result folder and create report in a txt file.
    """

    start_time = datetime.datetime.now()
    report_text = "Checking the images, if they contains just black and white pixels.\n"

    correct_imgs = 0

    # List all .png files in the directory
    files = [f for f in os.listdir(result_dir) if f.lower().endswith('.png')]
    print(f"Number of PNG files in dir: {len(files)}")

    report_text += f"Total number of files in dir: {len(files)} pcs \nList of wrong pictures"


    for file in files:
        img = cv2.imread(os.path.join(result_dir, file))
        pix_numb = int(img.shape[0]) * int(img.shape[1])

        white_pixs = 0
        black_pixs = 0
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img[i][j][0] == 255 and img[i][j][1] == 255 and img[i][j][2] == 255:
                    white_pixs +=1
                elif img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 0:
                    black_pixs +=1

        if (white_pixs + black_pixs) == pix_numb:
            correct_imgs +=1
        else:
            report_text += f"\n  - {file}"


    print(f"Correct: {correct_imgs} pcs.")
    report_text += f"\nCorrect: {correct_imgs} pcs."

    with open(
            file=f"logs/{start_time.strftime("%d_%m_%y__%H_%M_%S_%MS")}_report_{correct_imgs}.txt",
            mode="w",
            encoding="utf-8"
        ) as report:
            report.write(report_text)
