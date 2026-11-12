import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import platform

def open_folder(path):
    """根據作業系統開啟資料夾"""
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":  # macOS
        subprocess.Popen(["open", path])
    else:  # Linux
        subprocess.Popen(["xdg-open", path])

def split_logic():
    file_path = file_entry.get()
    if not file_path or not os.path.exists(file_path):
        messagebox.showerror("錯誤", "請先選擇有效的 TXT 檔案")
        return

    # 設定切割大小 10MB
    chunk_size = 10 * 1024 * 1024 
    output_dir = os.path.join(os.path.dirname(file_path), "Split_Results")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        file_num = 1
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                
                output_filename = f"{base_name}_part{file_num}.txt"
                save_path = os.path.join(output_dir, output_filename)
                
                with open(save_path, 'wb') as out_f:
                    out_f.write(chunk)
                file_num += 1
        
        messagebox.showinfo("成功", f"檔案已成功切分為 {file_num-1} 個區塊！\n儲存於: {output_dir}")
        open_folder(output_dir) # 自動開啟目錄
        
    except Exception as e:
        messagebox.showerror("錯誤", f"處理過程中發生問題: {e}")

def select_file():
    path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, path)

# --- GUI 介面設定 ---
root = tk.Tk()
root.title("TXT 大檔案切割器 (10MB)")
root.geometry("500x200")

tk.Label(root, text="請選擇要切割的 TXT 檔案:", font=("Arial", 10)).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

file_entry = tk.Entry(frame, width=40)
file_entry.pack(side=tk.LEFT, padx=5)

btn_browse = tk.Button(frame, text="瀏覽", command=select_file)
btn_browse.pack(side=tk.LEFT)

btn_run = tk.Button(root, text="開始切割並開啟資料夾", command=split_logic, 
                   bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), height=2, width=25)
btn_run.pack(pady=20)

root.mainloop()