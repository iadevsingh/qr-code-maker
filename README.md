# QR Code Maker

A simple beginner-friendly Python program that creates a QR code from text or a website URL.

## Features

- Accepts text or a website URL
- Creates a QR code image
- Saves the image as `my_qr_code.png`
- Checks for empty input

## Requirements

- Python 3
- The `qrcode` package

Install the package from the VS Code terminal:

```bash
python -m pip install "qrcode[pil]"
```

## How to run

Open the terminal in the folder containing `qr_maker.py`, then run:

```bash
python qr_maker.py
```

Enter text or a website URL when prompted. The program saves the QR code as `my_qr_code.png` in the same folder as the script.

## Example

```text
Enter text or a website URL: https://github.com
QR code created successfully: my_qr_code.png
```
