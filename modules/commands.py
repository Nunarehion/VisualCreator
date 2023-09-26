from _import import *


def create_preview_label(root):
    '''функция создания окна просмотра'''
    buff.preview_label = tk.Label(root, bg=color.main.black) # окно просмотра
    return buff.preview_label


def browse_file(photo_path_entry):
    '''функция выбора картинки из патча'''
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.gif *.bmp")])
    #заливка списка картинок из буфер в combobox
    buff.photo_path_entry['values'] = (*buff.photo_path_entry['values'], FooImage(file_path).name)
    buff.photo_path_entry.current(len(buff.photo_path_entry['values']) - 1)
    update_preview() #обновление [browse_file]

def update_preview():
    '''функция для отображения (прорисовки) картинок на гоавном холсте'''
    #photo = Image.open(FooImage.get().path).convert('RGBA')
    image = Image.new('RGBA', (400, 400), '#000000') # основной холст просмотра (основная картинка просмотра)
    for foo in buff.image_list: # цикл по списку картинок для отображения
        photo = foo.opacity(0.5).image 
        image.paste(photo, (foo.x, foo.y),photo) # вставка картинок в холст
    update_preview_image(image) # обновление картинки в окне просмотра [update_preview]

def update_preview_image(image):
    '''функция для обновления картинки в окне просмотра'''
    #Картинка буферизуется 
    buff.preview_image = image
    img = ImageTk.PhotoImage(image)
    buff.preview_label.config(image=img)
    buff.preview_label.image = img
