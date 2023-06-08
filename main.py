import pyxel
import random

class Menu():
    def __init__(self):
        pyxel.init(128, 128, "Pong by NextTap", 60)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_SPACE):
            Jeu()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(128 // 2 - 40, 128 // 2 - 5, 'Press [SPACE] to play', 7)

class Jeu:
    def __init__(self):
        self.ball_size = 2
        self.largeur_joueur = 20
        self.hauteur_joueur = 3
        self.joueur_1_x = 128 // 2
        self.joueur_1_y = 128 - self.hauteur_joueur
        self.joueur_2_x = 128 // 2
        self.joueur_2_y = 0
        self.ball_x_speed = 0
        self.ball_y_speed = random.choice([-1, 1])
        self.ball_x_position = 128 // 2 - self.ball_size // 2
        self.ball_y_position = 128 // 2 - self.ball_size // 2
        self.game_over = False
        self.score_joueur_1 = 0
        self.score_joueur_2 = 0
        self.gagnant = None
        pyxel.run(self.update, self.draw)


    def deplacements(self):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.joueur_1_x + self.largeur_joueur < 128:
            self.joueur_1_x += 1
        if pyxel.btn(pyxel.KEY_LEFT) and self.joueur_1_x > 0:
            self.joueur_1_x -= 1
        if pyxel.btn(pyxel.KEY_D) and self.joueur_2_x + self.largeur_joueur < 128:
            self.joueur_2_x += 1
        if pyxel.btn(pyxel.KEY_Q) and self.joueur_2_x > 0:
            self.joueur_2_x -= 1

    def update(self):
        if self.game_over and pyxel.btn(pyxel.KEY_SPACE):
            self.game_over = False
            Jeu()
        if not self.game_over:
            self.deplacements()
            self.ball_x_position += self.ball_x_speed
            self.ball_y_position += self.ball_y_speed

            if self.ball_x_position <= 0 or self.ball_x_position >= 128 - self.ball_size:
                self.ball_x_speed *= -1

            if (self.ball_y_position <= self.joueur_2_y + self.hauteur_joueur and self.ball_x_position + self.ball_size >= self.joueur_2_x and self.ball_x_position <= self.joueur_2_x + self.largeur_joueur):
                self.ball_y_speed *= -1

                if pyxel.btn(pyxel.KEY_D):
                    self.ball_x_speed = 1
                elif pyxel.btn(pyxel.KEY_Q):
                    self.ball_x_speed = -1
                self.score_joueur_1 += 1

            if (self.ball_y_position + self.ball_size >= self.joueur_1_y and self.ball_x_position + self.ball_size >= self.joueur_1_x and self.ball_x_position <= self.joueur_1_x + self.largeur_joueur):
                self.ball_y_speed *= -1

                if pyxel.btn(pyxel.KEY_RIGHT):
                    self.ball_x_speed = 1
                elif pyxel.btn(pyxel.KEY_LEFT):
                    self.ball_x_speed = -1
                self.score_joueur_2 += 1

            if self.ball_y_position <= 0 or self.ball_y_position >= 128 - self.ball_size:
                self.game_over = True

    def draw(self):
        pyxel.cls(7)
        pyxel.rect(self.joueur_1_x, self.joueur_1_y, self.largeur_joueur, self.hauteur_joueur, 0)
        pyxel.rect(self.joueur_2_x, self.joueur_2_y, self.largeur_joueur, self.hauteur_joueur, 0)
        pyxel.text(128 // 2 - 20, 20, 'Joueur 1 = ' + str(self.score_joueur_1), 0)
        pyxel.text(128 // 2 - 20, 128 - 20, 'Joueur 2 = ' + str(self.score_joueur_2), 0)
        pyxel.circ(self.ball_x_position, self.ball_y_position, self.ball_size, 8)

        if self.game_over:
            pyxel.text(128 // 2 - 15, 128 // 2 - 10, 'Game Over', 5)
            pyxel.text(128 // 2 - 45, 128 // 2 + 10, 'Press [SPACE] to restart', 5)
            if self.score_joueur_1 > self.score_joueur_2:
                pyxel.text(128 // 2 - 37, 128 // 2, 'Le joueur 1 a gagne !', 5)
            elif self.score_joueur_2 > self.score_joueur_1:
                pyxel.text(128 // 2 - 37, 128 // 2, 'Le joueur 2 a gagne !', 5)
            else:
                pyxel.text(128 // 2 - 30, 128 // 2, 'Il y a egalite !', 5)

Menu()