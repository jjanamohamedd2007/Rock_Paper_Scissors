
import cv2

from cvzone.HandTrackingModule import HandDetector
from game_logic import get_choice


cap = cv2.VideoCapture(0)

detector = HandDetector(
    detectionCon=0.8,
    maxHands=1
)


def detect_hand():

    success, img = cap.read()

    if not success:
        return False, None, "Unknown"

    img = cv2.flip(img, 1)
    cv2.rectangle(
    img,
    (200, 0),
    (650, 450),
    (20, 20, 25),
    -1
)

    hands, img = detector.findHands(img)

    if hands:

        hand = hands[0]

        fingers = detector.fingersUp(hand)

        choice = get_choice(fingers)

    else:

        choice = "Unknown"

    return True, img, choice
