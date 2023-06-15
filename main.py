import tkinter as tk

def button_click():
    label.config(text="ボタンがクリックされました！")

# メインウィンドウの作成
window = tk.Tk()

# ラベルの作成と配置
label = tk.Label(window, text="こんにちは、Tkinter！", padx=20, pady=20)
label.pack()

# ボタンの作成と配置
button = tk.Button(window, text="クリックしてください", command=button_click)
button.pack()

# イベントループの開始
window.mainloop()
