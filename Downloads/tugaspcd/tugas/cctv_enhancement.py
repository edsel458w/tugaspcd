import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

# fungsi memilih gambar
def load_image():
    global img_path, original_img

    img_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )

    if img_path:
        original_img = cv2.imread(img_path)

        show_image(original_img, panel_original)


# fungsi menampilkan gambar di GUI
def show_image(img, panel):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (350, 250))

    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)

    panel.config(image=img)
    panel.image = img


# fungsi enhancement
def enhance_image():
    global enhanced_img

    if original_img is None:
        return

    # 1. Noise Reduction
    denoise = cv2.GaussianBlur(original_img, (5,5), 0)

    # 2. Convert ke grayscale
    gray = cv2.cvtColor(denoise, cv2.COLOR_BGR2GRAY)

    # 3. Histogram Equalization
    contrast = cv2.equalizeHist(gray)

    # 4. Sharpening
    kernel = np.array([[0,-1,0],
                       [-1,5,-1],
                       [0,-1,0]])

    enhanced_img = cv2.filter2D(contrast, -1, kernel)

    # convert grayscale ke BGR agar bisa tampil
    enhanced_img = cv2.cvtColor(enhanced_img, cv2.COLOR_GRAY2BGR)

    show_image(enhanced_img, panel_result)


# fungsi save gambar
def save_image():

    if enhanced_img is None:
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".jpg",
        filetypes=[("JPEG", "*.jpg")]
    )

    if save_path:
        cv2.imwrite(save_path, enhanced_img)


# GUI setup
root = Tk()
root.title("CCTV Image Enhancement System")
root.geometry("800x500")

original_img = None
enhanced_img = None

# tombol upload
btn_upload = Button(root, text="Upload CCTV Image", command=load_image)
btn_upload.pack(pady=10)

# frame gambar
frame = Frame(root)
frame.pack()

panel_original = Label(frame)
panel_original.pack(side="left", padx=10)

panel_result = Label(frame)
panel_result.pack(side="right", padx=10)

# tombol enhance
btn_enhance = Button(root, text="Enhance Image", command=enhance_image)
btn_enhance.pack(pady=10)

# tombol save
btn_save = Button(root, text="Save Result", command=save_image)
btn_save.pack(pady=10)

root.mainloop()