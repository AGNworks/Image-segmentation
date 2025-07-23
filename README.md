# 🛣️ Image-Segmentation with U-Net

This project uses a **U-Net neural network** to perform binary image segmentation, specifically designed to identify roads or paths in webcam images. The workflow includes image preprocessing, dataset generation, model training, and evaluation.

## 🔧 Features

- Resize and normalize images using OpenCV
- Clean GIMP-prepared images into black-and-white masks
- Automatically generate training-ready image datasets
- Quality check of dataset integrity (only black and white pixels)
- U-Net model implemented in a Jupyter notebook

## Repository Structure
```
Image-segmentation/
├── assets/
│   ├── original_images/        # Original webcam frames
│   ├── gimp_prepared_images/   # Gimp prepared frames
│   └── prepared_images/        # Black-white images
├── functions/
│   └── image_processes.py      # Functions for image processing
│   └── road_finder_Unet.ipynb  # Neural network training process
├── logs/                       # report files
├── storage/                    # Generation results
├── main.py                     # Main
└── README.md                   # Project documentation
```

## 🖼️ Image Processing Pipeline

Image preprocessing is handled by `functions/image_processes.py` which includes:

- `change_img_size()` – Resizes images to target dimensions
- `color_pixels_to_black()` – Converts all non-white pixels to black
- `generate_training_images()` – Creates clean binary masks from input
- `check_generation_results()` – Ensures only white and black pixels are present in the masks

> All masks are used as labels in supervised training for U-Net.

<p align="center">
    <img src="https://github.com/AGNworks/Image-segmentation/blob/main/assets/original_images/0.jpg" alt="Original" width="30%" />
    <img src="https://github.com/AGNworks/Image-segmentation/blob/main/assets/gimp_prepared_images/0.png" alt="GIMP Prepared" width="30%" />
    <img src="https://github.com/AGNworks/Image-segmentation/blob/main/assets/prepared_images/y_0.png" alt="Final Mask" width="30%" />
</p>

## 🧠 Model Training

The training process is defined in `functions/road_finder_Unet.ipynb` and includes:

- Data loading and preprocessing
- U-Net architecture implementation
- Model training and validation
- Visualization of predictions

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/Image-segmentation.git
cd Image-segmentation
```

### 2. Install dependencies
Just for image preparing, for training process I used Google Collab.
```bash
poetry config virtualenvs.create false
poetry install
```

### 3. Prepare Your Data
- Add original webcam images to `assets/original_images/`
- Manually clean images using GIMP and save to `assets/gimp_prepared_images/`
- Use the functions from `functions/image_processes.py`, examples of use in `main.py`
- Examples of process reports you can find in `logs/`

### 4. Train the Model
Use the prepared data to train your own U-net model for segmentation.