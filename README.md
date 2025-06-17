## 🖼️ TinyScreen+ Animation from GIF

Animate a GIF on your TinyScreen+ by converting it into frame-by-frame `.h` files and displaying them as RGB332 pixel data.

---

### 🚀 How It Works

1. **Find or create a GIF**
   Use any short looping animation (ideally 1–3 seconds). Ensure it looks good at low resolutions.

2. **Resize & convert GIF to frames**
   Use this free tool to convert your GIF into individual 96x64 PNG frames:
   👉 [ezgif.com/split](https://ezgif.com/split)

   * Upload your GIF
   * Resize it to:

     * Width: `96`
     * Height: `64`
     * Resize method: `gifsicle`
   * After resizing, click on the **Split** option
   * Split options:

     * Output images in **PNG** format
   * Download the frames as a **zip** file and extract as `images/`

3. **Run the Python script to generate `.h` files**
   Place the PNGs in a folder (e.g., `images/`) and run the conversion script:

   ```bash
   pip install pillow # Install Pillow if not already installed
   python png_to_rgb332_header
   ```

   This generates one `.h` file per frame using RGB332 format for optimal performance.

4. **Include `.h` files in Arduino**
   In your Arduino sketch:

   * Include all the generated `.h` files
   * Add them to an array
   * Loop through them to animate

---

### 🧠 Tips

* Each image must be exactly **96x64 pixels**
* Keep the number of frames reasonable (e.g., 10–30) to stay within memory limits
* RGB332 is 1 byte per pixel (6144 bytes per frame)

---

### 🛠️ Requirements

* TinyScreen+ with TinyScreen OLED
* Arduino IDE + TinyScreen library
* Python 3 + `Pillow` library (`pip install pillow`)

---

### 📁 Example Directory Structure

```
/TinyScreenProject
  /images
    frame_00_delay-0.1s.png
    frame_01_delay-0.1s.png
    ...
  png_to_rgb332_header.py
  /main
    main.ino
    frame_00.h
    frame_01.h
  ...
```

---
