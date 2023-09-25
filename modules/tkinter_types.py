# modules import
from _import import *
from commands import *


def entry_image(root):
    entry_photo_frame = tk.Frame(root)
    photo_path_entry = ttk.Combobox(entry_photo_frame)
    browse_button = ttk.Button(entry_photo_frame, text="картинка", command=lambda: browse_file(photo_path_entry))

    photo_path_entry.pack(side='right')
    browse_button.pack(padx=5, pady=5)
    entry_photo_frame.pack()

    buff.photo_path_entry = photo_path_entry


def main(root):
    entry_image(root)
    create_preview_label(root).pack()
    update_preview_image(Image.new('RGB', (400, 400), '#000000'))
