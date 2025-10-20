import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="국가별 MBTI 비율 시각화",
    page_icon="🌍",
    layout="wide"
)

# --- 데이터 로드 ---
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# --- UI 구성 ---
st.title("🌍 국가별 MBTI 비율 시각화 대시보드")
st.markdown("""
이 앱은 각 나라의 MBTI 유형 분포를 보여줍니다.  
오른쪽 사이드바에서 국가를 선택하면, 해당 국가의 MBTI 비율이 막대그래프로 표시됩니다.
""")

# --- 국가 선택 ---
country_list = sorted(df["Country"].unique())
selected_country = st.sidebar.selectbox("국가 선택", country_list, index=0)

# --- 선택된 국가 데이터 추출 ---
country_data = df[df["Country"] == selected_country].T
country_data = country_data.reset_index()
country_data.columns = ["MBTI", "비율"]
country_data = country_data.iloc[1:]  # 첫 행(Country) 제거
country_data["비율"] = country_data["비율"].astype(float)

# --- Plotly 막대그래프 ---
fig = px.bar(
    country_data,
    x="MBTI",
    y="비율",
    text="비율",
    color="MBTI",
    color_discrete_sequence=px.colors.qualitative.Set3,
    title=f"{selected_country}의 MBTI 분포",
)
fig.update_traces(texttemplate="%{text:.2%}", textposition="outside")
fig.update_layout(
    yaxis_title="비율",
    xaxis_title="MBTI 유형",
    showlegend=False,
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

# --- 데이터 테이블 표시 ---
with st.expander("📊 원본 데이터 보기"):
    st.dataframe(country_data, use_container_width=True)
