import os, site, pickle, io, wave
from itertools import chain

import vosk, librosa, dill
from pyo import savefile

# site.addsitedir(r'E:\Projects\Monties\2020\operatingSystem')
# import filesystem2inheritance as fs
from m3ta import show, ffplay, load, save, nameSpacer, Directory, File, Address, pop, getsource, convert
    

models = Directory(r'vosk\models')

render = lambda samples, path, sr=44100, channels=1, fileformat=0, sampletype=0, quality=0.4: savefile(samples, path, sr, channels, fileformat, sampletype, quality)


def mono(path:str, dodge:bool=False):
    y, sr = librosa.load(path)
    fy = librosa.to_mono(y)
    
    f = File(path)
    new = os.path.join(f.up.path, f.name)
    new = nameSpacer(new) if dodge else new
    render(fy, new, sr)
    return new

def fix(path:str):
    if File(path).ext.lower() != '.wav':
        print('\n'*10, 10*'converting\n'.upper(), '\n'*10, sep='')
        path = convert(path)
    with wave.open(path,'rb') as wf:
        if (wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE"):
            print('\n'*10, 10*'monoizing\n'.upper(), '\n'*10, sep='')
            path = mono(path, True)
    return path

def scrape(path:str):
    path = fix(path)
    
    # show(models)
    mdl = max(models, key=lambda d:d.size)
    # print(f'CONFIGURING MODEL\n\t{mdl}')
    
    model = vosk.vosk.Model(mdl.path)
    
    print('=' * 50)
    print('\n\n\n')
    print(f'Now Transcribing:\t{path}')
    with wave.open(path,'rb') as wf:
        rec = vosk.KaldiRecognizer(model, wf.getframerate())
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                pass
            else:
                pass
    
    return eval(rec.FinalResult())['text']


if __name__ == '__main__':
    tp = r'F:\Samples\Soundflowering\spleeted\01 We Got Burlingame (feat. Stunna)\vocals.wav'
    tp = r'c:\users\kenneth\pyo_rec.wav'
    audiobooks = Directory('audiobooks')
    tfile = next(audiobooks.gather(ext='mp3'))
    print(tfile)
    n = convert(tfile)
    print(n)
    out = scrape(n)
    print(out)
    os.remove(n)
    # ffplay(mono(tp))
    