from pathlib import Path

import qrcode

# Ask what to include in the QR code
text = input("Enter text or a website URL: ").strip()

if not text:
    print("Please enter some text or a URL.")
else:
    # Save the image in the same folder as this Python file
    output_file = Path(__file__).with_name("my_qr_code.png")

    qr_image = qrcode.make(text)
    qr_image.save(output_file)

    print(f"QR code created successfully: {output_file.name}")
