# INFOZATECH – AI Internship

## Task 1: Rule-Based AI Chatbot

This project is a simple rule-based chatbot developed using Python. It responds to user messages using keyword matching and predefined responses.

### Features
- Responds to greetings such as hi, hello, and hey.
- Answers questions about its name.
- Responds to “How are you?”
- Provides a fallback response for unrecognized messages.
- Includes a graphical user interface (GUI) built with Tkinter.
- Supports sending messages using the Send button or Enter key.

### Technologies Used
- Python
- Tkinter
- Git and GitHub

### Project Structure
```text
INFOZATECH/
└── Task-1-Chatbot/
    ├── chatbot.py
    └── chatbot_gui.py
```

### How to Run

**Terminal chatbot**
```bash
python Task-1-Chatbot/chatbot.py
```

**GUI chatbot**
```bash
python Task-1-Chatbot/chatbot_gui.py
```

### Internship
Artificial Intelligence Virtual Internship – InfozaTech

### Author
Bhargavi



## Task 2: AI Cat vs Dog Classifier

### Project Overview
An image classification application that identifies whether an uploaded image contains a cat or a dog using transfer learning with a pretrained ResNet18 model.

### Features
- Upload cat or dog images (JPG, JPEG, PNG).
- Predict the animal category automatically.
- Display prediction confidence and class probabilities.
- Simple web interface built with Streamlit.

### Technologies Used
- Python
- PyTorch
- Torchvision
- Streamlit
- Pillow
- Transfer Learning (ResNet18)

### Model Testing
- Cat image: correctly predicted as Cats with 99.76% confidence.
- Dog image: correctly predicted as Dogs with 99.67% confidence.

*Note: These confidence scores are from individual test images and do not represent overall model accuracy.*

### How to Run
1. Install the required packages:
   `pip install -r requirements.txt`
2. Run the application:
   `python -m streamlit run app.py`

### Internship
Artificial Intelligence Virtual Internship – InfozaTech

### Author
Bhargavi
