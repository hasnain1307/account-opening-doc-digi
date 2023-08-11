import cv2
from aws_process import aws_process_cheque
from utils import get_image_names_in_directory


def page_one(image_path: str):
    page_one_data = {
        'Branch Manager': "",
        'Date': "",
        'Branch Code': "",
        'Customer id': "",
        'Account Tittle': "",
        'Country of Incorporation': "",
        'Date of Incorporation': "",
        'Nature of Business': "",
        'National Tax No': "",
        'No of Employees': "",
        'Reg./License No': "",
        'Issuing Authority': "",
        'Issue Date': "",
        'Expiry Date': "",
        'Signature Form': {},
        'Acknowledgement Form': {}
    }

    image = cv2.imread(image_path)
    max_display_width = 800
    max_display_height = 1000

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (max_display_width, max_display_height))
    extracted_data = []
    saved_rois = [(118, 52, 171, 39), (637, 36, 133, 24), (184, 101, 88, 22),
                  (467, 100, 304, 22), (116, 383, 654, 26), (243, 414, 195, 22), (619, 413, 149, 21),
                  (213, 439, 206, 28), (606, 451, 162, 16), (213, 468, 204, 22), (587, 468, 183, 24),
                  (202, 494, 212, 21), (490, 492, 103, 24), (663, 493, 105, 23)]

    for index, roi in enumerate(saved_rois):
        x, y, width, height = roi
        cropped_image = resized_image[y:y + height, x:x + width]
        result = aws_process_cheque(cropped_image)
        result = result['Blocks']
        extracted = ' '.join(prediction["Text"] for prediction in result if prediction['BlockType'] == "LINE")

        key = list(page_one_data.keys())[index]  # Get the corresponding key using index
        page_one_data[key] = extracted
    # for key, value in page_one_data.items():
    #     print(f"{key}: {value}")
    return page_one_data


def page_two(image_path: str):
    page_two_data = {
        "Branch Code": "",
        "Date": "",
        "Account Number": "",
        "Account Tittle": "",
        "Name 1 left: ": "",
        "Name 1 right: ": "",
        "Name 2 left: ": "",
        "Name 2 right: ": "",
    }

    image = cv2.imread(image_path)
    max_display_width = 800
    max_display_height = 1000

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (max_display_width, max_display_height))
    extracted_data = []
    saved_rois = [(135, 79, 97, 21), (575, 53, 101, 22), (488, 81, 188, 18),
                  (195, 99, 303, 20), (189, 175, 190, 16), (470, 157, 182, 31),
                  (193, 249, 152, 22), (486, 246, 140, 21)]

    for index, roi in enumerate(saved_rois):
        x, y, width, height = roi
        cropped_image = resized_image[y:y + height, x:x + width]
        result = aws_process_cheque(cropped_image)
        result = result['Blocks']
        extracted = ' '.join(prediction["Text"] for prediction in result if prediction['BlockType'] == "LINE")

        key = list(page_two_data.keys())[index]  # Get the corresponding key using index
        page_two_data[key] = extracted
    # for key, value in page_two_data.items():
    #     print(f"{key}: {value}")
    return page_two_data


def page_three(image_path: str):
    page_three_data = {
        "Account Tittle": "",
        "Date": "",
        "Product Chosen": "",
        "Mandate of Account": "",
        "Address": "",
        "Contact no": "",
        "Mobile no": "",
        "Email Address": "",
    }

    image = cv2.imread(image_path)
    max_display_width = 800
    max_display_height = 1000

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (max_display_width, max_display_height))
    extracted_data = []
    saved_rois = [(190, 550, 301, 19), (582, 548, 112, 20), (184, 570, 254, 21), (517, 567, 173, 24),
                  (170, 603, 378, 18), (175, 634, 94, 16), (315, 632, 102, 16), (474, 627, 215, 21)]

    for index, roi in enumerate(saved_rois):
        x, y, width, height = roi
        cropped_image = resized_image[y:y + height, x:x + width]
        result = aws_process_cheque(cropped_image)
        result = result['Blocks']
        extracted = ' '.join(prediction["Text"] for prediction in result if prediction['BlockType'] == "LINE")

        key = list(page_three_data.keys())[index]  # Get the corresponding key using index
        page_three_data[key] = extracted
    # for key, value in page_three_data.items():
    #     print(f"{key}: {value}")
    return page_three_data

# def ngo_data(directory_path: str):
#     image_names = get_image_names_in_directory(directory_path)
#     # page1 = page_one(f"{directory_path}/{image_names[0]}")
#     # page2 = page_two(f"{directory_path}/{image_names[1]}")
#     # page1['Signature Form'].update(page2)
#     page3 = page_three(f"{directory_path}/{image_names[2]}")
#     # page1['Acknowledgement Form'].update(page3)
#     # for key, value in page1.items():
#     #     print(f"{key}: {value}")
#
# ngo_data('Trust-NGO')


def ngo_data(image_names: list):
    # image_names = get_image_names_in_directory(directory_path)
    # print(image_names)
    page1 = page_one(f"{image_names[0]}")
    page2 = page_two(f"{image_names[1]}")
    print(page1.items())
    page1['Signature Form'].update(page2)
    page3 = page_three(f"{image_names[2]}")
    page1['Acknowledgement Form'].update(page3)
    return page1
