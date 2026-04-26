import streamlit as st
import plotly.express as px
from backend.db_queries_roles import get_experience_by_role

CB_COLORS = [
    "#4C8BF5",  # blue
    "#F5A623",  # amber
    "#E8789A",  # pink
    "#6B6B6B",  # dark grey
    "#56B4E9",  # sky blue
    "#009E73",  # bluish green
    "#D55E00",  # vermillion
    "#0072B2",  # deep blue
]


def show(job_title: str, finyear: int | None = None):
    plotly_config = {"displayModeBar": False}

    df = get_experience_by_role(job_title, finyear=finyear)

    if df.empty:
        st.info(f"No experience data available for {job_title}.")
        return

    df = df.sort_values("demand_count", ascending=True)

    colors = [CB_COLORS[i % len(CB_COLORS)] for i in range(len(df))]

    fig = px.bar(
        df,
        x="demand_count",
        y="experience_level",
        orientation="h",
        labels={
            "experience_level": "Experience Level",
            "demand_count": "Number of Job Postings",
        },
    )

    fig.update_traces(
        marker=dict(color=colors, line=dict(width=0)),
        text=df["demand_count"],
        textposition="outside",
    )

    fig.update_layout(
        title=dict(text=f"Experience Requirements for {job_title}", x=0.5, xanchor="center"),
        xaxis_title="Number of Job Postings",
        yaxis_title="Experience Level",
        showlegend=False,
        height=350,
        margin=dict(l=20, r=20, t=60, b=40),
        xaxis=dict(rangemode="tozero"),
    )

    st.plotly_chart(fig, use_container_width=True, config=plotly_config)
