import streamlit as st
from datetime import datetime, timedelta, time

# ---------------------
# スタイル設定（ベージュ系）
# ---------------------
st.markdown("""
    <style>
    body {
        background-color: #F5E1C0;
    }
    .main {
        background-color: #F5E1C0;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    table {
        background-color: white;
        border-radius: 8px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------
# コース定義
# ---------------------
courses = {
    "A. 小頭/小顔ドライヘッドスパ（60分）": [
        (10, "ストレッチ"),
        (15, "首・僧帽筋ほぐし"),
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
st.title("🌿 コース別タイムテーブル表示アプリ")
st.markdown("やさしいタッチでスケジュールをすっきり確認")

# 現在時刻（手動変更可）
now = datetime.now()
default_time = time(now.hour, now.minute)
selected_time = st.time_input("現在時刻を選択", default_time)

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
