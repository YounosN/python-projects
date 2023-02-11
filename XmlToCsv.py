import csv
import xml.etree.ElementTree as ET
import argparse
import sys
from pathlib import Path

def xml_to_csv(xml_path: str, csv_path: str) -> None:
    """
    Convert an XML file to CSV format.

    Args:
        xml_path: Path to the input XML file.
        csv_path: Path to the output CSV file.
    """
    try:
        # Check if input XML file exists
        if not Path(xml_path).exists():
            sys.exit(f"{xml_path} does not exist.")

        # Check if input XML file is well-formed
        with open(xml_path) as xml_file:
            try:
                ET.fromstring(xml_file.read())
            except ET.ParseError as e:
                sys.exit(f"Error parsing {xml_path}: {e}")

        # Parse input XML file and write to output CSV file
        tree = ET.parse(xml_path)
        root = tree.getroot()

        headers = [child.tag for child in root[0]]
        with open(csv_path, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            for record in root:
                writer.writerow({child.tag: child.text for child in record})

    except FileNotFoundError as e:
        sys.exit(f"Error converting {xml_path} to CSV: {e}")
    except ET.ParseError as e:
        sys.exit(f"Error parsing {xml_path}: {e}")

def main(args):
    """
    Main function to run the script.

    Args:
        args: The command-line arguments passed to the script.
    """
    try:
        xml_path = args.xml_path
        csv_path = Path(args.csv_path).with_suffix(".csv")
        xml_to_csv(xml_path, csv_path)

    except AttributeError:
        sys.exit("Two arguments required: an XML path and a CSV path.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert an XML file to CSV format.")
    parser.add_argument("xml_path", help="Path to the input XML file")
    parser.add_argument("csv_path", help="Path to the output CSV file")
    args = parser.parse_args()
    main(args)
