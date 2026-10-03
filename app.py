import streamlit as st
import urllib.parse

# 1. Setup the page title and look
st.set_page_config(page_title="Mama Dee's Kotas", page_icon="🍞", layout="centered")

# Custom CSS styling to make it look premium on a phone screen
st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: white; }
    h1 { color: #ffcc00; text-align: center; font-family: 'Arial Black', sans-serif; }
    p { text-align: center; font-size: 16px; }
    div.stButton > button:first-child {
        background-color: #ffcc00; color: black; font-weight: bold;
        font-size: 18px; border-radius: 8px; width: 100%; height: 50px;
        box-shadow: 0px 4px 10px rgba(255, 204, 0, 0.4); border: none;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🍞 Mama Dee's Kotas Portal 🍞")
st.write("Tap your choices below to place your order directly via WhatsApp!")

st.write("---")

# 2. STEP 1: Select the Base Kota
st.subheader("1. Choose Your Base Kota")
kota_options = {
    "Chips & Polony (R20)": 20,
    "Chips, Polony & Cheese (R25)": 25,
    "The Russian Standard (R40)": 40,
    "The Dagwood Special (R65)": 65,
    "The King Size Full House (R95)": 95
}
selected_kota = st.selectbox("Select a combo:", list(kota_options.keys()))
total_price = kota_options[selected_kota]

st.write("---")

# 3. STEP 2: Select Optional Extras
st.subheader("2. Add Optional Extras")
extra_cheese = st.checkbox("Extra Cheese (+R5)")
extra_egg = st.checkbox("Extra Fried Egg (+R5)")
extra_russian = st.checkbox("Extra Russian (+R15)")
extra_patty = st.checkbox("Extra Burger Patty (+R20)")

# Track what extras the customer added
selected_extras = []
if extra_cheese: 
    total_price += 5
    selected_extras.append("Extra Cheese")
if extra_egg: 
    total_price += 5
    selected_extras.append("Extra Fried Egg")
if extra_russian: 
    total_price += 15
    selected_extras.append("Extra Russian")
if extra_patty: 
    total_price += 20
    selected_extras.append("Extra Burger Patty")

st.write("---")

# 4. STEP 3: Collection Time
st.subheader("3. Preferred Collection Time")
pickup_time = st.text_input("Example: 12:30, or 'As soon as possible'", value="As soon as possible")

st.write("---")

# 5. DISPLAY TOTAL
st.markdown(f"<h2 style='text-align: center; color: #ffcc00;'>Total Amount: R{total_price}</h2>", unsafe_allow_html=True)

# 6. FORMAT WHATSAPP STRING LOGIC
# Formatting the message string cleanly for a text string link
extras_text = ", ".join(selected_extras) if selected_extras else "None"

raw_msg = (
    f"*🔥 NEW KOTA ORDER 🔥*\n"
    f"------------------------\n"
    f"*Base Item:* {selected_kota}\n"
    f"*Extras:* {extras_text}\n"
    f"*Collection Time:* {pickup_time}\n"
    f"------------------------\n"
    f"*Total Bill:* R{total_price}\n"
    f"------------------------\n"
    f"_Please confirm my order and prep time!_"
)

# Encode the string text variables so web browsers can read it safely
encoded_msg = urllib.parse.quote(raw_msg)

# Mama Dee's active phone number with country code (no spaces, no + sign)
shop_number = "27623539564" 
whatsapp_url = f"https://wa.me{shop_number}?text={encoded_msg}"

# Big clickable checkout button
if st.button("🚀 PLACE ORDER VIA WHATSAPP"):
    st.markdown(f'<meta http-serif="refresh" content="0;URL=\'{whatsapp_url}\'" />', unsafe_allow_html=True)
    st.success("Redirecting you straight to WhatsApp to hit send...")
    st.markdown(f"[Click here if it doesn't open automatically]({whatsapp_url})")
