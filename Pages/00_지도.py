# main.py
import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster
import webbrowser

st.set_page_config(page_title="Seoul Top10 for Foreigners", layout="wide")

st.title("🇰🇷 Seoul — Top 10 Tourist Spots (외국인 인기)")
st.markdown(
    "Folium 지도로 외국인들이 좋아하는 서울의 주요 관광지 Top10을 보여줍니다. "
    "마커를 클릭하면 간단한 설명과 (가능한 경우) 링크를 볼 수 있습니다."
)

# Top10 locations (name, lat, lon, short description, link)
ATTRACTIONS = [
    {
        "name": "Gyeongbokgung Palace (경복궁)",
        "lat": 37.579617,
        "lon": 126.977041,
        "desc": "조선의 대표적 궁궐. 수문장 교대식과 한복 체험으로 유명.",
        "link": "https://english.visitseoul.net/attractions/Gyeongbokgung-Palace_/87"
    },
    {
        "name": "Changdeokgung & Secret Garden (창덕궁)",
        "lat": 37.579292,
        "lon": 126.991416,
        "desc": "유네스코 세계유산, 후원이 특히 아름답습니다.",
        "link": "https://english.visitseoul.net/attractions/Changdeokgung-Palace---Huwon_/74"
    },
    {
        "name": "Bukchon Hanok Village (북촌한옥마을)",
        "lat": 37.582604,
        "lon": 126.984942,
        "desc": "전통 한옥이 모여있는 마을로 사진 명소.",
        "link": "https://english.visitseoul.net/attractions/Bukchon-Hanok-Village_/79"
    },
    {
        "name": "Insadong (인사동)",
        "lat": 37.574221,
        "lon": 126.984375,
        "desc": "전통 공예품, 찻집, 골동품 상점이 모여있는 거리.",
        "link": "https://english.visitseoul.net/attractions/Insadong_/73"
    },
    {
        "name": "Myeongdong (명동)",
        "lat": 37.560975,
        "lon": 126.985032,
        "desc": "쇼핑 & 스트리트 푸드의 중심가. 화장품·패션 인기 지역.",
        "link": "https://english.visitseoul.net/attractions/Myeong-dong_/64"
    },
    {
        "name": "N Seoul Tower / Namsan (남산서울타워)",
        "lat": 37.5511694,
        "lon": 126.9882266,
        "desc": "서울 전경을 감상하기 좋은 전망 타워. 사랑의 자물쇠로 유명.",
        "link": "https://english.visitseoul.net/attractions/N-Seoul-Tower_/88"
    },
    {
        "name": "Dongdaemun Design Plaza (DDP, 동대문디자인플라자)",
        "lat": 37.566388,
        "lon": 127.009176,
        "desc": "미래적 건축물과 야시장, 패션 도매 상가 근처.",
        "link": "https://english.visitseoul.net/attractions/Dongdaemun-Design-Plaza--DDP_/183"
    },
    {
        "name": "Gwangjang Market (광장시장)",
        "lat": 37.570176,
        "lon": 127.001699,
        "desc": "전통 시장의 길거리 음식 — 빈대떡, 비빔밥, 마약김밥 등.",
        "link": "https://english.visitseoul.net/attractions/Gwangjang-Market_/1436"
    },
    {
        "name": "Hongdae / Hongik University Area (홍대)",
        "lat": 37.554722,
        "lon": 126.923611,
        "desc": "젊음의 거리, 클럽·카페·스트리트 퍼포먼스가 활발한 지역.",
        "link": "https://english.visitseoul.net/attractions/Hongdae_/1580"
    },
    {
        "name": "Lotte World Tower & Mall (롯데월드타워)",
        "lat": 37.513056,
        "lon": 127.1025,
        "desc": "한국에서 가장 큰 타워 중 하나. 전망대와 대형 쇼핑몰 보유.",
        "link": "https://english.visitseoul.net/attractions/Lotte-World-Tower_/2432"
    },
]

# Sidebar controls
st.sidebar.header("지도 옵션")
show_cluster = st.sidebar.checkbox("마커 클러스터 사용", value=True)
show_markers = st.sidebar.multiselect(
    "표시할 관광지 선택 (여러 개 선택 가능)",
    options=[a["name"] for a in ATTRACTIONS],
    default=[a["name"] for a in ATTRACTIONS]
)

# Create folium map centered in Seoul
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12, tiles="OpenStreetMap")

# Optionally use MarkerCluster
if show_cluster:
    cluster = MarkerCluster().add_to(m)

# Add markers
for attr in ATTRACTIONS:
    if attr["name"] not in show_markers:
        continue
    popup_html = f"""
    <b>{attr['name']}</b><br>
    {attr['desc']}<br>
    <a href="{attr['link']}" target="_blank">더보기</a>
    """
    marker = folium.Marker(
        location=[attr["lat"], attr["lon"]],
        popup=folium.Popup(popup_html, max_width=300),
        tooltip=attr["name"],
        icon=folium.Icon(color="darkblue", icon="info-sign"),
    )
    if show_cluster:
        marker.add_to(cluster)
    else:
        marker.add_to(m)

# Add a mini legend / top10 list on map (as a FloatImage or marker)
legend_html = """
<div style="
position: fixed;
bottom: 50px; left: 10px; width: 260px; height: auto;
z-index:9999; background-color: white; padding: 10px; border-radius:8px;
box-shadow: 2px 2px 6px rgba(0,0,0,0.3);
font-size:12px;">
<b>Top 10 (외국인 인기)</b><br>
<ul style='margin:4px 0 0 16px; padding:0;'>
"""
for a in ATTRACTIONS:
    legend_html += f"<li>{a['name']}</li>"
legend_html += "</ul></div>"

m.get_root().html.add_child(folium.Element(legend_html))

# Display map in Streamlit (wider layout)
with st.container():
    st.subheader("서울 주요 관광지 지도")
    map_data = st_folium(m, width=1100, height=700)

# Show details table / list
with st.expander("관광지 목록(자세히)"):
    for a in ATTRACTIONS:
        st.markdown(f"**{a['name']}**  — {a['desc']}  \n[공식/소개 페이지]({a['link']})")

st.markdown("---")
st.caption("데이터 출처: VisitSeoul 및 여러 여행 가이드(편집 후 정리).")
