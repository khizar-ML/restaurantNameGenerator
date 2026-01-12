# 🍽️ Restaurant Name & Menu Generator

A simple Python-based tool that uses **LangChain** and **Google Gemini** to generate creative restaurant names based on cuisine and suggests a matching menu of popular dishes.

## 🚀 Features
- **Smart Naming:** Generates unique restaurant names using Gemini 2.0 Flash.
- **Menu Generation:** Automatically creates a list of popular dishes for the generated restaurant name.
- **Modern Architecture:** Built using LangChain Expression Language (LCEL) for efficient data piping.

## 🛠️ Tech Stack
- **Python**
- **LangChain** (v0.3+)
- **Google Gemini API**

## 🏁 Quick Start
1. **Clone this Repo**
2. **Create virtaul envoirnment**: python -m venv .venv
3. **Activate .venv:**
     .venv\Scripts\activate
4. **Install Dependencies:**
     pip install -r requirements.txt
5. **Add API Key:**
     Create a file named google_secret.py
     put your api key as ***key = ''***
6. **Hit Run:**
     streamlit run main.py
