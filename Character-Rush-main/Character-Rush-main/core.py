import os

SCREENSIZE = (1200, 600)

FPS = 60

AUDIO_PATHS = {
    'die': os.path.join(os.getcwd(), 'resources/audios/mdie.mp3'),
    'jump': os.path.join(os.getcwd(), 'resources/audios/4078.wav'),
    'point': os.path.join(os.getcwd(), 'resources/audios/point.wav'),
    'bgm' : os.path.join(os.getcwd(), 'resources/audios/bgm.mp3')
}
IMAGE_PATHS = {
    'cacti': [
        os.path.join(os.getcwd(), 'resources/images/nailong.svg'),
        os.path.join(os.getcwd(), 'resources/images/nailong.svg')
    ],
    'cloud': os.path.join(os.getcwd(), 'resources/images/cloud.svg'),
    'ch': [
        os.path.join(os.getcwd(), 'resources/images/miku.png'),
        os.path.join(os.getcwd(), 'resources/images/miku.png'),
    ],
    'ground': os.path.join(os.getcwd(), 'resources/images/ground-4x.svg'),
    'ptera': os.path.join(os.getcwd(), 'resources/images/rocket.png'),
    'replay': os.path.join(os.getcwd(), 'resources/images/replay.svg')
}
FONT_PATHS = {
    'joystix': os.path.join(os.getcwd(), 'resources/fonts/JoystixMonospace-Regular.ttf')
}

BACKGROUND_COLOR = (235, 235, 235)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
