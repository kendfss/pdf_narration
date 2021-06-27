import os,random
import pyttsx3, pyperclip
from PyPDF2 import PdfFileReader as reader

from m3ta import save

# help(slate)
# print(slate.__file__)
# pyperclip.copy(slate.__file__)


def play(page):
    eng = pyttsx3.init()
    eng.say(page)
    eng.runAndWait()

erroneous = \
r"""C:\Users\Kenneth\Documents\library\bostrom-superintelligentwill.pdf
C:\Users\Kenneth\Documents\library\cgt-Openproblems_final_40.pdf
C:\Users\Kenneth\Documents\library\HomotopyType Theory; Univalent Foundations of Mathematics.pdf
C:\Users\Kenneth\Documents\library\EthereumForBeginners.pdf
""".splitlines()

# print(erroneous)
loc = r'C:\Users\Kenneth\Documents\library'
files = tuple(p for i in os.listdir(loc) if i.lower().endswith('.pdf') and not (p:=os.path.join(loc,i)) in erroneous)
fp = random.choice(files)
# print(files)

# fp = r'C:\Users\Kenneth\Documents\library\big_o.pdf'
# fp = r'C:\Users\Kenneth\Documents\library\miller-Combinatorial Group Theory.pdf'
fp = r'C:\Users\Kenneth\Downloads\byextension\pdf\Dr_Faustroll.pdf'
print(fp)
with open(fp,'rb') as f:
    # doc = slate.PDF(f)
    doc = reader(f)
    # doc.close()
    print(doc.numPages)
    pages = tuple(p for i in range(doc.numPages) if 0 < len(p:=doc.getPage(i).extractText()))
    # print(pages[0])
    eng = pyttsx3.init()
    for i,page in enumerate(pages,1):
        # paragraphs = page.split('\n')
        # for paragraph
        lines = page.split('.')
        print(f'Page {i} of {len(pages)}:')
        save(page,os.path.join(r'E:\Projects\Monties\2020\musicTheory\generativeData\brokenFaustrollPages',f'page{i}.pkl'))
        # for j,line in enumerate(lines,1):
            # line = ' '.join(line.split())
            # print(f'\tline {j}:\n\t\t{line}\n\t\t\t{set(line)}')
            # eng.say(line)
            # eng.runAndWait()