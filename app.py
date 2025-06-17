# 123
import streamlit as st
import random

def number_guessing_game():
    st.set_page_config(
        page_title="数字当てゲーム",
        page_icon="🎲",
        layout="centered"
    )

    st.title("🎲 数字当てゲーム")
    st.write("私が0から100までの数字を心に決めました。当ててみてください！")

    # ゲームの初期設定
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(0, 100)
        st.session_state.guesses = 0
        st.session_state.game_over = False
        st.session_state.message = "さあ、最初の数字を入力してください！"

    # ゲームの状態をリセットする関数
    def reset_game():
        st.session_state.secret_number = random.randint(0, 100)
        st.session_state.guesses = 0
        st.session_state.game_over = False
        st.session_state.message = "新しいゲームが始まりました！"
        st.experimental_rerun()

    # ゲームが終了している場合
    if st.session_state.game_over:
        st.success(st.session_state.message)
        if st.button("もう一度プレイする"):
            reset_game()
        return

    # ユーザー入力
    user_guess = st.number_input("あなたの予想:", min_value=0, max_value=100, value=50, step=1, key="guess_input")

    # 予想を送信するボタン
    if st.button("予想を送信"):
        st.session_state.guesses += 1
        guess = int(user_guess)

        if guess < st.session_state.secret_number:
            st.session_state.message = f"{guess} は小さすぎます！もっと大きな数字です。"
            st.warning(st.session_state.message)
        elif guess > st.session_state.secret_number:
            st.session_state.message = f"{guess} は大きすぎます！もっと小さな数字です。"
            st.warning(st.session_state.message)
        else:
            st.session_state.message = f"🎉 正解です！ {st.session_state.secret_number} が正解でした！\n" \
                                       f"あなたは {st.session_state.guesses} 回で当てました！"
            st.session_state.game_over = True
            st.balloons()

    # 現在のゲーム状況を表示
    if not st.session_state.game_over:
        st.info(f"現在の試行回数: {st.session_state.guesses}回")
        st.write(st.session_state.message)

    st.markdown("---")
    st.write("**ヒント:** 試行回数を少なくして当てられるかな？")

if __name__ == "__main__":
    number_guessing_game()
