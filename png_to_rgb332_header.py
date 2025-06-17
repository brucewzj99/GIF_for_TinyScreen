import os
from PIL import Image

def convert_rgb_to_rgb332(r, g, b):
    return ((r & 0xE0) | ((g >> 3) & 0x1C) | (b >> 6))

def generate_header(image_path, output_dir):
    filename = os.path.splitext(os.path.basename(image_path))[0]
    filename = filename.replace("_delay-0.1s", "")
    array_name = f"{filename}"
    header_filename = os.path.join(output_dir, f"{filename}.h")

    # Open and convert image
    img = Image.open(image_path).convert("RGB")
    width, height = img.size
    pixels = list(img.getdata())

    # Convert to RGB332 format
    rgb_bytes = [convert_rgb_to_rgb332(r, g, b) for r, g, b in pixels]

    # Write to .h file
    with open(header_filename, 'w') as f:
        f.write(f"#pragma once\n\n")
        f.write(f"const uint8_t {array_name}[] PROGMEM = {{\n")

        for i, byte in enumerate(rgb_bytes):
            if i % width == 0:
                f.write("\n")
            f.write(f"0x{byte:02X}, ")
        f.write("\n};\n")

    print(f"✅ Generated: {header_filename}")

def convert_all_images(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for file in os.listdir(input_dir):
        if file.lower().endswith(".png"):
            convert_header_path = os.path.join(input_dir, file)
            generate_header(convert_header_path, output_dir)

if __name__ == "__main__":
    INPUT_FOLDER = "./images"      # Put PNGs here
    OUTPUT_FOLDER = "./main"   # .h files will be saved here

    convert_all_images(INPUT_FOLDER, OUTPUT_FOLDER)
