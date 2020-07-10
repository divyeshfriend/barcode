import qrcode

image = qrcode.make("https://www.linkedin.com/in/saurabh-singh-bhadoriya-186629103/")
image.save("linkedinqr.png","PNG")