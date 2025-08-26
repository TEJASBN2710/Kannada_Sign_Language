# 🤟 Kannada Sign Language Recognition

A deep learning–based web application for recognizing **Kannada Sign Language (KSL)** gestures.  
The system uses **Convolutional Neural Networks (CNN)** trained on gesture images and provides a simple web interface for users to interact with the model.

---

## 📂 Project Structure

```
KSL/
│── main.py              # Entry point of the web app
│── model.py             # CNN model architecture and prediction logic
│── my_model.h5          # Pre-trained model
│
├── Model/               # Saved deep learning models
│   ├── ksl_500.h5
│   ├── ksl_500.keras
│   ├── my_model.h5
│   ├── my_model.keras
│   └── new_model.h5
│
├── static/              # Static assets (images, CSS)
│   ├── *.jpg, *.png
│   └── style.css
│
├── templates/           # Frontend HTML templates
│   ├── index.html
│   ├── analyse.html
│   ├── analyze.html
│   ├── contact.html
│   └── result.html
│
└── __pycache__/         # Auto-generated Python cache files
```

---

## 🚀 Features
- 📸 Recognizes Kannada sign language gestures  
- 🧠 CNN-based deep learning model trained on gesture dataset  
- 🌐 Web interface with HTML/CSS templates  
- 📂 Supports multiple trained models (`.h5`, `.keras`)  

---

## ⚙️ Installation & Usage

1. Clone the repository and install dependencies:
   ```bash
   git clone <repo-url>
   cd KSL
   pip install -r requirements.txt
   ```

2. Run the web application:
   ```bash
   python main.py
   ```

3. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

---


## 📌 Future Scope
- Add support for real-time sign recognition via webcam  
- Expand dataset to include more gestures  
- Deploy the system online for public access  

---

