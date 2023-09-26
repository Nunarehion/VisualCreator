# modules import
from modules import tkinter_types
from modules import pillow_types
from _import import *

# запуск основого приложения

root = tk.Tk()
root["bg"] = color.main.black
root.title("VisualCreator")

# Устанавливаем размер окна по умолчанию
# root.geometry("1000x600")
root.resizable(False, False)

pillow_types.main(root)
tkinter_types.main(root)  # запуск основного приложения

root.mainloop()
