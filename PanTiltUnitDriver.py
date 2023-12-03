import serial
import time


# TS5000 ! Tilt speed cannot exceed 4002 pos/sec
# tp900 ! Maximum allowable Tilt position is 601
# tp-1900 ! Minimum allowable Tilt position is -903
# pp-1760 (valor medio)
# PS700 ! Pan speed cannot exceed 600 pos/sec
# pp4000 ! Maximum allowable Pan position is 3091
# pp-4000 ! Minimum allowable Pan position is -3090

# ser.readline()

class PanTiltUnitDriver:
    # Pan position
    pan: int
    # Tilt position
    tilt: int
    # Pan speed (pos/sec)
    pan_speed: int
    # Tilt speed (pos/sec)
    tilt_speed: int

    def __init__(self):
        # Serial
        self.s: serial.Serial = serial.Serial('/dev/ttyUSB0', 38400)
        # initial position
        self.init_pos: tuple = (-1760, 0)
        # Verbosity
        self.v: bool = True
        # Read current status
        self.read_current_status()

    def read_current_status(self):
        self.read_current_position()
        self.read_current_speed()

    def read_current_position(self):
        # Write commands
        self.s.write(b'pp ')
        self.s.write(b'tp ')
        # Read responses
        response_pp: str = self.s.readline().decode().strip()
        self.pan = int(response_pp.split()[-1])
        response_tp: str = self.s.readline().decode().strip()
        self.tilt = int(response_tp.strip().split()[-1])
        self.v and print(f'Pan: {self.pan}, Tilt: {self.tilt}')

    def read_current_speed(self):
        # Write commands
        self.s.write(b'ps ')
        self.s.write(b'ts ')
        # Read responses
        response_ps: str = self.s.readline().decode().strip()
        self.pan_speed = int(response_ps.strip().split()[-2])
        response_ts: str = self.s.readline().decode().strip()
        self.tilt_speed = int(response_ts.strip().split()[-2])
        self.v and print(f'Pan speed: {self.pan_speed}, Tilt speed: {self.tilt_speed}')

    def _pan_goto(self, pan: int) -> float:
        com: bytes = f'pp{pan} '.encode()
        self.s.write(com)
        to_move: int = abs(pan - self.pan)
        self.pan = pan
        return to_move / self.pan_speed

    # Panoramic movement (Panoramico)
    def _pan_move(self, pan: int) -> float:
        return self._pan_goto(self.pan + pan)

    # Tilt movement (Inclinacion)
    def _tilt_goto(self, tilt: int) -> float:
        com: bytes = f'tp{tilt} '.encode()
        self.s.write(com)
        to_move: int = abs(tilt - self.tilt)
        self.tilt = tilt
        return to_move / self.tilt_speed

    def _tilt_move(self, tilt: int) -> float:
        return self._tilt_goto(self.tilt + tilt)

    def goto(self, pan: int = None, tilt: int = None):
        t: float = 0
        if pan is not None:
            tp = self._pan_goto(pan)
            t = max(t, tp)
        if tilt is not None:
            tt = self._tilt_goto(tilt)
            t = max(t, tt)
        time.sleep(t)

    def move(self, pan: int = 0, tilt: int = 0):
        t: float = 0
        if 0 != pan:
            tp = self._pan_move(pan)
            t = max(t, tp)
        if 0 != tilt:
            tt = self._tilt_move(tilt)
            t = max(t, tt)
        time.sleep(t)

    def goto_init_pos(self):
        self.goto(*self.init_pos)

    def close(self):
        self.s.close()
