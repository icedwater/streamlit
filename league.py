"""
# Dumberland Cup Group 1
Basic dataframe using streamlit
"""

import streamlit as st

st.header("Dumberland Cup Group 1 Results")
st.write("A 1-0 C, A 0-2 B, A 4-0 H")
st.write("B 2-0 A, B 1-1 C, B 1-3 H")
st.write("C 0-1 A, C 1-1 B, C 1-0 H")
st.write("H 0-4 A, H 3-1 B, H 0-1 C")

# I could have read in a CSV, I guess

league = [
        {
            "name": "Antioch FC",
            "played": 3,
            "won": 2,
            "drew": 0,
            "lost": 1,
            "for": 5,
            "against": 2
        },
        {
            "name": "Bundlebay Town",
            "played": 3,
            "won": 1,
            "drew": 1,
            "lost": 1,
            "for": 4,
            "against": 4
        },
        {
            "name": "Cawthorn Rangers",
            "played": 3,
            "won": 1,
            "drew": 1,
            "lost": 1,
            "for": 2,
            "against": 2
        },
        {
            "name": "Hinsley AFC",
            "played": 3,
            "won": 1,
            "drew": 0,
            "lost": 2,
            "for": 3,
            "against": 6
        },
]

# computed fields
for team in league:
    team["gd"] = team.get("for") - team.get("against")
    team["points"] = 3 * team.get("won") + team.get("drew")

st.dataframe(league)
