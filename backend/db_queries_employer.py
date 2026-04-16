import pandas as pd
import streamlit as st
from sqlalchemy import text
from backend.db import get_engine


def _query(sql: str, params: dict) -> pd.DataFrame:
    engine = get_engine()
    with engine.connect() as conn:
        return pd.read_sql(text(sql), conn, params=params)


@st.cache_data(ttl=600)
def get_active_employers(finyear: int | None = None):
    sql = """
        SELECT
            dc.company_name,
            COUNT(*) AS demand_count
        FROM "FACT_Job_Posting" jp
        JOIN "DIM_Company" dc ON jp.company_id = dc.company_id
        JOIN "DIM_Date_Posted" d ON jp.date_posted = d.date
        WHERE (:finyear IS NULL OR d.finyear = :finyear)
        GROUP BY dc.company_name
        ORDER BY demand_count DESC
        LIMIT 10
    """
    return _query(sql, {"finyear": finyear})


@st.cache_data(ttl=600)
def get_roles_by_company(company_name: str, finyear: int | None = None):
    sql = """
        SELECT
            jt.job_title,
            COUNT(*) AS demand_count
        FROM "FACT_Job_Posting" jp
        JOIN "DIM_Company" dc ON jp.company_id = dc.company_id
        JOIN "DIM_Job_Title" jt ON jp.job_title_id = jt.job_title_id
        JOIN "DIM_Date_Posted" d ON jp.date_posted = d.date
        WHERE dc.company_name = :company_name
          AND (:finyear IS NULL OR d.finyear = :finyear)
        GROUP BY jt.job_title
        ORDER BY demand_count DESC
    """
    return _query(sql, {"company_name": company_name, "finyear": finyear})


@st.cache_data(ttl=600)
def get_skills_by_company(company_name: str, finyear: int | None = None):
    sql = """
        SELECT
            s.skill_name,
            COUNT(*) AS demand_count
        FROM "FACT_Job_Posting" jp
        JOIN "DIM_Company" dc ON jp.company_id = dc.company_id
        JOIN "FACT_Job_Skill" fs ON jp.job_posting_id = fs.job_posting_id
        JOIN "DIM_Skill" s ON fs.skill_id = s.skill_id
        JOIN "DIM_Date_Posted" d ON jp.date_posted = d.date
        WHERE dc.company_name = :company_name
          AND (:finyear IS NULL OR d.finyear = :finyear)
        GROUP BY s.skill_name
        ORDER BY demand_count DESC
        LIMIT 10
    """
    return _query(sql, {"company_name": company_name, "finyear": finyear})
