
from turtle import onkeypress
from player import Player
from projectile import Projectile
from enemy import Enemy
from ui import UI
from window import Window
from game_time import GameTime
from watched_key import WatchedKey
from group import Group
from utils import handle_movement, random_screen_pos
import globals as g

def spawn_enemies(enemies: Group, player: Player):
    for _ in range(g.ENEMY_SPAWN_COUNT):
        enemy = Enemy(random_screen_pos(), target=player)
        enemies.append(enemy)


def restart_game(*entities):
    for e in entities:
        e.restart()
    g.GAME_OVER = False

def quit_game(*_):
    exit()

def start_game():
    window = Window()
    enemies = Group[Enemy](collision_group=None)
    projectiles = Group[Projectile](collision_group=enemies)
    player = Player(projectiles)

    ui = UI(
        restart_callback=lambda *_: restart_game(player, enemies, ui),
        quit_callback=quit_game
    )

    spawn_timer = 0

    w = WatchedKey('w')
    a = WatchedKey('a')
    s = WatchedKey('s')
    d = WatchedKey('d')
    onkeypress(player.spawn_projectile, 'space')

    def update_loop():
        nonlocal spawn_timer
        GameTime.process_time()

        if g.GAME_OVER:
            ui.show_gameover()
        else:
            spawn_timer += GameTime.delta_time

            if spawn_timer >= g.ENEMY_SPAWN_INTERVAL:
                spawn_timer = 0
                spawn_enemies(enemies, player)

            handle_movement(w,a,s,d, player=player)
            player.update()
            enemies.update()

        window.screen.update()
        window.screen.ontimer(update_loop, g.FRAME_TIME_MS)

    GameTime.init()
    update_loop()

    window.screen.listen()
    window.screen.mainloop()

start_game()
