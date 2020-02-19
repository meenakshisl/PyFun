import PyPDF2

def rotate_pdf_by_degree(pdf_in,d,pdf_out) :
    pdf_reader = PyPDF2.PdfFileReader(pdf_in)
    pdf_writer = PyPDF2.PdfFileWriter()
    for page in range(pdf_reader.numPages) :
        pg = pdf_reader.getPage(page)
        pg.rotateClockwise(d)
        pdf_writer.addPage(pg)
    pdf_writer.write(pdf_out)     

if __name__ == "__main__" :
    pdf_in = open('PIPES+Tutorial.pdf','rb')
    pdf_out = open("PIPE-Tut-Fixed.pdf","wb")
    try :
        rotate_pdf_by_degree(pdf_in,90,pdf_out)
        print("Sucess")
    except :
        print("Error")


