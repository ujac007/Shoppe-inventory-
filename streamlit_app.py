import streamlit as st
import pandas as pd

# Set Page Config
st.set_page_config(page_title="Inventory Quick-Lookup", page_icon="🛍️", layout="wide")

# 1. The Data Structure
inventory_data = [
    # WOMENS RIGHT SIDE
    {"Section": "Womens", "Brand": "Mireille - Paris", "Item": "Shirts (beads & embroidery)", "Price": "195", "Note": "2 stores in Paris"},
    {"Section": "Womens", "Brand": "Mireille - Paris", "Item": "Blazers pink (oversized)", "Price": "575", "Note": ""},
    {"Section": "Womens", "Brand": "Mireille - Paris", "Item": "Cropped Tweed", "Price": "395", "Note": ""},
    {"Section": "Womens", "Brand": "Mireille - Paris", "Item": "Denim & Tweed", "Price": "395", "Note": ""},
    {"Section": "Womens", "Brand": "Mireille - Paris", "Item": "Long Tweed", "Price": "695", "Note": ""},
    {"Section": "Womens", "Brand": "System", "Item": "T-shirts", "Price": "95", "Note": ""},
    {"Section": "Womens", "Brand": "System", "Item": "Sweater Vest", "Price": "138", "Note": ""},
    {"Section": "Womens", "Brand": "System", "Item": "Hoodie Tweed", "Price": "295", "Note": "Lg left cream, Med navy; Fits Med vs Lg"},
    {"Section": "Womens", "Brand": "System", "Item": "Vest - Fringe", "Price": "95", "Note": ""},
    
    # HODGE PODGE
    {"Section": "Hodge Podge", "Brand": "DAHLO (Italian)", "Item": "General Inventory", "Price": "50% Off Tags", "Note": ""},
    {"Section": "Hodge Podge", "Brand": "Gap", "Item": "General Inventory", "Price": "50% Off", "Note": ""},
    {"Section": "Hodge Podge", "Brand": "Felicity", "Item": "General Inventory", "Price": "35", "Note": "Sizes 1-4 available"},
    {"Section": "Hodge Podge", "Brand": "The Drop", "Item": "General Inventory", "Price": "15", "Note": ""},
    {"Section": "Hodge Podge", "Brand": "New Vintage", "Item": "General Inventory", "Price": "35", "Note": "Retail value $215-$295"},
    {"Section": "Hodge Podge", "Brand": "We Are HAH", "Item": "General Inventory", "Price": "45", "Note": "Made from corn sugar"},
    {"Section": "Hodge Podge", "Brand": "Spiritual Gangster", "Item": "General Inventory", "Price": "60% Off", "Note": "Not System (NS)"},
    {"Section": "Hodge Podge", "Brand": "Unsubscribed", "Item": "Sweaters", "Price": "85", "Note": ""},
    {"Section": "Hodge Podge", "Brand": "Unsubscribed", "Item": "Dress", "Price": "55", "Note": ""},
    {"Section": "Hodge Podge", "Brand": "Tory Burch", "Item": "General Inventory", "Price": "60% Off", "Note": ""},
    {"Section": "Hodge Podge", "Brand": "Disney", "Item": "Sweats", "Price": "18", "Note": ""},
    
    # LUX SECTION
    {"Section": "Lux", "Brand": "Jil Sander", "Item": "Shoes", "Price": "60% Off", "Note": "Off the crossed out price; German brand"},
    {"Section": "Lux", "Brand": "Marni (Italy)", "Item": "Shoes", "Price": "50% Off", "Note": "Italian colors"},
    {"Section": "Lux", "Brand": "Moni Bags", "Item": "Bags", "Price": "60% Off", "Note": ""},
    
    # KIDS
    {"Section": "Kids", "Brand": "Milk Barn", "Item": "Onies", "Price": "14", "Note": "50% off $28 original"},
    {"Section": "Kids", "Brand": "Antebies", "Item": "Short Set", "Price": "33", "Note": "Made in Turkey; 0-10 yrs"},
    {"Section": "Kids", "Brand": "MUSLI", "Item": "Onie", "Price": "15", "Note": "Safari print; 40% Off"},
    {"Section": "Kids", "Brand": "Adidas / Nike", "Item": "Shoes/Apparel", "Price": "50% Off", "Note": "NS; Except shorts in system"},
]

df = pd.DataFrame(inventory_data)

# 2. Sidebar Navigation & Tools
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Search Inventory", "Sale Calculator"])

if page == "Search Inventory":
    st.title("🛍️ Store Inventory Lookup")
    
    # Filters
    search_query = st.text_input("Search by Brand or Item", placeholder="e.g., Marni, Tweed, or Milk Barn")
    selected_section = st.multiselect("Filter by Section", options=df["Section"].unique(), default=df["Section"].unique())

    # Filtering Logic
    filtered_df = df[df["Section"].isin(selected_section)]
    if search_query:
        filtered_df = filtered_df[
            filtered_df["Brand"].str.contains(search_query, case=False) | 
            filtered_df["Item"].str.contains(search_query, case=False)
        ]

    # Display Results
    if not filtered_df.empty:
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    else:
        st.warning("No items found. Try a different search term.")

elif page == "Sale Calculator":
    st.title("🧮 Quick Sale Calculator")
    st.write("Use this to calculate final prices for items listed as percentages.")
    
    col1, col2 = st.columns(2)
    with col1:
        original_price = st.number_input("Original Price ($)", min_value=0.0, value=100.0, step=5.0)
    with col2:
        discount = st.slider("Discount (%)", 0, 100, 50)
    
    savings = original_price * (discount / 100)
    final_price = original_price - savings
    
    st.metric(label="Final Sale Price", value=f"${final_price:,.2f}", delta=f"-${savings:,.2f} savings")

# 3. Footer Branding
st.markdown("---")
st.caption("Retail Inventory Tool | Hand-transcribed from store notes.")