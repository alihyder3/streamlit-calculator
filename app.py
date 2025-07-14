import streamlit as st
import math

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Scientific Calculator", layout="centered")
st.title("🧮 Scientific Calculator")

# ---------------- CUSTOM CSS ----------------
custom_css = '''
<style>
[data-testid="stHorizontalBlock"] {
    justify-content: center;
}
#display {
    font-size: 2em;
    font-weight: bold;
    text-align: right;
    padding: 10px;
    border: 2px solid #ddd;
    border-radius: 5px;
    background-color: #f9f9f9;
}
div.stButton > button {
    width: 100%;
    height: 60px;
    font-size: 1.3em;
    margin: 4px;
    border-radius: 8px;
    background-color: #4CAF50;
    color: white;
    border: none;
}
div.stButton > button:hover {
    background-color: #45a049;
}
</style>
'''
st.markdown(custom_css, unsafe_allow_html=True)

# ---------------- STATE ----------------
if "expression" not in st.session_state:
    st.session_state.expression = ""
if "angle_mode" not in st.session_state:
    st.session_state.angle_mode = "Radians"

# ---------------- SIDEBAR ----------------
st.sidebar.header("Calculator Settings")
st.session_state.angle_mode = st.sidebar.radio("Angle Mode", ["Radians", "Degrees"])

# ---------------- FUNCTIONS ----------------
def update_expression(symbol):
    if symbol == "C":
        clear_expression()
    elif symbol == "√":
        st.session_state.expression += "sqrt("
    elif symbol == "^":
        st.session_state.expression += "**"
    elif symbol == "π":
        st.session_state.expression += "pi"
    elif symbol == "e":
        st.session_state.expression += "e"
    else:
        st.session_state.expression += str(symbol)
    st.rerun()

def clear_expression():
    st.session_state.expression = ""
    st.rerun()

def backspace():
    st.session_state.expression = st.session_state.expression[:-1]
    st.rerun()

def calculate():
    expression = st.session_state.expression

    if not expression or expression[-1] in "+−×÷^(":
        st.error("Incomplete expression")
        return

    try:
        # Clean up symbols
        expression = expression \
            .replace("×", "*") \
            .replace("÷", "/") \
            .replace("−", "-")

        # Prepare math-safe context
        safe_context = math.__dict__.copy()

        # If Degrees mode is selected, override trig functions
        if st.session_state.angle_mode == "Degrees":
            safe_context["sin"] = lambda x: math.sin(math.radians(x))
            safe_context["cos"] = lambda x: math.cos(math.radians(x))
            safe_context["tan"] = lambda x: math.tan(math.radians(x))

        result = eval(expression, {"__builtins__": None}, safe_context)
        st.session_state.expression = str(result)
        st.rerun()

    except ZeroDivisionError:
        st.error("Error: Division by zero")
    except SyntaxError:
        st.error("Syntax error: check parentheses or operators")
    except Exception as e:
        st.error(f"Invalid expression: {e}")

# ---------------- DISPLAY ----------------
st.markdown(
    f"<div style='font-size: 2em; font-weight: bold; background-color: #222; padding: 10px; "
    f"border-radius: 5px; color: white; text-align: right;'>{st.session_state.expression or '0'}</div>",
    unsafe_allow_html=True
)

# ---------------- BUTTON GRID ----------------
button_grid = [
    ["sin(", "cos(", "tan(", "√"],
    ["(", ")", "^", "C"],
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "−"],
    ["0", ".", "=", "+"],
    ["π", "e", "exp(", "⌫"]
]

for row in button_grid:
    cols = st.columns(4)
    for i, button in enumerate(row):
        if cols[i].button(button):
            if button == "=":
                calculate()
            elif button == "⌫":
                backspace()
            else:
                update_expression(button)
