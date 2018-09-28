#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- Author: zhaohuan -*-
import pygame
import settings


class Ship():
    def __init__(self, ai_setting, screen):
        """初始化飞船并设置气初始位置"""
        self.screen = screen
        self.ai_setting = ai_setting
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
        self.moving_right = False
        self.moving_left = False

        # 上下移动代码（自定义）
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor

        # 上下移动代码（自定义）
        if self.moving_up and self.rect.bottom > self.rect.height:
            self.bottom -= self.ai_setting.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_setting.ship_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        self.center = self.screen_rect.centerx