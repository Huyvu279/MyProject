
from ili9341 import Display, color565
from machine import Pin, SPI, PWM, time_pulse_us
from micropython import const
import os
from xglcd_font import XglcdFont
import time
import utime
# Khởi tạo màn hình ILI9341
# Khởi tạo các hằng số và cấu hình ban đầu
SCR_WIDTH = const(320)
SCR_HEIGHT = const(240)
SCR_ROT = const(2)
CENTER_Y = int(SCR_WIDTH / 2)
CENTER_X = int(SCR_HEIGHT / 2)
#khoi tao mau
COLOR_RED = color565(255, 0, 0)
COLOR_BLUE = color565(0, 0, 255)
COLOR_GREEN = color565(0, 255, 0)
COLOR_YELLOW = color565(255, 255, 0)
COLOR_PURPLE = color565(128, 0, 128)
COLOR_CYAN = color565(0, 255, 255)
COLOR_MAGENTA = color565(255, 0, 255)
COLOR_ORANGE = color565(255, 165, 0)
COLOR_WHITE = color565(255, 255, 255)
COLOR_LAVENDER = color565(255, 165, 255)
spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(15))
display = Display(spi, dc=Pin(4), cs=Pin(16), rst=Pin(17))
#display.draw_image('TestRaw2.raw',120, 200, 120, 120)
# Thiết lập chân cho cảm biến HC-SR04
trigger = Pin(28, Pin.OUT)
echo = Pin(27, Pin.IN)
# Thiết lập chân điều khiển cho động cơ bước TB6600
PUL_PIN = 20
DIR_PIN = 19
ENA_PIN = 18
pulse = Pin(PUL_PIN, Pin.OUT)
direction = Pin(DIR_PIN, Pin.OUT)
enable = Pin(ENA_PIN, Pin.OUT)

# Cấu hình ban đầu cho TB6600
enable.value(0)  # Kích hoạt TB6600 (0 = kích hoạt, 1 = vô hiệu hóa)
# Tải font chữ
font = XglcdFont('Broadway17x15.c', 17, 15)


def measure_distance():
    # Đảm bảo Trigger ở mức thấp
    trigger.value(0)
    time.sleep_us(2)
    
    # Gửi xung Trigger
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)
    
    # Đo thời gian Echo
    duration = time_pulse_us(echo, 1)
    
    # Tính toán khoảng cách
    distance = (duration / 2) / 29.1  # cm
    
    return distance
# Hàm điều khiển động cơ bước quay 180 độ
def rotate_stepper(degrees):
    steps_per_revolution = 6400  # Giả sử động cơ bước 1.8 độ/bước
    steps = int(steps_per_revolution * (degrees / 360))
    
    direction.value(1)  # Đặt hướng quay (1 = chiều kim đồng hồ)
    
    for _ in range(steps):
        pulse.value(1)
        time.sleep_us(500)
        pulse.value(0)
        time.sleep_us(500)

while True:
    distance = measure_distance()
    current_time = utime.localtime()
    
    # Hiển thị khoảng cách lên màn hình
    display.fill_rectangle(0, 0, SCR_WIDTH, SCR_HEIGHT, color565(0, 0, 0))  # Xóa màn hình
    #display.draw_text(CENTER_X - 40, CENTER_Y + 60, "Distance: {:.2f} cm".format(distance), font, color565(255, 255, 255),landscape=True)
    display.draw_text(CENTER_X - 100, CENTER_Y + 154, "Please raise your hand, patient.", font, color565(255, 255, 255),landscape=True)
    
    display.draw_line(120, 0, 120, 319, COLOR_CYAN)
    display.draw_line(0, 319, 120, 319, COLOR_CYAN)
    display.draw_line(0, 319, 0, 0, COLOR_CYAN)
    display.draw_line(120, 0, 0, 0, COLOR_CYAN)
    text_x = CENTER_X - 80
    text_y = CENTER_Y + 154
    #hien thi anh len man hinh
    display.draw_image('TestRaw21_1.raw',120, 200, 120, 120)
    #hien thi gio len man hinh
    #time_str = "{:02}:{:02}:{:02}".format(current_time[3], current_time[4], current_time[5),
                     
    # Kiểm tra khoảng cách và điều khiển động cơ bước
    if distance < 10:
        rotate_stepper(180)  # Quay 180 độ
        #display.fill_rectangle(text_x, text_y, 50, 120, color565(0, 255, 0))
        display.draw_text(text_x, text_y, "Your medication match! ", font,
                          COLOR_GREEN,
                          landscape=True)
        display.draw_text(text_x + 20, text_y, "Please wait for your medication", font,
                          COLOR_GREEN,
                          landscape=True)
        #display.fill_rectangle(text_x, text_y, 50, 90, color565(0, 255, 0))
        time.sleep(10)  # Hiển thị thông báo trong 2 giây
       
        # Xóa thông báo bằng cách vẽ hình chữ nhật đen đè lên khu vực dòng chữ
        display.clear()
        
    time.sleep(1)