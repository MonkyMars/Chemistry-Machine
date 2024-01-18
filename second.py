import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Chemistry Machine", page_icon=":test_tube:")

with (st.sidebar):
    selected = option_menu(
        menu_title=None,
        options=["Home", "Chemistry Machine", "Projects", "About me"])
#
#
if selected == "Chemistry Machine":
    Water_moleculen = "H2", "0"
    Ammoniak_moleculen = "N", "H3"
    Koolstofdioxide_moleculen = "C", "O2"
    Alcohol_moleculen = "C2", "H6", "O"
    Methaan_moleculen = "C", "H4"
    Zwavelzuur_moleculen = "H2", "S", "O4"
    Zwaveldioxide_moleculen = "S", "O2"
    Zuurstof_moleculen = "O",
    Waterstof_moleculen = "H",
    Stikstof_moleculen = "N",
    Koolstof_moleculen = "C",
    Zwavel_moleculen = "S",
    Boor_moleculen = "B",
    Fluor_moleculen = "F",
    Fosfor_moleculen = "P",
    Jood_moleculen = "I",
    Chloor_moleculen = "Cl",
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
    Water_gewicht = H_gewicht * 2 + O_gewicht
    Ammoniak_gewicht = N_gewicht + H_gewicht * 3
    Koolstofdioxide_gewicht = C_gewicht + O_gewicht * 2
    Alcohol_gewicht = C_gewicht * 2 + H_gewicht * 6 + O_gewicht
    Methaan_gewicht = C_gewicht + H_gewicht * 4
    Zwavelzuur_gewicht = H_gewicht * 2 + S_gewicht + O_gewicht * 4
    Zwaveldioxide_gewicht = S_gewicht + O_gewicht * 2

# website deel 1

if selected == "Chemistry Machine":
    st.markdown('# My super cool chemistry machine!')
    st.write("This is a project I made myself using python and streamlit")
    st.write("#")
    Question1 = st.text_input("Which molecule do you want to know? **").lower()
    Question2 = st.selectbox('What do you want to know about this molecule or atom? **',
                             ('', 'Weight', 'Molecular formula'))

if selected == "Chemistry Machine": 
    if Question1 == "secret_login":
        st.success("succesfully logged in")
        st.write("Welcome dev")
    if Question1 == "" and Question2 == "":
        answer = ""
    if Question1 == "" and Question2 == "Weight" or "Molecular formula": 
        answer = ""

        
# moleculen
if selected == "Chemistry Machine":
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
    if Question1 == "sulfuric acid" and Question2 == "Molecular formula":
        answer = Zwavelzuur_moleculen
    if Question1 == "sulfuric dioxide" and Question2 == "Molecular formula":
        answer = Zwaveldioxide_moleculen
    if Question1 == "oxygen" and Question2 == "Molecular formula":
        answer = Zuurstof_moleculen
    if Question1 == "nitrogen" and Question2 == "Molecular formula":
        answer = Stikstof_moleculen
    if Question1 == "carbon" and Question2 == "Molecular formula":
        answer = Koolstof_moleculen
    if Question1 == "sulfur" and Question2 == "Molecular formula":
        answer = Zwavel_moleculen
    if Question1 == "boron" and Question2 == "Molecular formula":
        answer = Boor_moleculen
    if Question1 == "phosphorus" and Question2 == "Molecular formula":
        answer = Fosfor_moleculen
    if Question1 == "iodine" and Question2 == "Molecular formula":
        answer = Jood_moleculen
    if Question1 == "chlorine" and Question2 == "Molecular formula":
        answer = Chloor_moleculen

    


#gewichten
if selected == "Chemistry Machine":
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
    if Question1 == "oxygen" and Question2 == "Weight":
        answer = O_gewicht
    if Question1 == "hydrogen" and Question2 == "Weight":
        answer = H_gewicht

# website deel 2

if selected == "Chemistry Machine":
    st.write("** Required field")
    st.write("#")
    if Question2 == "Weight" or "Molecular formula":
        st.write("_Your answer is_", answer)
    st.write("---")
    st.write("##")
    st.subheader("Feedback")
    Feedback = st.text_input("What's your feedback?")
    if Feedback:
        st.success("Thank you for your feedback!")     

if selected == "Home":
    with st.container():
         def Name():
           name = st.text_input("What's your name?")
           while len(name) == 0:
               name = " "
           st.session_state['name'] = name
   
    if 'name' not in st.session_state:
        name = "NAN"
    else:
        name = st.session_state['name']
    st.title("Home")
    st.subheader("Welcome", name) st.subheader(" to my wonderful website, I hope you enjoy!")
    st.write("#")
    st.write("This is where I store all my projects, I make these project outside of school as a hobby. I'm excited to learn more as I go on with making stuff! Maybe even learn other programming languages.")
    st.write("All the projects I've made so far are made fully in python")
    st.write("#")
    Name()
             
       
if selected == "About me":
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.title("About me")
            st.write("Hello, I am a 14 year old, python learning student."" "
             "This is the first python project I've ever made.")
            st.write("I'm a big fan of computers and their hardware, I am a proud owner of a beautiful system myself")
        with right_column:
            st.write("#")
            st.write("My pc:")
            st.image("Pc_1.png")
            st.write("specs [here](https://nl.pcpartpicker.com/list/4RYJN6)")
        
if selected == "Projects":
    st.title("My projects")
    st.write("Welcome to my Projects!"" "
              "I've only made two projects as of January first 2024."" "
              "But I have a lot more planned for in the future")
    st.write("---")
    st.write("#")
    st.subheader("Chemistry Machine")
    st.write("This is a project I made to discover and learn Python, Thus the entire project is written in python.")
    st.write("Check my Chemistry Machine [here](https://chemistry-machine.streamlit.app/#my-super-cool-chemistry-machine)")
    st.write("#")
    st.subheader("This website")
    st.write("I made this website originally to make my Chemistry Machine more portable and accessible,"
             " but after a while it seemed like Im gonna use it for all my projects")
    st.write("#")
    st.subheader("Future")
    st.write("My plans for the future are")
    st.write("* make a Dutch version of this site and my projects")
    st.write("* create more projects which can either help people or to learn to understand python better")



