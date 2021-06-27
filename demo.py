from pdfreader import PDFDocument, SimplePDFViewer
import pyttsx3

fp = r"C:\Users\Kenneth\Documents\library\bostrom-superintelligentwill.pdf"

with open(fp, "rb") as fd:
    # doc = PDFDocument(fd)
    # print(doc.header)
    # help(doc.header)
    # print(doc.header,doc.root.Outlines.First['Title'],sep='\n',end='\n\n')
    # for page in doc.pages(): print(page)
    # print(doc.pages())
    # print(doc.root.Metadata.Subtype)

    viewer = SimplePDFViewer(fd)
    # print(len(viewer))
    print(viewer.getresources())
    help(viewer)
    
    viewer.render()
    markdown = viewer.canvas.text_content
    # print(markdown)
    print(''.join(viewer.canvas.strings))
    eng = pyttsx3.init()
    eng.say(''.join(viewer.canvas.strings))
    eng.runAndWait()