import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

table=pd.DataFrame({"column 1":[1,2,3,4,5,6,],"column 2":[11,12,13,14,15,16]})

x=np.linspace(0,10,100)
bar_x=np.array([1,2,3,4,5])

#json 

json = {"a":"1,2,3","b":"4,5,6"}
st.json(json)


#code

code= """
print("hello world")
def funct():
    return 0;
"""
st.code(code,language="python")


#metric

st.metric(label="wind speed",value="120ms")


#table,dataframe

st.table(table)
st.dataframe(table)


#checkbox

def change():
    print("changed")
    
st.checkbox("checkbox", value=True,on_change=change)


#radio button

radio_btn=st.radio("In wich country do you live?", options=("us","uk","canada"))
print(radio_btn)


#button 

def btn_click():
    print("button clicked")

btn=st.button("Click me",on_click=btn_click)
print(btn)


#selctbox

select=st.selectbox("what is your favourite color?",options=("red","blue","yellow"))
print(select)


#multi-selectbox

multi=st.multiselect("what is you favourite charactor",options=("r","s","t","u","v"))
print(multi)


#horizontol line

st.markdown("---")


#uploading files

image=st.file_uploader("please upload image",type=["png","jpg","jpeg"])
if image is not None:
    st.image(image)

pdf=st.file_uploader("please upload your document",type="pdf",accept_multiple_files=True)


#slider

sal=st.slider("this is the basic slider")
print(sal)
val=st.slider("this is the slider",min_value=-10,max_value=90,value=40)
print(val)


#text input

text=st.text_input("enter your question",max_chars=100)
print(text)


#text area

te=st.text_area("course description")
print(te)


#time and date input

tes=st.date_input("please select relevent date")
print(tes)

ses=st.time_input("set the time")
print(ses)


#progress bar


#form

st.markdown("<h1>User Registration Form</h1>",unsafe_allow_html=True)
with st.form("Form 2",clear_on_submit=True):
    col1,col2=st.columns(2)
    f_name=col1.text_input("fist name")
    l_name=col2.text_input("last name")
    st.text_input("email")
    col1,col2=st.columns(2)
    col1.text_input("password")
    col2.text_input("confirm password")
    
    day,month,year=st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    s_state=st.form_submit_button("Submit")
    if s_state:
        if f_name=="" and l_name=="":
            st.warning("please fill above fields")
        else:
            st.success("submitted successfuly")



#sidebar

opt=st.sidebar.radio("selct any gragh",options=("Line","bar","H-bar"))
if opt== "Line":
    st.markdown("<h1 style='text-align:center;'>Line chart</h1>")
    fig=plt.figure()
    plt.style.use(" ")
    
    plt.plot(x,np.sin(x))
    plt.plot(x,np.cos(x),'--')
    st.write(fig)

elif opt=="Bar":
    st.markdown("<h1 style='text-align:center;'>Line chart</h1>")
    fig=plt.figure()
    plt.style.use(" ")
    plt.bar(x,x*10)
    st.write(fig)

else:
    st.markdown("<h1 style='text-align:center;'>H bar chart</h1>")
    fig=plt.figure()
    plt.style.use(" ")
    plt.barh(bar_x*10,bar_x)
    st.write(fig)

