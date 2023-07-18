import streamlit as st

import controller.cliente as cliente

def deletar():
    st.title('deletar dados')
    profissoes = ['Analista de Dados', 'Engenheiro de Dados', 'Cientista de Dados']
    id = ['1', '2', '3', '4', '5']
    with st.form(key='insert'):
        input_id = st.text_input(label='Insira o id:')
       
        
        buttom_submit = st.form_submit_button('deletar')
        
        if buttom_submit:
            cliente.excluir( input_id)
            st.success('Cliente removido com sucesso')      