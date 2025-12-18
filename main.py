import os
import sys

import pandas as pd
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageOps
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeElapsedColumn

console = Console()


def create_directory_structure():
    """Create the necessary directory structure if it doesn't exist."""
    directories = ['./data', './fonts', './export']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def read_data(filepath):
    """Read the CSV data file."""
    if not os.path.isfile(filepath):
        console.print(f"[red bold]Error:[/] File not found: [cyan]{filepath}[/]")
        sys.exit(1)

    return pd.read_csv(filepath)


def generate_qr(data):
    """Generate a QR code image."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=60,
        border=1,
    )
    qr.add_data(data.upper())
    qr.make(fit=True)

    return qr.make_image(fill='black', back_color='white')


def add_text_to_image(img, text, font_path):
    """Add text to an image."""
    img_width, img_height = img.size
    base_height = max(img_height + 180, 720)
    base = Image.new('RGB', (img_width, base_height), 'white')
    base.paste(img, (0, 0))

    d = ImageDraw.Draw(base)
    font = ImageFont.truetype(font_path, 150)

    text_width, text_height = d.textbbox((0, 0), text=text.upper(), font=font)[2:4]
    text_x = (img_width - text_width) / 2
    text_y = img_height + (100 - text_height) / 2

    d.text((text_x, text_y), text, fill=(0, 0, 0), font=font)

    return base


def save_image(img, filename):
    """Invert colors and save an image."""
    inverted_image = ImageOps.invert(img.convert('RGB'))
    inverted_image.save(filename)


def main():
    console.print(Panel.fit(
        "[bold]QR Code Generator[/]\nGenerates QR codes from serial numbers",
        border_style="blue"
    ))

    create_directory_structure()

    data_file = './data/serials.csv'
    font_path = './fonts/arial.ttf'
    output_dir = './export'

    console.print(f"\n[dim]Reading data from[/] [cyan]{data_file}[/]")
    df = read_data(data_file)
    total = len(df)

    console.print(f"[dim]Found[/] [green]{total}[/] [dim]serial numbers to process[/]\n")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Generating QR codes...", total=total)

        for _, row in df.iterrows():
            serial = row['Serial']
            progress.update(task, description=f"[cyan]Processing [bold]{serial}[/bold]")

            img = generate_qr(serial)
            img_with_text = add_text_to_image(img, serial, font_path)
            save_image(img_with_text, f"{output_dir}/{serial}.png")

            progress.advance(task)

    console.print(f"\n[green]✓[/] Successfully generated [bold]{total}[/] QR codes")
    console.print(f"[dim]Output directory:[/] [cyan]{output_dir}[/]")


if __name__ == "__main__":
    main()
