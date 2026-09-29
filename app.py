import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="DSA Problem-Solving Tracker",
    page_icon="💻",
    layout="wide"
)

st.title(" DSA Problem-Solving Tracker")

st.write(
    "Track your Data Structures and Algorithms practice "
    "and monitor your problem-solving progress."
)

# -------------------------------
# Initialize problem storage
# -------------------------------

if "problems" not in st.session_state:
    st.session_state.problems = []


# -------------------------------
# DSA Topics
# -------------------------------

topics = [
    "Arrays",
    "Strings",
    "Linked Lists",
    "Stacks",
    "Queues",
    "Trees",
    "Graphs",
    "Sorting",
    "Searching",
    "Dynamic Programming"
]

st.subheader(" DSA Topics")

selected_topic = st.selectbox(
    "Select a DSA topic",
    topics
)


# -------------------------------
# Add Problem
# -------------------------------

st.subheader(" Add Problem")

problem_name = st.text_input("Problem Name")

difficulty = st.selectbox(
    "Difficulty",
    ["Easy", "Medium", "Hard"]
)

status = st.selectbox(
    "Status",
    ["Not Started", "In Progress", "Completed"]
)

if st.button("Add Problem"):

    if problem_name.strip():

        new_problem = {
            "Problem": problem_name,
            "Topic": selected_topic,
            "Difficulty": difficulty,
            "Status": status
        }

        st.session_state.problems.append(new_problem)

        st.success(
            f"Problem '{problem_name}' added successfully!"
        )

    else:
        st.warning("Please enter a problem name.")


# -------------------------------
# Problem List
# -------------------------------

st.subheader(" Problem List")

if st.session_state.problems:

    df = pd.DataFrame(st.session_state.problems)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    # -------------------------------
    # Delete Problem
    # -------------------------------

    st.subheader(" Delete Problem")

    problem_to_delete = st.selectbox(
        "Select a problem to delete",
        range(len(st.session_state.problems)),
        format_func=lambda x: st.session_state.problems[x]["Problem"]
    )

    if st.button("Delete Selected Problem"):

        deleted_problem = st.session_state.problems.pop(
            problem_to_delete
        )

        st.success(
            f"Problem '{deleted_problem['Problem']}' deleted successfully!"
        )

        st.rerun()

else:

    st.info("No problems added yet.")


# -------------------------------
# Statistics
# -------------------------------

st.subheader(" Practice Progress")

total_problems = len(st.session_state.problems)

completed = sum(
    problem["Status"] == "Completed"
    for problem in st.session_state.problems
)

in_progress = sum(
    problem["Status"] == "In Progress"
    for problem in st.session_state.problems
)

not_started = sum(
    problem["Status"] == "Not Started"
    for problem in st.session_state.problems
)


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Problems", total_problems)

with col2:
    st.metric("Completed", completed)

with col3:
    st.metric("In Progress", in_progress)

with col4:
    st.metric("Not Started", not_started)
    # -------------------------------
# Completion Rate
# -------------------------------

if total_problems > 0:
    completion_rate = (completed / total_problems) * 100
else:
    completion_rate = 0

st.subheader("🎯 Completion Rate")

st.progress(
    completion_rate / 100
)

st.write(f"{completion_rate:.1f}% completed")


# -------------------------------
# Progress Chart
# -------------------------------

st.subheader(" Progress Overview")

progress_data = pd.DataFrame(
    {
        "Status": [
            "Completed",
            "In Progress",
            "Not Started"
        ],
        "Problems": [
            completed,
            in_progress,
            not_started
        ]
    }
)

st.bar_chart(
    progress_data.set_index("Status")
)