import requests

# List of file paths to be sent
file_paths = ["image_1.jpg", "image_2.jpg", "image_3.jpg"]

# Prepare the files to be sent
files = [("files", open(file_path, "rb")) for file_path in file_paths]
print(files)

# API endpoint URL
url = "http://127.0.0.1:8000/ngo_files"

# Send the files as a list
response = requests.post(url, files=files)

# Print the response
print(response.status_code)
print(response.json())
