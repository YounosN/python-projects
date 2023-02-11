# XML to CSV Converter

This Python script converts an XML file to a CSV file. The script takes the name of the input XML file and the name of the output CSV file as command-line arguments.

## Usage

To use the script, run the following command in the terminal:

'python xml_to_csv.py input.xml output.csv'

Where **input.xml** is the path to the input XML file, and **output.csv** is the path to the output CSV file.

The script will parse the input XML file, and write the output to the CSV file. The first row of the CSV file will contain the headers, which are the tag names of the first element in the XML file. Each subsequent row will contain the values of the corresponding elements in the XML file.


## Requirements

The script requires Python 3.6 or higher, and the following packages:

- csv
- xml.etree.ElementTree
- argparse
- sys
- pathlib

## Limitations

The script can handle XML files of any size, but it reads the entire XML file into memory before converting it to CSV. This may cause the script to run out of memory for very large XML files.

## License

This script is released under the MIT license.