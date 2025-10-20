import streamlit as st

# ==========================
# Streamlit MBTI 진로 추천 앱 (main.py)
# 이 파일을 streamlit_cloud 또는 로컬에 올려서 사용하세요.
# ==========================

st.set_page_config(page_title="MBTI 진로 추천", page_icon="🧭", layout="centered")

# --- 스타일 ---
st.markdown(
    """
    <style>
    .main-title {font-size:2.2rem; font-weight:800; color:#2B6CB0; text-align:center; margin-bottom:0.2rem}
    .sub-title {font-size:1rem; color:#555; text-align:center; margin-bottom:1.2rem}
    .career-box {background:#ffffff; padding:0.9rem 1rem; border-radius:12px; box-shadow:0 6px 18px rgba(43,108,176,0.08); margin-bottom:0.8rem}
    .pill {display:inline-block; background:#EEF2FF; color:#2B6CB0; padding:6px 10px; border-radius:999px; font-weight:600}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='main-title'>🧭 MBTI별 진로 추천</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>본인의 MBTI를 선택하면 성향에 맞는 다양한 직업을 제안합니다. (예시는 참고용)</div>", unsafe_allow_html=True)

MBTI_LIST = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ",
]

# 확장된 추천 진로 맵
CAREER_MAP = {
    "ISTJ": [
        "회계사 — 정확하고 체계적인 업무 처리",
        "공무원(행정) — 절차 중심, 안정성 선호",
        "데이터 분석가 — 자료 정리와 규칙 적용에 강함",
        "품질관리(QA) 전문가 — 꼼꼼한 검수 능력",
        "보안/리스크 관리 — 규정 준수와 보호 업무",
    ],
    "ISFJ": [
        "간호사 — 세심한 돌봄과 책임감",
        "초중등 교사 — 학생 돌봄과 조직 지원",
        "사회복지사 — 실질적 도움 제공",
        "행정직(사무) — 체계적 업무 처리",
        "HR(인사) — 직원 지원과 조직 관리",
    ],
    "INFJ": [
        "심리상담사 — 깊은 공감과 통찰력",
        "작가/에디터 — 의미 중심의 창작",
        "비영리/NGO 활동가 — 가치 기반 업무",
        "교육 컨설턴트 — 개인 맞춤형 지도",
        "예술치료사 — 창의적 치유 활동",
    ],
    "INTJ": [
        "전략기획자 — 장기적 비전 수립",
        "연구원(기초/응용) — 문제 구조화와 해결",
        "데이터 사이언티스트 — 모델 설계와 해석",
        "경영 컨설턴트 — 구조적 분석 능력",
        "CTO/기술리더 — 기술 방향성과 구조 설계",
    ],
    "ISTP": [
        "현장 엔지니어 — 문제해결 중심의 실무",
        "파일럿/운송 관련 직무 — 상황 판단과 제어",
        "정비사/테크니션 — 도구와 기계 다루는 능력",
        "제품 설계자 — 프로토타이핑과 실험",
        "IT 지원/시스템 운영 — 즉시 대응과 수리",
    ],
    "ISFP": [
        "그래픽/패션 디자이너 — 감성적 미감 표현",
        "사진작가/영상편집자 — 시각적 스토리텔링",
        "요리사/제과제빵사 — 창의적 손맛 발휘",
        "인테리어 디자이너 — 공간 미학 구현",
        "아트 디렉터 보조 — 예술적 감각 활용",
    ],
    "INFP": [
        "소설가/시나리오 작가 — 가치 중심의 창작",
        "상담사/치료사 — 공감으로 돕는 역할",
        "콘텐츠 제작자 — 스토리텔링과 메시지 전달",
        "NGO 기획/커뮤니케이션 — 사명 중심 업무",
        "UX 리서처 — 사용자 중심 통찰 제공",
    ],
    "INTP": [
        "연구 개발(R&D) — 개념 탐구와 실험 설계",
        "AI/소프트웨어 엔지니어 — 논리적 설계 선호",
        "데이터 엔지니어/분석가 — 시스템적 사고",
        "교수/학자 — 이론적 탐구와 교육",
        "시스템 아키텍트 — 복잡도 관리와 최적화",
    ],
    "ESTP": [
        "영업/세일즈 — 상황 대응과 설득력",
        "이벤트 기획/운영 — 실전 중심 실행력",
        "응급구조/소방관 — 현장 중심의 활동",
        "스타트업 운영자 — 빠른 실행과 적응",
        "트레이드/중개인(금융) — 리스크 감수와 빠른 판단",
    ],
    "ESFP": [
        "공연/엔터테인먼트 — 사람 앞에서 빛남",
        "매장 운영/리테일 매니저 — 고객 응대 전문",
        "이벤트 스페셜리스트 — 현장 에너지 제공",
        "호스피탈리티/관광 가이드 — 서비스와 소통",
        "소셜 콘텐츠 크리에이터 — 표현과 연결성",
    ],
    "ENFP": [
        "광고/크리에이티브 기획 — 아이디어 발산",
        "창업/제품 매니저 — 사람 중심 문제 해결",
        "홍보/커뮤니케이션 — 네트워킹과 영감 제공",
        "교육/워크숍 진행자 — 열정적 전달자",
        "콘텐츠 전략가 — 트렌드 감지와 스토리텔링",
    ],
    "ENTP": [
        "컨설턴트 — 새로운 관점으로 문제 해결",
        "변호사(특허/소송) — 논리 대결과 설득",
        "스타트업 창업자 — 아이디어 실험과 확장",
        "비즈니스 개발(BD) — 기회 발굴과 협상",
        "미디어/저널리즘 — 빠른 관점 전환과 토론",
    ],
    "ESTJ": [
        "운영/오퍼레이션 매니저 — 절차와 성과 관리",
        "프로젝트 매니저 — 일정·리소스 통제",
        "금융/재무 직무 — 목표 지향적 분석",
        "관리자/팀 리더 — 조직 관리와 규율",
        "품질/프로세스 개선 담당 — 효율 추구",
    ],
    "ESFJ": [
        "HR/인사 전문가 — 조직과 사람의 균형 관리",
        "간호 관리자 — 돌봄과 운영 관리 결합",
        "고객 성공/CS 매니저 — 관계 유지와 만족도 향상",
        "교육 행정/학교 운영 — 사람 중심 운영",
        "이벤트 코디네이터 — 조화와 배려 기반 진행",
    ],
    "ENFJ": [
        "교육자/리더십 코치 — 영감을 주는 멘토",
        "PR/브랜드 매니저 — 메시지와 영향력 관리",
        "사회적 기업가/커뮤니티 매니저 — 조직화와 공감",
        "HR 디렉터 — 조직 문화와 개발 주도",
        "정책·공공운영 — 사람 중심의 설계",
    ],
    "ENTJ": [
        "경영진(CEO/CXO) — 전략 수립과 실행 주도",
        "전략 컨설턴트 — 구조적 분석과 실행력",
        "투자/VC 전문가 — 기회 판단과 포트폴리오 운영",
        "사업개발/BD 디렉터 — 성장 전략 수립",
        "프로덕트 디렉터 — 비전과 조직 운영 결합",
    ],
}

# --- UI 구성 ---
col1, col2 = st.columns([3, 1])
with col1:
    chosen = st.selectbox("당신의 MBTI를 선택하세요 👇", MBTI_LIST)

with col2:
    st.markdown("<div style='text-align:right'><span class='pill'>Tip</span></div>", unsafe_allow_html=True)
    st.write("MBTI는 참고용입니다.")

if chosen:
    st.markdown(f"### 🔷 {chosen} 유형 추천 직업")
    careers = CAREER_MAP.get(chosen, [])

    if careers:
        for i, c in enumerate(careers, 1):
            st.markdown(f"<div class='career-box'><b>{i}. {c}</b></div>", unsafe_allow_html=True)

        st.success("✨ 위 추천은 MBTI 성향을 기반으로 한 예시입니다. 개인의 흥미와 역량을 함께 고려하세요!")

        # 다운로드(텍스트) — 줄바꿈은 \n 으로 처리
        txt_lines = [f"MBTI: {chosen}", "추천 진로:"] + [f"- {c}" for c in careers]
        txt_out = "\n".join(txt_lines)
        st.download_button("📄 추천 목록 다운로드", txt_out, file_name=f"{chosen}_careers.txt")
    else:
        st.warning("해당 MBTI의 추천 진로가 없습니다.")

# 사이드바
st.sidebar.header("ℹ️ 사용법 & 배포")
st.sidebar.write(
    """
1) MBTI를 선택하면 추천 직업 목록이 표시됩니다.
2) 결과는 참고용이며, 실제 진로 선택은 다양한 요소를 고려하세요.
3) 로컬: `streamlit run main.py`, Streamlit Cloud: GitHub 리포지토리 연결 후 배포.
"""
)
st.sidebar.markdown("---")
st.sidebar.caption("Developed with ❤️ using Streamlit")
