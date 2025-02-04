import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()

	updatables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatables, drawables)
	Asteroid.containers = (asteroids, updatables, drawables)
	AsteroidField.containers = updatables
	Shot.containers = (shots, updatables, drawables)

	asteroid_field = AsteroidField()

	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		updatables.update(dt)

		for asteroid in asteroids:
			if asteroid.check_collision(player):
				print("Game over!")
				sys.exit()

			for shot in shots:
				if shot.check_collision(asteroid):
					shot.kill()
					asteroid.split()


		screen.fill("BLACK")

		for object in drawables:
			object.draw(screen)

		pygame.display.flip()

		# limit the frame rate to 60 fps
		dt = clock.tick(60)/1000

if __name__ == "__main__":
	main()
