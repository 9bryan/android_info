import toga
import os
import platform
import sys
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

class android_info(toga.App):

    def startup(self):

        main_box = toga.Box(style=Pack(direction=COLUMN))

        os_details_label = toga.Label(
            self.get_os_details(),
            style=Pack(padding=(0, 5))
        )

        os_details_box = toga.Box(style=Pack(direction=ROW, padding=5))
        os_details_box.add(os_details_label)

        main_box.add(os_details_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def get_os_details(widget):
        os_details = \
                "os.name: " + os.name + "\n" + \
                "sys.platform: " + sys.platform + "\n" + \
                "platform.system: " + platform.system() + "\n" + \
                "platform.release: " + platform.release() + "\n" + \
                "platform.processor: " + platform.processor() + "\n" + \
                "platform.node: " + platform.node() + "\n" + \
                "platform.python_version: " + platform.python_version() + "\n" + \
                "platform.release: " + platform.release() + "\n" + \
                "platform.version: " + platform.version() + "\n" + \
                "platform.machine: " + platform.machine() + "\n"
        return os_details

def main():
    return android_info()
