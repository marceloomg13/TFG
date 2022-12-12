import pygame, sys
from settings import *
from level import Level



class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Cinders')
		# pygame.display.toggle_fullscreen()
		self.clock = pygame.time.Clock()

		self.level = Level()


		self.main_sound = pygame.mixer.Sound('../audio/main.ogg')
		self.main_sound.set_volume(0.3)
		self.main_sound.play(loops = -1)
	
	
	def run(self):
		while True:
			if self.level.playing == False:
				self.main_sound.stop()
				self.level.showGameOverScreen()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			self.screen.fill(WATER_COLOR)
			self.level.run(self.level.playing)
			pygame.display.update()
			self.clock.tick(FPS)
			
		

if __name__ == '__main__':
	game = Game()
	game.run()
