import streamlit as st
import pandas as pd
import numpy as np

st.title("Currículo - Ricardo Guimarães")

with st.sidebar:
    st.image("/workspaces/Meu_Curriculo_Python/Soul Plena - Trade1-2.jpg",caption='*Ricardo de Oliveira Guimarães*')


st.subheader("SUMÁRIO")
st.write("Graduando em Ciências Econômicas pelo Ibmec-BH, com sólida base em Finanças Corporativas e experiência prática em Modelagem Financeira e Valuation de empresas. Possuo proficiência em Excel, PowerPoint, Word e Python, aplicando essas ferramentas em análises financeiras e estratégicas. Busco oportunidades de estágio em Finanças Corporativas e Valuation, com interesse especial em M&A, Investment Banking e Private Equity, para desenvolver ainda mais minhas habilidades técnicas e contribuir para a criação de valor em empresas e projetos.")

st.markdown("---")

st.subheader("EXPERIÊNCIA")

tab1, tab2 = st.tabs(["Consultor", "Alguns Projetos"])
with tab1:
    st.subheader("Consultor de Empresas")
    st.image("/workspaces/Meu_Curriculo_Python/trade-mensagem-de-natal.jpg",width=700)
with tab2:
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("Projeto - Varanda 1389")
        st.image("/workspaces/Meu_Curriculo_Python/imagem1trade.jpg",width=500)
    with col2:
        st.write("Projeto - AB&B Engenharia")
        st.image("/workspaces/Meu_Curriculo_Python/Imagem2Trade.jpg",width=500)

st.markdown("""
- Responsável pela **modelagem financeira**, **apresentações executivas** e **validação de análises** nas áreas de **Valuation**, **Estudos de Viabilidade** e **Business Plan**, com participação em **mais de 15 projetos** junto a clientes de diversos setores (principalmente **saúde**).
- Atuação em projetos de **M&A**, com desenvolvimento de **modelagens financeiras**, **Teasers** e **Memorandos de Informação (Memoinfos)** para suporte a processos de transação.
- Atuação em projetos de **Joint Venture**, com foco na **elaboração de modelagens financeiras** e **apresentações executivas**.
- Participação em projetos de **FP&A**, com foco na **elaboração de modelos de planejamento orçamentário e estratégico**, contribuindo para o **aprimoramento da performance financeira** das empresas.
""")


st.markdown("---")

st.subheader("EDUCAÇÃO")
col1, col2 = st.columns(2)

with col1:
    st.write("Colégio Magnum - Ensino Médio Completo")
    st.image("logomagnumv1.png",width=400)
with col2:
    st.write("""
    Bacharelado em Ciências Econômicas  
    IBMEC Belo Horizonte – MG  
    01/2022 – 12/2026
    """)
    st.image("logoibmec.png",width=500)

st.markdown("---")
st.subheader("ATIVIDADES EXTRACURRILARES")

