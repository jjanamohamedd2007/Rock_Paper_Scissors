
import time
import cv2
import pygame

from game_logic import computer_choice, find_winner, check_game_over
from hand_tracking import cap, detect_hand
from sounds import play_sound
from ui import draw_game_screen, show_start_screen




computer = ""
result = ""
player_choice = ""

player_score = 0
computer_score = 0

countdown = False
countdown_start = 0
countdown_number = 3

show_go = False
go_start = 0

game_over = False
game_result = ""




try:

    if show_start_screen():

        while True:


            success, img, choice = detect_hand()

            if not success:

                print("Camera not found!")
                break



            if countdown:

                elapsed_time = time.time() - countdown_start

                countdown_number = 3 - int(elapsed_time)

                if elapsed_time >= 3:

                    countdown = False

                    show_go = True

                    go_start = time.time()



            if show_go:

                if time.time() - go_start >= 0.8:

                    show_go = False

                    computer = computer_choice()

                    result = find_winner(
                        player_choice,
                        computer
                    )



                    if result == "You Win!":

                        player_score += 1

                        play_sound("win")

                    elif result == "Computer Wins!":

                        computer_score += 1

                        play_sound("lose")

                    else:

                        play_sound("draw")



                    game_result = check_game_over(
                        player_score,
                        computer_score
                    )

                    if game_result != "":

                        game_over = True



            img = draw_game_screen(
                img,
                choice,
                computer,
                result,
                player_score,
                computer_score,
                countdown,
                countdown_number,
                show_go,
                game_over,
                game_result
            )


        

            cv2.imshow(
                "Rock Paper Scissors",
                img
            )


         

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):

                break

            elif key == 32:

                if (
                    choice != "Unknown"
                    and not countdown
                    and not game_over
                    and not show_go
                ):

                    player_choice = choice

                    countdown = True

                    countdown_start = time.time()

                    countdown_number = 3


        

            elif key == ord("r") and game_over:

                player_score = 0

                computer_score = 0

                computer = ""

                result = ""

                player_choice = ""

                game_result = ""

                game_over = False

                countdown = False

                show_go = False

                countdown_number = 3


finally:

    cap.release()

    cv2.destroyAllWindows()

    pygame.mixer.quit()

    print("Camera closed successfully!")
