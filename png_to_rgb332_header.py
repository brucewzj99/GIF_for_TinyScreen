import os
from PIL import Image, ImageSequence
import sys

def resize_gif_and_save_frames(gif_path, output_folder, width=96, height=64):
    """Resize a GIF and save each frame as a centered, cropped PNG in output_folder, filling the area."""
    frame_count = 0
    os.makedirs(output_folder, exist_ok=True)
    with Image.open(gif_path) as im:
        for i, frame in enumerate(ImageSequence.Iterator(im)):
            frame = frame.convert("RGBA")
            # Calculate scale to cover
            ratio = max(width / frame.width, height / frame.height)
            new_size = (int(frame.width * ratio), int(frame.height * ratio))
            resized = frame.resize(new_size, Image.LANCZOS)
            # Calculate crop box to center
            left = (resized.width - width) // 2
            top = (resized.height - height) // 2
            right = left + width
            bottom = top + height
            cropped = resized.crop((left, top, right, bottom))
            cropped.save(os.path.join(output_folder, f"frame_{i:02d}.png"))
            frame_count += 1
    print(f"🖼️  {frame_count} frames generated in '{INPUT_FOLDER}'")

def convert_rgb_to_rgb332(r, g, b):
    # Round to nearest available value in each channel
    r = int(round(r / 255 * 7)) << 5  # 3 bits
    g = int(round(g / 255 * 7)) << 2  # 3 bits
    b = int(round(b / 255 * 3))       # 2 bits
    return r | g | b

def generate_header(image_path, output_dir):
    filename = os.path.splitext(os.path.basename(image_path))[0]
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

def convert_all_images(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for file in os.listdir(input_dir):
        if file.lower().endswith(".png"):
            convert_header_path = os.path.join(input_dir, file)
            generate_header(convert_header_path, output_dir)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python png_to_rgb332_header.py <your.gif>")
        sys.exit(1)

    gif_filename = sys.argv[1]

    INPUT_FOLDER = "./image_frames"      # Put PNGs here
    OUTPUT_FOLDER = "./main"   # .h files will be saved here

    resize_gif_and_save_frames(gif_filename, INPUT_FOLDER)  # Resize GIF and save frames

    convert_all_images(INPUT_FOLDER, OUTPUT_FOLDER)
    print(f"✅ Header files output to '{OUTPUT_FOLDER}'")