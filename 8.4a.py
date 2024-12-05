print ("Hà Mạnh Dũng")
print("235752021610006")
import tkinter as tk

window = tk.Tk()

window.title("Cửa sổ đồ họa Tkinter")

window.geometry("400x300")

label = tk.Label(window, text="Chào mừng bạn đến với Tkinter!", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(window, text="Nhấn vào đây", font=("Arial", 12))
button.pack(pady=10)
ổ
window.mainloop()
