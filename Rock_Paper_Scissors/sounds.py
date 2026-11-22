
import pygame



pygame.mixer.init()



def play_sound(sound_name):

    try:
        sound = pygame.mixer.Sound(sound_name + ".wav")
        sound.play()

    except Exception as e:
        print("Sound error:", e)
