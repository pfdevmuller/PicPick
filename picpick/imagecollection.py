import os

class ImageCollection:

    IMAGE_EXTENSIONS = ['.jpg', '.png']

    def __init__(self, root_path):
        self.root_path = root_path
        self._find_pictures()

    def _find_pictures(self):
        self.pictures = []
        for dir_path, subdirs, files in os.walk(self.root_path):
            for file in files:
                temp, extension = os.path.splitext(file)
                if extension in self.IMAGE_EXTENSIONS:
                    relpath = os.path.relpath(os.path.join(dir_path, file), self.root_path)
                    self.pictures.append(relpath)

