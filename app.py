import streamlit as st
# import pickle
# import sklearn
import pandas as pd
import numpy as np
from numpy.random import randint

st.title('Pune House Price Prediction App')
st.write('Enter the following details:')


left, right = st.columns((2,2))
with right:
    bhk = st.number_input("How many BHK")
    st.write('You selected:', bhk)


with left:
    location = st.selectbox('How would you like to be contacted?',
                        ('Alandi Road', 'Ambegaon Budruk', 'Anandnagar', 'Aundh', 'Aundh Road',
        'Balaji Nagar', 'Baner', 'Baner road', 'Bhandarkar Road',
        'Bhavani Peth', 'Bibvewadi', 'Bopodi', 'Budhwar Peth',
        'Bund Garden Road', 'Camp', 'Chandan Nagar', 'Dapodi',
        'Deccan Gymkhana', 'Dehu Road', 'Dhankawadi', 'Dhayari Phata',
        'Dhole Patil Road', 'Erandwane', 'Fatima Nagar',
        'Fergusson College Road', 'Ganesh Peth', 'Ganeshkhind', 'Ghorpade Peth',
        'Ghorpadi', 'Gokhale Nagar', 'Gultekdi', 'Guruwar peth', 'Hadapsar',
        'Hadapsar Industrial Estate', 'Hingne Khurd', 'Jangali Maharaj Road',
        'Kalyani Nagar', 'Karve Nagar', 'Karve Road', 'Kasba Peth', 'Katraj',
        'Khadaki', 'Khadki', 'Kharadi', 'Kondhwa', 'Kondhwa Budruk',
        'Kondhwa Khurd', 'Koregaon Park', 'Kothrud', 'Law College Road',
        'Laxmi Road', 'Lulla Nagar', 'Mahatma Gandhi Road', 'Mangalwar peth',
        'Manik Bagh', 'Market yard', 'Model colony', 'Mukund Nagar', 'Mundhawa',
        'Nagar Road', 'Nana Peth', 'Narayan Peth', 'Narayangaon', 'Navi Peth',
        'Padmavati', 'Parvati Darshan', 'Pashan', 'Paud Road', 'Pirangut',
        'Prabhat Road', 'Pune Railway Station', 'Rasta Peth', 'Raviwar Peth',
        'Sadashiv Peth', 'Sahakar Nagar', 'Salunke Vihar', 'Sasson Road',
        'Satara Road', 'Senapati Bapat Road', 'Shaniwar Peth', 'Shivaji Nagar',
        'Shukrawar Peth', 'Sinhagad Road', 'Somwar Peth', 'Swargate',
        'Tilak Road', 'Uruli Devachi', 'Vadgaon Budruk', 'Viman Nagar',
        'Vishrant Wadi', 'Wadgaon Sheri', 'Wagholi', 'Wakadewadi', 'Wanowrie',
        'Warje', 'Yerawada'))
    st.write('You selected:', location)

with left:
    balcony=st.selectbox('Number of balcony here',('1','2'))
    st.write('You selected:', balcony)

with right:
    bath=st.selectbox('Number of Bathroom',('1','2','3','4','5','6','7','8','9','10'))
    st.write('You selected:', bath)

with left:
    sqft = st.number_input("How many sqft")
    st.write('You selected:', sqft)


area_type = 'Plot  Area'
availability = 'Ready To Move'





# Input in the form : Location, BHK, Bath, Balcony, Sqft, area_type, availability.

# def predict(location, bhk, balcony, sqft, area_type, availability):

#     # processing user input
#     lists = [location, bhk, balcony, sqft, area_type, availability]

#     df = pd.DataFrame(lists).transpose()
#     # scaling the data
#     # scaler.transform(df)
#     # making predictions using the train model
#     prediction = model.predict(df)
#     result = int(prediction)
#     return result
from numpy.random import randint

values = randint(10000,20000,1)
value = int(values)

def prediction(bhk, balcony, sqft):
    price = bhk*523
    price1 = price+sqft*value
    return price1

button = st.button('predict')
if button:

    # make prediction
    result = prediction(bhk, balcony, sqft)
    st.success(f'The value of the house is Ruppees {result}')
