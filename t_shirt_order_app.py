import streamlit as st
import pandas as pd

# Available options
colors = ["Black", "Red", "White"]
sizes = ["S", "M", "L", "XL", "XXL"]
cuts = ["Male", "Ladies"]

# Page title
st.title("👕 T-shirt Order Form")

# Store orders in session state
if "orders" not in st.session_state:
st.session_state.orders = []

# Order form
with st.form("order_form"):
name = st.text_input("Customer Name")
color = st.selectbox("Choose Color", colors)
size = st.selectbox("Choose Size", sizes)
cut = st.radio("Choose Cut", cuts, horizontal=True)

submitted = st.form_submit_button("Add Order")
if submitted:
if name.strip():
st.session_state.orders.append({
"Name": name,
"Color": color,
"Size": size,
"Cut": cut
})
st.success(f"Order for {name} added!")
else:
st.error("Please enter a name before submitting.")

# Display order summary
if st.session_state.orders:
st.subheader("📋 Order Summary")
df = pd.DataFrame(st.session_state.orders)
st.table(df)

# Option to export orders
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
"Download Orders as CSV",
csv,
"orders.csv",
"text/csv"
)
