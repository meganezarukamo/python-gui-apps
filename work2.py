import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def convert_to_wareki():  # 関数の定義 ※ボタンが押されたときの動き
    seireki = int(entry1.get())  # 入力値を取得
    # 1868-明治
    # 1912-大正
    # 1926-昭和
    # 1989-平成
    # 2019-令和
    if seireki < 1912:
        gengo = "明治"
        wareki = seireki - 1868 + 1
    elif seireki < 1926:
        gengo = "大正"
        wareki = seireki - 1912 + 1
    elif seireki < 1989:
        gengo = "昭和"
        wareki = seireki - 1926 + 1
    elif seireki < 2019:
        gengo = "平成"
        wareki = seireki - 1989 + 1
    else:
        gengo = "令和"
        wareki = seireki - 2019 + 1

    label1.config(text=f"{gengo} {wareki} 年")  # 画面に出力


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="変換", command=convert_to_wareki)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
