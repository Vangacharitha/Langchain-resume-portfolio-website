# 🚀 Langchain-resume-portfolio-website

An **AI-powered Website Generator** that converts **natural language input** and **resume data** into a **complete, interactive portfolio website** using **LangChain**, **Google Gemini**, and **Streamlit**.

This application enables users to generate **HTML, CSS, and JavaScript** code instantly through a clean and intuitive UI.

---

## 🔥 Features

- 🧠 **Resume / Prompt → Website Code Generation**
- 🤖 Powered by **LangChain** and **Google Gemini LLM**
- 🎨 Clean & modern **Streamlit UI**
- 📄 Generates structured frontend code:
  - **HTML**
  - **CSS**
  - **JavaScript**
- 🔗 **Interactive LinkedIn & GitHub links**
- 🧩 Skills displayed as **clean tags (no percentages)**
- 📦 **One-click ZIP download** of generated website
- ⚡ **Real-time AI response**
- 💻 Beginner-friendly & extensible architecture

---

## 🖥️ Application Interface

<img width="1437" height="794" alt="portfolio reseme interface" src="https://github.com/user-attachments/assets/393adba5-a95c-4572-a8d6-639c31425b3e" />



### 🔹 Streamlit UI
> Upload your resume and generate a **premium, recruiter-ready portfolio website**.

### 🔹 Generated Portfolio Website
> A clean, modern, and interactive personal portfolio.

---

## 🗂️ Project Structure

```text
langchain-streamlit-website-generator/
│# UI assets & images
├── generated_files/        # AI-generated HTML, CSS, JS
├── screenshots/            # Application screenshots
├── main.py                 # Streamlit application
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
````

---

## ⚙️ Tech Stack

* **Python**
* **Streamlit** – UI Framework
* **LangChain** – LLM orchestration
* **Google Gemini API** – AI model
* **HTML / CSS / JavaScript** – Frontend output

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Vangacharitha/langchain-streamlit-website-generator.git
cd langchain-streamlit-website-generator
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate  # macOS / Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Environment Variable

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run main.py
```

Open in your browser:

```text
http://localhost:8501
```

---

## ✨ How It Works

1. 📄 User uploads a **resume (PDF / DOCX)**
2. 🧠 Resume text is extracted
3. 🔗 Data is sent to **LangChain**
4. 🤖 LangChain interacts with **Google Gemini**
5. 🎨 AI generates:

   * **HTML**
   * **CSS**
   * **JavaScript**
6. 📦 User downloads the **complete portfolio website (ZIP)**

---

## 📌 Example Input

```text
Generate a modern, professional portfolio website with
interactive projects and contact section.
```

---

## 📈 Future Enhancements

* 🎯 Template-based generation
* 🌙 Dark / Light mode toggle
* 🔗 Live preview inside Streamlit
* ☁️ Cloud deployment (GitHub Pages / Netlify)
* 🤖 AI-powered content enhancement

---

## 👩‍💻 Author

**Vanga Charitha**
Aspiring Data Analyst | Data Science Enthusiast
📍 Hyderabad, Telangana, India

📧 **Email**: [charithavanga@gmail.com](mailto:charithavanga@gmail.com)
🔗 **LinkedIn**: [https://www.linkedin.com/in/charitha-vanga/](https://www.linkedin.com/in/charitha-vanga/)
🐙 **GitHub**: [https://github.com/Vangacharitha](https://github.com/Vangacharitha)

---

🚀 *Built with passion for **AI**, **Web Development**, and **Automation***

````
