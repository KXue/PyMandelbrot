import pygame, colorsys, cmath
class Mandelbrot:
    @staticmethod
    def Mandelbrot(size, iterations):
        pixelArray = pygame.PixelArray(pygame.Surface(size))
        width = size[0]
        height = size[1]
        colors = []
        for i in range(iterations):
            v = colorsys.hsv_to_rgb(i/256.0, 1, i/(i+8.0))
            color = pygame.Color(int(v[0]*255), int(v[1]*255), int(v[2]*255))
            colors.append(color)
        for x in range(width):
            for y in range(height):
                real = (x - width / 2.0) * 4.0 / width
                imaginary = (y - height / 2.0) * 4.0 / height
                complexNum = complex(real, imaginary)
                zValue = complexNum
                step = 0
                while(cmath.polar(zValue * zValue)[0] <= 4 and step < iterations):
                    zValue = zValue * zValue + complexNum
                    step += 1
                if step < iterations:
                    pixelArray[x, y] = colors[step]
                else:
                    pixelArray[x, y] = 0x000000
        return pixelArray.surface
