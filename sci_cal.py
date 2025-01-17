import streamlit as st
import math

# Streamlit app
st.title("Scientific Calculator")

# User input
expression = st.text_input("Enter your mathematical expression (e.g., sin(30), log(10), 5+5):")

# Buttons for quick functions
st.markdown("### Quick Mathematical Operations")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("π (Pi)"):
        st.write(math.pi)

    if st.button("e (Euler's Number)"):
        st.write(math.e)

with col2:
    if st.button("sin(x)"):
        st.write("Usage: sin(x). Example: sin(30)")

    if st.button("log(x)"):
        st.write("Usage: log(x). Example: log(10)")

with col3:
    if st.button("√x (Square Root)"):
        st.write("Usage: sqrt(x). Example: sqrt(16)")

# Evaluate user expression
if expression:
    try:
        # Safe evaluation using math module
        allowed_functions = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log,
            'sqrt': math.sqrt,
            'pi': math.pi,
            'e': math.e,
            'factorial': math.factorial,
            'exp': math.exp
        }

        # Replace input string with allowed functions
        for key in allowed_functions:
            expression = expression.replace(key, f"allowed_functions['{key}']")

        # Evaluate the expression
        result = eval(expression)
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")
