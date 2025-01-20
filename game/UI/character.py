import pygame
from pygame import Surface

from game.media_data import *

coords = {
    'left': (110, 280),
    'left-center': (400, 280),
    'center': (710, 280),
    'right-center': (1000, 280),
    'right': (1310, 280)
}

class Character:
    def __init__(self, name, texture, pos):
        self.name = name
        self.texture = texture
        self.pos = pos

    def draw(self, on: Surface):
        on.blit(self.texture, self.pos)


# ТЁМА
tioma_o = {
    'left': Character('Тёма', t_o, coords['left']),
    'left-center': Character('Тёма', t_o, coords['left-center']),
    'center': Character('Тёма', t_o, coords['center']),
    'right-center': Character('Тёма', t_o, coords['right-center']),
    'right': Character('Тёма', t_o, coords['right'])
}

tioma_b = {
    'left': Character('Тёма', t_b, coords['left']),
    'left-center': Character('Тёма', t_b, coords['left-center']),
    'center': Character('Тёма', t_b, coords['center']),
    'right-center': Character('Тёма', t_b, coords['right-center']),
    'right': Character('Тёма', t_b, coords['right'])
}

tioma_v = {
    'left': Character('Тёма', t_v, coords['left']),
    'left-center': Character('Тёма', t_v, coords['left-center']),
    'center': Character('Тёма', t_v, coords['center']),
    'right-center': Character('Тёма', t_v, coords['right-center']),
    'right': Character('Тёма', t_v, coords['right'])
}

tioma_g = {
    'left': Character('Тёма', t_g, coords['left']),
    'left-center': Character('Тёма', t_g, coords['left-center']),
    'center': Character('Тёма', t_g, coords['center']),
    'right-center': Character('Тёма', t_g, coords['right-center']),
    'right': Character('Тёма', t_g, coords['right'])
}

tioma_s = {
    'left': Character('Тёма', t_s, coords['left']),
    'left-center': Character('Тёма', t_s, coords['left-center']),
    'center': Character('Тёма', t_s, coords['center']),
    'right-center': Character('Тёма', t_s, coords['right-center']),
    'right': Character('Тёма', t_s, coords['right'])
}

# МАХУТОВ
mahutov_o = {
    'left': Character('Махутов', m_o, coords['left']),
    'left-center': Character('Махутов', m_o, coords['left-center']),
    'center': Character('Махутов', m_o, coords['center']),
    'right-center': Character('Махутов', m_o, coords['right-center']),
    'right': Character('Махутов', m_o, coords['right'])
}

mahutov_b = {
    'left': Character('Махутов', m_b, coords['left']),
    'left-center': Character('Махутов', m_b, coords['left-center']),
    'center': Character('Махутов', m_b, coords['center']),
    'right-center': Character('Махутов', m_b, coords['right-center']),
    'right': Character('Махутов', m_b, coords['right'])
}

mahutov_v = {
    'left': Character('Махутов', m_v, coords['left']),
    'left-center': Character('Махутов', m_v, coords['left-center']),
    'center': Character('Махутов', m_v, coords['center']),
    'right-center': Character('Махутов', m_v, coords['right-center']),
    'right': Character('Махутов', m_v, coords['right'])
}

mahutov_g = {
    'left': Character('Махутов', m_g, coords['left']),
    'left-center': Character('Махутов', m_g, coords['left-center']),
    'center': Character('Махутов', m_g, coords['center']),
    'right-center': Character('Махутов', m_g, coords['right-center']),
    'right': Character('Махутов', m_g, coords['right'])
}

mahutov_s = {
    'left': Character('Махутов', m_s, coords['left']),
    'left-center': Character('Махутов', m_s, coords['left-center']),
    'center': Character('Махутов', m_s, coords['center']),
    'right-center': Character('Махутов', m_s, coords['right-center']),
    'right': Character('Махутов', m_s, coords['right'])
}

mahutov_z = {
    'left': Character('Махутов', m_z, coords['left']),
    'left-center': Character('Махутов', m_z, coords['left-center']),
    'center': Character('Махутов', m_z, coords['center']),
    'right-center': Character('Махутов', m_z, coords['right-center']),
    'right': Character('Махутов', m_z, coords['right'])
}

mahutov_sigma = {
    'left': Character('Махутов', m_sigma, coords['left']),
    'left-center': Character('Махутов', m_sigma, coords['left-center']),
    'center': Character('Махутов', m_sigma, coords['center']),
    'right-center': Character('Махутов', m_sigma, coords['right-center']),
    'right': Character('Махутов', m_sigma, coords['right'])
}

# ДИМАН
diman_o = {
    'left': Character('Диман', d_o, coords['left']),
    'left-center': Character('Диман', d_o, coords['left-center']),
    'center': Character('Диман', d_o, coords['center']),
    'right-center': Character('Диман', d_o, coords['right-center']),
    'right': Character('Диман', d_o, coords['right'])
}

diman_b = {
    'left': Character('Диман', d_b, coords['left']),
    'left-center': Character('Диман', d_b, coords['left-center']),
    'center': Character('Диман', d_b, coords['center']),
    'right-center': Character('Диман', d_b, coords['right-center']),
    'right': Character('Диман', d_b, coords['right'])
}

diman_v = {
    'left': Character('Диман', d_v, coords['left']),
    'left-center': Character('Диман', d_v, coords['left-center']),
    'center': Character('Диман', d_v, coords['center']),
    'right-center': Character('Диман', d_v, coords['right-center']),
    'right': Character('Диман', d_v, coords['right'])
}

diman_g = {
    'left': Character('Диман', d_g, coords['left']),
    'left-center': Character('Диман', d_g, coords['left-center']),
    'center': Character('Диман', d_g, coords['center']),
    'right-center': Character('Диман', d_g, coords['right-center']),
    'right': Character('Диман', d_g, coords['right'])
}

diman_s = {
    'left': Character('Диман', d_s, coords['left']),
    'left-center': Character('Диман', d_s, coords['left-center']),
    'center': Character('Диман', d_s, coords['center']),
    'right-center': Character('Диман', d_s, coords['right-center']),
    'right': Character('Диман', d_s, coords['right'])
}

# ВАНЯ
vania_o = {
    'left': Character('Ваня', v_o, coords['left']),
    'left-center': Character('Ваня', v_o, coords['left-center']),
    'center': Character('Ваня', v_o, coords['center']),
    'right-center': Character('Ваня', v_o, coords['right-center']),
    'right': Character('Ваня', v_o, coords['right'])
}

vania_b = {
    'left': Character('Ваня', v_b, coords['left']),
    'left-center': Character('Ваня', v_b, coords['left-center']),
    'center': Character('Ваня', v_b, coords['center']),
    'right-center': Character('Ваня', v_b, coords['right-center']),
    'right': Character('Ваня', v_b, coords['right'])
}

vania_v = {
    'left': Character('Ваня', v_v, coords['left']),
    'left-center': Character('Ваня', v_v, coords['left-center']),
    'center': Character('Ваня', v_v, coords['center']),
    'right-center': Character('Ваня', v_v, coords['right-center']),
    'right': Character('Ваня', v_v, coords['right'])
}

vania_g = {
    'left': Character('Ваня', v_g, coords['left']),
    'left-center': Character('Ваня', v_g, coords['left-center']),
    'center': Character('Ваня', v_g, coords['center']),
    'right-center': Character('Ваня', v_g, coords['right-center']),
    'right': Character('Ваня', v_g, coords['right'])
}

vania_s = {
    'left': Character('Ваня', v_s, coords['left']),
    'left-center': Character('Ваня', v_s, coords['left-center']),
    'center': Character('Ваня', v_s, coords['center']),
    'right-center': Character('Ваня', v_s, coords['right-center']),
    'right': Character('Ваня', v_s, coords['right'])
}

