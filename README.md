# QR Code Generator

A Python application that generates QR codes from serial numbers stored in a CSV file. The generated QR codes include the serial number text below the QR code image and are saved as inverted (white on black) PNG files.

## Features

- Reads serial numbers from a CSV file
- Generates QR codes for each serial number
- Adds the serial number text below the QR code
- Saves images in inverted color scheme (white QR codes on black background)
- Supports custom fonts (currently uses Arial)
- Creates organized output directory structure

## Requirements

- Python 3.9 or higher
- Poetry (recommended) or pip

## Installation

### Using Poetry (Recommended)

1. Clone the repository:
```bash
git clone <repository-url>
cd qr-maker
```

2. Install dependencies:
```bash
poetry install
```

3. Activate the virtual environment:
```bash
poetry shell
```

### Using pip

1. Clone the repository:
```bash
git clone <repository-url>
cd qr-maker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. **Prepare your data**: Create a CSV file named `serials.csv` in the `data/` directory with a column named "Serial" containing your serial numbers.

   Example `data/serials.csv`:
   ```csv
   Serial
   ABC123
   DEF456
   GHI789
   ```

2. **Run the application**:
```bash
python main.py
```

3. **Find your output**: Generated QR code images will be saved in the `export/` directory with filenames matching the serial numbers (e.g., `ABC123.png`).

## Project Structure

```
qr-maker/
├── main.py              # Main application script
├── pyproject.toml       # Poetry configuration
├── requirements.txt     # pip dependencies
├── README.md           # This file
├── .gitignore          # Git ignore rules
├── data/               # Input CSV files
│   └── serials.csv     # Serial numbers data
├── fonts/              # Font files
│   └── arial.ttf       # Arial font for text rendering
└── export/             # Generated QR code images
```

## Dependencies

- **pandas**: Data manipulation and CSV reading
- **qrcode**: QR code generation
- **Pillow (PIL)**: Image processing and manipulation
- **numpy**: Numerical operations (required by pandas)

## Configuration

The application uses the following default settings:
- QR code version: 1
- Error correction: Low (L)
- Box size: 60 pixels
- Border: 1 box
- Font size: 150 points
- Output format: PNG (inverted colors)

## Customization

To customize the application, you can modify the following parameters in `main.py`:

- Font path: Change `font_path` variable to use a different font
- QR code settings: Modify parameters in the `generate_qr()` function
- Text positioning: Adjust calculations in `add_text_to_image()` function
- Output directory: Change the `output_dir` variable

## License

This project is licensed under the MIT License.

## Author

Grant Johnson <grant.johnson@cloudresponse.co.uk>