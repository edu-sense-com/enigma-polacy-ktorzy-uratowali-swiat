# wprowadzamy globalny słownik - strukturę danych 
# dostępną z każdego miejsca aplikacji
# słownik jest rodzajem `mutable`
# a więc możemy zmieniać jego elementy

import pygame

# wczytujemy dwie funkcje z modułu
from random import randint, choice
from time import sleep

# definiujemy funkcje
def game_window(place):
    if place not in places:
        return None

    pygame.display.set_caption(
        "Polacy w Biurze Szyfrów - Enigma - "
        + hero["name"]
        + " | "
        + place
    )
    file = (
        "/sandbox/images/background/"
        + places[place]["background_file"]
    )
    background_picture = pygame.image.load(file)
    window.blit(background_picture, (0, 0))


def hero_get_picture():
    return (
        "character-"
        + hero["filename"]
        + "-"
        + hero["direction"]
        + "-0"
        + str(hero["frame"])
        + ".png"
    )


def display_hero():
    file = (
        "/sandbox/images/hero/"
        + hero_get_picture()
    )
    hero_picture = pygame.image.load(file)
    # losujemy dla bohatera miejsce pojawienia się
    hero["x"] = randint(10, 700)
    # bohater wyświetlany na zdefiniowanej 
    # wysokości HERO_Y
    window.blit(hero_picture, (hero["x"], HERO_Y))


def display_attachments(place):
    if not place in places:
        return None

    file = (
        "/sandbox/images/foreground/"
        + places[place]["attachment_file"]
    )
    attachment_picture = pygame.image.load(file)
    window.blit(attachment_picture, (0, 0))


# słowniki (ang. dict) z danymi gry, 
# z których będziemy korzystać
places = {
    "Anglia_1": {
        "background_file": "rooms-england-bletchley-park-01.jpg",
        "attachment_file": "rooms-england-bletchley-park-01.png",
    },
    "Anglia_2": {
        "background_file": "rooms-england-bletchley-park-02.jpg",
        "attachment_file": "rooms-england-bletchley-park-02.png",
    },
    "Anglia_3": {
        "background_file": "rooms-england-bletchley-park-03.jpg",
        "attachment_file": "rooms-england-bletchley-park-03.png",
    },
    "Francja_1": {
        "background_file": "rooms-france-paris-01.jpg",
        "attachment_file": "rooms-france-paris-01.png",
    },
    "Francja_2": {
        "background_file": "rooms-france-paris-02.jpg",
        "attachment_file": "rooms-france-paris-02.png",
    },
    "Francja_3": {
        "background_file": "rooms-france-paris-03.jpg",
        "attachment_file": "rooms-france-paris-03.png",
    },
    "Niemcy_1": {
        "background_file": "rooms-german-uboot-01.jpg",
        "attachment_file": "rooms-german-uboot-01.png",
    },
    "Niemcy_2": {
        "background_file": "rooms-german-uboot-02.jpg",
        "attachment_file": "rooms-german-uboot-02.png",
    },
    "Lwow_1": {
        "background_file": "rooms-poland-lwow-sknilow-01.jpg",
        "attachment_file": "rooms-poland-lwow-sknilow-01.png",
    },
    "Lwow_2": {
        "background_file": "rooms-poland-lwow-sknilow-02.jpg",
        "attachment_file": "rooms-poland-lwow-sknilow-02.png",
    },
    "Polska_1": {
        "background_file": "rooms-poland-warsaw-cipher-bureau-01.jpg",
        "attachment_file": "rooms-poland-warsaw-cipher-bureau-01.png",
    },
    "Polska_2": {
        "background_file": "rooms-poland-warsaw-cipher-bureau-02.jpg",
        "attachment_file": "rooms-poland-warsaw-cipher-bureau-02.png",
    },
    "Polska_3": {
        "background_file": "rooms-poland-warsaw-cipher-bureau-03.jpg",
        "attachment_file": "rooms-poland-warsaw-cipher-bureau-03.png",
    },
    "Polska_4": {
        "background_file": "rooms-poland-warsaw-cipher-bureau-04.jpg",
        "attachment_file": "rooms-poland-warsaw-cipher-bureau-04.png",
    },
}


# Definicja słownika danych o bohaterze
hero = {
    "name": "Zygalski",
    "filename": "zygalski",
    "direction": "right",
    "x": randint(
        10, 700
    ),  # losujemy współrzędną X
    "frame": 0,
    "action_place": choice(places.keys()),
}


pygame.init()
WINDOW_SIZE = (870, 435)
HERO_Y = 235
# tworzymy obiekt okna tylko 1 raz na początku
window = pygame.display.set_mode(WINDOW_SIZE)

# wyświetlamy wszystkie elementy - warstwy obrazu

for scene in places:
    # aktualizujemy wartość w słowniku
    hero["action_place"] = scene
    # wyświetlamy korzystając ze 
    # zaktualizowanych danych
    game_window(hero["action_place"])
    pygame.display.update()
    sleep(0.5)
    # dla każdej "warstwy obrazu" wprowadzamy 
    # krótki czas przerwy
    hero["x"] = randint(
        10, 700
    )  # losowo umieszczamy bohatera
    display_hero()
    pygame.display.update()
    sleep(0.5)
    # widać dobrze, jak budujemy pełny obrazu
    display_attachments(hero["action_place"])
    pygame.display.update()
    sleep(0.5)

# nieskończona pętla
while True:

    # pobieramy zdarzenie, jeśli zaszło 
    # (funkcja biblioteki)
    game_event = pygame.event.wait()

    # w momencie kliknięcia na "X" 
    # w prawym górnym rogu okna
    if game_event.type == pygame.QUIT:
        # to zakończy działanie gry
        # przerwiemy wykonywanie pętli while
        break


# koniec gry, koniec pętli while
pygame.quit()
