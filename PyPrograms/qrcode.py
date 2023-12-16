import pyqrcode
import png
from pyqrcode import QRCode

try:
    site = input("Enter a url: ")
    url = pyqrcode.create(site)
    url.png('myqr.png', scale=6)
    print("Downloaded QR code as png.")
except Exception as e:
    print("Ett fel uppstod:", e)
