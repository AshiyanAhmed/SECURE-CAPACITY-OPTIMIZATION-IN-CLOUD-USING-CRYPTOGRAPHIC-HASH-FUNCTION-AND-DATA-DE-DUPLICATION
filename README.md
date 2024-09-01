# SECURE-CAPACITY-OPTIMIZATION-IN-CLOUD-USING-CRYPTOGRAPHIC-HASH-FUNCTION-AND-DATA-DE-DUPLICATION
This Flask-based web app optimizes cloud storage by eliminating redundant data using deduplication and enhancing security with AES encryption and cryptographic hash functions. It ensures only unique, encrypted files are stored. The app supports Admin, Team Leader, and Member roles, each with specific functions for managing files, tasks, 

**This repository contains a project that focuses on secure data deduplication in cloud computing environments. The project features two main components:**

**Deduplication Server:** Manages data deduplication and secure storage of client data.

**Client(s):** Uploads and downloads data while ensuring secure, deduplicated data storage on the server.
Features

**Data Deduplication:** Reduces storage space by eliminating redundant data.

**Security:** Uses cryptographic techniques to ensure that deduplicated data is stored securely.

**Multiple Clients Support:** Supports communication between the server and single or multiple clients.

**System Requirements**

Server
Python 3.x
Flask (or other web frameworks)
Cloud storage provider (optional)

Client
Python 3.x
Installation and Setup

**Step 1: Clone the Repository**
bash
Copy code
git clone https://github.com/your-repository/your-project.git
cd your-project

**Step 2: Install Dependencies**
Make sure to install the necessary libraries for both the server and clients:

bash
Copy code
pip install -r requirements.txt

**Step 3: Run the Server**
To run the deduplication server, navigate to the server directory and run the following command:

bash
Copy code
python server.py

**Step 4: Run the Client**
You can configure single or multiple clients to connect to the server:

bash
Copy code
python client.py

**How It Works**
The project uses a deduplication mechanism to save space on the server by avoiding duplicate storage of files. It also ensures that client data is securely encrypted and only accessible by authorized clients.

**File Upload:**

Clients can upload files to the server.
The server checks if the file already exists and deduplicates it if necessary.

**File Download:**

Clients can download files securely from the server using the unique file identifier.

**Encryption:**

Secure encryption algorithms (e.g., AES) are used to protect the data both in storage and during transmission.

**Project Structure**
bash
Copy code
/server              # Contains server-side code for deduplication and storage management
/client              # Contains client-side code for uploading and downloading files
README.md            # Documentation file
requirements.txt     # Python dependencies
