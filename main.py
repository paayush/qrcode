'''import qrcode
fb_id = "https://www.facebook.com/photo/?fbid=344086437918224&set=a.103390275321176"

#import image
qrcode.make(fb_id).save(ram.png)'''

'''import qrcode

id = "100069506107789"
fb_url = f"https://www.facebook.com/people/Ram.Pariyar/{id}"
qrcode.make(fb_url).save(ram.png)'''

'''import random

for i in range(1,9+1):
    num = random.randint(1,9)
    last_num = id[14]
    last_num = f"{id[0:14]+str[num]}"'''
#qrcode.make(last_num).save(f"{i}.png")

# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode


# String which represents the QR code
s = "https://www.facebook.com/profile.php?id=100069506107789"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 8)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)
