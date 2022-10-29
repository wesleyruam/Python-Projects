from PIL import Image

white = "░"
gray = "▒"
black = "▓"

i = "albert.png"

sc = Image.open('adidas.png').convert("RGB")


largura, altura = sc.width, sc.height

with open("saida.txt", "w") as im:

    for y in range(0, altura, 2):
        for x in range(0, largura, 2):
            r,g,b = sc.getpixel((x, y))[0], sc.getpixel((x, y))[1], sc.getpixel((x, y))[2]

            if r < 50 and g < 50 and b < 50:
                print(white, end="")
                im.write(white)
            elif r > 50 and r < 150 and g > 50 and g < 150 and b > 50 and b < 150:
                print(gray, end="")
                im.write(gray)
            else:
                print(black, end="")
                im.write(black)
        print()
        im.write("\n")




sc.close()


