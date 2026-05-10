import random
import streamlit as st

st.set_page_config(page_title="랜덤 팀 배정기", page_icon="🎲")

st.title("🎲 랜덤 팀 배정기")
st.write("이름을 입력하면 랜덤으로 균등하게 팀을 나눠줍니다.")

# 이름 입력
names_input = st.text_area(
    "이름 입력 (쉼표로 구분)",
    placeholder="민수, 지훈, 서연, 하준"
)

# 팀 개수 입력
num_teams = st.number_input(
    "몇 팀으로 나눌까요?",
    min_value=1,
    value=2,
    step=1
)

# 버튼
if st.button("팀 나누기"):

    # 이름 정리
    names = [name.strip() for name in names_input.split(",") if name.strip()]

    # 예외 처리
    if len(names) == 0:
        st.warning("이름을 입력해주세요.")

    elif num_teams > len(names):
        st.warning("팀 수가 사람 수보다 많습니다.")

    else:
        # 랜덤 섞기
        random.shuffle(names)

        # 균등 분배 계산
        base_size = len(names) // num_teams
        extra = len(names) % num_teams

        teams = []
        start = 0

        for i in range(num_teams):
            team_size = base_size + (1 if i < extra else 0)
            team = names[start:start + team_size]
            teams.append(team)
            start += team_size

        st.success("팀 배정 완료!")

        # 결과 출력
        for idx, team in enumerate(teams, start=1):
            st.subheader(f"{idx}팀 ({len(team)}명)")
            st.write(", ".join(team))
