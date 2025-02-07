# Python TTD Random Pilgrim Picker

## 📌 Project Overview
The **Python TTD Random Pilgrim Picker** is a tool designed to randomly select a specified number of pilgrims while ensuring that the same individuals are not selected again within a 3-month period. The project uses **SQLite** as a database to store selections and a **Flask-based web interface** to display results.

## 🚀 Features
- Randomly selects **10 pilgrims** per batch.
- Implements a **3-month exclusion rule** to avoid repeat selections.
- Uses **SQLite** for data storage.
- Provides a **Flask-based web interface** for easy access.
- Can be deployed locally or publicly via **Render/Railway/ngrok**.

## 📂 Project Structure
```
📁 pythonTTD_Random-Piligrim-picker
│── 📄 database_setup.py       # Creates the SQLite database and table
│── 📄 insert_pilgrims.py      # Inserts sample pilgrims into the database
│── 📄 select_pilgrims.py      # Randomly selects eligible pilgrims
│── 📄 app.py                  # Flask web app for displaying selected pilgrims
│── 📄 requirements.txt        # Python dependencies
│── 📄 README.md               # Project documentation
```

## 🛠 Installation & Setup
### Prerequisites
Ensure you have **Python 3.10+** and **pip** installed on your system.

### Step 1: Clone the Repository
```sh
git clone https://github.com/yourusername/pythonTTD_Random-Piligrim-picker.git
cd pythonTTD_Random-Piligrim-picker
```

### Step 2: Create a Virtual Environment
```sh
python -m venv .venv
source .venv/bin/activate   # On macOS/Linux
# OR
.venv\Scripts\activate      # On Windows
```

### Step 3: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 4: Setup the Database
```sh
python database_setup.py
python insert_pilgrims.py
```

### Step 5: Run the Flask App
```sh
python app.py
```
Then, open **http://127.0.0.1:5000/** in your browser.

## 🌍 Deployment Options
- **Localhost:** The app runs only on your computer.
- **Public Access:** Use services like **Render, Railway, or ngrok** to share your project.

## 📜 License
This project is licensed under the **MIT License**.

## 🤝 Contributing
Feel free to submit issues or pull requests if you'd like to improve the project!

## 📧 Contact
For any inquiries, reach out to **ravens_mordant_0n@icloud.com** or open a GitHub issue.

---
⭐ **If you like this project, consider giving it a star on GitHub!** ⭐

