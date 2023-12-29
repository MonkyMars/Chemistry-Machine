import streamlit as st

#moleculen
Water_moleculen = "H2", "0"
Ammoniak_moleculen = "N", "H3"
Koolstofdioxide_moleculen = "C", "O2"
Alcohol_moleculen = "C2", "H6", "O"
Methaan_moleculen = "C", "H4"
Zwavelzuur_moleculen = "H2", "S", "O4"
Zwaveldioxide_moleculen = "S", "O2"
#alleengewicht
H_gewicht = 1.008
O_gewicht = 16.00
N_gewicht = 14.01
C_gewicht = 12.01
S_gewicht = 32.06
B_gewicht = 10.81
F_gewicht = 19.00
P_gewicht = 30.97
I_gewicht = 126.9
Cl_gewicht = 35.45

#samengewicht
Water_gewicht = H_gewicht*2 + O_gewicht
Ammoniak_gewicht = N_gewicht + H_gewicht*3
Koolstofdioxide_gewicht = C_gewicht + O_gewicht*2
Alcohol_gewicht = C_gewicht*2 + H_gewicht*6 +O_gewicht
Methaan_gewicht = C_gewicht + H_gewicht*4
Zwavelzuur_gewicht = H_gewicht*2 + S_gewicht + O_gewicht*4
Zwaveldioxide_gewicht = S_gewicht + O_gewicht*2

# website deel 1
st.set_page_config(page_title="Chemistry Machine", page_icon=":test_tube:")
st.markdown('# My super cool chemistry machine!')

st.write("This is a project I made myself using python and streamlit")
st.write("#")

Question1 = st.text_input("Which molecule do you want to know? **").lower()
Question2 = st.selectbox(
    'What do you want to know about this molecule or atom?',('','Weight','Molecular formula'))

if Question1 == "" and Question2 == "Weight" or "Molecular formula":
    answer = ""

#moleculen
if Question1 == "water" and Question2 == "Molecular formula":
    answer = Water_moleculen

if Question1 == "ammonia" and Question2 == "Molecular formula":
    answer = Ammoniak_moleculen

if Question1 == "carbon dioxide" and Question2 == "Molecular formula":
    answer = Koolstofdioxide_moleculen

if Question1 == "alcohol" and Question2 == "Molecular formula":
    answer = Alcohol_moleculen

if Question1 == "methane" and Question2 == "Molecular formula":
    answer = Methaan_moleculen

if Question1 == "sulphuric acid" and Question2 == "Molecular formula":
    answer = Zwavelzuur_moleculen

if Question1 == "sulphuric dioxide" and Question2 == "Molecular formula":
    answer = Zwaveldioxide_moleculen

#gewichten
if Question1 == "water" and Question2 == "Weight":
    answer = Water_gewicht

if Question1 == "ammonia" and Question2 == "Weight":
    answer = Ammoniak_gewicht

if Question1 == "carbon dioxide" and Question2 == "Weight":
    answer = Koolstofdioxide_gewicht

if Question1 == "alcohol" and Question2 == "Weight":
   answer = Alcohol_gewicht

if Question1 == "methane" and Question2 == "Weight":
    answer = Methaan_gewicht

if Question1 == "sulphuric acid" and Question2 == "Weight":
    answer = Zwavelzuur_gewicht

if Question1 == "sulphuric dioxide" and Question2 == "Weight":
   answer = Zwaveldioxide_gewicht

if Question1 == "" and Question2 == "":
    answer = ""

#website deel 2
st.write("** Required field")
st.write("#")

if Question2 == "Weight" or "Molecular formula":
    st.write("Your answer is",answer)

st.write("[My socials](Www.Instagram.Com/harrythelazycat)") 




