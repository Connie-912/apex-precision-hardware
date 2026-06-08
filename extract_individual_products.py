import os
from PIL import Image

os.makedirs('furniture-hardware-site/images', exist_ok=True)

# 1. Standard Silver Gas Spring (Page 6)
img6 = Image.open('furniture-hardware-site/temp_catalog/page_06.webp')
# Crop the gas spring product render
gas_spring_std = img6.crop((120, 180, 1500, 520))
gas_spring_std = gas_spring_std.resize((600, int(600 * (gas_spring_std.height / gas_spring_std.width))), Image.Resampling.LANCZOS)
gas_spring_std.save('furniture-hardware-site/images/gas-spring-standard.jpg', 'JPEG', quality=90)
print("Extracted gas-spring-standard.jpg")

# 2. Gold/Champagne Gas Spring (Page 7)
img7 = Image.open('furniture-hardware-site/temp_catalog/page_07.webp')
gas_spring_gold = img7.crop((120, 180, 1500, 520))
gas_spring_gold = gas_spring_gold.resize((600, int(600 * (gas_spring_gold.height / gas_spring_gold.width))), Image.Resampling.LANCZOS)
gas_spring_gold.save('furniture-hardware-site/images/gas-spring-gold.jpg', 'JPEG', quality=90)
print("Extracted gas-spring-gold.jpg")

# 3. Matte Black Gas Spring (Page 12)
img12 = Image.open('furniture-hardware-site/temp_catalog/page_12.webp')
gas_spring_black = img12.crop((100, 200, 1520, 560))
gas_spring_black = gas_spring_black.resize((600, int(600 * (gas_spring_black.height / gas_spring_black.width))), Image.Resampling.LANCZOS)
gas_spring_black.save('furniture-hardware-site/images/gas-spring-black.jpg', 'JPEG', quality=90)
print("Extracted gas-spring-black.jpg")

# 4. Standard Cylinder Bouncer (Page 18 - wait, page_18.webp in reading page, which is actually page_18.webp)
# Let's crop model 3001 and 3002 from page_18.webp (which is labeled PAGE / 18, and actually saved as page_18.webp or page_19.webp depending on offset)
# Wait, page_18.webp is shown as bouncers 3001 to 3006 in see_image!
img18 = Image.open('furniture-hardware-site/temp_catalog/page_18.webp')
# Crop 3001 (standard cylinder gray bouncer) at top left
bouncer_3001 = img18.crop((110, 130, 480, 310))
bouncer_3001 = bouncer_3001.resize((400, int(400 * (bouncer_3001.height / bouncer_3001.width))), Image.Resampling.LANCZOS)
bouncer_3001.save('furniture-hardware-site/images/bouncer-cylinder.jpg', 'JPEG', quality=90)

# Crop 3002 (fly bouncer with ears) at top right
bouncer_3002 = img18.crop((520, 130, 890, 310))
bouncer_3002 = bouncer_3002.resize((400, int(400 * (bouncer_3002.height / bouncer_3002.width))), Image.Resampling.LANCZOS)
bouncer_3002.save('furniture-hardware-site/images/bouncer-fly.jpg', 'JPEG', quality=90)
print("Extracted individual bouncers")

# 5. Hanging Codes (Page 20 of interior numbering, which is page_20.webp or page_23.webp depending on offset)
# In see_image, page_23.webp is labeled PAGE / 20, and shows model 4001 and 4002 hanging codes!
img23 = Image.open('furniture-hardware-site/temp_catalog/page_23.webp')
# Crop model 4001 (standard white hanging code) at top left
code_4001 = img23.crop((110, 120, 480, 300))
code_4001 = code_4001.resize((400, int(400 * (code_4001.height / code_4001.width))), Image.Resampling.LANCZOS)
code_4001.save('furniture-hardware-site/images/hanging-code-standard.jpg', 'JPEG', quality=90)

# Crop model 4002 (adjustable steel plate white hanging code) at top right
code_4002 = img23.crop((520, 120, 890, 300))
code_4002 = code_4002.resize((400, int(400 * (code_4002.height / code_4002.width))), Image.Resampling.LANCZOS)
code_4002.save('furniture-hardware-site/images/hanging-code-adjustable.jpg', 'JPEG', quality=90)
print("Extracted individual hanging codes")
