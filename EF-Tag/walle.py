from microbit import *
from mbrobot import *

GRUNDGESCHWINDIGKEIT = 15
KURVEN_KORREKTUR = 15
TRIM = 0
AUSSEN_RAD_FAKTOR = 1.25
INNEN_RAD_FAKTOR = 1.00001
INNENKURVE = -1

_hb_next = 0
_hb_state = 0

OUTPIN = pin0
music.set_tempo(ticks=4, bpm=96)
LOOP = [
    "A4:2", "E5:2", "A5:2", "R:2",
    "A5:2", "E5:2", "A5:4", "R:2",
    "E5:2", "F5:2", "G5:2", "A5:2",
    "R:2", "A5:4", "E5:4", "A5:8"
]


# Überprüft den linken Sensor
def left_black():
    return irLeft.read_digital() == 0


# Überprüft den rechten Sensor
def right_black():
    return irRight.read_digital() == 0


# Steuert die Motoren einzeln an
def drive(left_pwm, right_pwm):
    motL.rotate(left_pwm)
    motR.rotate(right_pwm)


# Startet die Musik
def start_music():
    try:
        music.play(LOOP, pin=OUTPIN, wait=False, loop=True)
    except TypeError:
        music.play(LOOP, wait=False, loop=True)


# Stoppt die Musik
def stop_music():
    music.stop()


# Lässt das Herz durch kleiner und grösser werden pulsieren
def heartbeat_step(period_ms=280):
    global _hb_next, _hb_state
    now = running_time()
    if now >= _hb_next:
        display.show(Image.HEART if _hb_state == 0 else Image.HEART_SMALL)
        _hb_state ^= 1
        _hb_next = now + period_ms


start_music()

# Main Loop
while True:
    # Liest die hell & dunkel Werte ein
    L = left_black()
    R = right_black()
    heartbeat_step()
    # Schaut, welcher Fall eingetreten ist.
    if L and R:
        drive(GRUNDGESCHWINDIGKEIT * 1.5, GRUNDGESCHWINDIGKEIT * 1.5)
    elif L and not R:
        drive(max(0, GRUNDGESCHWINDIGKEIT - KURVEN_KORREKTUR * INNEN_RAD_FAKTOR) - TRIM,
              min(100, GRUNDGESCHWINDIGKEIT + KURVEN_KORREKTUR * AUSSEN_RAD_FAKTOR) + TRIM)
        sleep(50)
    elif R and not L:
        drive(min(100, GRUNDGESCHWINDIGKEIT + KURVEN_KORREKTUR * AUSSEN_RAD_FAKTOR) - TRIM,
              max(0, GRUNDGESCHWINDIGKEIT - KURVEN_KORREKTUR * INNEN_RAD_FAKTOR) + TRIM)
        sleep(50)
    else:
        drive(GRUNDGESCHWINDIGKEIT - TRIM, GRUNDGESCHWINDIGKEIT + TRIM)
    delay(10)

stop_music()