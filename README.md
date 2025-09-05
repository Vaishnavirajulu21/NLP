# 🇮🇳 **Wikipedia Text Analysis – India Page**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)  
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-yellow)  
![NLTK](https://img.shields.io/badge/NLTK-NLP-green)  
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)  

This project extracts text from the **Wikipedia page of India**, cleans it using **Natural Language Processing (NLP)**, and generates insights such as the **Top 100 most frequent words**. The results are saved into a **CSV file** and visualized using a **frequency distribution plot**.

---

## 🚀 **Features**

- Fetches **raw HTML content** from the Wikipedia page of India.  
- Cleans and processes the text:  
  - Converts words to **lowercase**  
  - Removes **punctuation** and **numbers**  
  - Removes **stopwords** (e.g., *is, the, at*)  
- Performs **tokenization** and **word frequency distribution**  
- Extracts the **Top 100 most common words**  
- Saves results in a **CSV file** (`top_100_words.csv`)  
- Visualizes the top words using **Matplotlib**  

---

## 🛠️ **Technologies Used**

- **Python**  
- **BeautifulSoup** – for web scraping and parsing HTML  
- **NLTK** – for stopword removal and frequency analysis  
- **Matplotlib** – for data visualization  
- **CSV module** – for saving results  

---

## 📂 **Project Structure**

├── script.py # Main Python script
├── top_100_words.csv # Output CSV file (Top 100 words with counts)
└── README.md # Documentation


---


# installation:
  - pip install beautifulsoup4
  - pip install nltk
  - pip install matplotlib
  - pip install html5lib

# run:
  command: "python script.py"

# 📊 output:
  files:
    - "📄 CSV File → top_100_words.csv"
    - "📊 Word Frequency Plot → Displays Top 20 words"
  csv_file: "top_100_words.csv"
  csv_preview:
    - { Words: "india", Count: 120 }
    - { Words: "indian", Count: 80 }
    - { Words: "states", Count: 65 }
    - { Words: "history", Count: 50 }
    - { Words: "people", Count: 45 }
 📈 visualization: "📈 A bar chart showing the Top 20 most frequent words."

# ✅use_cases:
  - "Text cleaning and preprocessing practice in NLP"
  - "Frequency distribution analysis"
  - "Web scraping + NLP mini-project"
  - "Beginner-friendly project to learn NLTK + BeautifulSoup"

# 📌future_improvements:
  - "Add Word Cloud visualization"
  - "Extend analysis to other Wikipedia pages"
  - "Perform Sentiment Analysis"
  - "Store results in a Database"

# 👩‍💻Author:
  name: "Vaishnavi"
  bio: "Biomedical Engineer turned Data Enthusiast | Python | NLP | Data Analytics"
  note: "📌 If you like this project, don’t forget to ⭐ the repo!"



