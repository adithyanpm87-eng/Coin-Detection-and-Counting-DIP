
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# COIN DETECTION AND COUNTING USING IMAGE SEGMENTATION
# ============================================================


def detect_coins(image, min_area=1000, invert=True):
    """
    Detect coins using:
    1. Grayscale conversion
    2. Median filtering
    3. Otsu thresholding
    4. Morphological processing
    5. Contour detection
    6. Area-based filtering
    """

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce noise using median filtering
    blurred = cv2.medianBlur(gray, 5)

    # Otsu thresholding
    threshold_type = cv2.THRESH_BINARY_INV if invert else cv2.THRESH_BINARY

    otsu_value, threshold = cv2.threshold(
        blurred,
        0,
        255,
        threshold_type + cv2.THRESH_OTSU
    )

    # Morphological processing
    kernel = np.ones((5, 5), np.uint8)

    opening = cv2.morphologyEx(
        threshold,
        cv2.MORPH_OPEN,
        kernel
    )

    closing = cv2.morphologyEx(
        opening,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=2
    )

    # Find external contours
    contours, _ = cv2.findContours(
        closing,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Filter contours based on area
    coin_contours = []

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > min_area:
            coin_contours.append(contour)

    return (
        gray,
        blurred,
        threshold,
        closing,
        contours,
        coin_contours,
        otsu_value
    )


def draw_detections(image, coin_contours):
    """
    Draw detected coin boundaries and numbers.
    """

    result = image.copy()

    for i, contour in enumerate(coin_contours, start=1):

        x, y, w, h = cv2.boundingRect(contour)

        cv2.drawContours(
            result,
            [contour],
            -1,
            (0, 255, 0),
            3
        )

        cv2.putText(
            result,
            str(i),
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    return result


def calculate_accuracy(actual, detected):
    """
    Calculate counting error and simple counting accuracy.
    """

    error = abs(actual - detected)

    accuracy = (
        1 - (error / actual)
    ) * 100 if actual > 0 else 0

    return error, accuracy


# ============================================================
# DATASET
# ============================================================

dataset = [
    {
        "filename": "dip3.jpeg",
        "actual": 15,
        "min_area": 5000,
        "invert": True
    },
    {
        "filename": "international-coins.jpg",
        "actual": 57,
        "min_area": 8000,
        "invert": True
    },
    {
        "filename": "famous-heads-coin-collection.jpg",
        "actual": 6,
        "min_area": 5000,
        "invert": False
    }
]


# ============================================================
# PROCESS EACH IMAGE
# ============================================================

results = []

for item in dataset:

    filename = item["filename"]

    image = cv2.imread(filename)

    if image is None:
        print("Could not load:", filename)
        continue

    (
        gray,
        blurred,
        threshold,
        closing,
        contours,
        coin_contours,
        otsu_value
    ) = detect_coins(
        image,
        min_area=item["min_area"],
        invert=item["invert"]
    )

    detected = len(coin_contours)

    error, accuracy = calculate_accuracy(
        item["actual"],
        detected
    )

    result_image = draw_detections(
        image,
        coin_contours
    )

    output_name = "result_" + filename.rsplit(".", 1)[0] + ".jpg"

    cv2.imwrite(
        output_name,
        result_image
    )

    results.append({
        "Image": filename,
        "Actual Coins": item["actual"],
        "Detected Coins": detected,
        "Counting Error": error,
        "Accuracy (%)": round(accuracy, 2),
        "Otsu Threshold": round(otsu_value, 2)
    })


# ============================================================
# FINAL RESULTS
# ============================================================

results_df = pd.DataFrame(results)

print("\nFINAL COIN COUNTING RESULTS")
print("=" * 60)

print(results_df.to_string(index=False))

average_accuracy = results_df["Accuracy (%)"].mean()
total_error = results_df["Counting Error"].sum()

print("\nAverage counting accuracy:",
      round(average_accuracy, 2), "%")

print("Total counting error:",
      total_error)

# Save results
results_df.to_csv(
    "coin_counting_results.csv",
    index=False
)

print("\nResults saved to coin_counting_results.csv")
