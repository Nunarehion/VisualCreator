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


def update_preview(x=0, y=0, opacity=255):
    photo = Image.open(buff.photo_path_entry.get()).convert('RGBA')
    image = Image.new('RGBA', (400, 400), '#000000')
    image.putalpha(opacity)
    image.paste(photo, (x, y))
    update_preview_image(image)
    buff.img_x = x
    buff.img_y = y
    buff.opacity = opacity


def update_preview_image(image):
    buff.preview_image = image
    img = ImageTk.PhotoImage(image)
    buff.preview_label.config(image=img)
    buff.preview_label.image = img
