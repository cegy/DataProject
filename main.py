import streamlit as st

# Streamlit MBTI Career Recommendation App
# 파일명: streamlit_mbti_careers.py
# 사용법: streamlit run streamlit_mbti_careers.py

st.set_page_config(page_title="MBTI 진로 추천", page_icon="🧭", layout="centered")

st.title("MBTI별 진로 추천")
st.write("아래에서 본인의 MBTI를 골라 진로 추천을 받아보세요.")

MBTI_LIST = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ",
]

# MBTI -> 추천 직업(간단 설명 포함)
CAREER_MAP = {
    "ISTJ": [
        "회계사 — 규칙과 절차를 잘 지키고 세부사항에 강함",
        "공무원 — 안정성과 체계적 일 처리 선호",
        "품질관리(QA) — 꼼꼼한 검토와 표준 준수",
    ],
    "ISFJ": [
        "간호사 — 다른 사람 돌보는 것을 중시",
        "교사(초등) — 책임감 있고 헌신적이며 학생 돌봄에 적합",
        "사회복지사 — 실질적 도움 제공에 보람을 느낌",
    ],
    "INFJ": [
        "심리상담사 — 타인의 감정을 깊게 이해함",
        "작가/콘텐츠 크리에이터 — 내향적 통찰을 글로 표현",
        "비영리기구(NGO) 기획 — 가치 중심의 직무",
    ],
    "INTJ": [
        "전략기획자 — 장기 플랜 수립과 시스템 설계에 강함",
        "연구원(과학/AI) — 논리적 문제 해결 선호",
        "스타트업 창업자/CTO — 비전 제시와 구조화 능력",
    ],
    "ISTP": [
        "엔지니어(하드웨어/현장) — 손으로 직접 문제 해결",
        "파일럿/운전자 — 실용적 기술 활동 선호",
        "정비사/테크니션 — 도구와 기계 다루는 능력",
    ],
    "ISFP": [
        "디자이너(그래픽/패션) — 감성적 표현과 미적 감각",
        "사진작가/영상편집자 — 순간과 감정을 시각화",
        "요리사/바리스타 — 창의적 실습 활동 선호",
    ],
    "INFP": [
        "창작자(작가/시나리오) — 이상과 가치 중심의 표현",
        "상담사/치료사 — 공감과 지원으로 타인 돕기",
        "콘텐츠 전략가 — 스토리텔링 강점 활용",
    ],
    "INTP": [
        "소프트웨어 개발자 — 논리적 구조화와 문제 해결",
        "데이터 분석가/연구원 — 개념적 사고와 실험",
        "아키텍트(시스템) — 구조 설계 및 최적화",
    ],
    "ESTP": [
        "영업/마케팅 실행가 — 즉각적 상황 대응 능력",
        "이벤트 기획자 — 빠른 판단과 실행 선호",
        "응급구조대원/소방관 — 현장 중심의 활동",
    ],
    "ESFP": [
        "연예/공연(배우, 가수) — 사람들 앞에서 빛남",
        "리테일/매장 운영 — 사람 응대와 서비스에 능함",
        "여행 가이드/호스피탈리티 — 즉흥성과 친화력 활용",
    ],
    "ENFP": [
        "광고기획/크리에이티브 디렉터 — 아이디어 발산",
        "창업/제품 매니저 — 사람 중심의 비전 제시",
        "커뮤니케이션 스페셜리스트 — 네트워킹과 설득",
    ],
    "ENTP": [
        "컨설턴트 — 문제발견과 창의적 해결책 제시",
        "스타트업 창업자 — 새 아이디어 실험과 확장",
        "변호사(소송/특허) — 논리싸움과 변론 즐김",
    ],
    "ESTJ": [
        "운영관리(Operations) — 조직 관리와 절차 개선",
        "프로젝트 매니저 — 일정·자원 통제에 능함",
        "은행원/재무관리 — 규칙과 목표 달성 중심",
    ],
    "ESFJ": [
        "HR(인사) — 사람 관리와 지원에 강함",
        "간호/헬스케어 관리자 — 돌봄과 조직화 결합",
        "고객 성공 매니저 — 고객 지향적 소통 능력",
    ],
    "ENFJ": [
        "교육자/리더십 코치 — 타인을 이끄는 능력",
        "PR/브랜드 매니저 — 공감과 메시지 전달 탁월",
        "사회운동/커뮤니티 매니저 — 영향력 행사",
    ],
    "ENTJ": [
        "경영진(CEO/CXO) — 비전 설정과 조직 운영",
        "전략 컨설턴트 — 구조적 분석과 실행력",
        "투자은행/VC — 큰 그림 판단과 리더십",
    ],
}

# 앱 레이아웃
with st.form(key='mbti_form'):
    chosen = st.selectbox("당신의 MBTI를 선택하세요:", MBTI_LIST)
    submitted = st.form_submit_button("추천 받기")

if submitted:
    st.markdown(f"### 선택: **{chosen}**")
    careers = CAREER_MAP.get(chosen, [])
    if careers:
        st.markdown("**추천 진로(예시)**")
        for i, c in enumerate(careers, 1):
            st.write(f"{i}. {c}")

        st.info("위 직업들은 MBTI의 경향성을 기반으로 한 예시입니다. 개인의 흥미, 가치관, 강점 검사를 함께 고려하세요.")

        # 추가 기능: 세부설명 보여주기
        with st.expander("직업별 더 자세한 설명 보기"):
            for c in careers:
                st.write(f"**{c.split('—')[0].strip()}**")
                desc = "—".join(c.split('—')[1:]).strip()
                if desc:
                    st.write(desc)
                else:
                    st.write("직업 설명이 없습니다.")
                st.write("---")

        # 다운로드 버튼 (추천 목록을 텍스트로 다운로드)
        txt_out = f"MBTI: {chosen}\n추천 진로:\n" + "\n".join([f"- {c}" for c in careers])
        st.download_button("추천 목록 다운로드(.txt)", txt_out, file_name=f"{chosen}_careers.txt")
    else:
        st.warning("해당 MBTI에 대한 추천이 없습니다.")

# 추가 안내
# st.sidebar.header("사용법 & 배포")
# st.sidebar.write("1. 이 파일을 streamlit_mbti_careers.py 로 저장하세요.\n2. 로컬에서 실행: `streamlit run streamlit_mbti_careers.py`\n3. Streamlit Cloud에 배포하려면 GitHub에 푸시한 뒤 Streamlit에 연결하세요.")
# st.sidebar.write("필요하면 추천 직업 목록을 편집하거나 더 많은 설명을 추가해 확장할 수 있습니다.")

# st.caption("앱 생성: Streamlit | 간단한 MBTI 기반 진로 추천 예시")
