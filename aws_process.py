import base64
import requests
import cv2
import ast

AWS_API = "https://ta57zu3sri.execute-api.us-east-2.amazonaws.com/default/aws-textract"
API_KEY = "VkPZZtgH8SSEGF1H8P5J7wcmt4rFdqe7FZWhqqG2"


def aws_process_cheque(image):
    try:
        # Read the image from the local directory
        # image = cv2.imread(image_path)

        if image is None:
            raise ValueError("Unable to read the image file.")

        # Encode the image as base64
        retval, buffer = cv2.imencode('.jpg', image)
        encoded_image = base64.b64encode(buffer).decode('utf-8')

        # Prepare data for the AWS API with double quotes around keys
        dat = {"Image": encoded_image}
        # dat = json.dumps(dat)
        url = AWS_API
        headers = {"x-api-key": API_KEY, "Content-Type": "application/json"}

        # Call the AWS Textract API using the 'json' parameter
        response = requests.post(url, json=dat, headers=headers)
        # Parse the response
        load = response.text
        load = ast.literal_eval(load)
        print("Textract response:", type(load))
        return load

    except Exception as e:
        print("Error:", str(e))
        return None
