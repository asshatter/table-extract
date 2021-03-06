import sys
import argparse
from table_extractor import extract_tables

parser = argparse.ArgumentParser(
    description="Extract tables from a pre-processed PDF",
    epilog="Example usage: python do_extract.py ~/documents/my_pdf")

parser.add_argument(nargs="?", dest="doc_path",
    default="", type=str,
    help="The path to the desired document. The folder should contain the folders 'png' and 'tesseract'")

arguments = parser.parse_args()

if len(arguments.doc_path) == 0:
    print "Please enter a valid document path"
    sys.exit(1)

extract_tables(arguments.doc_path)
#extract_tables('/Users/john/code/table-extract/test_files/Cap_Dolostones')
