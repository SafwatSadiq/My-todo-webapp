import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo.title() + '\n')
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""
    


st.title("My Todo App")
st.subheader("My Todo List")
st.write("This App Is for increase your productivity")

for todo in todos:
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
    
st.text_input(label="Todo_Add_Box",
              placeholder="Add New Todo...",
              label_visibility="hidden",
              on_change=add_todo, key='new_todo')