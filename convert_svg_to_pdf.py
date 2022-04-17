
import argparse
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
parser = argparse.ArgumentParser(description="Advanced screening always by hash")
parser.add_argument("-f1","--file1",help="the original file,tabulated,make sure do not contain blank line")
parser.add_argument("-f2","--file2",help="the list by which you want to extract from the file")
args = parser.parse_args()
svg_file = args.file1
pdf_file = args.file2
drawing = svg2rlg(svg_file)
renderPDF.drawToFile(drawing, pdf_file)
