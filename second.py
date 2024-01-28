import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from streamlit_modal import Modal
import time
import pandas as pd 
from streamlit_gsheets import GSheetsConnection
#
st.set_page_config(page_title="Chemistry Machine", page_icon=":test_tube:")

with (st.sidebar):
    selected = option_menu(
        menu_title=None,
        options=["Home", "Chemistry Machine", "Projects", "About me"])
#
if selected == "Chemistry Machine":
    elements = {
        "hydrogen": "H",
        "helium": "He",
        "lithium": "Li",
        "beryllium": "Be",
        "boron": "B",
        "carbon": "C",
        "nitrogen": "N",
        "oxygen": "O",
        "fluorine": "F",
        "neon": "Ne",
        "sodium": "Na",
        "magnesium": "Mg",
        "aluminum": "Al",
        "silicon": "Si",
        "phosphorus": "P",
        "sulfur": "S",
        "chlorine": "Cl",
        "argon": "Ar",
        "potassium": "K",
        "calcium": "Ca",
        "scandium": "Sc",
        "titanium": "Ti",
        "vanadium": "V",
        "chromium": "Cr",
        "manganese": "Mn",
        "iron": "Fe",
        "cobalt": "Co",
        "nickel": "Ni",
        "copper": "Cu",
        "zinc": "Zn",
        "gallium": "Ga",
        "germanium": "Ge",
        "arsenic": "As",
        "selenium": "Se",
        "bromine": "Br",
        "krypton": "Kr",
        "rubidium": "Rb",
        "strontium": "Sr",
        "yttrium": "Y",
        "zirconium": "Zr",
        "niobium": "Nb",
        "molybdenum": "Mo",
        "technetium": "Tc",
        "ruthenium": "Ru",
        "rhodium": "Rh",
        "palladium": "Pd",
        "silver": "Ag",
        "cadmium": "Cd",
        "indium": "In",
        "tin": "Sn",
        "antimony": "Sb",
        "tellurium": "Te",
        "iodine": "I",
        "xenon": "Xe",
        "cesium": "Cs",
        "barium": "Ba",
        "lanthanum": "La",
        "cerium": "Ce",
        "praseodymium": "Pr",
        "neodymium": "Nd",
        "promethium": "Pm",
        "samarium": "Sm",
        "europium": "Eu",
        "gadolinium": "Gd",
        "terbium": "Tb",
        "dysprosium": "Dy",
        "holmium": "Ho",
        "erbium": "Er",
        "thulium": "Tm",
        "ytterbium": "Yb",
        "lutetium": "Lu",
        "hafnium": "Hf",
        "tantalum": "Ta",
        "tungsten": "W",
        "rhenium": "Re",
        "osmium": "Os",
        "iridium": "Ir",
        "platinum": "Pt",
        "gold": "Au",
        "mercury": "Hg",
        "thallium": "Tl",
        "lead": "Pb",
        "bismuth": "Bi",
        "polonium": "Po",
        "astatine": "At",
        "radon": "Rn",
        "francium": "Fr",
        "radium": "Ra",
        "actinium": "Ac",
        "thorium": "Th",
        "protactinium": "Pa",
        "uranium": "U",
        "neptunium": "Np",
        "plutonium": "Pu",
        "americium": "Am",
        "curium": "Cm",
        "berkelium": "Bk",
        "californium": "Cf",
        "einsteinium": "Es",
        "fermium": "Fm",
        "mendelevium": "Md",
        "nobelium": "No",
        "lawrencium": "Lr",
        "rutherfordium": "Rf",
        "dubnium": "Db",
        "seaborgium": "Sg",
        "bohrium": "Bh",
        "hassium": "Hs",
        "meitnerium": "Mt",
        "darmstadtium": "Ds",
        "roentgenium": "Rg",
        "copernicium": "Cn",
        "nihonium": "Nh",
        "flerovium": "Fl", 
        "moscovium": "Mc",   
        "livermorium": "Lv", 
        "tennessine": "Ts",  
        "oganesson": "Og"   
    }
    elements2 = {
        "h": "Hydrogen",
        "he": "Helium",
        "li": "Lithium",
        "be": "Beryllium",
        "b": "Boron",
        "c": "Carbon",
        "n": "Nitrogen",
        "o": "Oxygen",
        "f": "Fluorine",
        "ne": "Neon",
        "na": "Sodium",
        "mg": "Magnesium",
        "al": "Aluminum",
        "si": "Silicon",
        "p": "Phosphorus",
        "s": "Sulfur",
        "cl": "Chlorine",
        "ar": "Argon",
        "k": "Potassium",
        "ca": "Calcium",
        "sc": "Scandium",
        "ti": "Titanium",
        "v": "Vanadium",
        "cr": "Chromium",
        "mn": "Manganese",
        "fe": "Iron",
        "co": "Cobalt",
        "ni": "Nickel",
        "cu": "Copper",
        "zn": "Zinc",
        "ga": "Gallium",
        "ge": "Germanium",
        "as": "Arsenic",
        "se": "Selenium",
        "br": "Bromine",
        "kr": "Krypton",
        "rb": "Rubidium",
        "sr": "Strontium",
        "y": "Yttrium",
        "zr": "Zirconium",
        "nb": "Niobium",
        "mo": "Molybdenum",
        "tc": "Technetium",
        "ru": "Ruthenium",
        "rh": "Rhodium",
        "pd": "Palladium",
        "ag": "Silver",
        "cd": "Cadmium",
        "in": "Indium",
        "sn": "Tin",
        "sb": "Antimony",
        "te": "Tellurium",
        "i": "Iodine",
        "xe": "Xenon",
        "cs": "Cesium",
        "ba": "Barium",
        "la": "Lanthanum",
        "ce": "Cerium",
        "pr": "Praseodymium",
        "nd": "Neodymium",
        "pm": "Promethium",
        "sm": "Samarium",
        "eu": "Europium",
        "gd": "Gadolinium",
        "tb": "Terbium",
        "dy": "Dysprosium",
        "ho": "Holmium",
        "er": "Erbium",
        "tm": "Thulium",
        "yb": "Ytterbium",
        "lu": "Lutetium",
        "hf": "Hafnium",
        "ta": "Tantalum",
        "w": "Tungsten",
        "re": "Rhenium",
        "os": "Osmium",
        "ir": "Iridium",
        "pt": "Platinum",
        "au": "Gold",
        "hg": "Mercury",
        "tl": "Thallium",
        "pb": "Lead",
        "bi": "Bismuth",
        "po": "Polonium",
        "at": "Astatine",
        "rn": "Radon",
        "fr": "Francium",
        "ra": "Radium",
        "ac": "Actinium",
        "th": "Thorium",
        "pa": "Protactinium",
        "u": "Uranium",
        "np": "Neptunium",
        "pu": "Plutonium",
        "am": "Americium",
        "cm": "Curium",
        "bk": "Berkelium",
        "cf": "Californium",
        "es": "Einsteinium",
        "fm": "Fermium",
        "md": "Mendelevium",
        "no": "Nobelium",
        "lr": "Lawrencium",
        "rf": "Rutherfordium",
        "db": "Dubnium",
        "sg": "Seaborgium",
        "bh": "Bohrium",
        "hs": "Hassium",
        "mt": "Meitnerium",
        "ds": "Darmstadtium",
        "rg": "Roentgenium",
        "cn": "Copernicium",
        "nh": "Nihonium",
        "fl": "Flerovium",
        "mc": "Moscovium",
        "lv": "Livermorium",
        "ts": "Tennessine",
        "og": "Oganesson"
    }  
    #samengewicht
    H_gewicht = 1.008
    O_gewicht = 16.00
    N_gewicht = 14.01 
    C_gewicht = 12.01
    S_gewicht = 32.06
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
    Q1 = st.text_input("Which molecule do you want to know? **").lower()
    Q2 = st.selectbox('What do you want to know about this molecule or atom? **',
                             ('', 'Weight', 'Molecular formula/Name'))    

# website deel 2
if selected == "Chemistry Machine":
    conn = st.connection("gsheets", type=GSheetsConnection) 
    existing_data = conn.read(worksheet="data", usecols=list(range(4)), ttl=5)
    existing_data = existing_data.dropna(how="all")
    st.write("** Required field")
    Submit1 = st.button("submit")
    data_Q = pd.DataFrame(
        [
            { 
                 "Q1": Q1,
                 "Q2": Q2
            }
        ]
    )
    updated_df = pd.concat([existing_data, data_Q])
    if Submit1:
        if Q1 and Q2:
            if Q2 == "Molecular formula/Name" and Q1:
                try:
                    answer = elements.get(Q1)
                    answer = elements2.get(Q1)
                except:
                    st.error("")
                try:
                    time.sleep(2)
                    conn.update(worksheet="data", data=updated_df)
                except: 
                    st.error("unexpected error happened")
                    st.stop()
        else: 
            st.warning("Please fill out both fields")
            if Q1 and Q2 == "Weight"":
                st.write(f"_Your answer is_ {answer} u")
            
                    
                
               
if selected == "Home":
    conn = st.connection("gsheets", type=GSheetsConnection) 
    existing_data = conn.read(worksheet="data", usecols=list(range(4)), ttl=5)
    existing_data = existing_data.dropna(how="all")
    st.title("Home")
    st.subheader("Welcome, to my wonderful website, I hope you enjoy!")
    st.write("#")
    st.write("This is where I store all my projects, I make these project outside of school as a hobby. I'm excited to learn more as I go on with making stuff! Maybe even learn other programming languages.")
    st.write("All the projects I've made so far are made fully in python")
    st.write("#")
    st.write("---")
    st.write("#")
    st.write("#")
    st.subheader("Feedback")
    Name = st.text_input("Enter your name").capitalize()
    if Name == "Francis":
        st.balloons()
    Feedback = st.text_input("Enter your feedback")
    data_F = pd.DataFrame(
        [
             { 
                  "Name": Name,
                    "Feedback": Feedback
              }
          ]
      )
    updated_df = pd.concat([existing_data, data_F])
    Submit0 = st.button("Submit feedback") 
    if Submit0: 
         if Name and Feedback:
             try:
                 time.sleep(2)
                 conn.update(worksheet="data", data=updated_df)
                 st.success("Feedback submitted succesfully!")
             except: 
                st.error("Something went wrong, please try again later")
         else: 
             st.warning("Please fill out both fields")
        
    
if selected == "About me":
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.title("About me")
            st.write("Hello, I am a 14 year old, python learning student."" "
             "This is the first python project I've ever made.")
            st.write("I'm a big fan of computers and their hardware, I am a proud owner of a beautiful system myself.")
            st.write("I built this computer myself in august of 2023, I would 100% do it again, either for myself or someone else. If it wasn't for this pc I wouldn't have had the chance to learn python. Personally I would fully recommend building your own pc instead of buying a prebuild or a console.")
        with right_column:
            st.write("#")
            st.write("My pc:")
            def load_model(model_name):
                model = st.image(model_name)
                return (model)
            model = load_model("Pc_1.png")
            st.write("specs [here](https://nl.pcpartpicker.com/list/4RYJN6)")
           
        
if selected == "Projects":
    st.title("My projects")
    st.write("Welcome to my Projects!"" "
              "I've only made two projects as of January first 2024."" "
              "But I have a lot more planned for in the future.")
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

    
