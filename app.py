
import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = load_model('emotion_model.keras') 
def predict_emotion(tweet):
    padded_seq = pad_sequences(get_sequences(tokenizer, [tweet]), maxlen=50)
    prediction = model.predict(padded_seq)
    emotion_class = tf.argmax(prediction, axis=1).numpy()[0]
    return emotion_class
def main():
    st.title("Emotion Prediction App")
    user_input = st.text_area("Enter your tweet:", "")
    if st.button("Predict Emotion"):
        if user_input:
            emotion_class = predict_emotion(user_input)
            st.success(f"The predicted emotion class is: {emotion_class}")

if __name__ == "__main__":
    main()





