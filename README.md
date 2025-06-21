## 🖼️ TinyScreen+ Animation from GIF

Animate a GIF on your TinyScreen+ by converting it into frame-by-frame `.h` files and displaying them as RGB332 pixel data.

---

### 🚀 How It Works

1. **Find or create a GIF**  
   Use any short looping animation (ideally 1–3 seconds). Ensure it looks good at low resolutions.

2. **Run the Python script to generate `.h` files**  
   Just run the script with your GIF as input:

   ```bash
   pip install pillow  # Install dependencies if not already installed
   python png_to_rgb332_header.py your.gif
   ```

   This will:
   - Automatically extract and resize frames to 96x64 (center-cropped to fill, no borders)
   - Convert each frame to RGB332 format with dithering for better color quality
   - Generate one `.h` file per frame in the `/main` folder

3. **Include `.h` files in Arduino**  
   In your Arduino sketch:
   - Include the auto-generated `frames.h` (which includes all frame headers and the frame array)
   - Loop through the frames to animate

---

### 🧠 Tips

* Each image/frame is automatically resized and cropped to **96x64 pixels**
* Keep the number of frames reasonable (e.g., 10–30) to stay within memory limits
* RGB332 is 1 byte per pixel (6144 bytes per frame)
* For best color results, use high-contrast GIFs and preview your animation after conversion

---

### 🛠️ Requirements

* TinyScreen+ with TinyScreen OLED
* Arduino IDE + TinyScreen library
* **Board Selection:** In Arduino IDE, select **TinyZero** as the board (not TinyScreen+)
* Python 3 + `Pillow` libraries (`pip install pillow`)

---

### 📁 Example Directory Structure

```
/TinyScreenProject
  png_to_rgb332_header.py
  /image_frames
    frame_00.png
    frame_01.png
    ...
  /main
    main.ino
    frame_00.h
    frame_01.h
  ...
```

---

### ⚡ Quick Start

1. Place your GIF anywhere, then run:
   ```bash
   python png_to_rgb332_header.py your.gif
   ```
2. Open the `/main/main.ino` sketch in Arduino IDE.
3. Select **TinyZero** as the board.
4. Upload and enjoy your animation! (You might have to adjust the number of frames and frame delay in the sketch)