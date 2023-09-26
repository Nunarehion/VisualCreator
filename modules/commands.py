from _import import *


def create_preview_label(root):
    buff.preview_label = tk.Label(root, bg=color.main.black)
    return buff.preview_label


def browse_file(photo_path_entry):
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.gif *.bmp")])
    buff.photo_path_entry['values'] = (*buff.photo_path_entry['values'], FooImage(file_path).name)
    buff.photo_path_entry.current(len(buff.photo_path_entry['values']) - 1)

    update_preview()


def update_preview(x=0, y=0, opacity=255):
    #photo = Image.open(FooImage.get().path).convert('RGBA')
    image = Image.new('RGBA', (400, 400), '#000000')
    image.putalpha(opacity)
    for foo in buff.image_list:
        photo = foo.image
        image.paste(photo, (foo.x, foo.y),photo)
    update_preview_image(image)
    buff.img_x = x
    buff.img_y = y
    buff.opacity = opacity
def update_preview_image(image):
    buff.preview_image = image
    img = ImageTk.PhotoImage(image)
    buff.preview_label.config(image=img)
    buff.preview_label.image = img
