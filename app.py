import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
    .main {
        background-color: #f5f7fb;
    }

    .title {
        text-align: center;
        color: #4F46E5;
        font-size: 38px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #555;
        margin-bottom: 30px;
    }

    .result {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-top: 25px;
    }

    .good {
        background-color: #dcfce7;
        color: #15803d;
    }

    .average {
        background-color: #fef3c7;
        color: #b45309;
    }

    .poor {
        background-color: #fee2e2;
        color: #b91c1c;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    '<div class="title">🎓 Student Performance Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict student performance using study hours, attendance and previous marks.</div>',
    unsafe_allow_html=True
)

# Inputs
st.subheader("📊 Enter Student Details")

study_hours = st.slider(
    "📚 Study Hours per Day",
    min_value=0.0,
    max_value=12.0,
    value=5.0,
    step=0.5
)

attendance = st.slider(
    "🏫 Attendance Percentage",
    min_value=0,
    max_value=100,
    value=75
)

previous_marks = st.slider(
    "📝 Previous Marks Percentage",
    min_value=0,
    max_value=100,
    value=60
)

# Prediction button
if st.button("🔮 Predict Performance", use_container_width=True):

    # Simple prediction logic
    if (
        study_hours >= 5
        and attendance >= 75
        and previous_marks >= 60
    ):
        performance = "GOOD"
        emoji = "🎉"
        css_class = "good"
        message = "The student is likely to perform well."

    elif (
        study_hours >= 3
        and attendance >= 60
        and previous_marks >= 50
    ):
        performance = "AVERAGE"
        emoji = "👍"
        css_class = "average"
        message = "The student has average predicted performance."

    else:
        performance = "NEEDS IMPROVEMENT"
        emoji = "📈"
        css_class = "poor"
        message = "The student may need more study time and improvement."

    # Display result
    st.markdown(
        f"""
        <div class="result {css_class}">
            {emoji}<br>
            Predicted Performance<br>
            {performance}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(message)

# Project information
st.divider()

st.subheader("ℹ️ About This Project")

st.write(
    """
    This application demonstrates a simple student performance prediction
    system. It uses three factors — study hours, attendance and previous marks —
    to estimate the student's performance.
    """
)

st.caption("Student Performance Predictor | Built with Python & Streamlit")
