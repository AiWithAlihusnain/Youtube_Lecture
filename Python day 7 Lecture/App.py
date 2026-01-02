import streamlit as st

# ---------- Page Configuration ----------
st.set_page_config(
    page_title="Student Result Management System",
    page_icon="🎓",
    layout="centered"
)

# ---------- Title ----------
st.title("🎓 Student Result Management System")
st.write("A simple and professional result calculator built with **Python & Streamlit**.")

st.divider()

# ---------- Fixed Subjects (Tuple) ----------
subjects = ("Math", "Physics", "Chemistry", "Computer", "English")
TOTAL_MARKS = 500

# ---------- Student Information ----------
st.subheader("🧑‍🎓 Student Information")
student_name = st.text_input("Enter Student Name")

# ---------- Marks Input ----------
st.subheader("📝 Enter Marks")
marks = []

for subject in subjects:
    score = st.number_input(
        f"{subject} Marks",
        min_value=0,
        max_value=100,
        step=1
    )
    marks.append(score)

# ---------- Result Button ----------
st.divider()

if st.button("📊 Generate Result", use_container_width=True):

    if student_name.strip() == "":
        st.error("Please enter the student name.")
    else:
        obtained_marks = sum(marks)
        percentage = (obtained_marks / TOTAL_MARKS) * 100

        # ---------- Grade System ----------
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "Fail"

        # ---------- Display Results ----------
        st.success("✅ Result Generated Successfully!")

        st.subheader("📄 Student Report Card")

        col1, col2, col3 = st.columns(3)
        col1.metric("Obtained Marks", obtained_marks)
        col2.metric("Total Marks", TOTAL_MARKS)
        col3.metric("Percentage", f"{percentage:.2f}%")

        st.divider()

        st.write(f"**Student Name:** {student_name}")
        st.write(f"**Grade:** {grade}")

        if grade == "Fail":
            st.warning("⚠️ Student needs improvement.")
        else:
            st.balloons()
            st.success("🎉 Congratulations!")

# ---------- Footer ----------
st.divider()
st.caption("Built with ❤️ using Python & Streamlit")
