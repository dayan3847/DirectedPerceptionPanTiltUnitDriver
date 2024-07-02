import unittest
from src.PanTiltUnitDriver import PanTiltUnitDriver


def move_square(ptu):
    ptu.goto_init_pos()
    # ptu.goto(pan=-ptu.pan)
    # ptu.move(pan=-20)
    # ptu.move(tilt=50)
    square_side: int = 300
    ptu.move(pan=0, tilt=square_side)
    ptu.move(pan=-square_side, tilt=0)
    ptu.move(pan=0, tilt=-2 * square_side)
    ptu.move(pan=2 * square_side, tilt=0)
    ptu.move(pan=0, tilt=2 * square_side)
    ptu.move(pan=-square_side, tilt=0)
    ptu.goto_init_pos()
    ptu.close()


class MoveTest(unittest.TestCase):

    def test_linux_square(self):
        device = '/dev/ttyUSB0'
        ptu = PanTiltUnitDriver(device)
        move_square(ptu)
        self.assertTrue(True)

    def test_macos_square(self):
        device = '/dev/tty.usbserial-10'
        ptu = PanTiltUnitDriver(device)
        move_square(ptu)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
