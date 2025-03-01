import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the trained model
with open('model/svc.pkl', 'rb') as file:  # Open file in read-binary mode
    svc = pickle.load(file)  # Load the model

# Load datasets
symptoms_df = pd.read_csv('data/Training.csv', encoding='utf-8', low_memory=False)
description_df = pd.read_csv('data/description.csv', encoding='utf-8')
precautions_df = pd.read_csv('data/precautions_df.csv', encoding='utf-8')
medications_df = pd.read_csv('data/medications.csv', encoding='utf-8')
diets_df = pd.read_csv('data/diets.csv', encoding='utf-8')
workout_df = pd.read_csv('data/workout_df.csv', encoding='utf-8')

# Prepare symptom dictionary
symptoms_dict = {symptom: idx for idx, symptom in enumerate(symptoms_df.drop('prognosis', axis=1).columns)}

# Encode disease labels

le = LabelEncoder()
y = le.fit_transform(symptoms_df['prognosis'])
diseases_list = {idx: disease for idx, disease in enumerate(le.classes_)}

def get_recommendations(disease):
    description = description_df[description_df['Disease'] == disease]['Description'].values
    precautions = precautions_df[precautions_df['Disease'] == disease].iloc[:, 1:].values.flatten()
    medications = medications_df[medications_df['Disease'] == disease]['Medication'].values
    diet = diets_df[diets_df['Disease'] == disease]['Diet'].values
    workout = workout_df[workout_df['disease'] == disease]['workout'].values
    
    return {
        "Description": description[0] if len(description) > 0 else "No description available",
        "Precautions": precautions.tolist() if len(precautions) > 0 else ["No precautions available"],
        "Medications": medications.tolist() if len(medications) > 0 else ["No medication available"],
        "Diet": diet.tolist() if len(diet) > 0 else ["No diet plan available"],
        "Workout": workout.tolist() if len(workout) > 0 else ["No workout plan available"]
    }

def predict_disease(symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    
    for symptom in symptoms:
        if symptom in symptoms_dict:
            input_vector[symptoms_dict[symptom]] = 1
    
    predicted_index = svc.predict([input_vector])[0]
    return diseases_list.get(predicted_index, "Unknown disease")

# Streamlit UI
st.set_page_config(page_title="Disease Prediction System", page_icon="🩺", layout="wide")
# Header Section
st.markdown("""
    <h1 style='text-align: center; color: #2E8B57;'>🩺 Disease Prediction System</h1>
    <p style='text-align: center; font-size:18px;'>Enter your symptoms to receive disease predictions and health recommendations.</p>
    """, unsafe_allow_html=True)

# Custom CSS
st.markdown(
    """
    <style>
    /* Change Navbar background color */
        header[data-testid="stHeader"] {
            background-color: #d1dbe4 !important; /* Dark Blue */
            height: 50px;
            padding: 10px;
        }

        /* Change navbar text color */
        header[data-testid="stHeader"] * {
            color: white !important;
        }
        .stApp {background-color: #d1dbe4; color: black; padding: 20px; border-radius: 10px;}
        .stButton>button {
            background-color: #00b4d8;
            color: white;
            font-size: 18px;
            padding: 12px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: 0.3s;
        }
        .title-text {
                font-size: 40px;
                font-weight: bold;
            }
        .subtitle-text {
                font-size: 20px;
                margin-bottom: 20px;
            }
        .stButton>button:hover {
            background-color: #00ffff ;
            color: black;
        }
        .header {text-align: center; font-size: 28px; font-weight: bold; color: #333;}
    </style>
    """,
    unsafe_allow_html=True,
)

# User input
selected_symptoms = st.multiselect("Select symptoms", list(symptoms_dict.keys()))

if st.button("Predict Disease"):
    if not selected_symptoms:
        st.warning("⚠️ Please select at least one symptom.")
    else:
        predicted_disease = predict_disease(selected_symptoms)        
        recommendations = get_recommendations(predicted_disease)
        
        # Display results
        st.markdown(f"""
            <div style='background-color: #d1dbe4; padding: 20px; border-radius: 10px;'>
                <h2 style='color: black;'>Predicted Disease: {predicted_disease}</h2>
                <p style='font-size:16px;'>{recommendations["Description"]}</p>
            </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🛡️ Precautions")
            for pre in recommendations["Precautions"]:
                st.markdown(f"✅ {pre}")

            st.markdown("### 💊 Medications")
            med_list = "\n".join([f"- {med}" for med in recommendations["Medications"]])
            st.markdown(f"""
            <div style='background-color: #ffebcc; padding: 20px; border-radius: 10px;'>
                <p style='font-size:16px;'>{med_list}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 🥗 Diet Plan")
            diet_list = "\n".join([f"- {diet}" for diet in recommendations["Diet"]])
            st.markdown(f"""
            <div style='background-color: #ccf5ff; padding: 20px; border-radius: 10px;'>
                <p style='font-size:16px;'>{diet_list}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("### 🏋️ Workout Plan")
            for workout in recommendations["Workout"]:
                st.markdown(f"🔵 {workout}")

        st.success("✅ Follow these recommendations for a speedy recovery!")
        
#Footer
st.markdown("---")
st.markdown("""<p style= 'text-align: center;' >🚀 Powered by <b>Streamlit</b> and <b>Google Gemini AI</b> | Developed by <a href="https://www.linkedin.com/in/himanshunagapure"  target="_blank" style='text-decoration: none; color: light blue'><b>Himanshu Nagapure</b></a></p>""", unsafe_allow_html=True)