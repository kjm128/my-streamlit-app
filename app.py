import streamlit as st
import pytz
from datetime import datetime, time, timedelta

# ▼ ここがCSS（スタイル）
st.markdown("""
    <style>
    body {
        background-color: #FFFFFF;
    }
    .main {
        background-color: #FFFFFF;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 4rem;
    }
    table {
        background-color: #FFFDF9 !important;
        color: #5D3A00 !important;
        font-weight: 500;
    }
    th {
        background-color: #F2E8DA !important;
        color: #5D3A00 !important;
    }
    td {
        background-color: #FFFAF0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------
# コース定義
# ---------------------
courses = {
    "A. 小頭/小顔ドライヘッドスパ（60分）": [
        (10, "ストレッチ"),
        (10, "首・僧帽筋ほぐし"),
        (30, "ヘッドスパ（左右15分ずつ）"),
        (5, "正面ヘッドスパ"),
        (5, "顔ほぐし")
    ],
    "B. 小頭/小顔ドライヘッドスパ（75分）": [
        (10, "ストレッチ"),
        (5, "ミミスパ"),
        (20, "首・肩甲骨・腕"),
        (30, "ヘッドスパ（左右15分ずつ）"),
        (5, "正面ヘッドスパ"),
        (5, "顔ほぐし")
    ],
    "C. ディープボディドライケア（60分）": [
        (15, "右向き"),
        (15, "左向き"),
        (15, "背中"),
        (15, "ヘッド")
    ],
    "D. ディープボディドライケア（75分）": [
        (20, "右向き"),
        (20, "左向き"),
        (15, "背中"),
        (20, "ヘッド")
    ],
    "E. ディープボディドライケア（105分）": [
        (20, "右向き"),
        (1, "移動"),
        (20, "左向き"),
        (2, "移動"),
        (20, "足（左右）"),
        (20, "背中"),
        (3, "移動"),
        (20, "ヘッド")
    ]
}

# ---------------------
# UI要素
# ---------------------
st.markdown("""
    <h1 style='
        text-align: center;
        color: #5D3A00;
        font-family: "Segoe UI", "Hiragino Kaku Gothic ProN", Meiryo, sans-serif;
        font-size: 2.5rem;
        letter-spacing: 2px;
        text-shadow: 1px 1px 2px rgba(93, 58, 0, 0.1);
        margin-bottom: 2rem;
    '>
        Dry Head Spa GOKUJO CourseTime
    </h1>
""", unsafe_allow_html=True)


# 日本時間（JST）で現在時刻を取得
jst = pytz.timezone("Asia/Tokyo")
now = datetime.now(jst)
default_time = time(now.hour, now.minute)

# 現在時刻を選択できるように表示
selected_time = st.time_input("現在時刻を選択", default_time)

# --- 時間と分の選択（10:00〜19:00、15分刻み）---
st.markdown("### 🕘 現在時刻を選択")

# 時間選択（10〜19時）
selected_hour = st.selectbox("時", list(range(10, 20)), index=0)

# 分選択（0, 15, 30, 45）
selected_minute = st.selectbox("分", [00,05,10,15,20,25,30,35,40,45,50,55], index=0)

# 選択された時間＋分を datetime.time に変換
selected_time = time(selected_hour, selected_minute)

start_dt = datetime.combine(datetime.today(), selected_time)

col1, col2 = st.columns(2)

with col1:
    selected_hour = st.selectbox("時を選択", list(range(10, 20)), index=0, key="select_hour")

with col2:
    selected_minute = st.selectbox("分を選択", [0, 15, 30, 45], index=0, key="select_minute")

# コース選択
selected_course = st.selectbox("コース一覧", list(courses.keys()))

# ---------------------
# 処理・出力
# ---------------------
if selected_course:
    steps = courses[selected_course]
    start_dt = datetime.combine(datetime.today(), selected_time)
    current_time = start_dt
    timetable = []

    total_duration = sum([min for min, _ in steps])
    end_time = start_dt + timedelta(minutes=total_duration)

    # タイムテーブル生成
    for duration, description in steps:
        step_start = current_time
        step_end = step_start + timedelta(minutes=duration)
        timetable.append({
            "開始時刻": step_start.strftime("%H:%M"),
            "終了時刻": step_end.strftime("%H:%M"),
            "内容": description
        })
        current_time = step_end

    # ---------------------
    # 表示
    # ---------------------
    st.markdown("---")
    st.subheader("📋 コース情報")

    st.write(f"**合計時間：** {total_duration} 分")
    st.write(f"**終了予定時刻：** {end_time.strftime('%H:%M')}")

    st.markdown("---")
    st.subheader("🕒 タイムテーブル")

    st.table(timetable)

# 下に余白を追加
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("<br><br><br>", unsafe_allow_html=True)
