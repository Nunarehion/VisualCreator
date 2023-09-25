from _import import *

buff = adict()


def create_preview_label(root):
    buff.preview_label = tk.Label(root, bg="Red")
    return buff.preview_label


def browse_file(photo_path_entry):
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.gif *.bmp")])
    buff.photo_path_entry.delete(0, tk.END)
    buff.photo_path_entry.insert(0, file_path)
    update_preview()


def update_preview():
    photo = Image.open(buff.photo_path_entry.get())
    image = Image.new('RGB', (400, 400), '#000000')
    image.paste(photo, (0, 0))

    update_preview_image(image)


def update_preview_image(image):
    buff.preview_image = image
    img = ImageTk.PhotoImage(image)
    buff.preview_label.config(image=img)
    buff.preview_label.image = img
