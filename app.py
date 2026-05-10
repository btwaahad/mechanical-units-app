import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Mechanical Unit Converter", layout="centered")

# --- HEADER SECTION ---
st.title("🔧 Mechanical Unit Converter & Material Density Checker")
st.markdown(f"""
**Developer:** MUHAMMAD ABDUL AHAD  
**Roll Number:** 25-ME-04  
---
""")

# --- NAVIGATION ---
option = st.sidebar.selectbox("Select Function", ["Unit Converter", "Material Density Checker"])

# --- UNIT CONVERTER ---
if option == "Unit Converter":
    st.header("Unit Converter")
    
    category = st.selectbox("Category", ["Length", "Pressure", "Force"])
    
    col1, col2 = st.columns(2)
    
    if category == "Length":
        with col1:
            val = st.number_input("Value", value=1.0)
            unit_from = st.selectbox("From", ["Meters", "Millimeters", "Inches", "Feet"])
        
        # Conversion Logic (To Meters as base)
        to_meters = {"Meters": 1, "Millimeters": 0.001, "Inches": 0.0254, "Feet": 0.3048}
        base_val = val * to_meters[unit_from]
        
        with col2:
            unit_to = st.selectbox("To", ["Meters", "Millimeters", "Inches", "Feet"])
            result = base_val / to_meters[unit_to]
            st.metric("Converted Value", f"{result:.4f} {unit_to}")

    elif category == "Pressure":
        with col1:
            val = st.number_input("Value", value=1.0)
            unit_from = st.selectbox("From", ["Pascal (Pa)", "Bar", "PSI", "Atmosphere"])
        
        to_pa = {"Pascal (Pa)": 1, "Bar": 100000, "PSI": 6894.76, "Atmosphere": 101325}
        base_val = val * to_pa[unit_from]
        
        with col2:
            unit_to = st.selectbox("To", ["Pascal (Pa)", "Bar", "PSI", "Atmosphere"])
            result = base_val / to_pa[unit_to]
            st.metric("Converted Value", f"{result:.4f}")

    elif category == "Force":
        with col1:
            val = st.number_input("Value", value=1.0)
            unit_from = st.selectbox("From", ["Newton (N)", "Kilonewton (kN)", "Pound-force (lbf)"])
        
        to_n = {"Newton (N)": 1, "Kilonewton (kN)": 1000, "Pound-force (lbf)": 4.44822}
        base_val = val * to_n[unit_from]
        
        with col2:
            unit_to = st.selectbox("To", ["Newton (N)", "Kilonewton (kN)", "Pound-force (lbf)"])
            result = base_val / to_n[unit_to]
            st.metric("Converted Value", f"{result:.2f}")

# --- MATERIAL DENSITY CHECKER ---
elif option == "Material Density Checker":
    st.header("Material Density Database")
    
    # Dictionary of common materials (kg/m^3)
    materials = {
        "Steel (Mild)": 7850,
        "Aluminum (6061)": 2700,
        "Stainless Steel (304)": 8000,
        "Titanium": 4500,
        "Copper": 8960,
        "Brass": 8500,
        "ABS Plastic": 1040,
        "Carbon Fiber (CFRP)": 1600,
        "Cast Iron": 7200
    }
    
    search = st.selectbox("Select Material", list(materials.keys()))
    density = materials[search]
    
    st.info(f"The density of **{search}** is approximately **{density} kg/m³**.")
    
    # Quick Mass Calculator
    st.subheader("Quick Mass Calculator")
    volume = st.number_input("Enter Volume (m³)", value=0.1, step=0.01)
    mass = volume * density
    st.success(f"Estimated Mass: {mass:.2f} kg")
