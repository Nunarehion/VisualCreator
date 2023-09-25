# modules import
from _import import *
from .commands import *


#preview_label_ok = tk.Label()

def entry_image(root):
    entry_photo_frame = tk.Frame(root, bg="#E9E9EB")
    photo_path_entry = ttk.Combobox(entry_photo_frame)
    browse_button = ttk.Button(entry_photo_frame, text="картинка", command=lambda: browse_file(photo_path_entry))

    photo_path_entry.pack(side='right')
    browse_button.pack(padx=5, pady=5)
    entry_photo_frame.pack()

    buff.photo_path_entry = photo_path_entry


def image_label_move(x, y):
    buff.new_img_x = buff.img_x + x
    buff.new_img_y = buff.img_y + y
    update_preview(buff.new_img_x, buff.new_img_y)


def image_opacity_change(val):
    buff.new_opacity = buff.opacity + val
    update_preview(buff.new_img_x, buff.new_img_y, buff.new_opacity)


def image_control(root):
    button_style = ttk.Style()
    button_style.configure('TButton', fieldbackground='#43506c', borderwidth='0', background="#43506c")
    control_panel = tk.Frame(root, bg="#E9E9EB", bd='10')
    up_button = ttk.Button(control_panel, text='↑', command=lambda: image_label_move(0, -1))
    down_button = ttk.Button(control_panel, text='↓', command=lambda: image_label_move(0, 1))
    left_button = ttk.Button(control_panel, text='←', command=lambda: image_label_move(-1, 0))
    right_button = ttk.Button(control_panel, text='→', command=lambda: image_label_move(1, 0))
    opacity_plus = ttk.Button(control_panel, text='+', command=lambda: image_opacity_change(1))
    opacity_minus = ttk.Button(control_panel, text='-', command=lambda: image_opacity_change(-1))
    up_button.pack(side='top')
    down_button.pack(side='bottom')
    opacity_plus.pack(side='right', padx=15)
    opacity_minus.pack(side='left', padx=15)
    left_button.pack(side='left', padx=5, pady=5)
    right_button.pack(side='right', padx=5, pady=5)
    control_panel.pack(side='bottom')


def main(root):
    entry_image(root)
    image_control(root)
    create_preview_label(root).pack()
    update_preview_image(Image.new('RGB', (400, 400), '#000000'))
