#installing library module qrcode
import qrcode
#user can enter the url or text 
url=input("Enter the url to generate Qr code : ")

qr=qrcode.make(url)

qr.save('qr.png',scale=8)

print(qr)

