import os
import pygame

dirname = os.path.dirname(__file__)


def load_images():
    images = []
    for i in range(7):
        image = pygame.image.load(os.path.join(
            dirname, "status_images", "hangman" + str(i) + ".png"))
        images.append(image)
    return images
