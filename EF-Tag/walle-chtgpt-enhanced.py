from microbit import *
from mbrobot import *


# ===== Sensoren: schwarz == 0 (falls bei euch 1 -> unten invertieren) =====
def left_black():  return irLeft.read_digital() == 0


def right_black(): return irRight.read_digital() == 0


# ===== Motoren (0..100). clamp + TRIM zentral geregelt =====
TRIM = 0  # +: bremst links / pusht rechts; −: umgekehrt


def clamp(v):
    return max(0, min(100, int(v)))


def motors(left_pwm, right_pwm):
    # TRIM anwenden und klemmen
    l = clamp(left_pwm - TRIM)
    r = clamp(right_pwm + TRIM)
    motL.rotate(l)
    motR.rotate(r)


def stop():
    motors(0, 0)


def hard_stop():
    for _ in range(4):
        motors(0, 0);
        delay(15)


# ===== Geometrie / Racing-Tuning =====
TRACK_CM = 3.5  # Mitte-zu-Mitte Radabstand (8.0..9.5 feinjustieren)
MIN_DIAM_CM = 10.0  # kleinster Bahnradius (Ø)
RADIUS_CM = MIN_DIAM_CM / 2.0
RATIO_TIGHT = max(0.0, (RADIUS_CM - TRACK_CM / 2.0) / (RADIUS_CM + TRACK_CM / 2.0))  # ~0.13
RATIO_MED = 0.70  # mittlere Kurve
RATIO_EASY = 0.88  # leichte Kurve

# Grundgeschwindigkeiten (Aussenrad). Start konservativ, dann steigern.
S_FAST_OUT = 45  # Geradeaus-Speed
S_MED_OUT = 45  # mittlere Kurve
S_TIGHT_OUT = 35  # enge Kurve (Aussenrad)

MIN_PWM_INNER = 20  # wenn Innenrad darunter -> Pivot (Innen 0, Aussen Pulse)

# Hysterese & Rampen
DEBOUNCE_MS = 8
SLEW_STEP = 8  # max. PWM-Änderung pro Zyklus

# Kurvenerkennung über Zeit (robuster als reines L/R)
curve_score = 0  # 0..100
CURVE_UP = 12
CURVE_DOWN = 5
TH_MED = 18
TH_TIGHT = 40

# weiche Rampen (Slew)
curL, curR = 0, 0


def apply_slew(tL, tR):
    global curL, curR
    dL = max(-SLEW_STEP, min(SLEW_STEP, int(tL) - curL))
    dR = max(-SLEW_STEP, min(SLEW_STEP, int(tR) - curR))
    curL += dL;
    curR += dR
    motors(curL, curR)


# Pivot-Pulse für ultratiefe Radien
def pivot_pulse(left_turn):
    if left_turn:
        motors(0, S_TIGHT_OUT);
        delay(35)
    else:
        motors(S_TIGHT_OUT, 0);
        delay(35)


# „Last side“ hilft beim Wiederfinden der Linie
last_side = 0  # -1 = links war schwarz, +1 = rechts, 0 = neutral

while True:
    # Debounce
    L1, R1 = left_black(), right_black()
    delay(DEBOUNCE_MS)
    L2, R2 = left_black(), right_black()
    L, R = (L1 and L2), (R1 and R2)

    # Kurven-Score integrieren
    if L ^ R:  # genau eine Seite schwarz -> auf Kante
        curve_score = min(100, curve_score + CURVE_UP)
    else:
        curve_score = max(0, curve_score - CURVE_DOWN)

    if L and R:
        # Kreuzung / dicker Balken -> kurz stabilisieren
        apply_slew(40, 40)
        delay(60);
        hard_stop();
        delay(40)
        last_side = 0

    elif L and not R:
        # Linkskurve – links = innen
        if curve_score >= TH_TIGHT:
            out, ratio = S_TIGHT_OUT, RATIO_TIGHT
        elif curve_score >= TH_MED:
            out, ratio = S_MED_OUT, RATIO_MED
        else:
            out, ratio = S_FAST_OUT, RATIO_EASY

        inner = int(out * ratio)
        if inner < MIN_PWM_INNER:
            pivot_pulse(left_turn=True)
        else:
            apply_slew(inner, out)
        last_side = -1

    elif R and not L:
        # Rechtskurve – rechts = innen
        if curve_score >= TH_TIGHT:
            out, ratio = S_TIGHT_OUT, RATIO_TIGHT
        elif curve_score >= TH_MED:
            out, ratio = S_MED_OUT, RATIO_MED
        else:
            out, ratio = S_FAST_OUT, RATIO_EASY

        inner = int(out * ratio)
        if inner < MIN_PWM_INNER:
            pivot_pulse(left_turn=False)
        else:
            apply_slew(out, inner)
        last_side = +1

    else:
        # Weiss/Weiss -> nach letzter Seite suchen (leicht biasen)
        if last_side < 0:
            apply_slew(S_FAST_OUT * RATIO_EASY, S_FAST_OUT)
        elif last_side > 0:
            apply_slew(S_FAST_OUT, S_FAST_OUT * RATIO_EASY)
        else:
            apply_slew(S_FAST_OUT, S_FAST_OUT)

    delay(10)