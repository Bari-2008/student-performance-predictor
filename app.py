import streamlit as st

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓"
)

st.title("🎓 Student Performance Predictor")
st.write("Enter the student's details to predict performance.")

# Inputs
study_hours = st.number_input(
    "📚 Study Hours per Day",
    min_value=0.0,
    max_value=24.0,
    value=5.0,
    step=0.5
)

attendance = st.number_input(
    "📅 Attendance (%)",
    min_value=0,
    max_value=100,
    value=75
)

previous_marks = st.number_input(
    "📝 Previous Marks (%)",
    min_value=0,
    max_value=100,
    value=60
)

# Prediction
if st.button("🔮 Predict Performance"):

    if study_hours >= 5 and attendance >= 75 and previous_marks >= 60:
        result = "GOOD"
        st.success("🎉 Predicted Performance: GOOD")

    elif study_hours >= 3 and attendance >= 60 and previous_marks >= 50:
        result = "AVERAGE"
        st.warning("📊 Predicted Performance: AVERAGE")

    else:
        result = "NEEDS IMPROVEMENT"
        st.error("📚 Predicted Performance: NEEDS IMPROVEMENT")

    st.write("---")
    st.subheader("📋 Student Details")

    st.write(f"**Study Hours:** {study_hours} hours/day")
    st.write(f"**Attendance:** {attendance}%")
    st.write(f"**Previous Marks:** {previous_marks}%")
