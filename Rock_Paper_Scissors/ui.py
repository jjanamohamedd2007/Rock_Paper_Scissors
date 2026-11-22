
import cv2

BLACK = (20, 20, 25)
WHITE = (255, 255, 255)
GREEN = (0, 255, 100)
RED = (0, 0, 255)
YELLOW = (0, 255, 255)
BLUE = (255, 150, 0)

WIDTH = 900
HEIGHT = 900


def draw_text(img, text, position, size, color, thickness=2):
    cv2.putText(img, text, position,
                cv2.FONT_HERSHEY_SIMPLEX,
                size, color, thickness, cv2.LINE_AA)


def show_start_screen():

    while True:
        img = cv2.UMat(HEIGHT, WIDTH, cv2.CV_8UC3).get()
        img[:] = BLACK

        draw_text(img, "ROCK PAPER SCISSORS",
                  (130, 200), 1.4, YELLOW, 3)

        draw_text(img, "PLAY WITH YOUR HAND",
                  (260, 280), 0.8, WHITE)

        draw_text(img, "FIRST TO 3 WINS",
                  (310, 340), 0.7, GREEN)

        draw_text(img, "SPACE - PLAY",
                  (330, 440), 0.7, WHITE)

        draw_text(img, "Q - EXIT",
                  (370, 490), 0.7, RED)

        cv2.imshow("Rock Paper Scissors", img)

        key = cv2.waitKey(1) & 0xFF

        if key == 32:
            return True

        elif key == ord("q"):
            return False


def draw_game_screen(img, choice, computer, result,
                     player_score, computer_score,
                     countdown, countdown_number,
                     show_go, game_over, game_result):

    h, w = img.shape[:2]

    camera_view = img.copy()

    img[:] = BLACK

    small_camera = cv2.resize(camera_view, (160, 120))

    img[h-140:h-20, 20:180] = small_camera

    cv2.rectangle(
        img,
        (20, h-140),
        (180, h-20),
        WHITE,
        2
    )

    draw_text(img, "ROCK PAPER SCISSORS",
              (int(w*.18), 70), 1, YELLOW, 2)

    draw_text(img, "YOU: " + choice,
              (40, 170), 0.8, GREEN)

    draw_text(img, "ROBOT: " + computer,
              (40, 230), 0.8, BLUE)

    draw_text(img, "RESULT: " + result,
              (40, 290), 0.8, YELLOW)

    x = int(w*.65)

    cv2.rectangle(img, (x, 120), (w-30, 280), WHITE, 2)

    draw_text(img, "SCORE",
              (x+35, 165), 0.8, YELLOW)

    draw_text(img, f"YOU: {player_score}",
              (x+25, 215), 0.7, GREEN)

    draw_text(img, f"ROBOT: {computer_score}",
              (x+25, 255), 0.7, BLUE)

    if countdown:
        draw_text(img, str(max(1, countdown_number)),
                  (int(w*.46), int(h*.48)), 3, YELLOW, 6)

    if show_go:
        draw_text(img, "GO!",
                  (int(w*.42), int(h*.48)), 2, GREEN, 5)

    if game_over:

        cv2.rectangle(img, (200, int(h*.58)),
                      (w-30, int(h*.88)), BLACK, -1)

        cv2.rectangle(img, (200, int(h*.58)),
                      (w-30, int(h*.88)), YELLOW, 3)

        color = GREEN if player_score >= 3 else RED

        draw_text(img, "GAME OVER!",
                  (int(w*.35), int(h*.66)), 1.2, YELLOW, 3)

        draw_text(img, game_result,
                  (int(w*.25), int(h*.74)), 0.7, color, 2)

        draw_text(img, f"FINAL SCORE: {player_score} - {computer_score}",
                  (int(w*.30), int(h*.81)), 0.7, WHITE)

        draw_text(img, "PRESS R TO RESTART",
                  (int(w*.32), int(h*.86)), 0.6, WHITE)

    elif not countdown and not show_go:

        draw_text(img, "PRESS SPACE TO PLAY",
                  (int(w*.35), h-40), 0.6, WHITE)

    return img
