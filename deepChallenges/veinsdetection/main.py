import time
from modules.vein_detection import VeinDetection

def main():
    vd_class = VeinDetection(0)

    # wait for camera to warm up
    time.sleep(1)
    vd_class.run()


if __name__ == "__main__":
    main()
