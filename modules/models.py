from _import import *

buff = adict(image_list = [])
class FooImage(): # Класс для работы с изображениями
    get = lambda: buff.image_list[buff.photo_path_entry.current()]
    def __init__(self,path=None):
        self.path =  path
        self.image = Image.open(path).convert('RGBA')
        self.name = path.split('/')[-1]
        self.configurate(
            x=0,
            y=0,
            scale = 1,
            _opacity = 1,
        )
        buff.image_list.append(self)

    def configurate(self, **kwargs):
        self.__dict__.update(kwargs) # update the dict with the new Atributes
    def opacity(self, value=1):
        self.image.putalpha(int(value*255))
        return self
    def zoom(self):
        return self.image.resize((int(self.scale * self.image.width),
                                  int(self.scale * self.image.height)))

    def __str__(self):
        return self.name


list = []
get = lambda: Image_Info.list[buff.photo_path_entry.current()]


def __init__(self, path):
    self.name = path.split('/')[-1]
    self.path = path
    self.image = Image.open(path).convert('RGBA')
    self.opacity()
    # self.root = root

    self.crop_x, self.crop_y = 0, 0
    self.crop_width, self.crop_height = 1000, 1000
    self.scale = 1

    Image_Info.list.append(self)


def opacity(self, value=20):
    self.image.putalpha(value)
    return self.image


def zoom(self):
    return self.image.resize((int(self.scale * self.image.width),
                              int(self.scale * self.image.height)))


def __str__(self):
    return self.name