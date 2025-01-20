import pygame


pygame.init()


# ШРИФТЫ

big_font = pygame.font.Font('game/media/other/Lilita One Regular.ttf', 90)
small_font = pygame.font.Font('game/media/other/Lilita One Regular.ttf', 50)


# ПЕРСОНАЖИ

# тёма
t_o = pygame.image.load('game/media/characters/tioma/тёма обычный.png')
t_b = pygame.image.load('game/media/characters/tioma/тёма бабайка.png')
t_v = pygame.image.load('game/media/characters/tioma/тёма весёлый.png')
t_g = pygame.image.load('game/media/characters/tioma/тёма грусть.png')
t_s = pygame.image.load('game/media/characters/tioma/тёма смешной.png')

# диман
d_o = pygame.image.load('game/media/characters/diman/диман обычный.png')
d_b = pygame.image.load('game/media/characters/diman/диман бабайка.png')
d_v = pygame.image.load('game/media/characters/diman/диман весёлый.png')
d_g = pygame.image.load('game/media/characters/diman/диман грусть.png')
d_s = pygame.image.load('game/media/characters/diman/диман смешной.png')

# ваня
v_o = pygame.image.load('game/media/characters/vania/ваня обычный.png')
v_b = pygame.image.load('game/media/characters/vania/ваня бабайка.png')
v_v = pygame.image.load('game/media/characters/vania/ваня весёлый.png')
v_g = pygame.image.load('game/media/characters/vania/ваня грусть.png')
v_s = pygame.image.load('game/media/characters/vania/ваня смешной.png')

# махутов
m_o = pygame.image.load('game/media/characters/mahutov/махутов обычный.png')
m_b = pygame.image.load('game/media/characters/mahutov/махутов бабайка.png')
m_v = pygame.image.load('game/media/characters/mahutov/махутов весёлый.png')
m_g = pygame.image.load('game/media/characters/mahutov/махутов грусть.png')
m_s = pygame.image.load('game/media/characters/mahutov/махутов смешной.png')
m_z = pygame.image.load('game/media/characters/mahutov/махутов злой.png')
m_sigma = pygame.image.load('game/media/characters/mahutov/махутов сигма.png')


# ЗАДНИЕ ФОНЫ

main_menu = pygame.image.load('game/media/backgrounds/главное меню.jpg')
m_room = pygame.image.load('game/media/backgrounds/комната сани.jpg')

