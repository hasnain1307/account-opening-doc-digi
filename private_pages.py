import cv2
from aws_process import aws_process_cheque
from utils import get_image_names_in_directory


def page_one(image_path: str):
    page_one_data = {
        'Opening Date': '',
        'Account Tittle': '',
        'Account No': '',
        'IBAN': '',
        'Form page 2': {},
        'Form page 3': {},
        'Form page 4': {},
        'Form page 6': {},
        'Form page 7': {},
        'Form page 8': {},
    }

    image = cv2.imread(image_path)
    max_display_width = 800
    max_display_height = 1000

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (max_display_width, max_display_height))

    extracted_data = []
    saved_rois = [(212, 821, 150, 21), (213, 848, 324, 35), (217, 892, 271, 19), (213, 917, 428, 23)]

    for index, roi in enumerate(saved_rois):
        x, y, width, height = roi
        cropped_image = resized_image[y:y + height, x:x + width]
        result = aws_process_cheque(cropped_image)
        result = result['Blocks']
        extracted = ' '.join(prediction["Text"] for prediction in result if prediction['BlockType'] == "LINE")

        key = list(page_one_data.keys())[index]  # Get the corresponding key using index
        page_one_data[key] = extracted

    # print(page_one_data)
    return page_one_data


def page_two(image_path: str):
    page_two_data = {
        'Branch Name': "",
        'Date': "",
        'Branch Code': "",
        'Customer Client ID': "",
        'Account Title': "",
        'Country of Incorporation': "",
        'Date of Incorporation': "",
        'Nature of Business': "",
        'National Tax No': "",
        'No of Employees': "",
        'Reg./License No': "",
        'Issuing Authority': "",
        'Issue Date': "",
        'Expiry Date': "",
        'Partner Name 1': "",
        'ID Type': "",
        'ID No': "",
        'ID Expiry Date': "",
        'Date of ID Issue': "",
        'Place of ID Issue': "",
        'Nationality': "",
        'Fathers Name': "",
        'Residential Address': "",
        'Mobile Number': "",
        'Email': "",
    }

    image = cv2.imread(image_path)
    max_display_width = 800
    max_display_height = 1000

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (max_display_width, max_display_height))
    extracted_data = []
    saved_rois = [(89, 0, 161, 16), (626, 4, 128, 16), (166, 50, 83, 16),
                  (455, 50, 299, 17), (210, 313, 321, 20), (216, 356, 203, 25), (607, 357, 145, 22),
                  (182, 381, 196, 30), (593, 396, 88, 15), (203, 412, 40, 22), (582, 415, 113, 22),
                  (201, 438, 80, 21), (460, 439, 53, 19), (638, 440, 105, 16), (238, 681, 518, 36),
                  (156, 717, 71, 28), (343, 716, 148, 30), (611, 719, 113, 34), (178, 771, 93, 24),
                  (426, 777, 133, 19), (610, 776, 106, 20), (244, 797, 510, 38), (226, 836, 498, 22),
                  (642, 861, 114, 16), (145, 881, 430, 39)]

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
        'Partner Name 2': "",
        'ID Type': "",
        'ID No': "",
        'ID Expiry Date': "",
        'Date of ID Issue': "",
        'Place of ID Issue': "",
        'Nationality': "",
        'Fathers Name': "",
        'Residential Address': "",
        'Mobile Number': "",
        'Email': "",
        'Initial deposit': "",
        'Contact Person Name': "",
        'Address': "",
        'Street':"",
        'Nearest Landmark': "",
        'Area/Town': "",
        'City': "",
        'Country': "",
        'Postal Code': "",
        'Mobile number': "",
    }

    image = cv2.imread(image_path)
    max_display_width = 800
    max_display_height = 1000

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (max_display_width, max_display_height))

    saved_rois = [(234, 18, 523, 43), (154, 62, 145, 31),
                  (347, 65, 176, 25), (615, 63, 137, 28), (178, 107, 169, 32),
                  (435, 109, 135, 32), (606, 123, 143, 18), (243, 142, 512, 40),
                  (227, 182, 528, 25), (648, 208, 108, 19),
                  (152, 225, 269, 23), (210, 618, 98, 31), (230, 755, 522, 41),
                  (154, 857, 555, 20), (177, 876, 106, 23),
                  (454, 877, 75, 24), (635, 880, 119, 23), (134, 900, 147, 22),
                  (358, 901, 171, 22), (633, 905, 118, 19), (380, 924, 147, 22)]

    extracted_data = []
    for index, roi in enumerate(saved_rois):
        x, y, width, height = roi
        cropped_image = resized_image[y:y + height, x:x + width]
        result = aws_process_cheque(cropped_image)
        result = result['Blocks']
        extracted = ' '.join(prediction["Text"] for prediction in result if prediction['BlockType'] == "LINE")

        key = list(page_three_data.keys())[index]  # Get the corresponding key using index
        page_three_data[key] = extracted

    return page_three_data


def page_four(image_path: str):
    page_four_data = {
        'Email': "",
        'Applicant Name 1': "",
        'Applicant Name 2': ""
    }

    image = cv2.imread(image_path)
    max_display_width = 800
    max_display_height = 1000

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (max_display_width, max_display_height))

    saved_rois = [(565, 91, 213, 27), (176, 752, 119, 35), (395, 747, 127, 36)]

    for index, roi in enumerate(saved_rois):
        x, y, width, height = roi
        cropped_image = resized_image[y:y + height, x:x + width]
        result = aws_process_cheque(cropped_image)
        result = result['Blocks']
        extracted = ' '.join(prediction["Text"] for prediction in result if prediction['BlockType'] == "LINE")

        key = list(page_four_data.keys())[index]  # Get the corresponding key using index
        page_four_data[key] = extracted

    # print(page_four_data)
    return page_four_data


def page_six(image_path: str):
    page_six_data = {
        'Personal Account No': "",
        'Name': "",
        'Company type': "",
        'Code Sector': "",
        'Segment': "",
        'Category': "",
        'Subsector': ""
    }

    image = cv2.imread(image_path)
    max_display_width = 800
    max_display_height = 1000

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (max_display_width, max_display_height))

    saved_rois = [(246, 9, 84, 19), (366, 10, 177, 19), (231, 193, 197, 30),
                  (241, 233, 186, 29), (256, 273, 173, 30), (251, 314, 178, 29),
                  (593, 193, 157, 29)]

    for index, roi in enumerate(saved_rois):
        x, y, width, height = roi
        cropped_image = resized_image[y:y + height, x:x + width]
        result = aws_process_cheque(cropped_image)
        result = result['Blocks']
        extracted = ' '.join(prediction["Text"] for prediction in result if prediction['BlockType'] == "LINE")

        key = list(page_six_data.keys())[index]  # Get the corresponding key using index
        page_six_data[key] = extracted
    # print(page_six_data)
    return page_six_data


def page_seven(image_path: str):
    page_seven_data = {
        "Branch Code": "",
        "Date": "",
        "Account Tittle": "",
        "Company Type": "",
        "Name 1 left: ": "",
        "Name 1 right: ": "",
        "Name 2 left: ": "",
        "Name 2 right: ": ""
    }
    image = cv2.imread(image_path)
    max_display_width = 800
    max_display_height = 1000

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (max_display_width, max_display_height))

    saved_rois = [(157, 81, 71, 20), (582, 64, 100, 16), (197, 99, 302, 24),
                  (497, 134, 45, 13), (197, 170, 178, 23), (482, 170, 157, 25),
                  (198, 247, 120, 20), (492, 248, 132, 19)]

    for index, roi in enumerate(saved_rois):
        x, y, width, height = roi
        cropped_image = resized_image[y:y + height, x:x + width]
        result = aws_process_cheque(cropped_image)
        result = result['Blocks']
        extracted = ' '.join(prediction["Text"] for prediction in result if prediction['BlockType'] == "LINE")

        key = list(page_seven_data.keys())[index]  # Get the corresponding key using index
        page_seven_data[key] = extracted
    # print(page_seven_data)
    return page_seven_data


def page_eight(image_path: str):
    page_eight_data = {
        'Customer Name': "",
        'Date': "",
        'Product': "",
        'Address': ""
    }

    image = cv2.imread(image_path)
    max_display_width = 800
    max_display_height = 1000

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (max_display_width, max_display_height))

    saved_rois = [(201, 534, 351, 20), (592, 554, 123, 17), (201, 552, 154, 24), (216, 587, 339, 19)]

    for index, roi in enumerate(saved_rois):
        x, y, width, height = roi
        cropped_image = resized_image[y:y + height, x:x + width]
        result = aws_process_cheque(cropped_image)
        result = result['Blocks']
        extracted = ' '.join(prediction["Text"] for prediction in result if prediction['BlockType'] == "LINE")

        key = list(page_eight_data.keys())[index]  # Get the corresponding key using index
        page_eight_data[key] = extracted

    # print(page_eight_data)
    return page_eight_data


# def private_data(directory_path: str):
#     image_names = get_image_names_in_directory(directory_path)
#     page1 = page_one(f"{directory_path}/{image_names[0]}")
#     page2 = page_two(f"{directory_path}/{image_names[1]}")
#     page1['Form page 2'].update(page2)
#     page3 = page_three(f"{directory_path}/{image_names[2]}")
#     page1['Form page 3'].update(page3)
#     page4 = page_four(f"{directory_path}/{image_names[3]}")
#     page1['Form page 4'].update(page4)
#     page6 = page_six(f"{directory_path}/{image_names[5]}")
#     page1['Form page 6'].update(page6)
#     page7 = page_seven(f"{directory_path}/{image_names[6]}")
#     page1['Form page 7'].update(page7)
#     page8 = page_eight(f"{directory_path}/{image_names[7]}")
#     page1['Form page 8'].update(page8)
#     for key, value in page1.items():
#         print(f"{key}: {value}")
#     return page1
def private_data(image_names: list):
    # image_names = get_image_names_in_directory(directory_path)
    page1 = page_one(f"{image_names[0]}")
    page2 = page_two(f"{image_names[1]}")
    page1['Form page 2'].update(page2)
    page3 = page_three(f"{image_names[2]}")
    page1['Form page 3'].update(page3)
    page4 = page_four(f"{image_names[3]}")
    page1['Form page 4'].update(page4)
    page6 = page_six(f"{image_names[5]}")
    page1['Form page 6'].update(page6)
    page7 = page_seven(f"{image_names[6]}")
    page1['Form page 7'].update(page7)
    page8 = page_eight(f"{image_names[7]}")
    page1['Form page 8'].update(page8)
    return page1

# private_data("Private")
# private_data("Private")
