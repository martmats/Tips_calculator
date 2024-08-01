import streamlit as st

# Inject custom CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #77a8f7;
        color: white;
        font-size: 16px;
    }
    .stTextInput>div>div>input {
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Tip Calculator")

bill = st.number_input("What is the total bill?", min_value=0.0, format="%.2f")
tip = st.slider("What percentage tip would you like to give?", min_value=0, max_value=100, step=1)
people = st.number_input("How many people would you like to split the bill?", min_value=1, step=1)

if st.button("Calculate"):
    tip_percentage = tip / 100
    total_tip = bill * tip_percentage
    total_tip_total = total_tip + bill
    total_amount = total_tip_total / people
    total_round = round(total_amount, 2)

    st.success(f"Each person should pay £{total_round}")

