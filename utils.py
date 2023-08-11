import numpy as np
import cv2
import os

partnership = {
    "Account Opening Date": "",
    "Account Tittle": "",
    "Account No": "",
    "IBAN": ""
}


def get_image_names_in_directory(directory_path, image_extensions=None):
    if image_extensions is None:
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    try:
        # Get a list of all files in the directory
        file_list = os.listdir(directory_path)

        # Loop through each file in the directory
        image_names = []
        for file_name in file_list:
            # Construct the full file path
            file_path = os.path.join(directory_path, file_name)

            # Check if the path is a file and has a valid image extension
            if os.path.isfile(file_path) and any(file_name.lower().endswith(ext) for ext in image_extensions):
                image_names.append(file_name)

        # Sort the image names alphabetically
        sorted_image_names = sorted(image_names)

        return sorted_image_names

    except Exception as e:
        print("Error:", str(e))
        return []


def roi_selected(image_path: str):
    try:
        # Read the image from the local directory
        image = cv2.imread(image_path)
        max_display_width = 800
        max_display_height = 1000

        # Resize the image while maintaining the aspect ratio
        resized_image = cv2.resize(image, (max_display_width, max_display_height))

        # List to store selected ROIs
        selected_rois = []
        while True:
            # Display the resized image and select ROI
            roi = cv2.selectROI('Select ROI', resized_image, fromCenter=False, showCrosshair=True)

            # Break the loop if no ROI is selected
            if roi == (0, 0, 0, 0):
                break

            selected_rois.append(roi)
        mask = np.zeros_like(resized_image) * 255
        for roi in selected_rois:
            x, y, w, h = roi
            cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 255, 255), -1)

        result = cv2.bitwise_and(resized_image, mask)
        # Display the image with drawn rectangles
        black_pixels = (result[:, :, 0] == 0) & (result[:, :, 1] == 0) & (result[:, :, 2] == 0)
        result[black_pixels] = [255, 255, 255]
        cv2.imshow('Image with Selected ROIs', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(selected_rois)
    except Exception as e:
        print("Error:", str(e))
        return []


def generate_crop(image_path, saved_rois: list):
    image = cv2.imread(image_path)
    max_display_width = 800
    max_display_height = 1000

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (max_display_width, max_display_height))
    mask = np.zeros_like(resized_image) * 255
    for roi in saved_rois:
        x, y, w, h = roi
        cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 255, 255), -1)

    result = cv2.bitwise_and(resized_image, mask)
    black_pixels = (result[:, :, 0] == 0) & (result[:, :, 1] == 0) & (result[:, :, 2] == 0)
    result[black_pixels] = [255, 255, 255]
    cv2.imwrite('cropped.jpg', result)


def handwritten(result: list):
    result = result['Blocks']
    handwritten_text = []
    for i in range(0, len(result)):
        prediction = result[i]
        # print(prediction)
        # print(f"{prediction['Confidence'] , prediction['Text']}")
        if 'TextType' in prediction and prediction['TextType'] == 'HANDWRITING':
            handwritten_text.append({
                "pred": prediction['Text'],
                # "confidence": prediction['Confidence'],
                # "left": prediction['Geometry']['BoundingBox']['Left'],
                # "top": prediction['Geometry']['BoundingBox']['Top']
            })
    return handwritten_text
