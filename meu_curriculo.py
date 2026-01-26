import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

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

col1, col2 = st.columns(2,vertical_alignment="center")

with col1:
    st.image("/workspaces/Meu_Curriculo_Python/imagemligaifs.jpg")
    st.write("Ibmec Finance Society - IFS IBMEC-BH")

    st.markdown("""
- Treinamento em análise de empresas, modelagem financeira e valuation.
- Desenvolvimento de um relatório completo de equity research no estilo CFA da Raia Drogasil para o IFS Trainee Challenge. Relatório CFA - Raia Drogasil IFS.
""")
    
with col2:
    st.image("Imagemligaconvidadoufmg.jpg")
    st.write("Professor convidado - UFMG - Liga de Mercado e Negócios")

    st.markdown("""
                Conduzi uma aula a convite da Equipe de Empreendedorismo e Gestão da Liga de Mercado e Negócios da UFMG, abordando Valuation e Estudo de Viabilidade Econômico-Financeira. 
- O tema principal da aula foi a simulação de um Estudo de Viabilidade de uma Academia Nova.
- Promovi discussões sobre métodos de avaliação de empresas, análise financeira e aplicação de diferentes modelos de valuation em contextos reais, além de compartilhar experiências práticas do meu dia a dia como consultor.
""")

st.markdown("---")
st.subheader("CURSOS")
col1, col2, col3 = st.columns(3,vertical_alignment="center")

with col1:
    st.image("Screenshot 2026-01-26 172656.png")
    st.write("*Alfa Research - Treinamento em Análise Fundamentalista e Valuation*")
with col2:
    st.image("Screenshot 2026-01-26 172726.png")
    st.write("*M&A na Prática - Valuation e Modelagem Financeira*")
with col3:
    st.image("Screenshot 2026-01-26 172750.png")
    st.write("*Análise Macro - Análise dos Demonstrativos Financeiros*")

st.markdown("---")
st.subheader("HABILIDADES")