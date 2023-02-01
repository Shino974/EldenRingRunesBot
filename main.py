import time
from helpers.win32_helpers import Win32Helpers

class Bot():
    def __init__(self):
        self.elden_ring_window = Win32Helpers.get_window('ELDEN RING™')

    def run_to_point(self):
        if not self.check_window():
            return False
        Win32Helpers.pressAndHold("spacebar", "z")
        time.sleep(6.5)
        Win32Helpers.pressAndHold("spacebar", "q")
        time.sleep(2.0)
        Win32Helpers.release("spacebar", "q")
        time.sleep(0.5)
        Win32Helpers.pressAndHold("spacebar", "z")
        time.sleep(3)
        Win32Helpers.release("spacebar", "z")
        time.sleep(0.5)
        return True

    def refresh_session(self):
        if not self.check_window():
            return False
        Win32Helpers.press("g")
        time.sleep(0.5)
        Win32Helpers.press("f")
        time.sleep(0.5)
        Win32Helpers.press("e")
        time.sleep(0.5)
        Win32Helpers.press("e")
        time.sleep(6)
        return True

    def start_session(self):
        Win32Helpers.click_mouse(1000, 500)

    def do_routine(self):
        if not self.run_to_point(): return False
        if not self.refresh_session(): return False
        return True

    def check_window(self):
        activeWindow = Win32Helpers.get_active_window()
        return activeWindow == self.elden_ring_window

    def main(self):
        i = 0
        self.start_session()
        while self.check_window():
            i += 1008
            print("Argent gagné = " + str(i))
            if not self.do_routine(): break
        print("Azy c'est fini")
        return

if __name__ == '__main__':
    bot = Bot()
    bot.main()