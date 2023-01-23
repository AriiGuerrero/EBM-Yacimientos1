import numpy as np
import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import plotly_express as px
from scipy import stats
from streamlit_option_menu import option_menu
from PIL import Image
from collections import namedtuple
from Funciones import data,Bo,Rs,grafica

# Insert an icon
icon = Image.open("Resources/inflow.png")

# State the design of the app
st.set_page_config(page_title="Oil Reservoir", page_icon=icon)

# Insert css codes to improve the design of the app
st.markdown(
    """
<style>
h1 {text-align: center;
}
body {background-color: #DCE3D5;
      width: 1400px;
      margin: 15px auto;
}
</style>""",
    unsafe_allow_html=True,
)

# Title of the app
st.title(" RESERVOIR ENGINEERING :link:")

st.write("---")

st.markdown(
    """ This app is used to visualize the results of oil reservoir by material balance equation and to upload csv files, 
to call data, and to realize basic calculations..

*Python Libraries:* Streamlit, pandas, plotly, PIL.
"""
)

# Add additional information
expander = st.expander("About")
expander.write("This app was created by Ariana Guerrero, student of Petroleum Engineering in ESPOL")

# Insert image
st.subheader("*MATERIAL BALANCE EQUATION*")
image = Image.open("Resources/ebm.PNG")
st.image(image, width=100, use_column_width=True)

# Insert video
st.subheader("*Deduction of Material Balance Equation*")
video = open("Resources/deduccion_ec.mp4", "rb")
st.video(video)

# Sidebar
Logo = Image.open("Resources/logo.jpg")
st.sidebar.image(Logo)

# Add title to the sidebar section
st.sidebar.title(":arrow_down: *Navigation*")

upload_file = st.sidebar.file_uploader("Upload your csv file")
# Pages
with st.sidebar:
    options = option_menu(
        menu_title="Menu",
        options=["Information", "Data","Reservoir Potential"],
        icons=["pencil-square","tv-fill", "server"],)

if upload_file:
    lData=pd.read_csv(upload_file)

# Call web app sections
if options=="Data":
    data(lData)

elif options == "Reservoir Potential":
    st.subheader("*Choose the option you require::*")
    if st.checkbox("Yacimiento Subsaturado sin correlaciones"):
        st.subheader("*Enter input values*")
        Pi = st.number_input("Enter Pi value: ")
        Bw = st.number_input("Enter Bw value: ")
        Cf = st.number_input("Enter Cf value: ")
        Cw = st.number_input("Enter Cw value: ")
        Sw = st.number_input("Enter Sw value")
        p = lData['P (psi)'].values
        Bo = lData['Bo (bbl/STB)'].values
        Np = lData['Np (STB)'].values
        Wp = lData['Wp'].values
        eai = lData['Bo (bbl/STB)'][0] * ((Cf + (Sw * Cw)) / (1 - Sw))
        lData['F'] = lData['Np (STB)'] * ((lData['Bo (bbl/STB)']))
        lData['Eo'] = lData['Bo (bbl/STB)'] - lData['Bo (bbl/STB)'][0]
        lData['DP'] = lData['P (psi)'][0] - lData['P (psi)']
        lData['Efw'] = eai * lData['DP']
        lData['Eo+Efw'] = lData['Efw'] + lData['Eo']
        lData
        #Grafica
        st.subheader("**Show results of graphic**")
        fig=px.scatter(lData,x="Eo+Efw",y="F",labels={"F":"F(BY)"},title="F vs Eo+Efw",trendline="ols")
        st.plotly_chart(fig,use_container_width=True)


    elif st.checkbox("Yacimiento Saturado sin correlaciones"):
        st.subheader("*Enter input values*")
        p = lData['P (psia)'].values
        F = lData['F(stb)'].values
        Eo = lData["Eo(bbl/stb)"].values
        We = lData['We(bbl)'].values
        lData['N'] = (lData['F(stb)'] - lData['We(bbl)'])/(lData["Eo(bbl/stb)"])
        lData
        #Grafica
        st.subheader("**Show results of graphic**")
        fig2=px.scatter(lData,x="Eo(bbl/stb)",y="F(stb)",labels={"F":"F(STB)"},title="F vs Eo",trendline="ols")
        st.plotly_chart(fig2,use_container_width=True)

    elif st.checkbox("Utilizando Correlaciones"):
        st.subheader("*Choose the option you require::*")
        Pb = st.number_input("Enter Pb value")
        Temp = st.number_input("Enter Temperature value: ")
        API = st.number_input("Enter API value: ")
        YG = st.number_input("Enter Yg value: ")
        YO = st.number_input("Enter Yo value: ")
        Sw = st.number_input("Enter Sw value: ")
        Cw = st.number_input("Enter Cw value: ")
        Cf = st.number_input("Enter Cf value: ")
        p = lData['P (psi)'].values
        nDdatos = len(p)
        Rs_corr=[]
        V_Pb = []
        v_Temp=[]
        v_API=[]
        V_Yg=[]
        v_Yo=[]
        Bo_corr=[]
        if st.checkbox("Correlación Rs:"):
            corr_Rs = st.selectbox("Correlacion:", ("Standing", "Al-Marhoun"))
        if st.checkbox("Correlación Bo:"):
            corr_Bo = st.selectbox("Correlacion:", ("Standing", "Al-Marhoun"))
        for i in range(nDdatos):
            Rs_corr.append(corr_Rs)
            V_Pb.append(Pb)
            v_Temp.append(Temp)
            v_API.append(API)
            V_Yg.append(YG)
            v_Yo.append(YO)
            Bo_corr.append(corr_Bo)

        #RS
        Params_Rs = pd.DataFrame(
            {"Correlacion": Rs_corr, "Presion": p, "Presion_Burb": V_Pb,
             "API": v_API, "Temperatura": v_Temp, "G_gas": V_Yg,
             "G_oil": v_Yo})
        v_Rs = []
        for i in range(nDdatos):
            Rs_resul = Rs(*(Params_Rs.iloc[i, 0], Params_Rs.iloc[i, 1], Params_Rs.iloc[i, 2], Params_Rs.iloc[i, 3],
                            Params_Rs.iloc[i, 4], Params_Rs.iloc[i, 5], Params_Rs.iloc[i, 6]))
            v_Rs.append(Rs_resul)
        lData["Rs"] = v_Rs

        #Bo
        Params_Bo = pd.DataFrame(
                {"Correlacion": Bo_corr, "Presion": p, "Presion_burb": V_Pb,
                 "Rs": v_Rs, "Rsb": v_Rs, "G_gas": V_Yg, "G_oil": v_Yo,
                 "Temperatura": v_Temp, "API": v_API})
        v_Bo = []
        for i in range(nDdatos):
            Bo_resul = Bo(*(
                Params_Bo.iloc[i, 0], Params_Bo.iloc[i, 1], Params_Bo.iloc[i, 2], Params_Bo.iloc[i, 3],
                Params_Bo.iloc[i, 4],
                Params_Bo.iloc[i, 5], Params_Bo.iloc[i, 6], Params_Bo.iloc[0, 7], Params_Bo.iloc[0, 8]))
            v_Bo.append(Bo_resul)
        lData["Bo"] = v_Bo

        #EBM
        p = lData['P (psi)'].values
        Np = lData['Np (MMSTB)'].values
        Gp = lData['Gp (MMScf)'].values
        We = lData['We (MMBl)'].values
        Bg = lData['Bg x104 (Cft/Scf)'].values
        eai = lData['Bo (bbl/STB)'][0] * ((Cf + (Sw * Cw)) / (1 - Sw))
        lData['Rp'] = lData['Gp (MMScf)'] / lData['Np (MMSTB)']
        lData["F"] =lData['Np (MMSTB)']*(lData["Bo"]+(lData["Rp"]-lData["Rs"][0])*lData["Bg x104 (Cft/Scf)"])
        lData['Eo'] = (lData['Bo'] - lData['Bo'][0])
        lData['Eg'] = lData['Bo'][0] * (lData['Bg x104 (Cft/Scf)']/lData['Bg x104 (Cft/Scf)'][0]-1)
        lData['DP'] = lData['P'][0] - lData['P']
        lData['Efw'] = eai * lData['DP']
        lData["F+We/ Eo+Efw"] = lData["F"]+lData["We (MMBl)"]/lData["Eo"]+lData['Efw']
        lData['Eg+Efw/Eo+Efw'] = lData["Eg"]+lData["Efw"]/ lData['Eo'] + lData['Efw']
        lData


