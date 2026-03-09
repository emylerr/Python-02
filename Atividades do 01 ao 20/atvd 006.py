import pygame
pygame.init()
pygame.mixer.music.load('atvd6.mp3')
pygame.mixer.music.play()

print("Música iniciada! Pressione ENTER para fechar o programa...")

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
pygame.quit()