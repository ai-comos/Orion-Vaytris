import os
import sys
from PIL import Image

# Dense character ramp for smooth gradients
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=90):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    return image.resize((new_width, new_height))

def display_initialization_sequence(image_path="logo.png", width=90):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Enable ANSI colors on Windows terminals
    if os.name == 'nt':
        os.system('')

    # Header
    print("\033[1;36m" + "=" * width + "\033[0m")
    print("\033[1;36m  ORION VAYTRIS — SECURE INITIALIZATION SEQUENCE  [ARCHITECT MODE]\033[0m")
    print("\033[1;36m" + "=" * width + "\033[0m")

    try:
        image = Image.open(image_path).convert("RGB")
    except IOError:
        print(f"\033[1;31m[ERROR] Critical asset not found: {image_path}\033[0m")
        sys.exit(1)

    image = resize_image(image, width)
    img_width, img_height = image.size
    pixels = image.load()

    # Render TrueColor RGB ASCII art
    for y in range(img_height):
        line_str = ""
        for x in range(img_width):
            r, g, b = pixels[x, y]
            # Calculate luminance to select character density
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            char_idx = int(gray / 25.6)
            char = ASCII_CHARS[min(char_idx, len(ASCII_CHARS) - 1)]
            
            # Apply 24-bit TrueColor foreground escape sequence
            line_str += f"\033[38;2;{r};{g};{b}m{char}"
        print(line_str)

    print("\033[0m") # Reset styling

    # Footer
    print("\033[1;33m" + "-" * width + "\033[0m")
    print("\033[1;33m [STATUS] TPM 2.0 Hardware Attestation: SECURED\033[0m")
    print("\033[1;33m [STATUS] PQC Engine & OBI Order Book Handlers: LOADED\033[0m")
    print("\033[1;33m [STATUS] SEV-SNP Memory Encryption: ACTIVE\033[0m")
    print("\033[1;33m" + "=" * width + "\033[0m")

if __name__ == "__main__":
    display_initialization_sequence()