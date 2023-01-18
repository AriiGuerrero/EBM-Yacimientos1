import numpy as np
import streamlit as st
import pandas as pd
#import plotly_express as px
from streamlit_option_menu import option_menu
from PIL import Image
from collections import namedtuple
from math import radians, acos, asin, cos, sin, atan, degrees, sqrt
from Funciones import F_caso1,Eo_caso1,Eo_caso3,Efw_caso1,Eg_caso3,Rp_corregido,Bo,Rs


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
st.title(" RESERVOIR ENGINEERING :database-add:")

st.write("---")

st.markdown(
    """ This app is used to visualize the results of oil reservoir by material balance equation.

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
# Pages
with st.sidebar:
    options = option_menu(
        menu_title="Menu",
        options=["Information", "Reservoir Potential", "Calculation"],
        icons=["pencil-square", "server", "calculator"],)

# Call web app sections
if options == "Reservoir Potential":
    st.set_option('deprecation.showPyplotGlobalUse', False)
    if st.checkbox("Yacimiento Subsaturado"):
        # method="Darcy"
        # st.subheader("*Enter input values*")
        # q_test = st.number_input("Enter q_test value: ")
        # pwf_test = st.number_input("Enter pwf_test value: ")
        # pr = st.number_input("Enter pr value: ")
        # pwf = st.number_input("Enter pwf value")
        # pb = st.number_input("Enter pb value")
        # st.subheader("*Show results*")
        # Q_darcy= qo_darcy(q_test, pwf_test, pr, pwf, pb)
        # st.success(f" Q_Darcy = {Q_darcy:.3f} bpd")
        # IP=j(q_test,pwf_test,pr,pb,ef=1,ef2=None)
        # st.success(f" IP = {IP:.3f} bpd/psia")
        # AOF=aof(q_test,pwf_test,pr,pb,ef=1,ef2=None)
        # st.success(f" AOF = {AOF:.3f} bpd")
        # QB= Qb(q_test,pwf,pr,pb,ef=1,ef2=None)
        # st.success(f" QB = {QB:.3f} bpd")
        # st.subheader("*THE IPR CURVE*")
        # pwf1=st.number_input("Enter the first pwf value: ")
        # pwf2=st.number_input("Enter the second pwf value: ")
        # pwf3=st.number_input("Enter the third pwf value: ")
        # pwf4=st.number_input("Enter the fourth pwf value: ")
        # pwf5=st.number_input("Enter the fifth pwf value: ")
        # list_pwf = np.array([pwf1,pwf2,pwf3,pwf4,pwf5])
        # curva = IPR_curve_methods(q_test, pwf_test, pr, list_pwf, pb, method, ef=1, ef2=None)
        # st.pyplot(curva)

    elif st.checkbox("Yacimiento Saturado"):
        # method = "Vogel"
        # st.subheader("*Enter input values*")
        # q_test = st.number_input("Enter q_test value: ")
        # pwf_test = st.number_input("Enter pwf_test value: ")
        # pr = st.number_input("Enter pr value: ")
        # pwf = st.number_input("Enter pwf value")
        # pb = st.number_input("Enter pb value")
        # st.subheader("*Show results*")
        # Q_Vogel= qo_vogel(q_test, pwf_test, pr, pwf, pb)
        # st.success(f" Q_VOGEL = {Q_Vogel:.3f} bpd")
        # IP=j(q_test,pwf_test,pr,pb,ef=1,ef2=None)
        # st.success(f" IP = {IP:.3f} bpd/psia")
        # AOF=aof(q_test,pwf_test,pr,pb,ef=1,ef2=None)
        # st.success(f" AOF = {AOF:.3f} bpd")
        # QB= Qb(q_test,pwf,pr,pb,ef=1,ef2=None)
        # st.success(f" QB = {QB:.3f} bpd")
        # st.subheader("*THE IPR CURVE*")
        # pwf1 = st.number_input("Enter the first pwf value: ")
        # pwf2 = st.number_input("Enter the second pwf value: ")
        # pwf3 = st.number_input("Enter the third pwf value: ")
        # pwf4 = st.number_input("Enter the fourth pwf value: ")
        # pwf5 = st.number_input("Enter the fifth pwf value: ")
        # list_pwf = np.array([pwf1, pwf2, pwf3, pwf4, pwf5])
        # curva = IPR_curve_methods(q_test, pwf_test, pr, list_pwf, pb, method, ef=1, ef2=None)
        # st.pyplot(curva)

    # elif st.checkbox("STANDING"):
    #     method = "Standing"
    #     st.subheader("*Enter input values*")
    #     q_test = st.number_input("Enter q_test value: ")
    #     pwf_test = st.number_input("Enter pwf_test value: ")
    #     pr = st.number_input("Enter pr value: ")
    #     pwf = st.number_input("Enter pwf value")
    #     pb = st.number_input("Enter pb value")
    #     st.subheader("*Show results*")
    #     Q_Stand=qo_standing(q_test, pwf_test, pr, pwf, pb, ef=1, ef2=None)
    #     st.success(f" Q_STANDING = {Q_Stand:.3f} bpd")
    #     IP=j(q_test,pwf_test,pr,pb,ef=1,ef2=None)
    #     st.success(f" IP = {IP:.3f} bpd/psia")
    #     AOF=aof(q_test,pwf_test,pr,pb,ef=1,ef2=None)
    #     st.success(f" AOF = {AOF:.3f} bpd")
    #     QB= Qb(q_test,pwf,pr,pb,ef=1,ef2=None)
    #     st.success(f" Q_B = {QB:.3f} bpd")
    #     st.subheader("*THE IPR CURVE*")
    #     pwf1 = st.number_input("Enter the first pwf value: ")
    #     pwf2 = st.number_input("Enter the second pwf value: ")
    #     pwf3 = st.number_input("Enter the third pwf value: ")
    #     pwf4 = st.number_input("Enter the fourth pwf value: ")
    #     pwf5 = st.number_input("Enter the fifth pwf value: ")
    #     list_pwf = np.array([pwf1, pwf2, pwf3, pwf4, pwf5])
    #     curva = IPR_curve_methods(q_test, pwf_test, pr, list_pwf, pb, method, ef=1, ef2=None)
    #     st.pyplot(curva)
    #
    # elif st.checkbox("Qo"):
    #     st.subheader("*Enter input values*")
    #     q_test = st.number_input("Enter q_test value: ")
    #     pwf_test = st.number_input("Enter pwf_test value: ")
    #     pr = st.number_input("Enter pr value: ")
    #     pwf = st.number_input("Enter pwf value")
    #     pb = st.number_input("Enter pb value")
    #     st.subheader("*Show results*")
    #     Qo=qo(q_test, pwf_test, pr, pwf, pb, ef=1, ef2=None)
    #     st.success(f" Qo = {Qo:.3f} bpd")
    #     IP=j(q_test,pwf_test,pr,pb,ef=1,ef2=None)
    #     st.success(f" IP = {IP:.3f} bpd/psia")
    #     AOF=aof(q_test,pwf_test,pr,pb,ef=1,ef2=None)
    #     st.success(f" AOF = {AOF:.3f} bpd")
    #     QB= Qb(q_test,pwf,pr,pb,ef=1,ef2=None)
    #     st.success(f" QB = {QB:.3f} bpd")
    #     st.subheader("*THE IPR CURVE*")
    #     pwf1 = st.number_input("Enter the first pwf value: ")
    #     pwf2 = st.number_input("Enter the second pwf value: ")
    #     pwf3 = st.number_input("Enter the third pwf value: ")
    #     pwf4 = st.number_input("Enter the fourth pwf value: ")
    #     pwf5 = st.number_input("Enter the fifth pwf value: ")
    #     list_pwf = np.array([pwf1, pwf2, pwf3, pwf4, pwf5])
    #     curva=IPR_Curve(q_test,pwf_test,pr,list_pwf,pb,ef=1,ef2=None,ax=None)
    #     st.pyplot(curva)


elif options == "Calculation":
    if st.checkbox("Graficas"):
        # st.subheader("*Enter input values*")
        # q_test = st.number_input("Enter Q_tets value: ")
        # pwf_test = st.number_input("Enter pwf_test value: ")
        # Q = st.number_input("Enter Q value: ")
        # pr = st.number_input("Enter Pr value: ")
        # pb = st.number_input("Enter pb value: ")
        # ID = st.number_input("Enter ID value: ")
        # THP = st.number_input("Enter THP value: ")
        # wc = st.number_input("Enter wc value: ")
        # sgh2o=st.number_input("Enter SGH2O value: ")
        # densid=st.number_input("Enter Densidad Oil value: ")
        # TVD = st.number_input("Enter TVD value: ")
        # MD = st.number_input("Enter MD value: ")
        # st.subheader("*Show results Inflow*")
        # pwf_D=pwf_darcy(q_test,pwf_test,Q,pr,pb)
        # st.success(f" Pwf_Darcy = {pwf_D:.3f} psi")
        # F_darcy = f_darcy(Q, ID, C=120)
        # TDH = tdh_(THP, sg_avg, TVD, F_darcy, MD)
        # st.success(f" TDH = {TDH:.3f} ")
        # st.subheader("*Show results Outflow*")
        # pgrav=Pgrav(sg_avg,TVD)
        # st.success(f" Pgrav = {pgrav:.3f} ")
        # st.success(f" f = {F_darcy:.3f} ")
        # F=F_(f_darcy,MD)
        # st.success(f" F = {F:.3f} ")
        # Pf=Pf_(F,sg_avg)
        # st.success(f" Pf = {Pf:.3f} ")
        # Po = Po_(THP,Pgrav,Pf)
        # st.success(f" Po = {Po:.3f} ")
        # Psys = Psys_(Po,pwf_darcy)
        # st.success(f" Psys = {Psys:.3f} ")


