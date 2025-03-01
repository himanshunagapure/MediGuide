# 🏥 MediGuide - Personalized Healthcare Assistant

MediGuide is an **Personalized healthcare assistant** that predicts possible diseases based on symptoms and provides personalized **medications, diet plans, workout recommendations, and precautions**. It uses **Machine Learning** to offer data-backed health suggestions.

Try :
---

## 🚀 Features

✅ **Disease Prediction** – Get possible disease predictions based on symptoms.  
✅ **Medication Recommendations** – Suggested medications for diagnosed conditions.  
✅ **Diet Plan** – Food recommendations tailored to your condition.  
✅ **Workout Plan** – Exercises suitable for your health condition.  
✅ **Precautions** – Important preventive measures for the condition.  
✅ **Fast & Lightweight** – Runs smoothly in a web environment.  

---

## 🎯 Project Overview

MediGuide is built to **help individuals** by providing **data backed healthcare insights**. It can be useful for:  
- **Early disease detection** based on symptoms.  
- **Lifestyle management** with diet and workout suggestions.  
- **Quick medical insights** before consulting a professional.  

⚠️ **Disclaimer**: MediGuide is not a replacement for professional medical advice. Always consult a healthcare provider for a proper diagnosis.

---

## 🏗️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)  
- **Backend**: Python  
- **Machine Learning**: Scikit-learn, Pandas, NumPy  
- **Database**: CSV files for medical data  
- **Deployment**: Streamlit Community Cloud  

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/MediGuide.git
cd MediGuide
```

### 2️⃣ Create a virtual environment and activate it:
```bash
# For Mac/Linux
python3 -m venv venv
source venv/bin/activate  
   
# On Windows use: 
venv\Scripts\activate
```
### 3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application:
```bash
streamlit run app.py
```

---

## Project Structure
```bash
MediGuide/
│── data/                  # Medical datasets
│   ├── description.csv
│   ├── diets.csv
│   ├── medications.csv
│   ├── precautions_df.csv
│   ├── Symptom-severity.csv
│   ├── symptoms_df.csv
│   ├── Training.csv
│   ├── workout_df.csv
│
│── model/                 # Trained ML model
│   ├── svc.pkl
│
│── notebook/              # Jupyter Notebook (ML training & analysis)
│   ├── MediGuide.ipynb
│
|── images/                # Images of website
│── venv/                  # Virtual environment (not included in repo)
│── app.py                 # Main Streamlit application
│── requirements.txt       # Required dependencies
│── README.md              # Documentation
```
---

## Screenshots

![Dashboard Image 1](https://github.com/himanshunagapure/MediGuide/blob/main/images/mediguide1.png)

![Dashboard Image 2](https://github.com/himanshunagapure/MediGuide/blob/main/images/mediguide2.png)
---

## 🤝 Contributing
We welcome contributions! If you'd like to help improve MediGuide:

Fork the repository.
Create a feature branch (git checkout -b feature-name).
Commit your changes (git commit -m "Added new feature").
Push to your fork (git push origin feature-name).
Open a Pull Request for review.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

For any queries or feedback, reach out to:
- **Developer:** [Himanshu Nagapure](https://www.linkedin.com/in/himanshunagapure)
- **Email:** himunagapure114@gmail.com

---
🚀Developed by **Himanshu Nagapure**