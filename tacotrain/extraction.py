"""
beforei ccontinue i must:\
    stop vosk from training while transcribing
        look for cgd comparison
"""

from zipfile import ZipFile
import os

from vosking import scrape

from m3ta import pop, main, show, Directory, File, Address, save


here, this = map(lambda x: Address(x).obj, os.path.split(__file__))
archives = Directory('audiobook_archives')
texts = Directory('audiobook_texts')
books = Directory('audiobooks')


def unzip(file:File):
    with ZipFile(file.path) as arch:
        show(arch.namelist(), 1, 1)
        newdir = os.path.join(books.path, file.title)
        os.makedirs(newdir, exist_ok=True)
        arch.extractall(newdir)
        return newdir



    

def extract():
    while [*archives.files]:
        arch = min(archives.files, key=lambda f: f.size)
        # print(f"Up next:\t{arch.name}")
        # zip = ZipFile(arch.path)
        book = Directory(unzip(arch))
        text_dir = Directory(os.path.join(texts.path, book.name))
        try:
            for file in book.files:
                print(f"Now reading:\t{arch.name}")
                text_path = os.path.join(text_dir.path, file.title+'.txt')
                text = File(text_path).create(scrape(file.path))
            arch.erase()
        except SystemError as e:
            print(f'{e}\n'*30)
            arch.move((archives / 'system_errors').path)
            book.erase()
            text_dir.erase()



if eval(main):
    extract()
    pass