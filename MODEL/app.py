#import libraries
import pandas as pd
import streamlit as st
import pickle
from PIL import Image


#load the pickle file
with open("C:\\Users\\sraks\\AIML Internship\\AIML-Internship\\MODEL/prediction.pickle", 'rb') as f:
    model = pickle.load(f)

#Header
st.write("<h1 style='text-align:center; color:purple;'>Price Prediction Model</h1>",unsafe_allow_html=True)


#-------------------SIDEBAR PANEL------------------------------
st.sidebar.header("Enter your details", divider='red')

#Input Features
def cnvrt(x):
    if x == 'Yes':
        return 1
    else:
        return 0

#x='No'
#st.write(cnvrt(x))

def conversion(x):
    if x == 'Yes':
        return 1
    elif x == 'No':
        return 2
    else:
        return 0

#Testing conversion() function
#x='No'
#st.write(conversion(x))


#------------------Gender-----------------
gender = st.sidebar.radio("Gender", ["Male","Female"])

#-----------------Senior Citizen----------
age = int(st.sidebar.number_input("Age"))
if age<60.00:
    senior_citizen=0
else:
    senior_citizen=1
#st.write(senior_citizen)

#-----------------Partner-----------------
partner = st.sidebar.radio("Partner", ["Yes","No"])

#-----------------Dependents--------------
dependents = st.sidebar.radio("Dependents", ["Yes","No"])

#-----------------Tenure------------------
tenure = st.sidebar.slider("Tenure",1.0,100.0,32.28 )

#-----------------Phone Service-----------
phone_services = st.sidebar.radio('Phone Service',['Yes', 'No'])
phone_service = cnvrt(phone_services)
#st.write(phone_service)

# --------------Multiple Lines------------
multiple_lines = 0
multiple_line = 'No Phone Service'
if phone_service == 1:
    multiple_line = st.sidebar.radio('Multiple Lines', ['Yes', 'No', 'No Phone Service'])
    multiple_lines = conversion(multiple_line)
# st.write(multiple_lines)

# -----------------Internet Service-----------
internet_services = st.sidebar.selectbox("Internet Service", ["DSL", 'Fiber optic', 'No'])
if internet_services == 'DSL':
    internet_service = 1
elif internet_services == 'Fiber optic':
    internet_service = 2
else:
    internet_service = 0
# st.write(internet_service)

#------------Online Security----------------
online_security = 0
online_backup = 0
device_protection = 0
tech_support = 0
streaming_tv = 0
streaming_movies = 0



if internet_service != 0:
    # ----------Online Security------------
    online_security = st.sidebar.radio('Online Security', ['Yes', 'No', 'No Internet Service'])
    online_security = conversion(online_security)

    # ----------Online Backup------------
    online_backup = st.sidebar.radio('Online Backup', ['Yes', 'No', 'No Internet Service'])
    online_backup = conversion(online_backup)

    # ----------Device Protection------------
    device_protection = st.sidebar.radio('Device Protection', ['Yes', 'No', 'No Internet Service'])
    device_protection = conversion(device_protection)

    # ----------Technical Support------------
    tech_support = st.sidebar.radio('Technical Support', ['Yes', 'No', 'No Internet Service'])
    tech_support = conversion(tech_support)

    # ----------Streaming TV------------
    streaming_tv = st.sidebar.radio('Streaming TV', ['Yes', 'No', 'No Internet Service'])
    streaming_tv = conversion(streaming_tv)

     # ----------Streaming Movies------------
    streaming_movies = st.sidebar.radio('Streaming Movies', ['Yes', 'No', 'No Internet Service'])
    streaming_movies = conversion(streaming_movies)

#st.write(online_security)
#st.write(online_backup)
#st.write(device_protection)
#st.write(tech_support)
#st.write(streaming_tv)
#st.write(streaming_movies)


#---------------Contract---------------
contract = st.sidebar.select_slider('Contract', ['Month-to-Month', '1 Year', '2 Year'])
if contract == 'Month-to-Month':
    contract = 0
elif contract == '1 Year':
    contract = 1
else:
    contract = 2
#st.write(contract)


#---------------Paperless Billing---------------
paperless_billings = st.sidebar.radio("Paperless Billing", ['Yes','No'])
paperless_billing = cnvrt(paperless_billings)
#st.write(paperless_billing)

# ---------------Payment Method---------------
payment_methods = st.sidebar.selectbox("Payment Method",
                                          ['Electronic check', 'Mailed check', 'Bank transfer (automatic)',
                                           'Credit card (automatic)'])
if payment_methods == 'Electronic check':
    payment_method = 2
elif payment_methods == 'Mailed check':
    payment_method = 3
elif payment_methods == 'Bank transfer (automatic)':
    payment_method = 0
else:
    payment_method = 1
# st.write(payment_method)

#--------------Monthly Charges------------------
monthly_charges = float(st.sidebar.number_input("Monthly Charges"))

#--------------Churn------------------
churn = st.sidebar.toggle("Churn")
churn = int(churn)



if st.sidebar.button("SUBMIT"):
    st.sidebar.success("Submitted Successfully..!")


    #----------------------MAIN PANEL------------------------
    st.header(":blue[Entered Details]", divider='rainbow')

    # ------------------Gender-----------------
    st.write("**Gender :** ", gender)
    if gender == 'Male':
        gender = 1
    else:
        gender = 0
    # st.write(gender)

    # -----------------Senior Citizen----------
    if senior_citizen == 0:
        st.write("**Senior citizen :** No ")
    else:
        st.write("**Senior citizen :** Yes ")
    # st.write(senior_citizen)

    # -----------------Partner-----------------
    st.write("**Partner :** ", partner)
    partner = cnvrt(partner)
    # st.write(partner)


    # -----------------Dependents--------------
    st.write("**Dependents :** ", dependents)
    dependents = cnvrt(dependents)
    # st.write(dependents)


    # -----------------Tenure------------------
    st.write("**Tenure :** ", tenure)
    # st.write(tenure)

    # -----------------Phone Service-----------
    st.write("**Phone Service :** ", phone_services)
    # st.write(phone_service)


    # --------------Multiple Lines------------
    st.write("**Multiple Lines :** ", multiple_line)
    # st.write(multiple_lines)

    # -----------------Internet Service-----------
    st.write("**Internet Service :** ", internet_services)

    if internet_service != 0:
        st.subheader(":blue[*Additional Internet Services*]")
        # ----------Online Security------------
        if online_security == 1:
            st.write("_Online Security_")
        # st.write(online_security)

        # ----------Online Backup------------
        if online_backup == 1:
            st.write("_Online Backup_")
        # st.write(online_backup)

        # ----------Device Protection------------
        if device_protection == 1:
            st.write("_device_protection_")
        # st.write(device_protection)

        # ----------Technical Support------------
        if tech_support == 1:
            st.write("_tech_support_")
        # st.write(tech_support)

        # ----------Streaming TV------------
        if streaming_tv == 1:
            st.write("_streaming_tv_")
        # st.write(streaming_tv)

        # ----------Streaming Movies------------
        if streaming_movies == 1:
            st.write("_streaming_movies_")
        # st.write(streaming_movies)

    # ---------------Contract---------------
    if contract == 0:
        st.write("**Contract Period** : 1 Month")
    elif contract == 1:
        st.write("**Contract Period** : 1 year")
    else:
        st.write("**Contract Period** : 2 years")
    # st.write(contract)

    # ---------------Paperless Billing---------------
    st.write("**Paperless Billing :**", paperless_billings)

    # ---------------Payment Method---------------
    st.write("**Payment Method :** ", payment_methods)

    # --------------Monthly Charges------------------
    st.write("**Monthly Charges :** ", monthly_charges)
    # st.write(monthly_charges)

    # --------------Churn------------------
    if churn == 1:
        st.write("**Churn :**", "Yes")
    else:
        st.write("**Churn :**", "No")
    # st.write(churn)

    # Model Prediction
    predicted = model.predict([[gender, senior_citizen, partner, dependents, tenure, phone_service, multiple_lines,
                                internet_service, online_security, online_backup, device_protection, tech_support,
                                streaming_tv, streaming_movies, contract, paperless_billing, payment_method,
                                monthly_charges, churn]])

    # predicted = model.predict([[0,0,1,1,69.0,1,1,1,1,2,2,1,0,2,2,0,1,61.40,0]])
    st.write(f"<h2 style='text-align:center; color:green '>Expected Total Charges <br> {predicted}<h2>",unsafe_allow_html=True)

else:
    image = Image.open("C:\\Users\\sraks\\AIML Internship\\AIML-Internship\\MODEL\\img.png")
    st.image(image, caption="Price prediction")