from graphics import *

def main():
    imgfile = input("Please input the name of a local image file: ")
    win = GraphWin("Image Greyscale", 600, 300)
    img = Image(Point(250, 125), imgfile).draw(win)
    win.setCoords(0.0, 0.0, img.getWidth(), img.getHeight())
    for x in range (1, img.getWidth()):
        for y in range (1, img.getHeight()):
            rgb = img.getPixel(x, y)
            brightness = int(round(0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2])) #b) #(rgb[0] + rgb[1] + rgb[2])/3
            newcolor = color_rgb(brightness, brightness, brightness)
            img.setPixel(x, y, newcolor)

    filename = 'grey' + imgfile
    img.save(filename)
    x = win.getMouse()

main()