# 🤖 Simple FAQ Chatbot

A lightweight, intelligent chatbot built using **Python**, **Streamlit**, and **Sentence Transformers** that can answer common customer queries like greetings, service information, pricing, and support contact.

---

## 🚀 Features

- 💬 Handles 4 core intents:
  - Greeting
  - Product/Service Information
  - Pricing Details
  - Support Contact
- 🧠 Uses semantic similarity with **SBERT** (`paraphrase-MiniLM-L6-v2`)
- ✅ Understands user queries even if phrased differently
- 🌐 Built with an interactive **Streamlit** UI

---

## 📁 Project Structure
faq-chatbot/

  ├── chatbot.py # Main Streamlit app 
  
  ├── intents.json # Intent patterns and responses
  
  ├── requirements.txt # Python dependencies
  
  └── README.md # Project documentation
## 🔧 Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/faq-chatbot.git
cd faq-chatbot
```
### 2.  Create a virtual environment
```
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt

```

### 4. Run the chatbot
```
streamlit run app.py

```

## How It Works
- User input is embedded using SentenceTransformer.
- All predefined intent patterns are also embedded in memory.
- Chatbot calculates cosine similarity between the input and each pattern.
- Returns a random response from the most relevant intent.

## License
This project is open-source and free to use under the MIT License.


  
