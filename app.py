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
    
    questions = [
        {"question": "¿Qué distingue a la IA generativa de la IA tradicional?",
         "options": ["Clasifica y predice patrones existentes.", "Genera contenido nuevo a partir de datos de entrenamiento.", "No utiliza datos de entrenamiento.", "Es lo mismo que la IA tradicional."],
         "answer": 1},
        {"question": "Menciona al menos dos aplicaciones comunes de la IA generativa.",
         "options": ["Clasificación de correos y predicción de ventas.", "Creación de contenido publicitario y generación de imágenes.", "Procesamiento de bases de datos y cálculo financiero.", "Envío de correos electrónicos masivos y generación de contraseñas."],
         "answer": 1},
        {"question": "¿Cuál es el rol de los 'datos de entrenamiento' en el desarrollo de modelos de IA generativa?",
         "options": ["No son necesarios para que la IA funcione.", "Son esenciales para que la IA aprenda a generar contenido relevante.", "Sirven solo para almacenar información sin afectar la generación.", "Solo se utilizan para entrenamiento inicial y luego se descartan."],
         "answer": 1},
        {"question": "¿Qué es un modelo de lenguaje grande (LLM) y por qué son importantes en IA generativa?",
         "options": ["Son modelos que permiten clasificar imágenes.", "Son modelos entrenados con grandes volúmenes de texto para generar lenguaje natural.", "Son modelos diseñados exclusivamente para cálculos matemáticos.", "Son modelos que no requieren entrenamiento previo."],
         "answer": 1}
    ]
    
    score = 0
    
    for idx, q in enumerate(questions):
        st.subheader(f"Pregunta {idx + 1}: {q['question']}")
        user_answer = st.radio("Selecciona tu respuesta:", q['options'], index=None, key=idx)
        if user_answer is not None:
            if q['options'].index(user_answer) == q['answer']:
                st.success("✅ ¡Correcto!")
                score += 1
            else:
                st.error(f"❌ Incorrecto. La respuesta correcta es: {q['options'][q['answer']]}")

    if st.button("Finalizar Examen"):
        st.write(f"### Tu puntaje final es: {score}/{len(questions)}")
        if user_name:
            save_response(user_name, score, len(questions))
            st.success("✅ Tus respuestas han sido guardadas.")
        else:
            st.warning("⚠️ Debes ingresar tu nombre antes de enviar el examen.")
    
    # Mostrar respuestas guardadas si 

