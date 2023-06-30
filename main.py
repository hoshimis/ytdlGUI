import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import subprocess


def on_clicked_start_dl_button():
    '''DLボタンが押された時の処理'''
    global url_entry, output_dir_entry, radio_option, pulldown_option

    video_url = url_entry.get()
    url_entry.delete(0, tk.END)

    # 出力パスの生成
    output_file_name = r"\%(upload_date)s-%(title)s.%(ext)s"
    output_dir = output_dir_entry.get()
    output_path = output_dir + output_file_name

    # DLコマンドの生成
    command = [
        "yt-dlp",
        video_url,
        "--embed-thumbnail",
        "--socket-timeout",
        "30",
        "--ignore-errors",
        "--output",
        output_path,
        "--retries",
        "3"
    ]

    # プルダウンリストの値によってオプションを変更
    selected_pulldown_list_option = pulldown_option.get()
    if selected_pulldown_list_option == 'オプションなし':
        ext = "m4a"
    else:
        ext = selected_pulldown_list_option

    # ラジオボタンの値によってオプションを変更
    selected_radio_option = radio_option.get()
    if selected_radio_option == '0':
        command.append("-f")
        command.append(
            "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best")
    else:
        command.append("-f")
        command.append(
            "bestaudio[ext=m4a]/bestaudio/best")
        # 音声のみを抽出
        command.append("--extract-audio")
        command.append("--audio-format")
        command.append(ext)

    subprocess.run(command, shell=True)

    messagebox.showinfo("ダウンロード完了", "ダウンロードが完了しました！")


def on_clicked_browse_button():
    '''参照ボタンが押された時の処理'''
    global output_dir_entry

    directory_path = filedialog.askdirectory()
    if directory_path:
        output_dir_entry.delete(0, tk.END)
        output_dir_entry.insert(tk.END, directory_path)


def create_label_entry_frame(parent, label_text, entry_width, padding_x=(0, 0)):
    '''ラベルと入力欄を持つframeを作成する'''
    frame = tk.Frame(parent)
    frame.pack(pady=10)

    label = tk.Label(frame, text=label_text)
    label.grid(row=0, column=0, sticky=tk.W)

    entry = tk.Entry(frame, width=entry_width)
    entry.grid(row=0, column=1, padx=(padding_x[0], padding_x[1]))

    return frame, entry


def update_pulldown_options():
    '''pulldown listのオプションを更新する'''
    global radio_option, pulldown_option, pulldown_menu
    selected_radio_option = radio_option.get()

    # 既存オプションの削除
    pulldown_menu['menu'].delete(0, 'end')

    # movie
    if selected_radio_option == '0':
        pulldown_menu['menu'].add_command(
            label='オプションなし', command=lambda: pulldown_option.set('オプションなし'))
    # audio
    else:
        pulldown_menu['menu'].add_command(
            label='オプションなし', command=lambda: pulldown_option.set('オプションなし'))
        pulldown_menu['menu'].add_command(
            label='m4a', command=lambda: pulldown_option.set('m4a'))
        pulldown_menu['menu'].add_command(
            label='mp3', command=lambda: pulldown_option.set('mp3'))
        pulldown_menu['menu'].add_command(
            label='wav', command=lambda: pulldown_option.set('wav'))


def update_ytdlp():
    '''yt-dlpの更新'''
    subprocess.run("yt-dlp --rm-cache-dir", shell=True)
    subprocess.run("yt-dlp -U --no-check-certificate", shell=True)


def main():
    global url_entry, output_dir_entry, radio_option, pulldown_option, pulldown_menu

    update_ytdlp()

    # メインウィンドウの作成
    window = tk.Tk()
    window.title("Movie Downloader")
    window.geometry("400x230")

    # URL入力欄のframe
    input_url_frame, url_entry = create_label_entry_frame(
        window, "URL:", 50, (0, 42))

    # 保存先入力欄のframe
    output_dir_frame, output_dir_entry = create_label_entry_frame(
        window, "OUT:", 50)

    # 参照ボタン
    browse_button = tk.Button(output_dir_frame, text="参照",
                              command=on_clicked_browse_button)
    browse_button.grid(row=0, column=2, padx=(5, 0))

    # * オプションのframe
    option_frame = tk.Frame(window)
    option_frame.pack(pady=10)

    radio_option = tk.StringVar(value="動画をダウンロードする")

    # radio button
    radio_options = [
        "動画をダウンロードする",
        "音声のみをダウンロードする",
    ]

    for option, option_text in enumerate(radio_options):
        radio_button = tk.Radiobutton(option_frame, text=option_text, variable=radio_option,
                                      value=option, command=update_pulldown_options, anchor=tk.W)
        radio_button.grid(row=option, column=0, sticky=tk.W)

    # pulldown list1
    pulldown_option = tk.StringVar(value="オプションなし")
    pulldown_menu = tk.OptionMenu(option_frame, pulldown_option, "")
    pulldown_menu.grid(row=1, column=1, padx=20)

    # DLボタン
    start_dl_button = tk.Button(
        window, text="ダウンロード", command=on_clicked_start_dl_button)
    start_dl_button.pack(pady=20)

    # イベントループの開始
    window.mainloop()


if __name__ == "__main__":
    main()
