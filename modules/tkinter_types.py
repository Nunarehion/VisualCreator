# modules import
from _import import *
from .commands import *

def entry_image(root):
    '''создание комбобокса для выбора картинок'''
    entry_photo_frame = tk.Frame(root, bg=color.main.black)
    buff.photo_path_entry = ttk.Combobox(entry_photo_frame) #буферизация комбобокса
    browse_button = tk.Button(entry_photo_frame, text="картинка", command=lambda: browse_file(buff.photo_path_entry),**style.button.tools_image_control)

    buff.photo_path_entry.pack(side='right')
    browse_button.pack(padx=5, pady=15)
    entry_photo_frame.pack()



#[Comments]:: Переделать функцию. Функция не должна ничего принимать. Функция должна менять значения текущей картинки из буфера
def image_label_move(x, y):
    buff.new_img_x = buff.img_x + x
    buff.new_img_y = buff.img_y + y
    update_preview(buff.new_img_x, buff.new_img_y)

#[Comments]:: Переделать. Опасити должно менятся у выбранной кароинки из буфера.
def image_opacity_change(val):
    buff.new_opacity = buff.opacity + val
    update_preview(buff.new_img_x, buff.new_img_y, buff.new_opacity) #[...]:: удалить аргументы

#[Comments]:: Переименовать. Имя должно содержать tools и frame. Прописать ретурн. Вернуть фрейм.
def image_control(root):
    '''Блок отвечающий за панель управления текущей картинки'''
    control_panel = tk.Frame(root, bg=color.main.black, bd='10')
    up_button     = tk.Button(control_panel, text='↑', command=lambda: image_label_move(0, -10), **style.button.tools_image_control)
    down_button   = tk.Button(control_panel, text='↓', command=lambda: image_label_move(0, 10),   **style.button.tools_image_control)
    left_button   = tk.Button(control_panel, text='←', command=lambda: image_label_move(-10, 0),  **style.button.tools_image_control)
    right_button  = tk.Button(control_panel, text='→', command=lambda: image_label_move(10, 0),**style.button.tools_image_control)
    opacity_plus  = tk.Button(control_panel, text='+', command=lambda: image_opacity_change(1),  **style.button.tools_image_control)
    opacity_minus = tk.Button(control_panel, text='-', command=lambda: image_opacity_change(-1), **style.button.tools_image_control)

    up_button.pack(side='top')
    down_button.pack(side='bottom')
    opacity_plus.pack(side='right', padx=15)
    opacity_minus.pack(side='left', padx=15)
    left_button.pack(side='left', padx=5, pady=5)
    right_button.pack(side='right', padx=5, pady=5)
    control_panel.pack(side='bottom')


def main(root):
    '''Основная функция отображения элементов'''
    #print(tk.font.families(root))
    #add_fonts.loadfonts()
    entry_image(root) # выбор картинки
    image_control(root) #[метка]// контрольный блок для управления картинкой
    create_preview_label(root).pack() # окно просмотра
    update_preview_image(Image.new('RGB', (400, 400), '#000000')) # для отображения картинки при первом запуске
