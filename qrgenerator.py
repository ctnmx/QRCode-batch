import argparse
import csv
import segno

def qr_generator(csv_file):
    """
    Read a CSV file as an input and generate QR Code from the links in the file.
    """
    with open(csv_file, newline='') as csvFile:
        csvReader = csv.reader(csvFile)
        next(csvReader)  # Skip header row
        for line in csvReader:
            if len(line) < 2:
                continue
            number, url = line[0].strip(), line[1].strip()
            qrcode = segno.make(url)
            # Adjust the save method to export with transparency and no border
            qrcode.save(f'QR_{number}.svg', scale=20, border=0)
            print(f'QR code for {url} saved as QR-FRA_{number}.svg')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Batch QR Code Generator from CSV file")
    parser.add_argument("-i", "--input", help="CSV file to generate QR code")

    args = parser.parse_args()
    csv_file = args.input

    if csv_file:
        qr_generator(csv_file)
    else:
        print("Please provide a CSV file as input.")
