import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="SIP Calculator", layout="wide")

st.title("📈 SIP Growth: Matplotlib Version")

# --- INPUTS ---
with st.sidebar:
    st.header("Investment Parameters")
    monthly_sip = st.number_input("Monthly SIP (₹)", min_value=500, value=5000, step=500)
    years = st.slider("Duration (Years)", min_value=1, max_value=40, value=15)

# --- CALCULATION ---
rates = [8, 10, 12, 14, 18]
plot_data = []

for rate in rates:
    plot_data.append({"Year": 0, "Rate": f"{rate}%", "Amount": 0})

# Calculate from year 1 onwards
for year in range(1, years + 1):
    months = year * 12
    for rate in rates:
        monthly_rate = (rate / 100) / 12
        fv = monthly_sip * (
            ((1 + monthly_rate) ** months - 1) / monthly_rate
        ) * (1 + monthly_rate)

        plot_data.append({
            "Year": year,
            "Rate": f"{rate}%",
            "Amount": fv
        })

df = pd.DataFrame(plot_data)

# --- VISUALIZATION ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Maturity Values")
    # Filter for the final year to show in table
   final_values = (
    df[df["Year"] == years][["Rate", "Amount"]]
    .reset_index(drop=True)
    )


    st.table(final_values.style.format({"Amount": "₹{:,.0f}"}))

    

with col2:
    st.subheader("Wealth Growth Over Time")
    
    # Create the Matplotlib Figure
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.set_style("whitegrid")
    
    # Plotting
    sns.lineplot(data=df, x="Year", y="Amount", hue="Rate", marker="o", ax=ax)
    
    # Formatting
    ax.set_title(f"SIP Growth Comparison over {years} Years", fontsize=14)
    ax.set_ylabel("Total Wealth (₹)")
    ax.set_xlabel("Years")
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    
    # Display in Streamlit
    st.pyplot(fig)

# Calculation for total invested
total_invested = monthly_sip * 12 * years
st.info(f"💡 Total amount invested over {years} years: **₹{total_invested:,}**")

st.subheader("What's Next")

st.write(
    "This calculator shows the math. "
    "If you want help finding the right investment, you can explore more here."
)

st.markdown(
    """
    <a href="https://shreemoney.in" target="_blank">
        <button style="
            background-color:#0f4c81;
            color:white;
            padding:10px 18px;
            border:none;
            border-radius:6px;
            font-size:16px;
            cursor:pointer;
        ">
            Visit ShreeMoney
        </button>
    </a>
    """,
    unsafe_allow_html=True
)

st.write(
        "You can reach me directly."
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        """
        <a href="tel:+917559161118">
            <button style="
                width:60%;
                background-color:#0f4c81;
                color:white;
                padding:12px;
                border:none;
                border-radius:6px;
                font-size:16px;
                cursor:pointer;
            ">
                📞 Call
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <a href="https://wa.me/917559161118" target="_blank">
            <button style="
                width:60%;
                background-color:#25D366;
                color:white;
                padding:12px;
                border:none;
                border-radius:6px;
                font-size:16px;
                cursor:pointer;
            ">
                WhatsApp
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )
