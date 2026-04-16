import streamlit as st
# from auth import require_auth
from visuals.skills import show as show_skills
from visuals.roles import show as show_roles, show_careers
from visuals.employer import show as show_employers
from visuals.jobdemand import show as show_demand, show_monthly
from visuals.sector import show as show_sectors

# require_auth()  # Blocks direct access if not logged in

st.set_page_config(layout="wide")

# ---------------------------------------------------------------
# Layout + hide sidebar
# ---------------------------------------------------------------
st.markdown("""
    <style>
        [data-testid="stSidebar"] { display: none; }
        [data-testid="collapsedControl"] { display: none; }
        .block-container {
            padding-top: 0.5rem !important;
            margin-top: 0rem !important;
            max-width: 100% !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# Logo + Title + Nav
# ---------------------------------------------------------------
logo_b64 = __import__('base64').b64encode(open('images/GradScope_Image.png', 'rb').read()).decode()

st.markdown(f"""
    <style>
        .nav-bar {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0px 0px 6px 0px;
            margin-bottom: 0px;
        }}
        .nav-logo img {{
            width: 44px;
            height: 44px;
            object-fit: contain;
            border-radius: 8px;
        }}
        .nav-buttons {{
            display: flex;
            gap: 10px;
        }}
        .nav-buttons a {{
            text-decoration: none;
            color: white;
            background-color: transparent;
            border: 1px solid rgba(255,255,255,0.3);
            border-radius: 6px;
            padding: 5px 18px;
            font-size: 14px;
            cursor: pointer;
        }}
        .nav-buttons a:hover {{
            background-color: rgba(255,255,255,0.1);
        }}
    </style>
    <div class="nav-bar">
        <div class="nav-logo">
            <img src="data:image/png;base64,{logo_b64}">
        </div>
        <div class="nav-buttons">
            <a href="/Home" target="_self">Home</a>
            <a href="/Dashboard" target="_self">Dashboard</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# Global card styling
# ---------------------------------------------------------------
st.markdown("""
    <style>
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 12px;
        padding: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# Initialise all visual session states
# ---------------------------------------------------------------
for key, default in [
    ("skill_page", "category"),
    ("roles_page", "overview"),
    ("careers_page", "treemap"),
    ("employers_page", "overview"),
    ("sectors_page", "overview"),
]:
    if key not in st.session_state:
        st.session_state[key] = default

# ---------------------------------------------------------------
# Centralised cursor control
# ---------------------------------------------------------------
on_final_level = (
    st.session_state.get("skill_page") == "trend" or
    st.session_state.get("roles_page") == "trend" or
    st.session_state.get("careers_page") == "job_detail" or
    st.session_state.get("employers_page") == "company_detail" or
    st.session_state.get("sectors_page") == "detail"
)

cursor = "default" if on_final_level else "pointer"

st.markdown(f"""
<style>
    [data-testid="stPlotlyChart"],
    [data-testid="stPlotlyChart"] *,
    [data-testid="stPlotlyChart"] iframe {{
        cursor: {cursor} !important;
    }}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------
# Tabbed Layout
# ---------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Skills",
    "Roles",
    "Employers",
    "Sectors",
    "Trends",
])

with tab1:
    with st.container(border=True):
        show_skills()
with tab2:
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            show_careers()
    with col2:
        with st.container(border=True):
            show_roles()

with tab3:
    with st.container(border=True):
        show_employers()

with tab4:
    with st.container(border=True):
        show_sectors()

with tab5:
    with st.container(border=True):
        show_monthly()
        
    with st.container(border=True):
        show_demand()
