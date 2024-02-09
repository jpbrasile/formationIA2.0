##  Objectif : Créer un hyperbook qui permet de naviguer dans une arborescence et qui parle 
```
import streamlit as st

# Titre de l'application
st.title('Ma Application Streamlit')

# Barre latérale
with st.sidebar:
    st.header('Course Outline')
    st.write('Introduction to Python')
    # Ajoutez ici d'autres sections de votre cours

# Contenu principal
st.header('Numbers: int, float, complex')
st.write("""
En Python, les types de données numériques incluent les entiers (int), les nombres à virgule flottante (float), et les nombres complexes (complex). Les entiers (int) sont des nombres entiers, les flottants (float) sont des nombres avec un point décimal, et les nombres complexes (complex) ont une partie réelle et imaginaire, écrites comme `a + bj`.

```python
int_number = 42
float_number = 3.14
complex_number = 1 + 5j

print(type(int_number))
print(type(float_number))
print(type(complex_number))
```
