import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

# ページ設定（スマホ表示に優しい設定）
st.set_page_config(
    page_title="コーススケジューラー",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# カスタムCSS（スマホ向け文字サイズ調整 & padding 調整）
st.markdown("""
<style>
    html, body, [class*="css"] {
        font-size: 18px !important;
    }
    .stTextInput, .stSelectbox {
        font-size: 18px !important;
    }
    .block-container {
        padding: 1rem 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧖‍♀️ ドライヘッドスパ コーススケジューラー")

# コースデータ
courses = {
    "A. 小頭/小顔ドライヘッドスパ（60分）": [
        ("ストレッチ", 10),
        ("首・僧帽筋ほぐし", 15),
        ("ヘッドスパ（左右15分ずつ）", 30),
        ("正面ヘッドスパ", 5),
        ("顔ほぐし", 5),
    ],
    "B. 小頭/小顔ドライヘッドスパ（75分）": [
        ("ストレッチ", 10),
        ("ミミスパ", 5),
        ("首・肩甲骨・腕", 20),
        ("ヘッドスパ（左右15分ずつ）", 30),
        ("正面ヘッドスパ", 5),
        ("顔ほぐし", 5),
    ],
    "C. ディープボディドライケア（60分）": [
        ("右向き", 15),
        ("左向き", 15),
        ("背中", 15),
        ("ヘッド", 15),
    ],
    "D. ディープボディドライケア（75分）": [
        ("右向き", 20),
        ("左向き", 20),
        ("背中", 15),
        ("ヘッド", 20),
    ],
    "E. ディープボディドライケア（105分）": [
        ("右向き", 20),
        ("移動", 1),
        ("左向き", 20),
        ("移動", 2),
        ("足（左右）", 20),
        ("背中", 20),
        ("移動", 3),
        ("ヘッド", 20),
    ],
}

# コース選択
course_name = st.selectbox("コースを選択してください", list(courses.keys()))

# 現在時刻入力
now = st.time_input("現在の時刻を入力してください", value=datetime.now().time())

# 開始時刻のdatetime変換
start_time = datetime.combine(datetime.today(), now)

# タイムスケジュールの処理と表示
if course_name:
    steps = courses[course_name]
    total_minutes = sum(duration for _, duration in steps)
    end_time = start_time + timedelta(minutes=total_minutes)

    st.subheader("📋 コース情報")
    st.markdown(f"**🕒 合計時間：{total_minutes}分**")
    st.markdown(f"**✅ 終了予定時刻：{end_time.strftime('%H:%M')}**")

    st.markdown("### 🗓️ タイムスケジュール")

    # タイムテーブルをテーブル形式で表示
    schedule_data = []
    current_time = start_time
    for step_name, duration in steps:
        next_time = current_time + timedelta(minutes=duration)
        schedule_data.append({
            "開始": current_time.strftime("%H:%M"),
            "終了": next_time.strftime("%H:%M"),
            "内容": step_name
        })
        current_time = next_time

        import streamlit as st

st.title("Hello, Streamlit!")
st.write("これは最初のStreamlitアプリです✨")
