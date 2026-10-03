import streamlit as st
import urllib.parse

# 1. Page Configuration & Aesthetic Theme Settings
st.set_page_config(page_title="Mama Dee's Fast Food", page_icon="🍔", layout="centered")

# Custom CSS styling matching her orange/black menu board brand color profile
st.markdown("""
    <style>
    .main { background-color: #fffaf5; color: #222222; }
    h1 { color: #ff6b00; text-align: center; font-family: 'Arial Black', sans-serif; font-weight: bold; margin-bottom: 5px; }
    .subtitle { text-align: center; font-size: 16px; color: #555555; font-weight: bold; margin-bottom: 20px; }
    div.stButton > button:first-child {
        background-color: #ff6b00; color: white; font-weight: bold;
        font-size: 18px; border-radius: 12px; width: 100%; height: 55px;
        border: none; box-shadow: 0px 4px 10px rgba(255, 107, 0, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🍊 MAMA DEE'S FAST FOOD 🍊")
st.markdown("<p class='subtitle'>Good Food for Good Moments • Mon - Fri: 10AM - 6PM</p>", unsafe_allow_html=True)

st.write("---")

# 2. Main Order Category Selection
st.subheader("🥪 1. Choose Your Meal")
order_type = st.radio("Select Category:", ["Kotas", "Footlong Russian Rolls", "No Food (Delivery Only Idea)"])

selected_food = "None"
food_price = 0

if order_type == "Kotas":
    # Complete 23-tier Kota menu extracted directly from her menu board picture
    kota_menu = {
        "None": 0,
        "Atchaar + Chips (R18)": 18,
        "Atchaar + Chips + French (R20)": 20,
        "Atchaar + Chips + French + Special (R22 - Tier A)": 22,
        "Atchaar + Chips + Cheese (R22 - Tier B)": 22,
        "Atchaar + Chips + French + Special + Vienna (R24 - Tier A)": 24,
        "Atchaar + Chips + French + Special + Cheese (R24 - Tier B)": 24,
        "Atchaar + Chips + French + Special + Vienna + Cheese (R26 - Tier A)": 26,
        "Atchaar + Chips + Cheese + Egg (R26 - Tier B)": 26,
        "Atchaar + Chips + French + Vienna + Cheese + Russian (R28 - Tier A)": 28,
        "Atchaar + Chips + French + Cheese + 2xViennas (R28 - Tier B)": 28,
        "Atchaar + Chips + French + Vienna + Egg + Russian (R28 - Tier C)": 28,
        "Atchaar + Chips + French + Egg + Cheese + Russian (R28 - Tier D)": 28,
        "Atchaar + Chips + French + Vienna + 2xSpecials + Russian (R28 - Tier E)": 28,
        "Atchaar + Chips + French + 2xSpecials + Russian + Cheese (R28 - Tier F)": 28,
        "Atchaar + Chips + French + Special + Vienna + Cheese + Egg (R30 - Tier A)": 30,
        "Atchaar + Chips + French + Cheese + Burger (R30 - Tier B)": 30,
        "Atchaar + Chips + French + Egg + Cheese + Burger (R32)": 32,
        "Atchaar + Chips + French + Vienna + Russian + Burger (R34 - Tier A)": 34,
        "Atchaar + Chips + French + Vienna + Cheese + Russian + Egg (R34 - Tier B)": 34,
        "Atchaar + Chips + French + Vienna + Cheese + Egg + Burger (R34 - Tier C)": 34,
        "Atchaar + Chips + French + 2xSpecials + Cheese + Russian + Burger (R34 - Tier D)": 34,
        "Atchaar + Chips + French + Cheese + 2xViennas + Burger (R34 - Tier E)": 34,
        "Atchaar + Chips + French + Vienna + Cheese + Russian + Burger + Egg (R40)": 40
    }
    selected_food = st.selectbox("Select your exact Kota combination:", list(kota_menu.keys()))
    food_price = kota_menu[selected_food]

elif order_type == "Footlong Russian Rolls":
    # New Footlong special category
    roll_menu = {
        "None": 0,
        "Footlong Russian Roll: Roll, Cheese, Russian & Chips (R50)": 50
    }
    selected_food = st.selectbox("Select Roll option:", list(roll_menu.keys()))
    food_price = roll_menu[selected_food]

st.write("---")

# 3. Delivery Method & Zone Calculations
st.subheader("🛵 2. Collection or Delivery")
delivery_option = st.radio("How would you like your order?", ["Collection (Free)", "Delivery"])

delivery_fee = 0
selected_zone = "N/A"

if delivery_option == "Delivery":
    # Exact neighborhood zone matrix from her delivery flyer picture
    delivery_zones = {
        "Select Your Location": 0,
        "Witpoortjie (R15)": 15,
        "Mindalore (R15)": 15,
        "Grobler Park (R15)": 15,
        "Chamdor (R20)": 20,
        "Leratong (R20)": 20,
        "Lindhaven (R20)": 20,
        "Wilrogate (R25)": 25,
        "Westgate (R25)": 25,
        "Horison View (R25)": 25,
        "Kagiso (R30)": 30,
        "Roodepoort CBD (R30)": 30
    }
    selected_zone = st.selectbox("Choose delivery area:", list(delivery_zones.keys()))
    delivery_fee = delivery_zones[selected_zone]

st.write("---")

# 4. Quantity Adjustments & Final Bill Logic
st.subheader("🔢 3. Final Details")
quantity = st.number_input("How many portions?", min_value=1, max_value=20, value=1, step=1)
notes = st.text_input("Special requests? (e.g., No atchaar, extra salt):", value="None")

# Calculate totals completely automatically
total_bill = (food_price * quantity) + delivery_fee

st.markdown(f"<h2 style='text-align: center; color: #ff6b00;'>Total Bill: R{total_bill}</h2>", unsafe_allow_html=True)

# 5. Build Clean WhatsApp Message String Output
raw_message = (
    f"*🍔 MAMA DEE'S ORDER FORM 🍔*\n"
    f"-------------------------------------\n"
    f"*Category:* {order_type}\n"
    f"*Item:* {selected_food}\n"
    f"*Quantity:* {quantity}x\n"
    f"-------------------------------------\n"
    f"*Method:* {delivery_option}\n"
    f"*Zone/Area:* {selected_zone}\n"
    f"*Special Notes:* {notes}\n"
    f"-------------------------------------\n"
    f"*TOTAL AMOUNT DUE:* R{total_bill}\n"
    f"-------------------------------------\n"
    f"_Order generated instantly via catalog link!_"
)

# URL encode the string to safely format spaces and special characters for web browsers
encoded_message = urllib.parse.quote(raw_message)

# Mama Dee's fast-food cell routing contact line 
mama_dee_number = "27688570125"
whatsapp_url = f"https://wa.me{mama_dee_number}?text={encoded_message}"

# Clean, bug-free redirect button setup
st.link_button("🔥 SUBMIT ORDER VIA WHATSAPP", whatsapp_url)
