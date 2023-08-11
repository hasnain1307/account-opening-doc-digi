import cv2
from aws_process import aws_process_cheque
from utils import get_image_names_in_directory


def page_one(image_path: str):
    page_one_data = {
        'Opening Date': "",
        'Account Tittle': "",
        'Account No': "",
        'IBAN': "",
        'Form page 2': {},
        'Form page 3': {},
        'Form page 4': {},
        'Form page 6': {},
        'Form page 7': {},
        'Form page 9': {},
    }
    image = cv2.imread(image_path)
    max_display_width = 800
    max_display_height = 1000

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (max_display_width, max_display_height))
    extracted_data = []
    saved_rois = [(206, 821, 149, 23),
                  (209, 851, 321, 36),
                  (209, 893, 266, 20),
                  (208, 919, 425, 23)]
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
        'Branch Name': "",
        'Date': "",
        'Branch Code': "",
        'Customer Client ID': "",
        'Account Title': "",
        'Country of Incorporation': "",
        'Date of Incorporation': "",
        'National Tax No': "",
        'Nature of Business': "",
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
    saved_rois = [(94, 32, 163, 41), (628, 21, 131, 17), (166, 85, 88, 18),
                  (455, 81, 303, 19), (93, 361, 666, 27), (219, 393, 116, 22), (606, 389, 150, 25),
                  (607, 430, 89, 12), (189, 419, 189, 26), (191, 449, 177, 19),
                  (571, 448, 158, 20), (188, 470, 185, 24), (466, 472, 113, 24), (655, 471, 83, 22),
                  (240, 713, 520, 37), (159, 751, 71, 27), (348, 754, 177, 23),
                  (620, 753, 140, 23), (186, 800, 168, 30), (442, 798, 137, 29), (641, 797, 120, 30),
                  (250, 832, 512, 38), (231, 873, 437, 20), (656, 895, 117, 15),
                  (162, 918, 323, 24)]
    for index, roi in enumerate(saved_rois):
        x, y, width, height = roi
        cropped_image = resized_image[y:y + height, x:x + width]
        result = aws_process_cheque(cropped_image)
        result = result['Blocks']
        extracted = ' '.join(prediction["Text"] for prediction in result if prediction['BlockType'] == "LINE")

        key = list(page_two_data.keys())[index]  # Get the corresponding key using index
        page_two_data[key] = extracted
        # print(extracted)
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
        'Nearest Landmark': "",
        'City': "",
        'Country': "",
        'Phone No': "",
    }

    image = cv2.imread(image_path)
    max_display_width = 800
    max_display_height = 1000

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (max_display_width, max_display_height))
    extracted_data = []
    saved_rois = [(225, 25, 520, 21), (148, 67, 85, 26), (334, 65, 163, 30), (600, 65, 141, 33),
                  (164, 108, 145, 34), (428, 108, 129, 37), (660, 113, 66, 29), (232, 144, 511, 41),
                  (216, 183, 573, 26), (591, 209, 156, 21), (134, 228, 339, 30), (190, 617, 106, 38),
                  (223, 761, 519, 38), (137, 857, 620, 27), (444, 881, 74, 23), (141, 904, 131, 21),
                  (351, 904, 169, 24), (153, 928, 120, 20)]
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


def page_four(image_path: str):
    page_four_data = {
        'Email': "",
        'Applicant Name 1': "",
        'Applicant Name 2': "",
    }
    image = cv2.imread(image_path)
    max_display_width = 800
    max_display_height = 1000

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (max_display_width, max_display_height))
    extracted_data = []
    saved_rois = [(586, 28, 150, 53), (176, 719, 125, 37), (410, 714, 103, 42)]
    for index, roi in enumerate(saved_rois):
        x, y, width, height = roi
        cropped_image = resized_image[y:y + height, x:x + width]
        result = aws_process_cheque(cropped_image)
        result = result['Blocks']
        extracted = ' '.join(prediction["Text"] for prediction in result if prediction['BlockType'] == "LINE")

        key = list(page_four_data.keys())[index]  # Get the corresponding key using index
        page_four_data[key] = extracted

    # for key, value in page_four_data.items():
    #     print(f"{key}: {value}")

    return page_four_data


def page_six(image_path: str):
    page_six_data = {
        'Personal Account No': "",
        'Name': "",
        'Company type': "",
        'Code Sector': "",
        'Segment': "",
        'Category': "",
        'Subtopic': "",
    }
    image = cv2.imread(image_path)
    max_display_width = 800
    max_display_height = 1000

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (max_display_width, max_display_height))
    extracted_data = []
    saved_rois = [(237, 40, 77, 19), (355, 41, 163, 22), (218, 225, 208, 29), (220, 264, 201, 30),
                  (220, 306, 202, 28), (220, 344, 204, 30), (576, 221, 168, 30)]
    for index, roi in enumerate(saved_rois):
        x, y, width, height = roi
        cropped_image = resized_image[y:y + height, x:x + width]
        result = aws_process_cheque(cropped_image)
        result = result['Blocks']
        extracted = ' '.join(prediction["Text"] for prediction in result if prediction['BlockType'] == "LINE")

        key = list(page_six_data.keys())[index]  # Get the corresponding key using index
        page_six_data[key] = extracted

    # for key, value in page_six_data.items():
    #     print(f"{key}: {value}")

    return page_six_data


def page_seven(image_path: str):
    page_seven_data = {
        'Customer Name': "",
        'Product': "",
        'Date': "",
        'Account Mandate': ""
    }
    image = cv2.imread(image_path)
    max_display_width = 800
    max_display_height = 1000

    # Resize the image while maintaining the aspect ratio
    resized_image = cv2.resize(image, (max_display_width, max_display_height))
    extracted_data = []
    saved_rois = [(203, 553, 356, 18), (215, 572, 144, 30), (593, 554, 112, 16), (539, 572, 165, 24)]
    for index, roi in enumerate(saved_rois):
        x, y, width, height = roi
        cropped_image = resized_image[y:y + height, x:x + width]
        result = aws_process_cheque(cropped_image)
        result = result['Blocks']
        for i in range(0, len(result)):
            extracted = ''
            prediction = result[i]
            if prediction['BlockType'] == "LINE":
                extracted = prediction["Text"]
                extracted_data.append(extracted)
            elif len(result) == 1:
                extracted_data.append(extracted)
    for index, roi in enumerate(saved_rois):
        x, y, width, height = roi
        cropped_image = resized_image[y:y + height, x:x + width]
        result = aws_process_cheque(cropped_image)
        result = result['Blocks']
        extracted = ' '.join(prediction["Text"] for prediction in result if prediction['BlockType'] == "LINE")

        key = list(page_seven_data.keys())[index]  # Get the corresponding key using index
        page_seven_data[key] = extracted

    # for key, value in page_seven_data.items():
    #     print(f"{key}: {value}")
    return page_seven_data


def page_nine(image_path: str):
    page_nine_data = {
        "Branch Code": "",
        "Date": "",
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
    saved_rois = [(170, 76, 94, 24), (600, 54, 107, 27), (233, 101, 386, 20),
                  (222, 174, 196, 18), (509, 172, 155, 20), (231, 246, 161, 21),
                  (516, 247, 171, 19)]
    for index, roi in enumerate(saved_rois):
        x, y, width, height = roi
        cropped_image = resized_image[y:y + height, x:x + width]
        result = aws_process_cheque(cropped_image)
        result = result['Blocks']
        extracted = ' '.join(prediction["Text"] for prediction in result if prediction['BlockType'] == "LINE")

        key = list(page_nine_data.keys())[index]  # Get the corresponding key using index
        page_nine_data[key] = extracted

    # for key, value in page_nine_data.items():
    #     print(f"{key}: {value}")

    return page_nine_data
    # print(extracted_data)


# def partnership_data(directory_path: str):
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
#     page9 = page_nine(f"{directory_path}/{image_names[8]}")
#     page1['Form page 9'].update(page9)
#     for key, value in page1.items():
#         print(f"{key}: {value}")
    # return page1

def partnership_data(image_names: list):
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
    page9 = page_nine(f"{image_names[8]}")
    page1['Form page 9'].update(page9)
    return page1
# partnership_data("Partnership")
