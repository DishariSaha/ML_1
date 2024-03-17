import streamlit as st
import pickle
with open('model.pkl','rb') as file:
    model = pickle.load(file)

st.title('Machine Learning on IRIS dataset')
sl = st.number_input('Enter your Sepal length(cm): ')
sw = st.number_input('Enter your Sepal width(cm): ')
pl = st.number_input('Enter your Petal length(cm): ')
pw = st.number_input('Enter your Petal width(cm): ')

prediction = model.predict([[sl,sw,pl,pw]])

st.write(f'Your predicted class is {prediction}')
