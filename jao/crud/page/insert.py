import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('inserir dados')
    profissoes = ['Analista de Dados', 'Engenheiro de Dados', 'Cientista de Dados']
    animais = ['cachorro', 'gato', 'vaca', 'ovelha', 'cavalo']
    with st.form(key='insert'):
        input_name = st.text_input(label='Insira o nome:')
        input_tipo = st.radio(label='escolha um animal', options = animais)
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(input_name, input_tipo)
            st.success('Cliente incluido com sucesso')      