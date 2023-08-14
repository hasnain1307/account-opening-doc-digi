from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from ngo_pages import ngo_data
from private_pages import private_data
from partnership_pages import partnership_data
from deposit import cash_slip
app = FastAPI()

# Configure CORS settings
origins = ["*"]  # Adjust the list of allowed origins as needed

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/ngo_files/")
async def process_files(files: list[UploadFile] = File(...)):
    # Save the uploaded files and get their paths
    file_paths = []
    for file in files:
        with open(file.filename, "wb") as f:
            f.write(file.file.read())
        file_paths.append(file.filename)
    file_paths = sorted(file_paths)
    # Call your ngo_data function with the list of file paths
    ngo_opening = ngo_data(file_paths)

    return ngo_opening


@app.post("/private_files/")
async def process_files(files: list[UploadFile] = File(...)):
    # Save the uploaded files and get their paths
    file_paths = []
    for file in files:
        with open(file.filename, "wb") as f:
            f.write(file.file.read())
        file_paths.append(file.filename)
    file_paths = sorted(file_paths)
    # Call your ngo_data function with the list of file paths
    private_opening = private_data(file_paths)

    return private_opening


@app.post("/partnership_files/")
async def process_files(files: list[UploadFile] = File(...)):
    # Save the uploaded files and get their paths
    file_paths = []
    for file in files:
        with open(file.filename, "wb") as f:
            f.write(file.file.read())
        file_paths.append(file.filename)
    file_paths = sorted(file_paths)
    # Call your ngo_data function with the list of file paths
    partnership_opening = partnership_data(file_paths)

    return partnership_opening


@app.post("/deposit_slip")
async def process_files(files: UploadFile = File(...)):
    # Save the uploaded files and get their paths
    file_path = files.filename
    with open(file_path, "wb") as f:
        f.write(files.file.read())

    # Call your ngo_data function with the list of file paths
    deposit_slip = cash_slip(file_path)

    return deposit_slip
