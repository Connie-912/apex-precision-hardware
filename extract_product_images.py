import os
from PIL import Image

# Create images directory
os.makedirs('furniture-hardware-site/images', exist_ok=True)
print("Created images/ directory")

# 1. Process Gas Springs (page_05.webp is a full-page artistic photo)
# We can save it as our main gas spring product image!
# Let's crop it slightly to remove any potential white page edge (e.g. crop 10px from all sides)
img5 = Image.open('furniture-hardware-site/temp_catalog/page_05.webp')
w, h = img5.size
img5_cropped = img5.crop((20, 20, w - 20, h - 20))
# Resize for web (e.g. width 800px)
img5_cropped = img5_cropped.resize((800, int(800 * (img5_cropped.height / img5_cropped.width))), Image.Resampling.LANCZOS)
img5_cropped.save('furniture-hardware-site/images/gas-spring-main.jpg', 'JPEG', quality=90)
print("Extracted gas-spring-main.jpg")

# 2. Process Door Bouncers (page_20.webp has the photo at the top, text at the bottom)
img20 = Image.open('furniture-hardware-site/temp_catalog/page_20.webp')
# Let's crop the actual photo at the top (roughly from y=130 to y=1270, x=110 to x=1390)
# Let's write a robust crop based on coordinates we see in see_image
w, h = img20.size
# Looking at page_20.webp:
# The image box runs horizontally from x=115 to x=1385, and vertically from y=135 to y=1275
img20_cropped = img20.crop((115, 135, 1385, 1275))
img20_cropped = img20_cropped.resize((800, int(800 * (img20_cropped.height / img20_cropped.width))), Image.Resampling.LANCZOS)
img20_cropped.save('furniture-hardware-site/images/bouncer-main.jpg', 'JPEG', quality=90)
print("Extracted bouncer-main.jpg")

# 3. Process Friction Stays (page_24.webp has the mechanical stays on concrete)
img24 = Image.open('furniture-hardware-site/temp_catalog/page_24.webp')
# Looking at page_24.webp, the image box is similar: from x=115 to x=1385, and y=135 to y=1275
img24_cropped = img24.crop((115, 135, 1385, 1275))
img24_cropped = img24_cropped.resize((800, int(800 * (img24_cropped.height / img24_cropped.width))), Image.Resampling.LANCZOS)
img24_cropped.save('furniture-hardware-site/images/friction-stay-main.jpg', 'JPEG', quality=90)
print("Extracted friction-stay-main.jpg")

# 4. Process Hydraulic Dampers (page_25.webp has double buffer dampers on concrete)
img25 = Image.open('furniture-hardware-site/temp_catalog/page_25.webp')
img25_cropped = img25.crop((115, 135, 1385, 1275))
img25_cropped = img25_cropped.resize((800, int(800 * (img25_cropped.height / img25_cropped.width))), Image.Resampling.LANCZOS)
img25_cropped.save('furniture-hardware-site/images/buffer-main.jpg', 'JPEG', quality=90)
print("Extracted buffer-main.jpg")
