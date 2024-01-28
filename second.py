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
        "oganesson": "Og",   
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
        "og": "Oganesson",
        "water": "H2O",
        "alcohol": "C2H6O",
        "glucose": "C6H12O6",
        "methane": "CH4",
        "carbon Dioxide": "CO2",
        "oxygen": "O2",
        "nitrogen": "N2",
        "ammonia": "NH3",
        "hydrogen Peroxide": "H2O2",
        "acetic Acid": "CH3COOH",
        "methanol": "CH3OH",
        "propane": "C3H8",
        "butane": "C4H10",
        "sulfuric Acid": "H2SO4",
        "sodium Chloride": "NaCl",
        "dna": "C10H13N5O4",
        "chloroform": "CHCl3",
        "benzene": "C6H6",
        "aspirin": "C9H8O4",
        "caffeine": "C8H10N4O2",
        "methionine": "C5H11NO2S",
    } 
    elements_weight = {
        "hydrogen": 1.008,
        "helium": 4.0026,
        "lithium": 6.94,
        "beryllium": 9.0122,
        "boron": 10.81,
        "carbon": 12.011,
        "nitrogen": 14.007,
        "oxygen": 15.999,
        "fluorine": 18.998,
        "neon": 20.180,
        "sodium": 22.990,
        "magnesium": 24.305,
        "aluminum": 26.982,
        "silicon": 28.085,
        "phosphorus": 30.974,
        "sulfur": 32.06,
        "chlorine": 35.45,
        "argon": 39.948,
        "potassium": 39.098,
        "calcium": 40.078,
        "scandium": 44.956,
        "titanium": 47.867,
        "vanadium": 50.942,
        "chromium": 51.996,
        "manganese": 54.938,
        "iron": 55.845,
        "cobalt": 58.933,
        "nickel": 58.693,
        "copper": 63.546,
        "zinc": 65.38,
        "gallium": 69.723,
        "germanium": 72.630,
        "arsenic": 74.922,
        "selenium": 78.971,
        "bromine": 79.904,
        "krypton": 83.798,
        "rubidium": 85.468,
        "strontium": 87.62,
        "yttrium": 88.906,
        "zirconium": 91.224,
        "niobium": 92.906,
        "molybdenum": 95.95,
        "technetium": 98.0,
        "ruthenium": 101.07,
        "rhodium": 102.91,
        "palladium": 106.42,
        "silver": 107.87,
        "cadmium": 112.41,
        "indium": 114.82,
        "tin": 118.71,
        "antimony": 121.76,
        "tellurium": 127.60,
        "iodine": 126.90,
        "xenon": 131.29,
        "cesium": 132.91,
        "barium": 137.33,
        "lanthanum": 138.91,
        "cerium": 140.12,
        "praseodymium": 140.91,
        "neodymium": 144.24,
        "promethium": 145.0,
        "samarium": 150.36,
        "europium": 151.96,
        "gadolinium": 157.25,
        "terbium": 158.93,
        "dysprosium": 162.50,
        "holmium": 164.93,
        "erbium": 167.26,
        "thulium": 168.93,
        "ytterbium": 173.05,
        "lutetium": 174.97,
        "hafnium": 178.49,
        "tantalum": 180.95,
        "tungsten": 183.84,
        "rhenium": 186.21,
        "osmium": 190.23,
        "iridium": 192.22,
        "platinum": 195.08,
        "gold": 196.97,
        "mercury": 200.59,
        "thallium": 204.38,
        "lead": 207.2,
        "bismuth": 208.98,
        "polonium": 209.98,
        "astatine": 210.0,
        "radon": 222.0,
        "francium": 223.0,
        "radium": 226.0,
        "actinium": 227.0,
        "thorium": 232.04,
        "protactinium": 231.04,
        "uranium": 238.03,
        "neptunium": 237.0,
        "plutonium": 244.0,
        "americium": 243.0,
        "curium": 247.0,
        "berkelium": 247.0,
        "californium": 251.0,
        "einsteinium": 252.0,
        "fermium": 257.0,
        "mendelevium": 258.0,
        "nobelium": 259.0,
        "lawrencium": 262.0,
        "rutherfordium": 267.0,
        "dubnium": 270.0,
        "seaborgium": 271.0,
        "bohrium": 270.0,
        "hassium": 277.0,
        "meitnerium": 276.0,
        "darmstadtium": 281.0,
        "roentgenium": 280.0,
        "copernicium": 285.0,
        "nihonium": 284.0,
        "flerovium": 289.0,
        "moscovium": 288.0,
        "livermorium": 293.0,
        "tennessine": 294.0,
        "oganesson": 294.0,
        "water": 18.01528,
        "alcohol": 46.06844,
        "glucose": 180.1559,
        "methane": 16.04,
        "carbon dioxide": 44.0095,
        "oxygen": 31.9988,
        "nitrogen": 28.0134,
        "ammonia": 17.0305,
        "hydrogen peroxide": 34.0147,
        "acetic acid": 60.052,
        "methanol": 32.04,
        "propane": 44.0956,
        "butane": 58.1222,
        "sulfuric acid": 98.079,
        "sodium chloride": 58.443,
        "dna": 331.2172,
        "chloroform": 119.378,
        "benzene": 78.1118,
        "aspirin": 180.1574,
        "caffeine": 194.1906,
        "methionine": 149.211,
        "serotonin": 176.215,
        "adrenaline": 183.204,
        "dopamine": 153.178,
        "histamine": 111.145,
        "insulin": 5808.65,
        "melatonin": 232.278,
        "testosterone": 288.429,
        "estrogen": 272.388,
        "progesterone": 314.464,
        "h": 1.008,
        "he": 4.0026,
        "li": 6.94,
        "be": 9.0122,
        "b": 10.81,
        "c": 12.011,
        "n": 14.007,
        "o": 15.999,
        "f": 18.998,
        "ne": 20.180,
        "na": 22.990,
        "mg": 24.305,
        "al": 26.982,
        "si": 28.085,
        "p": 30.974,
        "s": 32.06,
        "cl": 35.45,
        "ar": 39.948,
        "k": 39.098,
        "ca": 40.078,
        "sc": 44.956,
        "ti": 47.867,
        "v": 50.942,
        "cr": 51.996,
        "mn": 54.938,
        "fe": 55.845,
        "co": 58.933,
        "ni": 58.693,
        "cu": 63.546,
        "zn": 65.38,
        "ga": 69.723,
        "ge": 72.630,
        "as": 74.922,
        "se": 78.971,
        "br": 79.904,
        "kr": 83.798,
        "rb": 85.468,
        "sr": 87.62,
        "y": 88.906,
        "zr": 91.224,
        "nb": 92.906,
        "mo": 95.95,
        "tc": 98.0,
        "ru": 101.07,
        "rh": 102.91,
        "pd": 106.42,
        "ag": 107.87,
        "cd": 112.41,
        "in": 114.82,
        "sn": 118.71,
        "sb": 121.76,
        "te": 127.60,
        "i": 126.90,
        "xe": 131.29,
        "cs": 132.91,
        "ba": 137.33,
        "la": 138.91,
        "ce": 140.12,
        "pr": 140.91,
        "nd": 144.24,
        "pm": 145.0,
        "sm": 150.36,
        "eu": 151.96,
        "gd": 157.25,
        "tb": 158.93,
        "dy": 162.50,
        "ho": 164.93,
        "er": 167.26,
        "tm": 168.93,
        "yb": 173.05,
        "lu": 174.97,
        "hf": 178.49,
        "ta": 180.95,
        "w": 183.84,
        "re": 186.21,
        "os": 190.23,
        "ir": 192.22,
        "pt": 195.08,
        "au": 196.97,
        "hg": 200.59,
        "tl": 204.38,
        "pb": 207.2,
        "bi": 208.98,
        "po": 209.98,
        "at": 210.0,
        "rn": 222.0,
        "fr": 223.0,
        "ra": 226.0,
        "ac": 227.0,
        "th": 232.04,
        "pa": 231.04,
        "u": 238.03,
        "np": 237.0,
        "pu": 244.0,
        "am": 243.0,
        "cm": 247.0,
        "bk": 247.0,
        "cf": 251.0,
        "es": 252.0,
        "fm": 257.0,
        "md": 258.0,
        "no": 259.0,
        "lr": 262.0,
        "rf": 267.0,
        "db": 270.0,
        "sg": 271.0,
        "bh": 270.0,
        "hs": 277.0,
        "mt": 276.0,
        "ds": 281.0,
        "rg": 280.0,
        "cn": 285.0,
        "nh": 284.0,
        "fl": 289.0,
        "mc": 288.0,
        "lv": 293.0,
        "ts": 294.0,
        "og": 294.0,
        "h2o": 18.01528,    #water
        "c2h5oh": 46.06844,  # Alcohol (Ethanol)
        "c6h12o6": 180.1559,  # Glucose
        "ch4": 16.04,  # Methane
        "co2": 44.0095,  # Carbon Dioxide
        "o2": 31.9988,  # Oxygen
        "n2": 28.0134,  # Nitrogen
        "nh3": 17.0305,  # Ammonia
        "h2o2": 34.0147,  # Hydrogen Peroxide
        "c2h4o2": 60.052,  # Acetic Acid
        "ch3oh": 32.04,  # Methanol
        "c3h8": 44.0956,  # Propane
        "c4h10": 58.1222,  # Butane
        "h2so4": 98.079,  # Sulfuric Acid
        "nacl": 58.443,  # Sodium Chloride (Salt)
        "dna": 331.2172,  #dna
        "chcl3": 119.378,  # Chloroform
        "c6h6": 78.1118,  # Benzene
        "c9h8o4": 180.1574,  # Aspirin
        "c8h10n4o2": 194.1906,  # Caffeine
        "c5h11no2s": 149.211,  # Methionine
        "c10h12n2o": 176.215,  # Serotonin
        "c9h13no3": 183.204,  # Adrenaline
        "c8h11no2": 153.178,  # Dopamine
        "c5h9n3": 111.145,  # Histamine
        "c254h377n65o75s6": 5808.65,  # Insulin
        "c13h16n2o2": 232.278,  # Melatonin
        "c19h28o2": 288.429,  # Testosterone
        "c18h24o2": 272.388,  # Estrogen
        "c21h30o2": 314.464,  # Progesterone
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
            #Molecular formula/Name
            if Q2 == "Molecular formula/Name":
                try:
                    answer = elements.get(Q1) 
                except:
                    pass
            #Weight
            if Q2 == "Weight":
                try: 
                    answer = elements_weight.get(Q1)
                except: 
                    pass
            
    #data for gsheet
    if Submit1:
        if Q1 and Q2:
            try:
                time.sleep(1)
                conn.update(worksheet="data", data=updated_df)
            except: 
                st.error("unexpected error happened")
        else: 
            st.warning("Please fill out both fields")
    #display answer
    if Submit1:
        if Q2 == "Molecular formula/Name" and Q1:
            try:
                st.write(f"_Your answer is_ {answer}")
            except:
                pass
        if Q2 == "Weight" and Q1: 
            try:
                st.write(f"_Your answer is_ {answer}")
            except:
                pass
    
 #                       
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

    
