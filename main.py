"""
File to try the functions.
"""

from useful_functions.image_processes import generate_training_images, check_generation_results


if __name__ == '__main__':
    # Generate segmented images from GIMP prepared images for NN training process
    generate_training_images(
        orig_dir='assets/gimp_prepared_images',
        result_dir='storage'
    )

    # Check if the generation was correct or not
    check_generation_results(result_dir='storage')

    # What if the folder with not properly prepared images
    check_generation_results(result_dir='assets/gimp_prepared_images')
