# coding=utf-8
import sys

import pygame

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()# 初始化背景设置
	screen = pygame.display.set_mode((1000, 600))
	pygame.display.set_caption("Alien Invasion")

	# 开始游戏循环
	while True:

		# 监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# 让最近绘制的屏幕可见
		pygame.display.flip()

run_game()
