import tkinter as tk
from tkinter import messagebox
import subprocess


# buttonがクリックされたときの処理
def on_clicked_start_dl_button():
    video_url = url_entry.get()
    url_entry.delete(0, tk.END)

    # * ここをユーザが選択するオプションにしたい
    command = [
        "yt-dlp",
        video_url,
        "--embed-thumbnail",
        "--socket-timeout",
        "30",
        "--ignore-errors",
        "-f",
        "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "--output",
        r"movie\%(upload_date)s-%(title)s.%(ext)s",
        "--retries",
        "3"
    ]
    subprocess.run(command, shell=True)

    messagebox.showinfo("ダウンロード完了", "ダウンロードが完了しました！")


# メインウィンドウの作成
window = tk.Tk()
window.title("Youtube動画ダウンローダー")
window.geometry("400x300")

# ラベルの作成と配置
title_label = tk.Label(window, text="DLする動画のURLを貼り付けてください。", padx=20, pady=20)
title_label.pack()

# 入力欄の作成と配置
url_entry = tk.Entry(window, width=50)
url_entry.pack()


# ボタンの作成と配置
start_dl_button = tk.Button(
    window, text="動画をインストールする", command=on_clicked_start_dl_button)
start_dl_button.pack()

# イベントループの開始
window.mainloop()
