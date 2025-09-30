
import qrcode

data = input("Enter data or link: ")
filename = input("Enter file name: ")
qr = qrcode.QRCode(box_size=15, border=5)
qr.add_data(data)
img = qr.make_image(fill="black", back_color="white")
img.save(f"{filename}.png")
print("QR code generated successfully!")
