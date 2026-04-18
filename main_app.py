import streamlit as st
import pandas as pd
import plotly.express as px
from langchain_groq import ChatGroq
from langchain_experimental.agents import create_pandas_dataframe_agent
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="AI EV Optimizer", layout="wide", page_icon="🚗")
st.title("Smart EV Fleet Optimizer")


# --- 1. DATA LOADING FUNCTION ---
@st.cache_data
def load_data():
    # File must be in the same folder as this script
    file_path = "fleet_data_optimized.csv"
    if os.path.exists(file_path):
        # We ensure it reads the IDs and costs correctly
        df = pd.read_csv(file_path)
        return df
    return None


df = load_data()

if df is not None:
    # --- 2. SIDEBAR (KPI METRICS) ---
    st.sidebar.header("Global Metrics")
    total_savings = df["savings_eur"].sum()
    total_cost_dumb = df["dumb_cost_eur"].sum()
    savings_percent = (
        int((total_savings / total_cost_dumb) * 100) if total_cost_dumb > 0 else 0
    )

    st.sidebar.metric(
        "Total Savings", f"{total_savings:.2f} €", delta=f"{savings_percent}%"
    )
    st.sidebar.metric("Avg. Savings per EV", f"{df['savings_eur'].mean():.2f} €")
    st.sidebar.write(f"Active Vehicles: {len(df['vehicle_id'].unique())}")
    # --- 3. VISUALIZATIONS ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Savings by Vehicle")
        # Чтобы каждый столбец был своего цвета:
        # 1. color="vehicle_id" делает разные цвета для разных машин
        # 2. barmode="group" убирает "слоистость"
        fig = px.bar(
            df,
            x="vehicle_id",
            y="savings_eur",
            color="vehicle_id",
            color_discrete_sequence=px.colors.qualitative.Pastel,  # Или любая другая палитра
            labels={"savings_eur": "Savings (€)", "vehicle_id": "Vehicle ID"},
        )

        # Убираем легенду справа, так как ID машин и так подписаны внизу
        fig.update_layout(
            showlegend=False,
            bargap=0.1,
            # Попробуй 0.2, если хочешь еще шире
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Cost Comparison")
        cost_comparison = df[["dumb_cost_eur", "smart_cost_eur"]].sum()
        fig2 = px.pie(
            values=cost_comparison.values,
            names=["Dumb Charging", "Smart Charging"],
            hole=0.4,
            color_discrete_sequence=["#ef553b", "#00cc96"],
        )
        st.plotly_chart(fig2, use_container_width=True)
    # --- 4. AI ASSISTANT (GROQ) ---
    st.divider()
    st.subheader("🤖 AI Fleet Assistant")
    user_question = st.text_input("Ask a question about your fleet:")

    if user_question:
        try:
            API_KEY = st.sidebar.text_input("Enter Groq API Key", type="password")

            # Updated to the new working model name
            llm = ChatGroq(
                temperature=0, groq_api_key=API_KEY, model_name="llama-3.1-8b-instant"
            )

            # Creating the agent to read your dataframe
            agent = create_pandas_dataframe_agent(
                llm,
                df,
                verbose=False,
                allow_dangerous_code=True,
                handle_parsing_errors=True,
            )

            with st.spinner("Analyzing data..."):
                response = agent.run(user_question)
                st.info(response)

        except Exception as e:
            st.error(f"AI Assistant is having a moment. Error: {e}")

else:
    # This part runs only if 'fleet_data_optimized.csv' is missing
    st.error("⚠️ File 'fleet_data_optimized.csv' not found!")
    st.info(
        "Please make sure you have run your optimization script and the CSV is in the project folder."
    )
    st.write("Current folder content:", os.listdir())
