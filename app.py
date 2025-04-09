import streamlit as st

st.title("Cadastro de clientes")

nome = st.text_input("Informe o Nome Completo")
endereco = st.text_input("Informe o Endereço")
dt_nasc = st.date_input("Informe a Data de Nasimento")
tipo_cliente = st.selectbox("Tipo de Cliente",
                             ["Pessoa Física", "Pessoa Jurídica"])
cadastrar = st.button("Cadastrar Cliente")

if cadastrar:
    with open("clientes.csv", "a", encoding = "utf8") as arquivo: 
        arquivo.write(f"{nome}, {endereco}, {dt_nasc}, {tipo_cliente}\n")
        st.success("Cliente cadastrado com sucesso!")