import argparse
from pdf2docx import Converter

def main(pdf,docx):

    cv = Converter(pdf, password='')
    cv.convert(docx, start=0, end=None)
    cv.close()

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf", type=str)
    parser.add_argument('--docx', type=str)
    args = parser.parse_args()
    main(args.pdf,args.docx)
