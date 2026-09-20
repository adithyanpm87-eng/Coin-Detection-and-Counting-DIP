# Coin Detection and Counting Using Image Segmentation Techniques

## 1. Project Overview

This Digital Image Processing mini project implements an automatic coin detection and counting system using image segmentation techniques.

The system processes coin images and identifies individual coin regions using grayscale conversion, median filtering, thresholding, Otsu's method, morphological processing, contour detection, and area-based filtering.

## 2. Problem Statement

Manual counting of coins can be inconvenient when multiple coins are present in an image. This project aims to develop a simple image-processing system that can automatically detect and count coins from digital images.

## 3. Objectives

- To understand the application of image segmentation.
- To preprocess coin images using grayscale conversion and median filtering.
- To compare global thresholding and Otsu thresholding.
- To apply morphological operations for improving segmentation.
- To detect coin boundaries using contours.
- To filter unwanted regions using contour area.
- To automatically count detected coins.
- To evaluate the detected count against manually determined counts.

## 4. Technologies Used

- Python
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Google Colab
- GitHub

## 5. Methodology

The project follows this processing pipeline:

Input Image  
↓  
Grayscale Conversion  
↓  
Median Filtering  
↓  
Histogram Analysis  
↓  
Global / Otsu Thresholding  
↓  
Morphological Processing  
↓  
Contour Detection  
↓  
Area-Based Filtering  
↓  
Coin Detection  
↓  
Coin Counting  
↓  
Evaluation

## 6. Image Processing Techniques

### Grayscale Conversion

The input colour image is converted into a grayscale image to simplify intensity-based processing.

### Median Filtering

A 5×5 median filter is applied to reduce small noise while preserving useful boundaries.

### Thresholding

Global thresholding is tested using a manually selected threshold value.

### Otsu Thresholding

Otsu's method automatically determines a threshold from the image intensity distribution.

### Morphological Processing

Morphological opening and closing are applied to improve the binary segmentation.

### Contour Detection

External contours are detected using OpenCV.

### Area-Based Filtering

Small contours are removed using a minimum contour-area threshold.

## 7. Dataset

Three test images were used:

| Image | Purpose |
|---|---|
| `dip3.jpeg` | Basic separated-coin test |
| `international-coins.jpg` | Multi-coin test |
| `famous-heads-coin-collection.jpg` | Challenging overlapping-coin test |

## 8. Results

| Image | Actual Coins | Detected Coins | Error | Accuracy |
|---|---:|---:|---:|---:|
| `dip3.jpeg` | 15 | 15 | 0 | 100.00% |
| `international-coins.jpg` | 57 | 58 | 1 | 98.25% |
| `famous-heads-coin-collection.jpg` | 6 | 9 | 3 | 50.00% |

### Average Counting Accuracy

**82.75%**

The results show that the method works effectively when coins are sufficiently separated. The overlapping-coin image produced more detection errors.

## 9. Limitations

- The method works best when coins are clearly separated.
- Touching or overlapping coins can reduce counting accuracy.
- Lighting and shadows can affect segmentation.
- Background intensity can affect thresholding.
- Minimum contour area affects the final count.
- The system does not identify coin denominations.
- Only three test images were evaluated.

## 10. Future Scope

- Watershed segmentation can be used to separate touching coins.
- Adaptive thresholding can handle uneven illumination.
- Hough Circle Transform can be investigated for circular coin detection.
- Coin denomination recognition can be added.
- A larger dataset can be used for evaluation.
- The system can be extended to real-time camera-based coin counting.

## 11. Project Structure

```text
Coin-Detection-and-Counting-DIP/
│
├── source_code.py
├── requirements.txt
├── coin_counting_results.csv
│
├── images/
│   ├── dip3.jpeg
│   ├── international-coins.jpg
│   ├── famous-heads-coin-collection.jpg
│   ├── result_dip3.jpeg
│   ├── result_international_coins.jpeg
│   └── result_famous_heads_coins.jpeg
│
├── screenshots/
│   └── Project implementation screenshots
│
└── report/
    ├── Project Report DOCX
    └── Project Report PDF
