from graphics import *

def main():
    imgfile = input("Please input the name of a local image file: ")
    win = GraphWin("Image Greyscale", 600, 300)
    img = Image(Point(250, 125), imgfile).draw(win)
    win.setCoords(0.0, 0.0, img.getWidth(), img.getHeight())
    for x in range (1, img.getWidth()):
        for y in range (1, img.getHeight()):
            rgb = img.getPixel(x, y)
            newcolor = color_rgb(255-rgb[0], 255-rgb[1], 255-rgb[2])
            img.setPixel(x, y, newcolor)

    filename = 'negative' + imgfile
    img.save(filename)
    x = win.getMouse()

main()