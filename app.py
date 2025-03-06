import streamlit as st
import pandas as pd
import os

# Función para guardar las respuestas en un archivo CSV
def save_response(name, score, total_questions):
    file_path = "respuestas.csv"
    new_data = pd.DataFrame([[name, score, total_questions]], columns=["Nombre", "Puntaje", "Total Preguntas"])
    
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df = pd.concat([df, new_data], ignore_index=True)
    else:
        df = new_data
    
    df.to_csv(file_path, index=False)

def main():
    st.title("Examen IA Generativa")
    
    # Pedir el nombre del usuario antes de empezar el examen
    user_name = st.text_input("Escribe tu nombre o correo antes de iniciar:")
    
    if not user_name:
        st.warning("⚠️ Debes ingresar tu nombre antes de comenzar el examen.")
        return
    
    questions = [
        {"question": "¿Qué distingue a la IA generativa de la IA tradicional?",
         "options": ["Clasifica y predice patrones existentes.", "Genera contenido nuevo a partir de datos de entrenamiento.", "No utiliza datos de entrenamiento.", "Es lo mismo que la IA tradicional."],
         "answer": 1},
        {"question": "Menciona al menos dos aplicaciones comunes de la IA generativa.",
         "options": ["Clasificación de correos y predicción de ventas.", "Creación de contenido publicitario y generación de imágenes.", "Procesamiento de bases de datos y cálculo financiero.", "Envío de correos electrónicos masivos y generación de contraseñas."],
         "answer": 1},
        {"question": "¿Cuál es el rol de los 'datos de entrenamiento' en el desarrollo de modelos de IA generativa?",
         "options
