# -*- coding: utf-8 -*
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()# 初始化背景设置
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))#绘制屏幕的大小

	pygame.display.set_caption("Alien Invasion")#窗口名
	ship = Ship(screen)

	# 开始游戏循环
	while True:
		gf.check_events()
		gf.update_screen(ai_settings, screen, ship)

run_game()
