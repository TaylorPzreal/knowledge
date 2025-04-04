from PIL import Image

with Image.open("static/images/shell-operator-description.tiff") as img:
  for i in range(img.n_frames):
    img.seek(i)  # Move to the i-th frame
    img.save(f"output_page_{i+1}.png", "PNG")
