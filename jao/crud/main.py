import streamlit as st

import page.insert as insert
import page.select as select
import page.delete as delete
import page.atualizar as atualizar

#criando a barra lateral do menu
st.sidebar.title('Menu')
selectbox = st.sidebar.selectbox('Ação', ['Inserir', 'Consultar','deletar'])

if selectbox == 'Inserir':
    insert.inserir()

if selectbox == 'Consultar':
    select.consultar()

if selectbox == 'deletar':
    delete.deletar()

if selectbox == 'atualizar':
    atualizar.atualizar()