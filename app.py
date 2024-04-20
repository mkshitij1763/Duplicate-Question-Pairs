import streamlit as st
import helper
import pickle
import nltk
from nltk.corpus import stopwords

model = pickle.load(open('model.pkl','rb'))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')



# Download the stopwords for English (or any other language you need)
nltk.download('stopwords')

# Get the stopwords list
stop_words = stopwords.words('english')

# Save the stopwords list to a pickle file
with open('stopwords.pkl', 'wb') as f:
  pickle.dump(stop_words, f)

print("Stopwords saved to stopwords.pkl")


if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')


