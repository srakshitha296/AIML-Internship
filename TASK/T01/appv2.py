#import libraries
import pandas as pd
import streamlit as st
import pickle


#load the pickle file
with open("C:\\Users\\sraks\\AIML Internship\\AIML-Internship\\TASK/T01/prediction.pickle", 'rb') as f:
    model = pickle.load(f)

#Header
st.title("Price Prediction Model")
st.sidebar.header("Input Features", divider='red')

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
st.header(":blue[Entered Details]", divider='rainbow')
st.write("**Gender :** ",gender)
if gender == 'Male':
    gender = 1
else:
    gender = 0
#st.write(gender)

#-----------------Senior Citizen----------
age = int(st.sidebar.number_input("Age"))
if age<60.00:
    senior_citizen=0
    st.write("**Senior citizen :** No ")
else:
    st.write("**Senior citizen :** Yes ")
    senior_citizen=1
#st.write(senior_citizen)

#-----------------Partner-----------------
partner = st.sidebar.radio("Partner", ["Yes","No"])
st.write("**Partner :** ",partner)
partner = cnvrt(partner)
#st.write(partner)

#-----------------Dependents--------------
dependents = st.sidebar.radio("Dependents", ["Yes","No"])
st.write("**Dependents :** ",dependents)
dependents = cnvrt(dependents)
#st.write(dependents)

#-----------------Tenure------------------
tenure = st.sidebar.slider("Tenure",1.0,72.0,32.28 )
st.write("**Tenure :** ",tenure)
#st.write(tenure)

#-----------------Phone Service-----------
phone_service = st.sidebar.radio('Phone Service',['Yes', 'No'])
st.write("**Phone Service :** ",phone_service)
phone_service = cnvrt(phone_service)
#st.write(phone_service)
         #--------------Multiple Lines------------
multiple_lines = 0
if phone_service == 1:
    multiple_lines = st.sidebar.radio('Multiple Lines',['Yes', 'No', 'No Phone Service'])
    st.write("**Multiple Lines :** ", multiple_lines)
    multiple_lines = conversion(multiple_lines)
#st.write(multiple_lines)

#-----------------Internet Service-----------
internet_service = st.sidebar.selectbox("Internet Service",["DSL",'Fiber optic','No'])
st.write("**Internet Service :** ",internet_service)
if internet_service == 'DSL':
    internet_service = 1
elif internet_service == 'Fiber optic':
    internet_service = 2
else:
    internet_service = 0
#st.write(internet_service)

#------------Online Security----------------
online_security = 0
online_backup = 0
device_protection = 0
tech_support = 0
streaming_tv = 0
streaming_movies = 0



if internet_service != 0:
    st.subheader(":blue[*Additional Internet Services*]")
    # ----------Online Security------------
    online_security = st.sidebar.radio('Online Security', ['Yes', 'No', 'No Internet Service'])
    online_security = conversion(online_security)
    if online_security == 1:
        st.write("_Online Security_")
    #st.write(online_security)

    # ----------Online Backup------------
    online_backup = st.sidebar.radio('Online Backup', ['Yes', 'No', 'No Internet Service'])
    online_backup = conversion(online_backup)
    if online_backup == 1:
        st.write("_Online Backup_")
    #st.write(online_backup)

    # ----------Device Protection------------
    device_protection = st.sidebar.radio('Device Protection', ['Yes', 'No', 'No Internet Service'])
    device_protection = conversion(device_protection)
    if device_protection == 1:
        st.write("_device_protection_")
    #st.write(device_protection)

    # ----------Technical Support------------
    tech_support = st.sidebar.radio('Technical Support', ['Yes', 'No', 'No Internet Service'])
    tech_support = conversion(tech_support)
    if tech_support == 1:
        st.write("_tech_support_")
    #st.write(tech_support)

    # ----------Streaming TV------------
    streaming_tv = st.sidebar.radio('Streaming TV', ['Yes', 'No', 'No Internet Service'])
    streaming_tv = conversion(streaming_tv)
    if streaming_tv == 1:
        st.write("_streaming_tv_")
    #st.write(streaming_tv)

     # ----------Streaming Movies------------
    streaming_movies = st.sidebar.radio('Streaming Movies', ['Yes', 'No', 'No Internet Service'])
    streaming_movies = conversion(streaming_movies)
    if streaming_movies == 1:
        st.write("_streaming_movies_")
    #st.write(streaming_movies)

#st.write(online_security)
#st.write(online_backup)
#st.write(device_protection)
#st.write(tech_support)
#st.write(streaming_tv)
#st.write(streaming_movies)


#---------------Contract---------------
contract = st.sidebar.select_slider('Contract', ['Month-to-Month', '1 Year', '2 Year'])
if contract == 'Month-to-Month':
    st.write("**Contract Period** : 1 Month")
    contract = 0
elif contract == '1 Year':
    st.write("**Contract Period** : 1 year")
    contract = 1
else:
    st.write("**Contract Period** : 2 years")
    contract = 2
#st.write(contract)


#---------------Paperless Billing---------------
paperless_billing = st.sidebar.radio("Paperless Billing", ['Yes','No'])
st.write("**Paperless Billing :**",paperless_billing)
paperless_billing = cnvrt(paperless_billing)
#st.write(paperless_billing)

#---------------Payment Method---------------
payment_method = st.sidebar.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)',
       'Credit card (automatic)'])
st.write("**Payment Method :** ", payment_method)
if payment_method == 'Electronic check':
    payment_method = 2
elif payment_method == 'Mailed check':
    payment_method = 3
elif payment_method == 'Bank transfer (automatic)':
    payment_method = 0
else:
    payment_method = 1
#st.write(payment_method)

#--------------Monthly Charges------------------
monthly_charges = st.sidebar.slider("Monthly Charges",0.0,200.0,64.80)
st.write("**Monthly Charges :** ", monthly_charges)
#st.write(monthly_charges)

#--------------Churn------------------
churn = st.sidebar.toggle("Churn")
churn = int(churn)
if churn == 1:
    st.write("**Churn :**", "Yes")
else:
    st.write("**Churn :**", "No")
#st.write(churn)


#Model Prediction
predicted = model.predict([[gender, senior_citizen,partner, dependents, tenure, phone_service, multiple_lines, internet_service, online_security, online_backup, device_protection, tech_support, streaming_tv, streaming_movies, contract, paperless_billing, payment_method, monthly_charges, churn]])
st.write(f":green[**Total Charges :** {predicted}]")
#predicted = model.predict([[0,0,1,1,69.0,1,1,1,1,2,2,1,0,2,2,0,1,61.40,0]])
#st.write(predicted)



#st.sidebar.write("<h2 style='text-align:center; color:red'>SUBMIT</h2>",unsafe_allow_html = True)
st.success("Success")

if st.button("SUBMIT"):
    st.success("Submitted Successfully..!")