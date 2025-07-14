# 🧮 Scientific Calculator (Streamlit)

A powerful scientific calculator built with Python and Streamlit, now supporting both **degrees** and **radians** for trigonometric functions.

## ✨ Features

### 🧠 Core Capabilities
- **Basic operations**: `+`, `−`, `×`, `÷`, `^`
- **Parentheses** for proper order of operations
- **Advanced math functions**:
  - `sin`, `cos`, `tan`
  - `log`, `sqrt`, `exp`
- **Constants**: `π`, `e`

### ⚙️ Smart Input Modes
- Toggle between **Degrees** and **Radians** for trig functions
- Error handling for division by zero and syntax issues
- Dynamic expression evaluation and real-time updates

### 🎨 Interface
- Clean and modern UI styled with CSS
- Real-time display with session state
- Responsive layout with calculator-style button grid

## ▶️ How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📌 Notes
- Built-in Python `math` module is used under a safe evaluation context.
- Trig functions automatically convert input if degrees are selected.

---

Made with ❤️ using Streamlit and Python.