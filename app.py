import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Set page config - must be the first Streamlit command
st.set_page_config(layout="wide", page_title="Stock Visualization")

# Add a title and description
st.title("📈 Interactive Stock Visualization")
st.markdown("### Explore historical stock data with customizable parameters")

# Sidebar for customization options
st.sidebar.header("Visualization Settings")


# Load the stock data
@st.cache_data
def load_data():
    return px.data.stocks()


df = load_data()

# Display data information
with st.expander("View Raw Data"):
    st.dataframe(df)
    st.write(f"Features available: {', '.join(df.columns[1:])}")
    st.write(f"Date range: {df['date'].min()} to {df['date'].max()}")

# Sidebar options
# Company selection
companies = st.sidebar.multiselect(
    "Select Companies to Display",
    options=df.columns[1:],
    default=list(df.columns[1:])
)

# Color theme selection
color_theme = st.sidebar.selectbox(
    "Select Color Theme",
    options=["plotly_dark", "plotly", "ggplot2", "seaborn", "simple_white"],
    index=0
)

# Chart dimensions
col1, col2 = st.sidebar.columns(2)
with col1:
    width = st.number_input("Width", min_value=500, max_value=3000, value=1200, step=100)
with col2:
    height = st.number_input("Height", min_value=400, max_value=1600, value=600, step=100)

# Title customization
title_text = st.sidebar.text_input("Chart Title", "Stock Values Over Time")
title_size = st.sidebar.slider("Title Size", 10, 50, 24)
title_color = st.sidebar.color_picker("Title Color", "#FF0000")  # Red default

# Axis label customization
axis_label_size = st.sidebar.slider("Axis Label Size", 10, 40, 16)
axis_label_color = st.sidebar.color_picker("Axis Label Color", "#FFFF00")  # Yellow default

# Line customization
line_width = st.sidebar.slider("Line Width", 1, 10, 4)

# Create the visualization
if companies:
    # Create figure
    fig = go.Figure()

    for company in companies:
        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df[company],
            name=company,
            line=dict(width=line_width)
        ))

    # Update layout based on user selections
    fig.update_layout(
        title=title_text,
        title_font=dict(color=title_color, size=title_size, family='Arial'),
        title_x=0.5,
        xaxis_title='Date',
        yaxis_title='Stock Value',
        xaxis=dict(title_font=dict(color=axis_label_color, size=axis_label_size)),
        yaxis=dict(title_font=dict(color=axis_label_color, size=axis_label_size)),
        legend_title_font=dict(size=16),
        width=width,
        height=height,
        template=color_theme
    )

    # Display the chart
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Please select at least one company to display")

# Add some additional features
st.subheader("Stock Statistics")

if companies:
    # Create a stats dataframe for selected companies
    stats_df = pd.DataFrame({
        'Company': companies,
        'Min': [df[company].min().round(2) for company in companies],
        'Max': [df[company].max().round(2) for company in companies],
        'Mean': [df[company].mean().round(2) for company in companies],
        'Std Dev': [df[company].std().round(2) for company in companies],
        'Last Value': [df[company].iloc[-1].round(2) for company in companies]
    })

    st.dataframe(stats_df, use_container_width=True)

    # Add a feature to download the data
    st.download_button(
        label="Download Selected Data as CSV",
        data=df[['date'] + companies].to_csv(index=False).encode('utf-8'),
        file_name='selected_stock_data.csv',
        mime='text/csv',
    )

# Footer
st.markdown("---")
st.markdown("Created with Streamlit and Plotly")
