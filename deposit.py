import base64
import json
import numpy as np
import requests
import cv2
import ast
from aws_process import aws_process_cheque


def cash_slip(image_path: str):
    deposit_slip = {
        "Name": "",
        "Date": "dd-mm-yyyy",
        "Account no": "----",
        "Payment Type": "----",
        "Total Amount in words": "",
        "Amount in numbers": "----",
        "Deposited Account no": "----",
        "Deposited Name": "",
        "Deposited Cnic": "----",
        "Contact Number": "----",
        "Purpose of Transaction": "----"
    }

    # Example usage:
    result = aws_process_cheque(image_path)
    print(result)
    result = result['Blocks']
    handwritten_text = []
    for i in range (0,len(result)):
        prediction = result[i]
        # print(prediction)
        # print(f"{prediction['Confidence'] , prediction['Text']}")
        if 'TextType' in prediction and prediction['TextType'] == 'HANDWRITING':
            # print(f"{prediction['Text'], prediction['Geometry']['BoundingBox']['Left'] , prediction['Geometry']['BoundingBox']['Top']}")
            handwritten_text.append({
                "pred": prediction['Text'],
                "confidence": prediction['Confidence'],
                "left": prediction['Geometry']['BoundingBox']['Left'],
                "top": prediction['Geometry']['BoundingBox']['Top']
            })
    first = handwritten_text[0]
    top = first['top']
    left = first['left']
    # top = 0.12
    # left = 0.14
    for i in range (0,len(handwritten_text)):
        if handwritten_text[i]['top'] < (top+0.01) and handwritten_text[i]['left'] < (left+0.34):
            deposit_slip['Name'] += handwritten_text[i]['pred'] + " "
        elif handwritten_text[i]['top'] < (top+0.04) and handwritten_text[i]['left'] > (left+0.59):
            deposit_slip['Date'] = handwritten_text[i]['pred']
        elif handwritten_text[i]['top'] < (top+0.07) and handwritten_text[i]['left'] > (left+0.38):
            deposit_slip['Account no'] = handwritten_text[i]['pred']
        elif handwritten_text[i]['top'] < (top+0.40) and handwritten_text[i]['left'] < (left+0.24):
            deposit_slip['Payment Type'] = handwritten_text[i]['pred']
        elif handwritten_text[i]['top'] < (top+0.52) and handwritten_text[i]['left'] < (left+0.48):
            deposit_slip['Total Amount in words'] += handwritten_text[i]['pred'] + " "
        elif handwritten_text[i]['top'] < (top+0.52) and handwritten_text[i]['left'] > (left + 0.60):
            deposit_slip['Amount in numbers'] = handwritten_text[i]['pred']
        elif (top+0.52) < handwritten_text[i]['top'] < (top + 0.60) and handwritten_text[i]['left'] > (left + 0.17):
            deposit_slip['Deposited Account no'] = handwritten_text[i]['pred']
        elif (top+0.50) < handwritten_text[i]['top'] < (top + 0.64):
            deposit_slip['Deposited Name'] += handwritten_text[i]['pred'] + " "
        elif (top+0.64) < handwritten_text[i]['top'] < (top + 0.68):
            deposit_slip['Deposited Cnic'] = handwritten_text[i]['pred']
        elif (top+0.68) < handwritten_text[i]['top'] < (top + 0.71):
            deposit_slip['Contact Number'] = handwritten_text[i]['pred']
        elif (top+0.71) < handwritten_text[i]['top'] < (top + 0.72):
            deposit_slip['Purpose of Transaction'] = handwritten_text[i]['pred']
    return deposit_slip
