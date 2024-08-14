# Catyls_Assesment

# Flask Data Processing Application

## Overview

This Flask application simulates data retrieval from an external service, processes the data, and stores it in memory for later retrieval.

## Setup Instructions

### 1. Clone or Download the Project

Clone the repository or download the project files to your local machine.

### 2. Open the Project in VS Code

1. Launch Visual Studio Code.
2. Open the project folder in VS Code:
   - Go to `File` > `Open Folder...`
   - Select the folder containing the project files.

### 3. Create and Activate a Virtual Environment

1. Open the integrated terminal in VS Code:
   - Go to `View` > `Terminal`

2. Create a virtual environment in the project folder:
python -m venv venv

3.Activate the virtual environment:
venv\Scripts\activate

4. Install Dependencies
Install the required Python packages listed in requirements.txt
pip install -r requirements.txt

5.Run the Flask Application
Ensure the virtual environment is activated.

Run the Flask application:
python app.py
The application will start, and you can access it in your web browser at:
http://127.0.0.1:5000/
6. Use the API Endpoints
/fetch-data: Simulates fetching and processing data from an external service.

Example: GET http://127.0.0.1:5000/fetch-data

/get-processed-data: Retrieves the processed data stored in memory.

Example: GET http://127.0.0.1:5000/get-processed-data
