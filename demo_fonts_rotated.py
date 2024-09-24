"""ILI9341 demo (fonts rotated)."""
from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI
from xglcd_font import XglcdFont


def test():
    """Test code."""
    # Baud rate of 40000000 seems about the max
    spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(15))
    display = Display(spi, dc=Pin(4), cs=Pin(16), rst=Pin(17))

    print('Loading fonts...')
    print('Loading arcadepix')
    arcadepix = XglcdFont('ArcadePix9x11.c', 9, 11)
    

    # ArcadePix
    font_height = arcadepix.height
    display.draw_text(0, 0,
                      'Portrait', arcadepix,
                      color565(255, 255, 0),
                      landscape=False, rotate_180=False)
    text_width = arcadepix.measure_text('Landscape') 
    display.draw_text(0, display.height - 1,
                      'Landscape', arcadepix,
                      color565(255, 0, 0),
                      landscape=True, rotate_180=False)
    text_width = arcadepix.measure_text('Portrait, Rotate 180')
    display.draw_text(display.width - text_width - 1,
                      display.height - font_height,
                      'Portrait, Rotate 180', arcadepix,
                      color565(255, 0, 255),
                      landscape=False, rotate_180=True)
    text_width = arcadepix.measure_text('Landscape, Rotate 180')
    display.draw_text(display.width - font_height - 1 , text_width,
                      'Landscape, Rotate 180', arcadepix,
                      color565(0, 0, 255),
                      landscape=True, rotate_180=True)
    sleep(5)    

    # Espresso Dolce
      


test()
