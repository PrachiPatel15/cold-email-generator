# 📧 Streamlit Cold Mail Generator

This project is a **Cold Mail Generator** built using **Streamlit** and **LangChain**. It helps users generate professional cold emails for job applications based on job descriptions provided as text or URLs.

---

## 🚀 Features
- Extracts job details from the given text or URL.
- Generates a well-structured cold email using an **LLM**.
- Displays the generated email in a formatted manner.
- Provides an option to customize the email before sending it.
- Utilizes **Groq Cloud** for efficient LLM processing and customization.

---

## 🛠️ Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/PrachiPatel15/streamlit-cold-mail-generator.git
cd streamlit-cold-mail-generator
```

### **2️⃣ Set Up Virtual Environment**
```sh
python -m venv project5
```

### **3️⃣ Activate Virtual Environment**
- **Windows (PowerShell):**
  ```sh
  project5\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source project5/bin/activate
  ```

### **4️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## 🚀 Running the Application
```sh
streamlit run app.py
```

---

## 📝 Git Adjustments

### **1️⃣ Add `.gitignore`**
To exclude the virtual environment and other unnecessary files, create a `.gitignore` file and add the following lines:
```sh
# Virtual Environment
project5/

# Python Cache
__pycache__/
*.pyc
*.pyo

# Streamlit Cache
.streamlit/

# Environment Variables
.env
```

### **2️⃣ If `.gitignore` is not working**
If the virtual environment folder (`project5/`) was already tracked by Git before adding it to `.gitignore`, remove it manually:
```sh
git rm -r --cached project5
```
Then, commit and push:
```sh
git commit -m "Removed virtual environment from tracking"
git push origin main
```

### **3️⃣ Pushing Changes to GitHub**
```sh
git add .
git commit -m "Updated project files"
git push origin main
```

---

## 📌 Notes
- Ensure your `.gitignore` file is properly set up before committing files.
- If you face a push rejection error, run:
  ```sh
  git pull origin main --rebase
  git push origin main
  ```

---

## 📩 Contact
For any issues or suggestions, feel free to open an issue or reach out!

---

**🚀 Happy Coding!** 🎉

