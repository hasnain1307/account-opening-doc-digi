import numpy as np
import cv2
import os
# from partnership_pages import page_two, page_one, page_three, page_four, page_six, page_seven, page_nine
# from ngo_pages import page_one, page_two, page_three
# from private_pages import page_two, page_one, page_three, page_four, page_six, page_seven, page_nine
from utils import get_image_names_in_directory, roi_selected


directory_path = "Partnership"
image_names = get_image_names_in_directory(directory_path)
# print(image_names)
roi_selected(f"{directory_path}/{image_names[1]}")
# page_two(f"Partnership/{image_names[1]}")

# result = aws_process_cheque("cropped.jpg")
# print(result)

# def ngo_data(image_names: list):
#     # image_names = get_image_names_in_directory(directory_path)
#     # print(image_names)
#     page1 = page_one(f"{image_names[0]}")
#     page2 = page_two(f"{image_names[1]}")
#     print(page1.items())
#     page1['Signature Form'].update(page2)
#     page3 = page_three(f"{image_names[2]}")
#     page1['Acknowledgement Form'].update(page3)
#     return page1
    # for key, value in page1.items():
    #     print(f"{key}: {value}")

# def ngo_data(directory_path: str):
#     image_names = get_image_names_in_directory(directory_path)
#     page1 = page_one(f"{directory_path}/{image_names[0]}")
#     page2 = page_two(f"{directory_path}/{image_names[1]}")
#     page1['Signature Form'].update(page2)
#     page3 = page_three(f"{directory_path}/{image_names[2]}")
#     page1['Acknowledgement Form'].update(page3)
#     for key, value in page1.items():
#         print(f"{key}: {value}")


# ngo_data("Trust-NGO")


# def partnership_data(directory_path: str):
#     image_names = get_image_names_in_directory(directory_path)
#     page1 = page_one(f"{directory_path}/{image_names[0]}")
#     page2 = page_two(f"{directory_path}/{image_names[1]}")
#     page3 = page_three(f"{directory_path}/{image_names[2]}")
#     page4 = page_four(f"{directory_path}/{image_names[3]}")
#     page6 = page_six(f"{directory_path}/{image_names[5]}")
#     page7 = page_seven(f"{directory_path}/{image_names[6]}")
#     page9 = page_nine(f"{directory_path}/{image_names[8]}")
#     for key, value in page3.items():
#         print(f"{key}: {value}")
#     page1['Signature Form'].update(page2)
#     page3 = page_three(f"{directory_path}/{image_names[2]}")
#     page1['Acknowledgement Form'].update(page3)
#     for key, value in page1.items():
#         print(f"{key}: {value}")


# partnership_data("Partnership")