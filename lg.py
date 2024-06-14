import socket
import vgamepad
from enum import Enum
from vgamepad import XUSB_BUTTON
import ctypes
import win32api
import win32con
from time import sleep 
import threading
_MapVirtualKey = ctypes.windll.user32.MapVirtualKeyA


class controller():

    def __init__(self) -> None:
        super().__init__()
        self.v360 = vgamepad.VX360Gamepad()
        self.downingKeys = set()
        self.LS_X = 0
        self.LS_Y = 0
        self.RS_X = 0
        self.RS_Y = 0

    def __del__(self) -> None:
        self.releaseAll()

    def releaseAll(self,) -> None:
        self.LS_X = 0
        self.LS_Y = 0
        self.RS_X = 0
        self.RS_Y = 0
        self.setLS(0, 0)
        self.setRS(0, 0)
        self.setRT(0)
        self.setLT(0)
        for k in [x for x in self.downingKeys]:
            self.release(k)

    def press(self, code) -> None:
        self.downingKeys.add(code)
        if isinstance(code, KEY):
            win32api.keybd_event(
                code.value, _MapVirtualKey(code.value, 0), 0, 0)
        elif isinstance(code, MOUSE):
            if code == MOUSE.MOUSE_BTN_LEFT:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            elif code == MOUSE.MOUSE_BTN_RIGHT:
                win32api.mouse_event(
                    win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            elif code == MOUSE.MOUSE_BTN_MIDDLE:
                win32api.mouse_event(
                    win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)
        elif isinstance(code, BTN):
            self.v360.press_button(code.value)
            self.v360.update()
        else:
            raise TypeError(type(code))

    def release(self, code) -> None:
        if code in self.downingKeys:
            self.downingKeys.remove(code)
        if isinstance(code, KEY):
            win32api.keybd_event(code.value, _MapVirtualKey(
                code.value, 0), win32con.KEYEVENTF_KEYUP, 0)
        elif isinstance(code, MOUSE):
            if code == MOUSE.MOUSE_BTN_LEFT:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            elif code == MOUSE.MOUSE_BTN_RIGHT:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
            elif code == MOUSE.MOUSE_BTN_MIDDLE:
                win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)
        elif isinstance(code, BTN):
            self.v360.release_button(code.value)
            self.v360.update()
        else:
            raise TypeError(type(code))

    def click(self, code, ms=50) -> None:
        self.press(code=code)
        sleep(ms/1000)
        self.release(code=code)

    def mouseMove(self, x, y) -> None:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)

    def mouseWheel(self, value) -> None:
        for _ in range(abs(value)):
            if value > 0:
                win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 1, 0)
            else:
                win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -1, 0)

    def setLS(self, x=None, y=None) -> None:  # 浮点类型
        if x != None:
            self.LS_X = x
        if y != None:
            self.LS_Y = y
        self.v360.left_joystick_float(
            x_value_float=self.LS_X, y_value_float=self.LS_Y)
        self.v360.update()

    def setRS(self, x, y) -> None:
        if x != None:
            self.RS_X = x
        if y != None:
            self.RS_Y = y
        self.v360.right_joystick_float(
            x_value_float=self.RS_X, y_value_float=self.RS_Y)
        self.v360.update()

    def setLT(self, value) -> None:
        self.v360.left_trigger_float(value_float=value)
        self.v360.update()

    def setRT(self, value) -> None:
        self.v360.right_trigger_float(value_float=value)
        self.v360.update()


class KEY(Enum):
    KEY_BACKSPACE = 8
    KEY_TAB = 9
    KEY_CLEAR = 12
    KEY_ENTER = 13
    KEY_SHIFT = 16
    KEY_CTRL = 17
    KEY_ALT = 18
    KEY_PAUSE = 19
    KEY_CAPS_LOCK = 20
    KEY_ESC = 27
    KEY_SPACE = 32
    KEY_PAGE_UP = 33
    KEY_PAGE_DOWN = 34
    KEY_END = 35
    KEY_HOME = 36
    KEY_LEFT_ARROW = 37
    KEY_UP_ARROW = 38
    KEY_RIGHT_ARROW = 39
    KEY_DOWN_ARROW = 40
    KEY_SELECT = 41
    KEY_PRINT = 42
    KEY_EXECUTE = 43
    KEY_PRINT_SCREEN = 44
    KEY_INS = 45
    KEY_DEL = 46
    KEY_HELP = 47
    KEY_0 = 48
    KEY_1 = 49
    KEY_2 = 50
    KEY_3 = 51
    KEY_4 = 52
    KEY_5 = 53
    KEY_6 = 54
    KEY_7 = 55
    KEY_8 = 56
    KEY_9 = 57
    KEY_A = 65
    KEY_B = 66
    KEY_C = 67
    KEY_D = 68
    KEY_E = 69
    KEY_F = 70
    KEY_G = 71
    KEY_H = 72
    KEY_I = 73
    KEY_J = 74
    KEY_K = 75
    KEY_L = 76
    KEY_M = 77
    KEY_N = 78
    KEY_O = 79
    KEY_P = 80
    KEY_Q = 81
    KEY_R = 82
    KEY_S = 83
    KEY_T = 84
    KEY_U = 85
    KEY_V = 86
    KEY_W = 87
    KEY_X = 88
    KEY_Y = 89
    KEY_Z = 90
    KEY_LEFT_WINDOWS = 91
    KEY_RIGHT_WINDOWS = 92
    KEY_NUM_0 = 96
    KEY_NUM_1 = 97
    KEY_NUM_2 = 98
    KEY_NUM_3 = 99
    KEY_NUM_4 = 100
    KEY_NUM_5 = 101
    KEY_NUM_6 = 102
    KEY_NUM_7 = 103
    KEY_NUM_8 = 104
    KEY_NUM_9 = 105
    KEY_MULTIPLY = 106
    KEY_ADD = 107
    KEY_SEPARATOR = 108
    KEY_SUBTRACT = 109
    KEY_DIVIDE = 111
    KEY_F1 = 112
    KEY_F2 = 113
    KEY_F3 = 114
    KEY_F4 = 115
    KEY_F5 = 116
    KEY_F6 = 117
    KEY_F7 = 118
    KEY_F8 = 119
    KEY_F9 = 120
    KEY_F10 = 121
    KEY_F11 = 122
    KEY_F12 = 123
    KEY_NUM_LOCK = 144
    KEY_SCROLL_LOCK = 145
    KEY_LEFT_SHIFT = 160
    KEY_RIGHT_SHIFT = 161
    KEY_LEFT_CTRL = 162
    KEY_RIGHT_CTRL = 163


class MOUSE(Enum):
    MOUSE_BTN_LEFT = 0
    MOUSE_BTN_RIGHT = 1
    MOUSE_BTN_MIDDLE = 2


class BTN(Enum):
    BTN_DPAD_UP = XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
    BTN_DPAD_DOWN = XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
    BTN_DPAD_LEFT = XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
    BTN_DPAD_RIGHT = XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT
    BTN_START = XUSB_BUTTON.XUSB_GAMEPAD_START
    BTN_SELECT = XUSB_BUTTON.XUSB_GAMEPAD_BACK
    BTN_LS = XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB
    BTN_RS = XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB
    BTN_LB = XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER
    BTN_RB = XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER
    BTN_MODE = XUSB_BUTTON.XUSB_GAMEPAD_GUIDE
    BTN_A = XUSB_BUTTON.XUSB_GAMEPAD_A
    BTN_B = XUSB_BUTTON.XUSB_GAMEPAD_B
    BTN_X = XUSB_BUTTON.XUSB_GAMEPAD_X
    BTN_Y = XUSB_BUTTON.XUSB_GAMEPAD_Y


c = controller()


def test():
    c.click(BTN.BTN_A)
    c.click(BTN.BTN_A)
    sleep(0.1)
    c.click(BTN.BTN_X)
    sleep(0.2)
    c.click(BTN.BTN_A)

def relicSolid():
    c.click(BTN.BTN_LS)
    sleep(0.02)
    c.click(BTN.BTN_A)
    sleep(0.02)
    c.setRT(1)
    sleep(0.02)
    c.setRT(0)
    sleep(0.02)
    c.click(BTN.BTN_LB)
    sleep(0.02)
    c.click(BTN.BTN_LB)
    sleep(0.02)
    c.click(BTN.BTN_A)
    

def buyJianshang():
    for i in range(1):
        c.mouseMove(-10000,-10000)
        c.mouseMove(400,800)
        sleep(0.02)
        c.click(MOUSE.MOUSE_BTN_LEFT)
        sleep(0.02)
        c.mouseMove(0,100)
        sleep(0.1)
        c.click(MOUSE.MOUSE_BTN_LEFT)
        sleep(3)

def updatePrimeCard():
    for i in range(42  ):
    # for i in range(7 ):
        c.mouseMove(-10000,-10000)
        c.mouseMove(1300,1200)
        sleep(0.2)
        c.click(MOUSE.MOUSE_BTN_LEFT)
        sleep(0.3)
        c.click(KEY.KEY_ENTER)

        c.mouseMove(-10000,-10000)
        c.mouseMove(1300,700)
        sleep(0.5)
        c.click(MOUSE.MOUSE_BTN_LEFT)

        sleep(0.2)
        c.mouseMove(-10000,-10000)
        c.mouseMove(2620,860)

        sleep(0.2)
        for i in range(12):
            c.click(MOUSE.MOUSE_BTN_LEFT,10)
            sleep(0.01)
        
        c.mouseMove(-10000,-10000)
        c.mouseMove(4000    ,750)
        sleep(0.01)
        c.click(MOUSE.MOUSE_BTN_LEFT)
        sleep(0.2)
        c.click(KEY.KEY_ENTER)
        
        sleep(0.8)
        c.click(KEY.KEY_ESC)
        
        sleep(0.8)



funcMap = {
    # 7: test
    # 7: relicSolid
    # 7:buyJianshang
    7:updatePrimeCard
}


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_address = ('', 7779)
    udp_socket.bind(udp_address)
    while True:
        data, _ = udp_socket.recvfrom(1)
        args = int(data[0])
        if args in funcMap.keys():
            threading.Thread(target=funcMap[args]).start()

if __name__ == '__main__':
    main()
