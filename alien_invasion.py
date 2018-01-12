# coding=utf-8
import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()# 初始化背景设置
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))#绘制屏幕的大小

	pygame.display.set_caption("Alien Invasion")#窗口名
	ship = Ship(screen)
	# bg_color = (230, 0, 0)# 设置屏幕颜色，弹出来的屏幕仍是黑色？

	# 开始游戏循环
	while True:

		# 监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		screen.fill(ai_settings.bg_color)
		ship.blitme()

		# 让最近绘制的屏幕可见
		pygame.display.flip()

run_game()
