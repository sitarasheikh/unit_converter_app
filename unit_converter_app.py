# unit_converter_app.py
import streamlit as st
from pint import UnitRegistry

# Initialize Unit Registry
ureg = UnitRegistry()
Q_ = ureg.Quantity

# All Categories and Units
unit_categories = {
    "Length": ["meter", "kilometer", "mile", "foot", "inch", "centimeter"],
    "Mass": ["gram", "kilogram", "pound", "ounce", "ton"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Area": ["square meter", "square kilometer", "square mile", "acre", "hectare"],
    "Volume": ["liter", "milliliter", "gallon", "cubic meter"],
    "Time": ["second", "minute", "hour", "day"],
    "Speed": ["meter/second", "kilometer/hour", "mile/hour"],
    "Pressure": ["pascal", "bar", "psi", "atmosphere"],
    "Energy": ["joule", "calorie", "kilojoule", "kilocalorie", "kilowatt_hour"],
    "Digital Storage": ["byte", "kilobyte", "megabyte", "gigabyte", "terabyte"],
    "Data Transfer Rate": ["bit/second", "kilobit/second", "megabit/second", "gigabit/second"],
    "Fuel Economy": ["mile/gallon", "kilometer/liter", "liter/100 kilometer"],
    "Plane Angle": ["degree", "radian", "gradian"]
}

st.set_page_config(page_title="🧮 Unit Converter", layout="centered")
st.title("🔄 Universal Unit Converter")
st.markdown("Convert between various units just like Google — instantly!")

# Select Category
category = st.selectbox("Select a category", list(unit_categories.keys()))

# Units
units = unit_categories[category]
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)

# Input Value
value = st.number_input("Enter value", format="%.6f")

# Convert Button
if st.button("Convert"):
    try:
        input_qty = Q_(value, from_unit)
        output_qty = input_qty.to(to_unit)
        st.success(f"✅ {value} {from_unit} = {output_qty:.4f}")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
