import streamlit as st
from modules import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("TO-DO List App")
st.subheader("This is My TODO List App")
st.write("This App is to manage your TODOs")

for todo in todos:
    st.checkbox(todo)

st.text_input(label='',placeholder='Add New ToDo',
              on_change=add_todo, key="new_todo")

