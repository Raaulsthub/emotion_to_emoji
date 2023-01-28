import pygame
from pictureTaker import take_picture
from rekognitionAWS import EmotionGetter
import threading

class Communication:
    def __init__(self):
        self.emotion = 'Happy'


def emotion_getter(communication):
    emotion_decoder = EmotionGetter()
    path_to_picture = './rekognition/current_image.png'
    while(True):
        take_picture()
        communication.emotion, confidence = emotion_decoder.get_emotions(path_to_picture)

def game(communication):
    # initialize pygame
    pygame.init()

    # set the window size
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    # set the title of the window
    pygame.display.set_caption("Image Changer")

    # list of images
    images = ['./images/angry.png', './images/happy.png', './images/neutral.png', './images/sad.png', './images/surprise.png']

    # index of the current image
    current_image = 0

    # load the current image and scale it down
    image = pygame.image.load(images[current_image])
    image = pygame.transform.scale(image, (int(image.get_width()*0.5), int(image.get_height()*0.5)))

    # set a boolean to indicate if the game is running
    running = True

    # color variables for background color
    r = 0
    g = 0
    b = 0
    color_change_speed = 1

    # emotion getting thread
    background_thread = threading.Thread(target=emotion_getter, args=[communication])
    background_thread.start()

    # main game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if (communication.emotion == 'ANGRY' or communication.emotion == 'CONFUSED'):
            current_image = 0
            image = pygame.image.load(images[current_image])
            image = pygame.transform.scale(image, (int(image.get_width()*0.5), int(image.get_height()*0.5)))
        elif (communication.emotion == 'HAPPY'):
            current_image = 1
            image = pygame.image.load(images[current_image])
            image = pygame.transform.scale(image, (int(image.get_width()*0.25), int(image.get_height()*0.25)))
        elif (communication.emotion == 'CALM'):
            current_image = 2
            image = pygame.image.load(images[current_image])
            image = pygame.transform.scale(image, (int(image.get_width()*0.4), int(image.get_height()*0.4)))
        elif (communication.emotion == 'SAD'):
            current_image = 3
            image = pygame.image.load(images[current_image])
            image = pygame.transform.scale(image, (int(image.get_width()*0.5), int(image.get_height()*0.5)))
        elif (communication.emotion == 'SURPRISED'):
            current_image = 4
            image = pygame.image.load(images[current_image])
            image = pygame.transform.scale(image, (int(image.get_width()*0.5), int(image.get_height()*0.5)))

        # change background color
        r += color_change_speed
        g += color_change_speed
        b += color_change_speed
        if r >= 50 or r <= 0:
            r = 0
        if g >= 150 or g <= 0:
            g = 0
        if b >= 255 or b <= 0:
            b = 0
        
        # clear the screen
        screen.fill((r, g, b))
        # draw the image on the screen
        screen.blit(image, (200, 100))
        # update the display
        pygame.display.flip()

        clock.tick(20)

    # deactivating pygame library
    pygame.quit()

def main():

    communication = Communication()
    # emotion getting thread
    thread1 = threading.Thread(target=emotion_getter, args=[communication])
    thread1.start()

    thread2 = threading.Thread(target=game, args=[communication])
    thread2.start()

    # Wait for thread 1 to complete
    thread1.join()

    # Wait for thread 2 to complete
    thread2.join()

if __name__ == '__main__':
    main()