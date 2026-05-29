"""
personen_klassifizierung_manuell.py

Ein einziges Programm für das Projekt:
1. Fotos mit der Webcam aufnehmen
2. Gesicht automatisch erkennen und ausschneiden
3. Gesicht auf 64x64 skalieren und in Graustufen umwandeln
4. Modell MANUELL trainieren, ohne scikit-learn
5. Testbilder klassifizieren und Trefferquote ausgeben

Verwendetes Modell:
    Multi-Class Perceptron

Das bedeutet:
    - Jede Person/Klasse bekommt eigene Gewichte.
    - Für ein Bild wird für jede Person ein Punktwert berechnet.
    - Die Person mit dem höchsten Punktwert ist die Vorhersage.
    - Wenn die Vorhersage falsch ist, werden die Gewichte angepasst.

Installation:
    pip install opencv-python numpy

Start:
    python personen_klassifizierung_manuell.py
"""

from pathlib import Path
import cv2
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
import time


# ==============================
# Einstellungen
# ==============================

DATASET_DIR = Path("dataset")
BILD_GROESSE = (64, 64)

# Trainingsparameter
LERNRATE = 0.1
DURCHGAENGE = 30

# Gesichtserkennung von OpenCV
FACE_CASCADE = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


# ==============================
# Gesicht erkennen und vorbereiten
# ==============================

def gesicht_ausschneiden_und_vorbereiten(bild):
    """
    Sucht im Bild ein Gesicht.

    Wenn ein Gesicht gefunden wird:
        - nur das Gesicht wird ausgeschnitten
        - in Graustufen umgewandelt
        - auf 64x64 Pixel skaliert

    Rückgabe:
        vorbereitetes Bild als 64x64 Graustufenbild
        oder None, wenn kein Gesicht gefunden wurde
    """

    grau = cv2.cvtColor(bild, cv2.COLOR_BGR2GRAY)

    gesichter = FACE_CASCADE.detectMultiScale(
        grau,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80, 80)
    )

    if len(gesichter) == 0:
        return None

    # Falls mehrere Gesichter erkannt werden, nehmen wir das grösste.
    x, y, w, h = max(gesichter, key=lambda rechteck: rechteck[2] * rechteck[3])

    # Kleiner Rand, damit Stirn/Kinn nicht abgeschnitten werden,
    # aber möglichst wenig Hintergrund enthalten ist.
    rand = int(0.15 * w)

    x1 = max(0, x - rand)
    y1 = max(0, y - rand)
    x2 = min(grau.shape[1], x + w + rand)
    y2 = min(grau.shape[0], y + h + rand)

    gesicht = grau[y1:y2, x1:x2]
    gesicht_64 = cv2.resize(gesicht, BILD_GROESSE)

    return gesicht_64


# ==============================
# Fotos aufnehmen
# ==============================

def fotos_aufnehmen(person_name, split, anzahl):
    zielordner = DATASET_DIR / split / person_name
    zielordner.mkdir(parents=True, exist_ok=True)

    kamera = cv2.VideoCapture(0)

    if not kamera.isOpened():
        print("Fehler: Kamera konnte nicht geöffnet werden.")
        return

    gespeichert = 0

    print()
    print(f"Aufnahme für: {person_name}")
    print(f"Ordner: {zielordner}")
    print("Leertaste = Gesicht speichern")
    print("q = beenden")
    print()

    while gespeichert < anzahl:
        ok, frame = kamera.read()

        if not ok:
            print("Fehler: Kamerabild konnte nicht gelesen werden.")
            break

        anzeige = frame.copy()
        grau = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        gesichter = FACE_CASCADE.detectMultiScale(
            grau,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(80, 80)
        )

        for (x, y, w, h) in gesichter:
            cv2.rectangle(anzeige, (x, y), (x + w, y + h), (0, 255, 0), 2)

        text = f"{person_name} | {split} | {gespeichert}/{anzahl}"
        cv2.putText(
            anzeige,
            text,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("Fotoaufnahme", anzeige)

        taste = cv2.waitKey(1) & 0xFF

        if taste == ord("q"):
            break

        if taste == 32:  # Leertaste
            gesicht = gesicht_ausschneiden_und_vorbereiten(frame)

            if gesicht is None:
                print("Kein Gesicht erkannt. Bild wurde nicht gespeichert.")
                continue

            dateiname = zielordner / f"{person_name}_{gespeichert + 1:03d}.png"
            cv2.imwrite(str(dateiname), gesicht)

            gespeichert += 1
            print(f"Gespeichert: {dateiname}")

    kamera.release()
    cv2.destroyAllWindows()


def datensatz_aufnehmen():
    namen_text = input("Namen der Personen eingeben, getrennt mit Komma: ")
    personen = [name.strip() for name in namen_text.split(",") if name.strip()]

    if not personen:
        print("Keine Namen eingegeben.")
        return

    anzahl_train = int(input("Anzahl Trainingsbilder pro Person, z. B. 10: "))
    anzahl_test = int(input("Anzahl Testbilder pro Person, z. B. 5: "))

    for person in personen:
        fotos_aufnehmen(person, "train", anzahl_train)
        fotos_aufnehmen(person, "test", anzahl_test)

    print()
    print("Aufnahme abgeschlossen.")


# ==============================
# Bilder laden
# ==============================

def lade_bilder(split):
    basisordner = DATASET_DIR / split

    if not basisordner.exists():
        raise FileNotFoundError(f"Ordner nicht gefunden: {basisordner}")

    X = []
    y = []
    dateien = []

    for personenordner in sorted(basisordner.iterdir()):
        if not personenordner.is_dir():
            continue

        person_name = personenordner.name

        for bildpfad in sorted(personenordner.glob("*")):
            if bildpfad.suffix.lower() not in [".jpg", ".jpeg", ".png"]:
                continue

            bild = cv2.imread(str(bildpfad))

            if bild is None:
                print(f"Bild konnte nicht gelesen werden: {bildpfad}")
                continue

            vorbereitet = gesicht_ausschneiden_und_vorbereiten(bild)

            if vorbereitet is None:
                # Falls das Bild bereits beim Aufnehmen als 64x64-Gesicht
                # gespeichert wurde, erkennt OpenCV manchmal kein Gesicht mehr.
                # Dann verwenden wir das Bild direkt.
                grau = cv2.cvtColor(bild, cv2.COLOR_BGR2GRAY)
                vorbereitet = cv2.resize(grau, BILD_GROESSE)

            # Pixelwerte als Vektor mit 4096 Zahlen.
            # Normalisierung auf Werte zwischen 0 und 1.
            pixelwerte = vorbereitet.flatten() / 255.0

            X.append(pixelwerte)
            y.append(person_name)
            dateien.append(str(bildpfad))

    return np.array(X, dtype=float), np.array(y), dateien


# ==============================
# Manuelles Multi-Class Perceptron
# ==============================

def score_berechnen(x, W, b):
    """
    Berechnet für ein Bild x den Punktwert jeder Klasse.

    x: Pixelwerte eines Bildes
    W: Gewichtsmatrix
    b: Bias-Werte

    Rückgabe:
        scores, z. B. [2.1, -0.3, 0.8]
    """

    return np.dot(W, x) + b


def vorhersagen(x, W, b):
    """
    Gibt den Index der Klasse mit dem höchsten Punktwert zurück.
    """

    scores = score_berechnen(x, W, b)
    return int(np.argmax(scores))


def perceptron_trainieren(X_train, y_train):
    """
    Trainiert das Multi-Class Perceptron manuell.

    Kein scikit-learn.
    Keine fertige ML-Library.

    Ablauf:
        1. Klassen bestimmen, z. B. Anna, Max, Lea.
        2. Für jede Klasse Gewichte anlegen.
        3. Jedes Trainingsbild klassifizieren.
        4. Wenn falsch:
            - Gewichte der richtigen Klasse verstärken
            - Gewichte der falschen Klasse abschwächen
    """

    klassen = sorted(set(y_train))
    klassen_index = {klasse: i for i, klasse in enumerate(klassen)}

    anzahl_klassen = len(klassen)
    anzahl_pixel = X_train.shape[1]

    # W hat die Form:
    # Zeilen = Klassen
    # Spalten = Pixel
    W = np.zeros((anzahl_klassen, anzahl_pixel), dtype=float)
    b = np.zeros(anzahl_klassen, dtype=float)

    print()
    print("=== Manuelles Training: Multi-Class Perceptron ===")
    print(f"Klassen: {klassen}")
    print(f"Anzahl Pixel pro Bild: {anzahl_pixel}")
    print()

    for durchgang in range(DURCHGAENGE):
        fehler = 0

        # Reihenfolge zufällig mischen, damit das Training stabiler wird.
        indices = np.arange(len(X_train))
        np.random.shuffle(indices)

        for i in indices:
            x = X_train[i]
            richtige_klasse_name = y_train[i]
            richtige_klasse = klassen_index[richtige_klasse_name]

            vorhergesagte_klasse = vorhersagen(x, W, b)

            if vorhergesagte_klasse != richtige_klasse:
                fehler += 1

                # Richtige Klasse stärker machen
                W[richtige_klasse] = W[richtige_klasse] + LERNRATE * x
                b[richtige_klasse] = b[richtige_klasse] + LERNRATE

                # Falsch vorhergesagte Klasse schwächer machen
                W[vorhergesagte_klasse] = W[vorhergesagte_klasse] - LERNRATE * x
                b[vorhergesagte_klasse] = b[vorhergesagte_klasse] - LERNRATE

        print(f"Durchgang {durchgang + 1}: Fehler = {fehler}")

        if fehler == 0:
            print("Keine Fehler mehr auf den Trainingsdaten.")
            break

    return W, b, klassen


# ==============================
# Sklearn-basierte Modelle
# ==============================

def logistic_regression_trainieren(X_train, y_train):
    """
    Trainiert ein Logistic Regression Modell.
    """
    print("Trainiere Logistic Regression Modell...")
    modell = LogisticRegression(
        max_iter=1000,
        random_state=42,
        multi_class='multinomial',
        solver='lbfgs'
    )
    modell.fit(X_train, y_train)
    return modell


def knn_trainieren(X_train, y_train, k=5):
    """
    Trainiert ein K-Nearest Neighbours Modell.
    """
    print(f"Trainiere K-Nearest Neighbours Modell (k={k})...")
    modell = KNeighborsClassifier(n_neighbors=k)
    modell.fit(X_train, y_train)
    return modell


def svm_trainieren(X_train, y_train):
    """
    Trainiert ein Support Vector Machine Modell.
    """
    print("Trainiere Support Vector Machine Modell...")
    modell = SVC(kernel='rbf', gamma='scale', random_state=42)
    modell.fit(X_train, y_train)
    return modell


def modell_evaluieren(modell, X_test, y_test, modell_name):
    """
    Evaluiert ein Modell auf Testdaten.
    Gibt Genauigkeit und weitere Metriken zurück.
    """

    start_zeit = time.time()
    y_pred = modell.predict(X_test)
    predict_zeit = time.time() - start_zeit

    # Genauigkeit berechnen
    korrekt = np.sum(y_pred == y_test)
    genauigkeit = korrekt / len(y_test)

    return {
        'modell': modell_name,
        'genauigkeit': genauigkeit,
        'korrekt': korrekt,
        'gesamt': len(y_test),
        'predict_zeit': predict_zeit
    }


def zeige_confusion_matrix(y_true, y_pred, klassen, modell_name):
    """
    Berechnet und visualisiert die Confusion Matrix.

    y_true: Tatsächliche Labels
    y_pred: Vorhergesagte Labels
    klassen: Liste der Klassennamen
    modell_name: Name des Modells für den Titel
    """

    # Confusion Matrix berechnen
    cm = confusion_matrix(y_true, y_pred, labels=klassen)

    # Grösse der Figur basierend auf Anzahl Klassen
    figsize = (max(8, len(klassen)), max(6, len(klassen)))

    # Visualisierung
    plt.figure(figsize=figsize)
    sns.heatmap(
        cm,
        annot=True,  # Zahlen anzeigen
        fmt='d',     # Integer Format
        cmap='Blues',
        xticklabels=klassen,
        yticklabels=klassen,
        cbar_kws={'label': 'Anzahl'},
        square=True
    )

    plt.title(f'Confusion Matrix - {modell_name}', fontsize=14, fontweight='bold')
    plt.ylabel('Tatsächlich', fontsize=12)
    plt.xlabel('Vorhergesagt', fontsize=12)
    plt.tight_layout()

    # Fenster anzeigen
    plt.show()

    # Zusätzliche Statistiken berechnen und anzeigen
    print()
    print("=" * 80)
    print("DETAILLIERTE CONFUSION MATRIX ANALYSE")
    print("=" * 80)
    print()
    print(f"Modell: {modell_name}")
    print()
    print("Confusion Matrix (Zeilen=Tatsächlich, Spalten=Vorhergesagt):")
    print()

    # Header mit Klassennamen
    print(" " * 15, end="")
    for klasse in klassen:
        print(f"{klasse:>12}", end="")
    print()
    print("-" * (15 + len(klassen) * 12))

    # Matrix mit Labels
    for i, klasse in enumerate(klassen):
        print(f"{klasse:>14} |", end="")
        for j in range(len(klassen)):
            print(f"{cm[i, j]:>12}", end="")
        print()

    print()
    print("=" * 80)
    print("METRIKEN PRO KLASSE")
    print("=" * 80)
    print()

    # Classification Report
    print(classification_report(y_true, y_pred, target_names=klassen))

    # Gesamtgenauigkeit
    gesamt_genauigkeit = accuracy_score(y_true, y_pred)
    print(f"Gesamt-Genauigkeit: {gesamt_genauigkeit:.2%}")
    print()


def vergleiche_modelle(X_train, y_train, X_test, y_test, test_dateien, y_test_original):
    """
    Trainiert alle drei Modelle und vergleicht sie.
    """

    klassen = sorted(set(y_train))

    print()
    print("=" * 100)
    print("VERGLEICH DER ML-MODELLE")
    print("=" * 100)
    print()

    modelle = {}
    ergebnisse = []

    # 1. Perceptron (Manuell)
    print("1/4: Trainiere Manuelles Perceptron...")
    W, b, _ = perceptron_trainieren(X_train, y_train)

    # Perceptron evaluieren
    y_pred_perceptron = []
    for x in X_test:
        klasse_index = vorhersagen(x, W, b)
        y_pred_perceptron.append(klassen[klasse_index])
    y_pred_perceptron = np.array(y_pred_perceptron)

    korrekt_perceptron = np.sum(y_pred_perceptron == y_test_original)
    genauigkeit_perceptron = korrekt_perceptron / len(y_test)
    ergebnisse.append({
        'modell': 'Perceptron (Manuell)',
        'genauigkeit': genauigkeit_perceptron,
        'korrekt': korrekt_perceptron,
        'gesamt': len(y_test)
    })
    modelle['Perceptron'] = (W, b, klassen)

    # 2. Logistic Regression
    print()
    print("2/4: Trainiere Logistic Regression...")
    modell_lr = logistic_regression_trainieren(X_train, y_train)
    y_pred_lr = modell_lr.predict(X_test)
    korrekt_lr = np.sum(y_pred_lr == y_test_original)
    genauigkeit_lr = korrekt_lr / len(y_test)
    ergebnisse.append({
        'modell': 'Logistic Regression',
        'genauigkeit': genauigkeit_lr,
        'korrekt': korrekt_lr,
        'gesamt': len(y_test)
    })
    modelle['LogisticRegression'] = modell_lr

    # 3. K-Nearest Neighbours
    print()
    print("3/4: Trainiere K-Nearest Neighbours...")
    modell_knn = knn_trainieren(X_train, y_train, k=5)
    y_pred_knn = modell_knn.predict(X_test)
    korrekt_knn = np.sum(y_pred_knn == y_test_original)
    genauigkeit_knn = korrekt_knn / len(y_test)
    ergebnisse.append({
        'modell': 'K-Nearest Neighbours',
        'genauigkeit': genauigkeit_knn,
        'korrekt': korrekt_knn,
        'gesamt': len(y_test)
    })
    modelle['KNN'] = modell_knn

    # 4. Support Vector Machine
    print()
    print("4/4: Trainiere Support Vector Machine...")
    modell_svm = svm_trainieren(X_train, y_train)
    y_pred_svm = modell_svm.predict(X_test)
    korrekt_svm = np.sum(y_pred_svm == y_test_original)
    genauigkeit_svm = korrekt_svm / len(y_test)
    ergebnisse.append({
        'modell': 'Support Vector Machine',
        'genauigkeit': genauigkeit_svm,
        'korrekt': korrekt_svm,
        'gesamt': len(y_test)
    })
    modelle['SVM'] = modell_svm

    # Ergebnisse anzeigen
    print()
    print("=" * 100)
    print("ERGEBNISSE - VERGLEICH")
    print("=" * 100)
    print()
    print(f"{'Modell':<30} {'Korrekt':<15} {'Genauigkeit':<20}")
    print("-" * 100)

    for result in ergebnisse:
        print(f"{result['modell']:<30} {result['korrekt']}/{result['gesamt']:<12} {result['genauigkeit']*100:>6.2f}%")

    print("=" * 100)
    print()

    # Berechne Durchschnittsgenauigkeit
    durchschnitt_genauigkeit = np.mean([r['genauigkeit'] for r in ergebnisse])
    print(f"📊 DURCHSCHNITTLICHE GENAUIGKEIT (über alle Modelle): {durchschnitt_genauigkeit*100:.2f}%")
    print()

    # Bestes Modell finden
    best_result = max(ergebnisse, key=lambda x: x['genauigkeit'])
    print(f"🏆 BESTES MODELL: {best_result['modell']} mit {best_result['genauigkeit']*100:.2f}% Genauigkeit")
    print("=" * 100)
    print()

    # Frage ob Confusion Matrices angezeigt werden sollen
    print()
    zeige_cm = input("Confusion Matrices für alle Modelle anzeigen? (j/n): ").strip().lower()

    if zeige_cm == 'j':
        # Confusion Matrix für Perceptron
        zeige_confusion_matrix(y_test_original, y_pred_perceptron, klassen, "Perceptron (Manuell)")

        # Confusion Matrix für Logistic Regression
        zeige_confusion_matrix(y_test_original, y_pred_lr, klassen, "Logistic Regression")

        # Confusion Matrix für K-Nearest Neighbours
        zeige_confusion_matrix(y_test_original, y_pred_knn, klassen, "K-Nearest Neighbours")

        # Confusion Matrix für Support Vector Machine
        zeige_confusion_matrix(y_test_original, y_pred_svm, klassen, "Support Vector Machine")

    return modelle, ergebnisse


# ==============================
# Echtzeit-Erkennung mit Kamera
# ==============================

def echtzeit_erkennung(W, b, klassen):
    """
    Öffnet die Kamera und erkennt Personen in Echtzeit.

    Drücke 'q' um das Programm zu beenden.
    """

    kamera = cv2.VideoCapture(0)

    if not kamera.isOpened():
        print("Fehler: Kamera konnte nicht geöffnet werden.")
        return

    print()
    print("=== Echtzeit-Personenerkennung ===")
    print("Drücke 'q' zum Beenden")
    print()

    while True:
        ok, frame = kamera.read()

        if not ok:
            print("Fehler: Kamerabild konnte nicht gelesen werden.")
            break

        grau = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gesichter = FACE_CASCADE.detectMultiScale(
            grau,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(80, 80)
        )

        # Wenn Gesichter erkannt werden, klassifiziere sie
        for (x, y, w, h) in gesichter:
            # Gesicht ausschneiden und vorbereiten
            gesicht = grau[y:y+h, x:x+w]
            gesicht_64 = cv2.resize(gesicht, BILD_GROESSE)
            pixelwerte = gesicht_64.flatten() / 255.0

            # Vorhersage treffen
            klasse_index = vorhersagen(pixelwerte, W, b)
            erkannte_person = klassen[klasse_index]

            # Score berechnen für Konfidenz
            scores = score_berechnen(pixelwerte, W, b)
            score = scores[klasse_index]

            # Rechteck um Gesicht zeichnen
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Text mit erkannter Person
            text = f"{erkannte_person} (Score: {score:.2f})"
            cv2.putText(
                frame,
                text,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        # Anleitung anzeigen
        cv2.putText(
            frame,
            "Druecke 'q' zum Beenden",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        cv2.imshow("Personenerkennung", frame)

        taste = cv2.waitKey(1) & 0xFF
        if taste == ord('q'):
            break

    kamera.release()
    cv2.destroyAllWindows()


def modell_laden_und_erkennen():
    """
    Lädt ein trainiertes Modell und startet die Echtzeit-Erkennung.
    """

    print()
    print("Lade Trainingsbilder zum Trainieren des Modells...")
    X_train, y_train, _ = lade_bilder("train")

    if len(X_train) == 0:
        print("Keine Trainingsbilder gefunden. Bitte zuerst Fotos aufnehmen.")
        return

    if len(set(y_train)) < 2:
        print("Es braucht mindestens 2 Personen/Klassen.")
        return

    print("Trainiere Modell...")
    W, b, klassen = perceptron_trainieren(X_train, y_train)

    print()
    print("Modell trainiert. Starte Echtzeit-Erkennung...")
    echtzeit_erkennung(W, b, klassen)


# ==============================
# Trainieren und Testen
# ==============================

def modell_trainieren_und_testen():
    """
    Lädt Trainings- und Testdaten, trainiert das Modell und evaluiert es.
    """

    print()
    print("Lade Trainingsbilder...")
    X_train, y_train, train_dateien = lade_bilder("train")

    print("Lade Testbilder...")
    X_test, y_test, test_dateien = lade_bilder("test")

    print()
    print(f"Trainingsbilder: {len(X_train)}")
    print(f"Testbilder: {len(X_test)}")
    print(f"Personen/Klassen: {sorted(set(y_train))}")

    if len(X_train) == 0 or len(X_test) == 0:
        print("Zu wenige Bilder. Bitte zuerst Fotos aufnehmen.")
        return

    if len(set(y_train)) < 2:
        print("Es braucht mindestens 2 Personen/Klassen.")
        return

    W, b, klassen = perceptron_trainieren(X_train, y_train)

    print()
    print("=" * 90)
    print("Ergebnisse pro Testbild")
    print("=" * 90)

    richtig = 0
    verwechslungen = {}

    for datei, erwartete_klasse in zip(test_dateien, y_test):
        x = X_test[test_dateien.index(datei)]
        klasse_index = vorhersagen(x, W, b)
        erkannte_klasse = klassen[klasse_index]

        if erwartete_klasse == erkannte_klasse:
            status = "RICHTIG"
            richtig += 1
        else:
            status = "FALSCH"
            paar = (erwartete_klasse, erkannte_klasse)
            verwechslungen[paar] = verwechslungen.get(paar, 0) + 1

        print(
            f"{status:7} | erwartet: {erwartete_klasse:12} "
            f"| erkannt: {erkannte_klasse:12} | {datei}"
        )

    genauigkeit = richtig / len(y_test)

    print("=" * 90)
    print(f"Trefferquote: {richtig}/{len(y_test)} = {genauigkeit * 100:.1f}%")
    print("=" * 90)

    print()
    print("Auswertung pro Person:")

    for klasse in klassen:
        gesamt = 0
        korrekt = 0

        for i in range(len(y_test)):
            if y_test[i] == klasse:
                gesamt += 1
                klasse_index = vorhersagen(X_test[i], W, b)
                erkannt = klassen[klasse_index]

                if erkannt == klasse:
                    korrekt += 1

        if gesamt > 0:
            print(f"{klasse}: {korrekt}/{gesamt} richtig = {100 * korrekt / gesamt:.1f}%")
        else:
            print(f"{klasse}: keine Testbilder vorhanden")

    print()
    print("Falsch klassifizierte Gruppen:")

    if not verwechslungen:
        print("Keine falschen Klassifizierungen.")
    else:
        for (erwartet, erkannt), anzahl in verwechslungen.items():
            print(f"{erwartet} wurde {anzahl}x als {erkannt} erkannt.")


# ==============================
# Weitere Bilder hinzufügen
# ==============================

def weitere_bilder_hinzufuegen(split):
    """
    Ermöglicht es, nachträglich weitere Trainings- oder Testbilder hinzuzufügen.

    split: "train" oder "test"
    """

    basisordner = DATASET_DIR / split

    if not basisordner.exists():
        print(f"Ordner {basisordner} existiert nicht. Bitte zuerst Fotos aufnehmen.")
        return

    # Finde alle existierenden Personen
    existierende_personen = [
        ordner.name for ordner in basisordner.iterdir()
        if ordner.is_dir()
    ]

    if not existierende_personen:
        print(f"Keine Personen im {split}-Ordner vorhanden. Bitte zuerst Fotos aufnehmen.")
        return

    print()
    print("Existierende Personen:")
    for i, person in enumerate(sorted(existierende_personen), 1):
        anzahl_bilder = len(list((basisordner / person).glob("*")))
        print(f"{i} = {person} ({anzahl_bilder} Bilder)")
    print(f"{len(existierende_personen) + 1} = Neue Person hinzufügen")
    print()

    auswahl = input("Person auswählen (Nummer eingeben): ").strip()

    try:
        auswahl_index = int(auswahl) - 1
    except ValueError:
        print("Ungültige Eingabe.")
        return

    if auswahl_index == len(existierende_personen):
        # Neue Person
        person_name = input("Name der neuen Person: ").strip()
        if not person_name:
            print("Kein Name eingegeben.")
            return
    elif 0 <= auswahl_index < len(existierende_personen):
        # Existierende Person
        person_name = sorted(existierende_personen)[auswahl_index]
    else:
        print("Ungültige Auswahl.")
        return

    anzahl = int(input(f"Anzahl neuer Bilder (z.B. 5): "))

    fotos_aufnehmen(person_name, split, anzahl)


# ==============================
# Schnelle Test- und Erkennungs-Optionen
# ==============================

def testbilder_testen_schnell():
    """
    Trainiert schnell auf Trainingsbildern und testet dann Testbilder.
    Keine zusätzliche Konfiguration nötig.
    """

    print()
    print("Lade Trainingsbilder...")
    X_train, y_train, train_dateien = lade_bilder("train")

    print("Lade Testbilder...")
    X_test, y_test, test_dateien = lade_bilder("test")

    print()
    print(f"Trainingsbilder: {len(X_train)}")
    print(f"Testbilder: {len(X_test)}")
    print(f"Personen/Klassen: {sorted(set(y_train))}")

    if len(X_train) == 0 or len(X_test) == 0:
        print("Zu wenige Bilder. Bitte zuerst Fotos aufnehmen.")
        return

    if len(set(y_train)) < 2:
        print("Es braucht mindestens 2 Personen/Klassen.")
        return

    print()
    print("Trainiere Modell...")
    W, b, klassen = perceptron_trainieren(X_train, y_train)

    print()
    print("=" * 90)
    print("Ergebnisse pro Testbild")
    print("=" * 90)

    richtig = 0
    verwechslungen = {}

    for datei, erwartete_klasse in zip(test_dateien, y_test):
        x = X_test[test_dateien.index(datei)]
        klasse_index = vorhersagen(x, W, b)
        erkannte_klasse = klassen[klasse_index]

        if erwartete_klasse == erkannte_klasse:
            status = "RICHTIG"
            richtig += 1
        else:
            status = "FALSCH"
            paar = (erwartete_klasse, erkannte_klasse)
            verwechslungen[paar] = verwechslungen.get(paar, 0) + 1

        print(
            f"{status:7} | erwartet: {erwartete_klasse:12} "
            f"| erkannt: {erkannte_klasse:12} | {datei}"
        )

    genauigkeit = richtig / len(y_test)

    print("=" * 90)
    print(f"Trefferquote: {richtig}/{len(y_test)} = {genauigkeit * 100:.1f}%")
    print("=" * 90)

    print()
    print("Auswertung pro Person:")

    for klasse in klassen:
        gesamt = 0
        korrekt = 0

        for i in range(len(y_test)):
            if y_test[i] == klasse:
                gesamt += 1
                klasse_index = vorhersagen(X_test[i], W, b)
                erkannt = klassen[klasse_index]

                if erkannt == klasse:
                    korrekt += 1

        if gesamt > 0:
            print(f"{klasse}: {korrekt}/{gesamt} richtig = {100 * korrekt / gesamt:.1f}%")
        else:
            print(f"{klasse}: keine Testbilder vorhanden")

    print()
    print("Falsch klassifizierte Gruppen:")

    if not verwechslungen:
        print("Keine falschen Klassifizierungen.")
    else:
        for (erwartet, erkannt), anzahl in verwechslungen.items():
            print(f"{erwartet} wurde {anzahl}x als {erkannt} erkannt.")


def live_erkennung_schnell():
    """
    Trainiert schnell auf Trainingsbildern und startet dann Live-Erkennung.
    Keine zusätzliche Konfiguration nötig.
    """

    print()
    print("Lade Trainingsbilder zum Trainieren des Modells...")
    X_train, y_train, _ = lade_bilder("train")

    if len(X_train) == 0:
        print("Keine Trainingsbilder gefunden. Bitte zuerst Fotos aufnehmen.")
        return

    if len(set(y_train)) < 2:
        print("Es braucht mindestens 2 Personen/Klassen.")
        return

    print()
    print("Trainiere Modell...")
    W, b, klassen = perceptron_trainieren(X_train, y_train)

    print()
    print("Modell trainiert. Starte Echtzeit-Erkennung...")
    print()
    echtzeit_erkennung(W, b, klassen)


# ==============================
# Modell-Auswahl und Trainieren
# ==============================

def waehle_modell():
    """
    Menü zur Auswahl des Trainingsmodells.
    """
    print()
    print("==========================================")
    print("Wähle ein Trainingsmodell")
    print("==========================================")
    print("1 = Perceptron (Manuell)")
    print("2 = Logistic Regression")
    print("3 = K-Nearest Neighbours")
    print("4 = Support Vector Machine")
    print("0 = Zurück")
    print()

    auswahl = input("Auswahl: ").strip()
    return auswahl


def trainiere_ausgewaehltes_modell(X_train, y_train, modell_wahl):
    """
    Trainiert das ausgewählte Modell.
    """

    if modell_wahl == "1":
        print()
        print("Trainiere Perceptron (Manuell)...")
        W, b, klassen = perceptron_trainieren(X_train, y_train)
        return ('perceptron', W, b, klassen)

    elif modell_wahl == "2":
        print()
        print("Trainiere Logistic Regression...")
        modell = logistic_regression_trainieren(X_train, y_train)
        return ('lr', modell, None, None)

    elif modell_wahl == "3":
        print()
        print("Trainiere K-Nearest Neighbours...")
        modell = knn_trainieren(X_train, y_train)
        return ('knn', modell, None, None)

    elif modell_wahl == "4":
        print()
        print("Trainiere Support Vector Machine...")
        modell = svm_trainieren(X_train, y_train)
        return ('svm', modell, None, None)

    else:
        return None


def modell_testen_mit_auswahl(X_train, y_train, X_test, y_test, test_dateien, y_test_original):
    """
    Trainiert ein ausgewähltes Modell und testet es.
    """

    modell_wahl = waehle_modell()

    if modell_wahl == "0":
        return

    trainiertes_modell = trainiere_ausgewaehltes_modell(X_train, y_train, modell_wahl)

    if trainiertes_modell is None:
        print("Ungültige Auswahl.")
        return

    modell_type = trainiertes_modell[0]
    klassen = sorted(set(y_train))  # Klassen bestimmen

    print()
    print("=" * 90)
    print("Ergebnisse pro Testbild")
    print("=" * 90)

    richtig = 0
    verwechslungen = {}
    y_pred_all = []

    if modell_type == 'perceptron':
        W, b, klassen = trainiertes_modell[1], trainiertes_modell[2], trainiertes_modell[3]

        for datei, erwartete_klasse in zip(test_dateien, y_test_original):
            x = X_test[test_dateien.index(datei)]
            klasse_index = vorhersagen(x, W, b)
            erkannte_klasse = klassen[klasse_index]
            y_pred_all.append(erkannte_klasse)

            if erwartete_klasse == erkannte_klasse:
                status = "RICHTIG"
                richtig += 1
            else:
                status = "FALSCH"
                paar = (erwartete_klasse, erkannte_klasse)
                verwechslungen[paar] = verwechslungen.get(paar, 0) + 1

            print(
                f"{status:7} | erwartet: {erwartete_klasse:12} "
                f"| erkannt: {erkannte_klasse:12} | {datei}"
            )

    else:
        modell = trainiertes_modell[1]
        y_pred = modell.predict(X_test)
        y_pred_all = list(y_pred)

        for datei, erwartete_klasse, vorhersage in zip(test_dateien, y_test_original, y_pred):
            if vorhersage == erwartete_klasse:
                status = "RICHTIG"
                richtig += 1
            else:
                status = "FALSCH"
                paar = (erwartete_klasse, vorhersage)
                verwechslungen[paar] = verwechslungen.get(paar, 0) + 1

            print(
                f"{status:7} | erwartet: {erwartete_klasse:12} "
                f"| erkannt: {vorhersage:12} | {datei}"
            )

    genauigkeit = richtig / len(y_test)

    print("=" * 90)
    print(f"Trefferquote: {richtig}/{len(y_test)} = {genauigkeit * 100:.1f}%")
    print("=" * 90)

    print()
    print("Falsch klassifizierte Gruppen:")

    if not verwechslungen:
        print("Keine falschen Klassifizierungen.")
    else:
        for (erwartet, erkannt), anzahl in verwechslungen.items():
            print(f"{erwartet} wurde {anzahl}x als {erkannt} erkannt.")

    # Confusion Matrix anzeigen
    print()
    zeige_confusion_matrix(y_test_original, np.array(y_pred_all), klassen,
                           "Perceptron" if modell_type == 'perceptron' else
                           ["Logistic Regression", "K-Nearest Neighbours", "Support Vector Machine"]
                           [["lr", "knn", "svm"].index(modell_type)])


# ==============================
# Hauptmenü
# ==============================

def main():
    while True:
        print()
        print("=" * 50)
        print("PERSONEN-KLASSIFIZIERUNG")
        print("=" * 50)
        print()
        print("  DATENSATZ VORBEREITUNG:")
        print("  1 = Neuen Datensatz aufnehmen")
        print("  2 = Weitere Trainingsbilder hinzufügen")
        print("  3 = Weitere Testbilder hinzufügen")
        print()
        print("  TESTEN & LIVE-ERKENNUNG:")
        print("  4 = Schnell Testbilder testen (Perceptron)")
        print("  5 = Schnell Live-Erkennung starten (Perceptron)")
        print("  6 = Detailliertes Trainieren und Testen (Perceptron)")
        print()
        print("  MODELLAUSWAHL & VERGLEICH:")
        print("  7 = Mit spezifischem Modell trainieren und testen")
        print("  8 = Vergleich aller 4 Modelle")
        print()
        print("  KOMBINIERT:")
        print("  9 = Aufnahmen + sofort trainieren + testen")
        print(" 10 = Aufnahmen + sofort Live-Erkennung")
        print()
        print("  0 = Beenden")
        print()
        print("=" * 50)

        auswahl = input("Auswahl (0-10): ").strip()

        if auswahl == "1":
            datensatz_aufnehmen()

        elif auswahl == "2":
            weitere_bilder_hinzufuegen("train")

        elif auswahl == "3":
            weitere_bilder_hinzufuegen("test")

        elif auswahl == "4":
            testbilder_testen_schnell()

        elif auswahl == "5":
            live_erkennung_schnell()

        elif auswahl == "6":
            modell_trainieren_und_testen()

        elif auswahl == "7":
            # Mit ausgewähltem Modell trainieren und testen
            print()
            print("Lade Trainingsbilder...")
            X_train, y_train, train_dateien = lade_bilder("train")

            print("Lade Testbilder...")
            X_test, y_test, test_dateien = lade_bilder("test")

            print()
            print(f"Trainingsbilder: {len(X_train)}")
            print(f"Testbilder: {len(X_test)}")
            print(f"Personen/Klassen: {sorted(set(y_train))}")

            if len(X_train) == 0 or len(X_test) == 0:
                print("Zu wenige Bilder. Bitte zuerst Fotos aufnehmen.")
            elif len(set(y_train)) < 2:
                print("Es braucht mindestens 2 Personen/Klassen.")
            else:
                modell_testen_mit_auswahl(X_train, y_train, X_test, y_test, test_dateien, y_test)

        elif auswahl == "8":
            # Vergleich aller Modelle
            print()
            print("Lade Trainingsbilder...")
            X_train, y_train, train_dateien = lade_bilder("train")

            print("Lade Testbilder...")
            X_test, y_test, test_dateien = lade_bilder("test")

            print()
            print(f"Trainingsbilder: {len(X_train)}")
            print(f"Testbilder: {len(X_test)}")
            print(f"Personen/Klassen: {sorted(set(y_train))}")

            if len(X_train) == 0 or len(X_test) == 0:
                print("Zu wenige Bilder. Bitte zuerst Fotos aufnehmen.")
            elif len(set(y_train)) < 2:
                print("Es braucht mindestens 2 Personen/Klassen.")
            else:
                vergleiche_modelle(X_train, y_train, X_test, y_test, test_dateien, y_test)

        elif auswahl == "9":
            datensatz_aufnehmen()
            modell_trainieren_und_testen()

        elif auswahl == "10":
            datensatz_aufnehmen()
            modell_laden_und_erkennen()

        elif auswahl == "0":
            print("Programm beendet.")
            break

        else:
            print("Ungültige Auswahl.")


if __name__ == "__main__":
    main()
