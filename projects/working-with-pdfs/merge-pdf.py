import PyPDF2
import sys

inputs = sys.argv[1:]  # Means accept 1 to many params


def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super_omega.pdf')


pdf_merger(inputs)
