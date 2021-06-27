import site, zipfile, os

import librosa
from pydub import AudioSegment

site.addsitedir(r'E:\Projects\Monties\2020\operatingSystem')
# import filesystem2inheritance as fs
from m3ta import show, Directory, File, Address


# origin = Directory(os.getcwd())
here, this = map(lambda x: Address(x).obj, os.path.split(__file__))
audiobooks = Directory(r'audiobooks')

def unzip(path):
    # os.chdir(path)
    file = File(path)
    with zipfile.ZipFile(path) as arch:
        show(arch.namelist(),0,1)
        # arch.extractall(file.title)
    
def extractsmallest():
    os.chdir(audiobooks.path)
    smallest = min(audiobooks.files,key=lambda f: f.size)
    
    name = smallest.title
    # fs.directory(name).delete() if os.path.exists(smallest.title) else None
    print(smallest.name)
    print(smallest.size)
    unzip(smallest.path)
    # smallest.delete()
    os.chdir(here.path)
# song = AudioSegment.from_wav("never_gonna_give_you_up.wav")

if __name__ == '__main__':
    extractsmallest()
    pass