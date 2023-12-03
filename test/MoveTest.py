import unittest
from src.PanTiltUnitDriver import PanTiltUnitDriver


class MoveTest(unittest.TestCase):
    def test_square(self):
        self.assertTrue(True)

        ptu = PanTiltUnitDriver()
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


if __name__ == '__main__':
    unittest.main()
