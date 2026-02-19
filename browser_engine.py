import undetected_chromedriver as uc
import platform
import sys
from config import CHROME_VERSION
class BrowserManager:
    driver_instance = None
    @classmethod
    def get_driver(cls):
        if cls.driver_instance is None:
            options = uc.ChromeOptions()
            options.add_argument("--start-maximized")
            if platform.system() == "Linux":
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
            try:
                cls.driver_instance = uc.Chrome(version_main=CHROME_VERSION, options=options)
            except Exception as e:
                print(f"❌ فشل فتح المتصفح: {e}")
                sys.exit(1)
        return cls.driver_instance
    @classmethod
    def quit_driver(cls):
        if cls.driver_instance:
            cls.driver_instance.quit()
            cls.driver_instance = None