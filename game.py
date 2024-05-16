import pygame, time, math, random
from pygame.locals import *
from pygame.math import Vector2

pygame.init()

targetFPS = 60
playing = True

rawTileSize = 64
scale = 1
tileSize = rawTileSize * scale

WINDOW_W = 1150
WINDOW_H = 760

screen = pygame.display.set_mode([WINDOW_W, WINDOW_H])
pygame.display.set_caption("Spel 1")

##################################################################################

bullets = []
enemies = []
objects = []
items = []

show_hitboxes = False

margin = 5

coins_per_drop = 30

dayCount = 0
dayTime = True
lastSwitch = 0
dayDurationSeconds = 20
nightDurationSeconds = 20

YELLOW = (255, 255, 100)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 237, 255)
GREEN = (0, 255, 0)
RED = (179, 21, 21)
GRAY = (158, 158, 158)

font32 = pygame.font.Font("freesansbold.ttf", 32)
font24 = pygame.font.Font("freesansbold.ttf", 24)
font16 = pygame.font.Font("freesansbold.ttf", 16)

map1 = pygame.image.load("assets/map1.png").convert_alpha()

bulletpicture = pygame.transform.rotate(pygame.image.load("assets/bullet.png").convert_alpha(), 90)
soldier_pistol = pygame.image.load("assets/soldier/soldier1_gun.png").convert_alpha()
soldier_bigpistol = pygame.image.load("assets/soldier/soldier1_silencer.png").convert_alpha()
soldier_smg = pygame.image.load("assets/soldier/soldier1_machine.png").convert_alpha()
soldier_reload = pygame.image.load("assets/soldier/soldier1_reload.png").convert_alpha()
soldier_hold = pygame.image.load("assets/soldier/soldier1_hold.png").convert_alpha()

woman_pistol = pygame.image.load("assets/Woman/womanGreen_gun.png").convert_alpha()
woman_bigpistol = pygame.image.load("assets/Woman/womanGreen_silencer.png").convert_alpha()
woman_smg = pygame.image.load("assets/Woman/womanGreen_machine.png").convert_alpha()
woman_reload = pygame.image.load("assets/Woman/womanGreen_reload.png").convert_alpha()
woman_hold = pygame.image.load("assets/Woman/womanGreen_hold.png").convert_alpha()

robot_pistol = pygame.image.load("assets/Robot/robot1_gun.png").convert_alpha()
robot_bigpistol = pygame.image.load("assets/Robot/robot1_silencer.png").convert_alpha()
robot_smg = pygame.image.load("assets/Robot/robot1_machine.png").convert_alpha()
robot_reload = pygame.image.load("assets/Robot/robot1_reload.png").convert_alpha()
robot_hold = pygame.image.load("assets/Robot/robot1_hold.png").convert_alpha()

zombie_pistol = pygame.image.load("assets/Zombie/zoimbie1_gun.png").convert_alpha()
zombie_bigpistol = pygame.image.load("assets/Zombie/zoimbie1_silencer.png").convert_alpha()
zombie_smg = pygame.image.load("assets/Zombie/zoimbie1_machine.png").convert_alpha()
zombie_reload = pygame.image.load("assets/Zombie/zoimbie1_reload.png").convert_alpha()
zombie_hold = pygame.image.load("assets/Zombie/zoimbie1_hold.png").convert_alpha()

hitman_pistol = pygame.image.load("assets/Hitman/hitman1_gun.png").convert_alpha()
hitman_bigpistol = pygame.image.load("assets/Hitman/hitman1_silencer.png").convert_alpha()
hitman_smg = pygame.image.load("assets/Hitman/hitman1_machine.png").convert_alpha()
hitman_reload = pygame.image.load("assets/Hitman/hitman1_reload.png").convert_alpha()
hitman_hold = pygame.image.load("assets/Hitman/hitman1_hold.png").convert_alpha()

survivor_pistol = pygame.image.load("assets/Survivor/survivor1_gun.png").convert_alpha()
survivor_bigpistol = pygame.image.load("assets/Survivor/survivor1_silencer.png").convert_alpha()
survivor_smg = pygame.image.load("assets/Survivor/survivor1_machine.png").convert_alpha()
survivor_reload = pygame.image.load("assets/Survivor/survivor1_reload.png").convert_alpha()
survivor_hold = pygame.image.load("assets/Survivor/survivor1_hold.png").convert_alpha()

soldier_icon = pygame.transform.scale(pygame.image.load("assets/soldier/soldier1_gun.png").convert_alpha(), (60, 60))
woman_icon = pygame.transform.scale(pygame.image.load("assets/Woman/womanGreen_gun.png").convert_alpha(), (60, 60))
robot_icon = pygame.transform.scale(pygame.image.load("assets/Robot/robot1_gun.png").convert_alpha(), (60, 60))
zombie_icon = pygame.transform.scale(pygame.image.load("assets/Zombie/zoimbie1_gun.png").convert_alpha(), (60, 60))
hitman_icon = pygame.transform.scale(pygame.image.load("assets/Hitman/hitman1_gun.png").convert_alpha(), (60, 60))
survivor_icon = pygame.transform.scale(pygame.image.load("assets/Survivor/survivor1_gun.png").convert_alpha(), (60, 60))

dmg_overlay_img = pygame.transform.scale(pygame.image.load("assets/dmg_overlay.png").convert_alpha(),
                                         (WINDOW_W, WINDOW_H))

dmg_image_1 = dmg_overlay_img.copy()
dmg_image_2 = dmg_overlay_img.copy()
dmg_image_3 = dmg_overlay_img.copy()
dmg_image_4 = dmg_overlay_img.copy()
dmg_image_1.fill((255, 255, 255, 60), None, pygame.BLEND_RGBA_MULT)
dmg_image_2.fill((255, 255, 255, 90), None, pygame.BLEND_RGBA_MULT)
dmg_image_3.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)
dmg_image_4.fill((255, 255, 255, 170), None, pygame.BLEND_RGBA_MULT)

dmg_overlay = dmg_overlay_img

box_sprite = pygame.image.load("assets/Tiles/box_big.png").convert_alpha()
small_box_sprite = pygame.image.load("assets/Tiles/box_small.png").convert_alpha()
tree_sprite = pygame.image.load("assets/Tiles/tree.png").convert_alpha()

box_icon = pygame.transform.scale(box_sprite, (40, 40))
big_box_icon = pygame.transform.scale(box_sprite, (24, 24))
tree_icon = pygame.transform.scale(tree_sprite, (40, 40))

gameover = pygame.image.load("assets/gameover.png").convert_alpha()

zombiesprite = pygame.image.load("assets/zombie/zoimbie1_hold.png").convert_alpha()

soldier_pfp = pygame.transform.scale(pygame.image.load("assets/pfps/soldier_pfp.png").convert_alpha(), (60, 60))
woman_pfp = pygame.transform.scale(pygame.image.load("assets/pfps/woman_pfp.png").convert_alpha(), (60, 60))
robot_pfp = pygame.transform.scale(pygame.image.load("assets/pfps/robot_pfp.png").convert_alpha(), (60, 60))
zombie_pfp = pygame.transform.scale(pygame.image.load("assets/pfps/zombie_pfp.png").convert_alpha(), (60, 60))
hitman_pfp = pygame.transform.scale(pygame.image.load("assets/pfps/hitman_pfp.png").convert_alpha(), (60, 60))
survivor_pfp = pygame.transform.scale(pygame.image.load("assets/pfps/survivor_pfp.png").convert_alpha(), (60, 60))

shop_bg = pygame.image.load("assets/shop_bg.png").convert_alpha()
upgrade_area = pygame.Rect(590, 140, 35, 35)

item1 = font16.render("GUN", True, WHITE)
item2 = font16.render("SMG", True, WHITE)
item3 = font16.render("MED", True, WHITE)
upgr1 = font16.render("DMG +", True, WHITE)
upgr2 = font16.render("SKINS", True, WHITE)
upgr3 = font16.render("C/DROP", True, WHITE)

shop_text = font24.render("- SHOP -", True, YELLOW)
shop_rect = shop_text.get_rect()

back_text = font16.render("BACK", True, WHITE)

skins_text = font24.render("- SKINS -", True, YELLOW)
skins_rect = skins_text.get_rect()


######################################################################

class DroppedCoins:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        i = random.randint(1, 100)
        if i < 80:
            self.value = coins_per_drop
            self.radius = 10
        elif i < 97:
            self.value = round(coins_per_drop * 1.5)
            self.radius = 13
        else:
            self.value = coins_per_drop * 4
            self.radius = 16

        self.hitbox = pygame.Rect(self.x, self.y, self.radius, self.radius)
        self.distance2player = 0
        self.speed = 0

    def update(self):
        dx = player.x - self.x
        dy = player.y - self.y

        self.distance2player = math.sqrt((dx * dx) + (dy * dy))
        if self.distance2player < player.pickup_distance:
            x_dir, y_dir = pygame.math.Vector2(dx, dy).normalize()

            self.speed = 0.8 * player.pickup_distance / self.distance2player

            self.x += self.speed * x_dir
            self.y += self.speed * y_dir

        if self.hitbox.colliderect(player.hitbox):
            player.coins += self.value
            items.remove(self)

        self.hitbox = pygame.Rect(self.x, self.y, self.radius, self.radius)

    def draw(self):
        pygame.draw.rect(screen, YELLOW, self.hitbox)


class box_class:
    def __init__(self, x, y, angle):
        self.x = round_to_base(x, 64)
        self.y = round_to_base(y, 64)
        self.rotation_angle = angle
        self.radius = 50

        self.sprite = box_sprite

        self.hitbox = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)

    def update(self):
        self.hitbox = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)

    def draw(self):
        w, h = self.sprite.get_size()
        self.hitbox = rotate(self.sprite, (self.x, self.y), (w / 2, h / 2), self.rotation_angle)
        rotated_image = image_rotate(self.sprite, (self.x, self.y), (w / 2, h / 2), self.rotation_angle)
        screen.blit(rotated_image, self.hitbox)


class small_box_class:
    def __init__(self, x, y, angle):
        self.x = round_to_base(x, 32)
        self.y = round_to_base(y, 32)
        self.rotation_angle = angle
        self.radius = 30

        self.sprite = small_box_sprite
        self.small_sprite = pygame.transform.scale(self.sprite, (32, 32))

        self.hitbox = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)

    def draw(self):
        w, h = self.sprite.get_size()
        self.hitbox = rotate(self.small_sprite, (self.x, self.y), (w / 2, h / 2), self.rotation_angle)
        rotated_image = image_rotate(self.sprite, (self.x, self.y), (w / 2, h / 2), self.rotation_angle)
        screen.blit(rotated_image, (self.hitbox.x - (self.hitbox.width / 2), self.hitbox.y - (self.hitbox.height / 2)))
        self.hitbox = pygame.Rect(self.x - (self.sprite.get_width() * 0.75), self.y - (self.sprite.get_height() * 0.75),
                                  2 * self.radius, 2 * self.radius)


class tree_class:
    def __init__(self, x, y, angle):
        self.x = round_to_base(x, 64)
        self.y = round_to_base(y, 64)
        self.rotation_angle = angle
        self.radius = 20

        self.sprite = tree_sprite

        self.hitbox = pygame.Rect(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)

    def draw(self):
        w, h = self.sprite.get_size()
        self.hitbox = rotate(self.sprite, (self.x, self.y), (w / 2, h / 2), self.rotation_angle)
        rotated_image = image_rotate(self.sprite, (self.x, self.y), (w / 2, h / 2), self.rotation_angle)
        screen.blit(rotated_image, self.hitbox)


######################################################################

class Pistol:
    def __init__(self):
        self.name = "pistol"
        self.weapondmg = 15

        self.reload_time = 1000
        self.shoot_cooldown = 300
        self.clipsize = 21
        self.ammo_in_clip = 21

        self.unlocked = True


class SMG:
    def __init__(self):
        self.name = "smg"
        self.weapondmg = 18

        self.reload_time = 1800
        self.shoot_cooldown = 75
        self.clipsize = 30
        self.ammo_in_clip = 30

        self.unlocked = False


class Revolver:
    def __init__(self):
        self.name = "revolver"
        self.weapondmg = 50

        self.reload_time = 1300
        self.shoot_cooldown = 600
        self.clipsize = 11
        self.ammo_in_clip = 11

        self.unlocked = False


######################################################################

class Shop:
    def __init__(self):
        self.opened = False
        self.bg = shop_bg
        rect = self.bg.get_rect()
        self.bg_rect = pygame.Rect((WINDOW_W / 2) - (self.bg.get_width() / 2),
                                   (WINDOW_H / 2) - (self.bg.get_height() / 2), rect.width, rect.height)

        self.slot_w = 60
        self.slot_h = 60

        self.player_cd_multi = 1
        self.player_dmg_multi = 1

        self.last_med = pygame.time.get_ticks()
        self.med_cost = 100
        self.med_cooldown = 500

        self.clicking = False

        self.show_skinshop = False

        self.upgrade1_slot = pygame.Rect(465, 380, self.slot_w, self.slot_h)  # 25, 20
        self.upgrade2_slot = pygame.Rect(545, 380, self.slot_w, self.slot_h)
        self.upgrade3_slot = pygame.Rect(625, 380, self.slot_w, self.slot_h)

        self.item1_slot = pygame.Rect(465, 300, self.slot_w, self.slot_h)
        self.item2_slot = pygame.Rect(545, 300, self.slot_w, self.slot_h)
        self.item3_slot = pygame.Rect(625, 300, self.slot_w, self.slot_h)

        self.back_button = pygame.Rect(465, 450, self.slot_w, 20)

        self.cost_box = pygame.Rect(625, 450, 600 + self.slot_w, 20)

        self.cost_txt_box = pygame.Rect(545, 450, 600 + self.slot_w, 20)
        self.cost_txt = font16.render("COST:", True, YELLOW)

        self.upgr1_price = 70
        self.upgr3_price = 100

        self.item1_cost = font16.render("500", True, YELLOW)
        self.item2_cost = font16.render("2500", True, YELLOW)
        self.item3_cost = font16.render("100", True, YELLOW)
        self.upgr1_cost = font16.render("70", True, YELLOW)
        self.upgr2_cost = font16.render("-", True, YELLOW)
        self.upgr3_cost = font16.render("100", True, YELLOW)
        self.skin_cost = font16.render("FREE", True, YELLOW)
        self.unlocked_txt = font16.render("UNLOCKED", True, YELLOW)

    def draw(self, mx, my):
        screen.blit(self.bg, self.bg_rect)
        if self.show_skinshop:
            screen.blit(skins_text, pygame.Rect((self.bg_rect.width / 2) - (skins_rect.width / 2) + self.bg_rect.x,
                                                self.bg_rect.y + 20, skins_rect.width, skins_rect.height))

            if self.item1_slot.collidepoint((mx, my)):
                pygame.draw.rect(screen, YELLOW, self.item1_slot, 1)
                screen.blit(self.skin_cost, self.cost_box)
            else:
                pygame.draw.rect(screen, RED, self.item1_slot, 1)
            screen.blit(soldier_icon, self.item1_slot)

            if self.item2_slot.collidepoint((mx, my)):
                pygame.draw.rect(screen, YELLOW, self.item2_slot, 1)
                screen.blit(self.skin_cost, self.cost_box)
            else:
                pygame.draw.rect(screen, RED, self.item2_slot, 1)
            screen.blit(woman_icon, self.item2_slot)

            if self.item3_slot.collidepoint((mx, my)):
                pygame.draw.rect(screen, YELLOW, self.item3_slot, 1)
                screen.blit(self.skin_cost, self.cost_box)
            else:
                pygame.draw.rect(screen, RED, self.item3_slot, 1)
            screen.blit(robot_icon, self.item3_slot)

            if self.upgrade1_slot.collidepoint((mx, my)):
                pygame.draw.rect(screen, YELLOW, self.upgrade1_slot, 1)
                screen.blit(self.skin_cost, self.cost_box)
            else:
                pygame.draw.rect(screen, RED, self.upgrade1_slot, 1)
            screen.blit(zombie_icon, self.upgrade1_slot)

            if self.upgrade2_slot.collidepoint((mx, my)):
                pygame.draw.rect(screen, YELLOW, self.upgrade2_slot, 1)
                screen.blit(self.skin_cost, self.cost_box)
            else:
                pygame.draw.rect(screen, RED, self.upgrade2_slot, 1)
            screen.blit(hitman_icon, self.upgrade2_slot)

            if self.upgrade3_slot.collidepoint((mx, my)):
                pygame.draw.rect(screen, YELLOW, self.upgrade3_slot, 1)
                screen.blit(self.skin_cost, self.cost_box)
            else:
                pygame.draw.rect(screen, RED, self.upgrade3_slot, 1)
            screen.blit(survivor_icon, self.upgrade3_slot)

            if self.back_button.collidepoint((mx, my)):
                pygame.draw.rect(screen, YELLOW, self.back_button, 1)
            else:
                pygame.draw.rect(screen, RED, self.back_button, 1)
            screen.blit(back_text, self.back_button)

            screen.blit(self.cost_txt, self.cost_txt_box)
        else:
            screen.blit(shop_text, pygame.Rect((self.bg_rect.width / 2) - (shop_rect.width / 2) + self.bg_rect.x,
                                               self.bg_rect.y + 20, shop_rect.width, shop_rect.height))

            if self.upgrade1_slot.collidepoint((mx, my)):
                pygame.draw.rect(screen, YELLOW, self.upgrade1_slot, 1)
                screen.blit(self.upgr1_cost, self.cost_box)
            else:
                pygame.draw.rect(screen, RED, self.upgrade1_slot, 1)
            screen.blit(upgr1, self.upgrade1_slot)

            if self.upgrade2_slot.collidepoint((mx, my)):
                pygame.draw.rect(screen, YELLOW, self.upgrade2_slot, 1)
                screen.blit(self.upgr2_cost, self.cost_box)
            else:
                pygame.draw.rect(screen, RED, self.upgrade2_slot, 1)
            screen.blit(upgr2, self.upgrade2_slot)

            if self.upgrade3_slot.collidepoint((mx, my)):
                pygame.draw.rect(screen, YELLOW, self.upgrade3_slot, 1)
                screen.blit(self.upgr3_cost, self.cost_box)
            else:
                pygame.draw.rect(screen, RED, self.upgrade3_slot, 1)
            screen.blit(upgr3, self.upgrade3_slot)

            if revolver.unlocked:
                if self.item1_slot.collidepoint((mx, my)):
                    screen.blit(self.unlocked_txt, self.cost_box)
                pygame.draw.rect(screen, GREEN, self.item1_slot, 1)
            elif self.item1_slot.collidepoint((mx, my)) and (not revolver.unlocked):
                pygame.draw.rect(screen, YELLOW, self.item1_slot, 1)
                screen.blit(self.item1_cost, self.cost_box)
            else:
                pygame.draw.rect(screen, RED, self.item1_slot, 1)
            screen.blit(item1, self.item1_slot)

            if smg.unlocked:
                if self.item2_slot.collidepoint((mx, my)):
                    screen.blit(self.unlocked_txt, self.cost_box)
                pygame.draw.rect(screen, GREEN, self.item2_slot, 1)
            elif self.item2_slot.collidepoint((mx, my)) and (not smg.unlocked):
                pygame.draw.rect(screen, YELLOW, self.item2_slot, 1)
                screen.blit(self.item2_cost, self.cost_box)
            else:
                pygame.draw.rect(screen, RED, self.item2_slot, 1)
            screen.blit(item2, self.item2_slot)

            if self.item3_slot.collidepoint((mx, my)):
                pygame.draw.rect(screen, YELLOW, self.item3_slot, 1)
                screen.blit(self.item3_cost, self.cost_box)
            else:
                pygame.draw.rect(screen, RED, self.item3_slot, 1)
            screen.blit(item3, self.item3_slot)

            if self.back_button.collidepoint((mx, my)):
                pygame.draw.rect(screen, YELLOW, self.back_button, 1)
            else:
                pygame.draw.rect(screen, RED, self.back_button, 1)
            screen.blit(back_text, self.back_button)

            screen.blit(self.cost_txt, self.cost_txt_box)

    def click(self, mx, my):
        if self.opened:
            if self.show_skinshop:
                if self.item1_slot.collidepoint((mx, my)):
                    player.changeSkinTo("soldier")

                if self.item2_slot.collidepoint((mx, my)):
                    player.changeSkinTo("woman")

                if self.item3_slot.collidepoint((mx, my)):
                    player.changeSkinTo("robot")

                if self.upgrade1_slot.collidepoint((mx, my)):
                    player.changeSkinTo("zombie")

                if self.upgrade2_slot.collidepoint((mx, my)):
                    player.changeSkinTo("hitman")

                if self.upgrade3_slot.collidepoint((mx, my)):
                    player.changeSkinTo("survivor")

                if self.back_button.collidepoint((mx, my)):
                    self.show_skinshop = False

                player.updateSprite()

            else:
                global coins_per_drop
                if self.item1_slot.collidepoint((mx, my)):
                    if (not revolver.unlocked) and player.coins >= 500:
                        player.coins -= 500
                        revolver.unlocked = True
                if self.item2_slot.collidepoint((mx, my)):
                    if (not smg.unlocked) and player.coins >= 2500:
                        player.coins -= 2500
                        smg.unlocked = True
                if self.item3_slot.collidepoint((mx, my)):
                    if player.coins >= self.med_cost:
                        player.coins -= self.med_cost
                        self.item3_cost = font16.render(str(self.med_cost), True, YELLOW)
                        self.med_cost += 50
                        player.medkits += 1

                if self.upgrade1_slot.collidepoint((mx, my)):
                    if player.coins >= self.upgr1_price:
                        player.coins -= self.upgr1_price
                        self.upgr1_price += round(50 + 1.2 * self.player_dmg_multi)
                        self.upgr1_cost = font16.render(str(self.upgr1_price), True, YELLOW)
                        smg.weapondmg *= 1.15
                        revolver.weapondmg *= 1.15
                        pistol.weapondmg *= 1.15
                        self.player_dmg_multi *= 1.15

                if self.upgrade2_slot.collidepoint((mx, my)):
                    self.show_skinshop = True

                if self.upgrade3_slot.collidepoint((mx, my)):
                    if player.coins >= self.upgr3_price:
                        player.coins -= self.upgr3_price
                        self.upgr3_price += round((coins_per_drop * 1.2) + 50)
                        self.upgr3_cost = font16.render(str(self.upgr3_price), True, YELLOW)
                        coins_per_drop = coins_per_drop + 10

                if self.back_button.collidepoint((mx, my)):
                    self.opened = False

    def update(self, mx, my):
        if self.opened:
            global coins_per_drop
            if not dayTime:
                self.show_skinshop = False
                self.opened = False
            if player.holdingLeftMouse and not self.bg_rect.collidepoint((mx, my)):
                self.show_skinshop = False
                self.opened = False


######################################################################

class Player:
    def __init__(this, x, y, size):
        this.x = x
        this.y = y
        this.size = size
        this.rotation_degrees = 0

        this.coins = 0

        this.maxHP = 200
        this.hp = this.maxHP
        this.medkits = 0

        this.speed = 1

        this.holdingLeftMouse = False

        this.changeSkinTo("soldier")

        this.hitbox = pygame.Rect(this.x, this.y, this.size, this.size)

        this.equippedGun = pistol
        this.lastShotTime = pygame.time.get_ticks()
        this.reloading = False
        this.startedReloadingTime = 0
        this.reloadingProgress = 0

        this.pickup_distance = 175

        this.medkit_cooldown = 1000
        this.last_medkit_use = 0

        this.killcount = 0

    def update(this, keys, mx, my):
        this.updateSprite()

        if this.hp < 0:
            this.hp = 0

        w, h = this.sprite.get_size()
        this.rotation_degrees = (180 / math.pi) * - math.atan2(my - this.hitbox.centery, mx - this.hitbox.centerx)

        this.hitbox = rotate(this.sprite, (this.x, this.y), (w / 2, h / 2), this.rotation_degrees)

        if keys[pygame.K_r] and not this.equippedGun.ammo_in_clip == this.equippedGun.clipsize:
            this.reloading = True
            this.startedReloadingTime = pygame.time.get_ticks()

        if this.reloading:
            timeSinceReload = pygame.time.get_ticks() - this.startedReloadingTime
            if timeSinceReload <= this.equippedGun.reload_time:
                this.reloadingProgress = round((timeSinceReload / this.equippedGun.reload_time) * 100)
            else:
                this.reloading = False
                this.equippedGun.ammo_in_clip = this.equippedGun.clipsize

        if this.holdingLeftMouse:
            this.shoot()

        dx = 0
        dy = 0

        if keys[pygame.K_w] and not this.hitbox.midtop[1] < margin:
            dy = -1
        if keys[pygame.K_s] and not this.hitbox.midbottom[1] > (WINDOW_H - margin):
            dy = 1
        if keys[pygame.K_a] and not this.hitbox.midleft[0] < margin:
            dx = -1
        if keys[pygame.K_d] and not this.hitbox.midright[0] > (WINDOW_W - margin):
            dx = 1

        for obj in objects:
            if obj.hitbox.collidepoint(this.hitbox.midleft) and dx < 0:
                dx = 0
            if obj.hitbox.collidepoint(this.hitbox.midright) and dx > 0:
                dx = 0
            if obj.hitbox.collidepoint(this.hitbox.midtop) and dy < 0:
                dy = 0
            if obj.hitbox.collidepoint(this.hitbox.midbottom) and dy > 0:
                dy = 0

        move_vector = pygame.math.Vector2(0, 0)
        if not dx == 0 or not dy == 0:
            move_vector = pygame.math.Vector2(dx, dy).normalize()

        this.x += move_vector[0] * this.speed
        this.y += move_vector[1] * this.speed

        if keys[pygame.K_e]:
            if upgrade_area.collidepoint((player.hitbox.centerx, player.hitbox.centery)):
                if dayTime:
                    shop.opened = True
            elif player.medkits > 0 and this.hp < this.maxHP:
                this.use_medkit()

        if keys[pygame.K_1] and this.equippedGun.name != "pistol" and pistol.unlocked:
            this.reloading = False
            this.equippedGun = pistol
        elif keys[pygame.K_2] and this.equippedGun.name != "revolver" and revolver.unlocked:
            this.reloading = False
            this.equippedGun = revolver
        elif keys[pygame.K_3] and this.equippedGun.name != "smg" and smg.unlocked:
            this.reloading = False
            this.equippedGun = smg

    def use_medkit(this):
        if pygame.time.get_ticks() - this.last_medkit_use > this.medkit_cooldown:
            this.medkits -= 1
            this.hp += random.randint(30, 50)
            if this.hp > this.maxHP:
                this.hp = this.maxHP
            this.last_medkit_use = pygame.time.get_ticks()

    def draw(this):
        w, h = this.sprite.get_size()

        rotated_image = image_rotate(this.sprite, (this.x, this.y), (w / 2, h / 2), this.rotation_degrees)

        screen.blit(rotated_image, this.hitbox)

    def shoot(this):
        if this.reloading:
            return 0
        if shop.opened:
            return 0
        if pygame.time.get_ticks() - this.lastShotTime <= this.equippedGun.shoot_cooldown:
            return 0

        if this.equippedGun.ammo_in_clip <= 0:
            this.reloading = True
            this.startedReloadingTime = pygame.time.get_ticks()
        else:
            this.lastShotTime = pygame.time.get_ticks()
            bullets.append(Bullet(this.hitbox.centerx, this.hitbox.centery, this.rotation_degrees))
            this.equippedGun.ammo_in_clip -= 1

    def updateSprite(this):
        if this.reloading:
            this.sprite = this.spriteReloading
        elif this.equippedGun.name == "pistol":
            this.sprite = this.spritePistol
        elif this.equippedGun.name == "revolver":
            this.sprite = this.spriteRevolver
        elif this.equippedGun.name == "smg":
            this.sprite = this.spriteSMG

    def changeSkinTo(this, skinName):
        this.skin = skinName
        this.spritePistol = eval(skinName + "_pistol")
        this.spriteSMG = eval(skinName + "_smg")
        this.spriteRevolver = eval(skinName + "_bigpistol")
        this.spriteReloading = eval(skinName + "_reload")
        this.pfp = eval(skinName + "_pfp")


######################################################################

class Zombie:
    def __init__(self, x, y, size):
        self.rotation_degrees = 0
        self.name = "zombie"

        self.x = x
        self.y = y
        self.size = size
        self.color = RED
        self.pos = [self.x, self.y]
        self.sprite = zombiesprite
        self.speed = random.uniform(0.3, 0.5) + (0.05 * dayCount)

        self.spawn_time = pygame.time.get_ticks()

        self.max_hp = 60 + 13 * (dayCount * 1.5)
        self.health = self.max_hp

        self.hitbox = pygame.Rect(self.x, self.y, self.size, self.size)
        self.attack_damage = 16
        self.attack_cooldown = 300
        self.last_attack = 0

    def draw(self):
        w, h = self.sprite.get_size()

        rotated_image = image_rotate(self.sprite, (self.x, self.y), (w / 2, h / 2), self.rotation_degrees)

        screen.blit(rotated_image, self.hitbox)

    def attack(self, entity):
        if pygame.time.get_ticks() - self.last_attack > self.attack_cooldown:
            entity.hp -= self.attack_damage
            if entity.hp < 0:
                entity.hp = 0
            self.last_attack = pygame.time.get_ticks()

    def draw_hp_bar(self):
        if self.health < self.max_hp:
            pygame.draw.rect(screen, RED, pygame.Rect(self.x - (0.5 * self.sprite.get_height()), self.y - 30,
                                                      self.sprite.get_height() * 0.6, 5), 1)
            pygame.draw.rect(screen, RED, pygame.Rect(self.x - (0.5 * self.sprite.get_height()), self.y - 30,
                                                      (self.sprite.get_height() / self.max_hp) * self.health * 0.6, 5))

    def update(self):
        w, h = self.sprite.get_size()
        self.hitbox = rotate(self.sprite, (self.x, self.y), (w / 2, h / 2), self.rotation_degrees)

        direction_vector = pygame.math.Vector2(player.x - self.x, player.y - self.y)

        x_dir, y_dir = {0, 0} if direction_vector.length() == 0 else direction_vector.normalize()

        self.rotation_degrees = (180 / math.pi) * - math.atan2(player.hitbox.centery - self.hitbox.centery,
                                                               player.hitbox.centerx - self.hitbox.centerx)

        for obj in objects:
            if obj.hitbox.collidepoint(self.hitbox.midleft) and x_dir < 0:
                x_dir = 0
            if obj.hitbox.collidepoint(self.hitbox.midright) and x_dir > 0:
                x_dir = 0
            if obj.hitbox.collidepoint(self.hitbox.midtop) and y_dir < 0:
                y_dir = 0
            if obj.hitbox.collidepoint(self.hitbox.midbottom) and y_dir > 0:
                y_dir = 0

        for enemy in enemies:
            if enemy.hitbox.center == self.hitbox.center:
                break
            if enemy.name != "zombie":
                break

            if enemy.hitbox.collidepoint(self.hitbox.midleft) and x_dir < 0:
                x_dir = 0
            if enemy.hitbox.collidepoint(self.hitbox.midright) and x_dir > 0:
                x_dir = 0
            if enemy.hitbox.collidepoint(self.hitbox.midtop) and y_dir < 0:
                y_dir = 0
            if enemy.hitbox.collidepoint(self.hitbox.midbottom) and y_dir > 0:
                y_dir = 0

        if not self.hitbox.colliderect(player.hitbox):
            self.x += self.speed * x_dir
            self.y += self.speed * y_dir
            self.last_attack = pygame.time.get_ticks()
        else:
            self.attack(player)

        if dayTime:
            self.health -= 0.5


######################################################################

class Bullet:
    def __init__(self, x, y, rotation_degrees):
        self.x = x
        self.y = y
        self.pos = [self.x, self.y]
        self.direction = math.radians(rotation_degrees)
        self.bullet = pygame.Surface((15, 5), pygame.SRCALPHA)
        self.bullet.fill(WHITE)
        self.rotated_bullet = pygame.transform.rotate(self.bullet, rotation_degrees)
        self.time = 0
        self.hitRadius = 32

        self.hitbox = pygame.Rect(self.x - self.hitRadius, self.y - self.hitRadius, 2 * self.hitRadius,
                                  2 * self.hitRadius)
        self.speed = 4

    def move(self):
        self.pos[0] += math.cos(self.direction) * self.speed
        self.pos[1] -= math.sin(self.direction) * self.speed

        self.hitbox = pygame.Rect(self.pos[0] - self.hitRadius, self.pos[1] - self.hitRadius, 2 * self.hitRadius,
                                  2 * self.hitRadius)

    def draw(self):
        screen.blit(self.rotated_bullet, self.rotated_bullet.get_rect(center=self.pos))


######################################################################

def image_rotate(image, pos, originPos, angle):
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
    return rotated_image


def get_rotated_center(image, pos, originPos, angle):
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    return rotated_image_center


def rotate(image, pos, originPos, angle):
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
    return rotated_image_rect


def round_to_base(x, base=5):
    return base * round(x / base)


def abs(value):
    if value < 0:
        return -value
    else:
        return value


def drop_loot(x, y):
    items.append(DroppedCoins(x, y))


def spawnZombies():
    if len(enemies) < 4 + (dayCount * 2) and not dayTime:
        i = random.randint(1, 4)

        b = 80

        if i == 1:
            x = random.randint(0, WINDOW_W)
            y = -b
        elif i == 2:
            x = random.randint(0, WINDOW_W)
            y = WINDOW_H + b
        elif i == 3:
            x = -b
            y = random.randint(0, WINDOW_H)
        elif i == 4:
            x = WINDOW_W + b
            y = random.randint(0, WINDOW_H)
        enemies.append(Zombie(x, y, tileSize))


def placeObjects():
    i = 0
    while i < 11:
        if not (i == 6 or i == 7 or i == 8 or i == 1):
            objects.append(small_box_class(480 + (i * 32), 630, random.randint(0, 19)))
            objects.append(small_box_class(480 + (i * 32), 630 - (32 * 5), random.randint(0, 19)))
        i += 1
    objects.append(small_box_class(480 + (10 * 32), 630 - (32 * 4), random.randint(0, 19)))
    objects.append(small_box_class(480 + (10 * 32), 630 - 32, random.randint(0, 19)))

    objects.append(small_box_class(480, 630 - (32 * 4), random.randint(0, 19)))
    objects.append(small_box_class(480, 630 - (32 * 3), random.randint(0, 19)))

    objects.append(box_class(250, 100, -9))
    objects.append(tree_class(1000, 600, random.randint(0, 360)))


######################################################################

def update(mx, my):
    player.update(pygame.key.get_pressed(), mx, my)

    shop.update(mx, my)

    for bullet in bullets:
        bullet.move()
        if not bullet.hitbox.colliderect(pygame.Rect(-100, -100, WINDOW_W + 100, WINDOW_H + 100)):
            bullets.remove(bullet)

    for enemy in enemies:
        enemy.update()

    for item in items:
        item.update()

    for enemy in enemies:
        for bullet in bullets:
            if bullet.hitbox.colliderect(enemy.hitbox):
                enemy.health -= player.equippedGun.weapondmg
                if enemy.health <= 0:
                    drop_loot(enemy.hitbox.centerx, enemy.hitbox.centery)
                    player.killcount += 1
                    enemies.remove(enemy)
                bullets.remove(bullet)

    global lastSwitch
    global dayTime
    global dayCount

    ticks = pygame.time.get_ticks()
    timeSinceSwitch = (ticks - lastSwitch) / 1000
    if dayTime and timeSinceSwitch >= dayDurationSeconds:
        dayTime = False
        lastSwitch = ticks
    elif not dayTime and timeSinceSwitch >= nightDurationSeconds:
        dayTime = True
        lastSwitch = ticks
        dayCount += 1


def drawUI():
    pygame.draw.rect(screen, RED, pygame.Rect(80, 40, 300, 10), 1)
    pygame.draw.rect(screen, RED, pygame.Rect(80, 40, (300 / player.maxHP) * player.hp, 10))

    hp_text = font24.render(str(round(player.hp)), True, RED)
    hp_rect = hp_text.get_rect()
    screen.blit(hp_text, pygame.Rect(80, 15, hp_rect.width, hp_rect.height))

    max_hp_text = font16.render("/" + str(player.maxHP), True, RED)
    max_hp_rect = max_hp_text.get_rect()
    screen.blit(max_hp_text, pygame.Rect(80 + hp_rect.width, 20, max_hp_rect.width, max_hp_rect.height))

    screen.blit(player.pfp, (10, 15))

    ####### - items bottom left

    meds_txt = font16.render("medkits: " + str(round(player.medkits)), True, RED)
    meds_rect = meds_txt.get_rect()

    dmg_multi = font16.render("damage multiplier: " + str(round(shop.player_dmg_multi, 2)), True, RED)
    dmg_multi_rect = dmg_multi.get_rect()

    cd_multi = font16.render("coins / drop: " + str(round(coins_per_drop, 2)), True, RED)
    cd_multi_rect = cd_multi.get_rect()

    if smg.unlocked:
        smg_txt = font16.render("machine gun: unlocked", True, RED)
    else:
        smg_txt = font16.render("machine gun: locked", True, RED)
    smg_rect = smg_txt.get_rect()

    if revolver.unlocked:
        bpistol_txt = font16.render("revolver: unlocked", True, RED)
    else:
        bpistol_txt = font16.render("revolver: locked", True, RED)
    bpistol_rect = bpistol_txt.get_rect()

    screen.blit(meds_txt, pygame.Rect(30, 500, meds_rect.width, meds_rect.height))
    screen.blit(dmg_multi, pygame.Rect(30, 515, dmg_multi_rect.width, dmg_multi_rect.height))
    screen.blit(cd_multi, pygame.Rect(30, 530, cd_multi_rect.width, cd_multi_rect.height))
    screen.blit(smg_txt, pygame.Rect(30, 545, smg_rect.width, smg_rect.height))
    screen.blit(bpistol_txt, pygame.Rect(30, 560, bpistol_rect.width, bpistol_rect.height))

    coin_text = font16.render(
        "Coins: " + str(player.coins) + " | day: " + str(dayCount) + " | kills: " + str(player.killcount), True, YELLOW)
    coin_text_rect = coin_text.get_rect()
    screen.blit(coin_text, pygame.Rect(80, 60, coin_text_rect.width, coin_text_rect.height))

    screen.blit(player.pfp, (10, 10))

    ######## - ammo bar in bottom right of screen

    pygame.draw.rect(screen, RED, pygame.Rect(WINDOW_W * 0.85, WINDOW_H * 0.92, 100, 10), 1)

    ammo_text_rect = pygame.Rect((WINDOW_W * 0.85) + 100, (WINDOW_H * 0.9) - 20, 50, 50)
    ammo_text = font32.render(str(player.equippedGun.ammo_in_clip), True, WHITE)
    screen.blit(ammo_text, ammo_text_rect)

    if player.reloading:
        ammo_bar = pygame.Rect(WINDOW_W * 0.85, WINDOW_H * 0.92, (player.reloadingProgress), 10)
        pygame.draw.rect(screen, RED, ammo_bar)

        reloading_text = font16.render("reloading...", True, WHITE)
        reloading_rect = pygame.Rect(WINDOW_W * 0.85, (WINDOW_H * 0.92) - 20, 100, 10)

        screen.blit(reloading_text, reloading_rect)
        screen.blit(ammo_text, ammo_text_rect)
    else:
        pygame.draw.rect(screen, RED, pygame.Rect(WINDOW_W * 0.85, WINDOW_H * 0.92,
                                                  (100 / player.equippedGun.clipsize) * (
                                                      player.equippedGun.ammo_in_clip), 10))

    max_ammo_text = font16.render("/" + str(player.equippedGun.clipsize), True, WHITE)
    max_ammo_rect = pygame.Rect((WINDOW_W * 0.85) + 110, WINDOW_H * 0.92, 50, 20)

    screen.blit(max_ammo_text, max_ammo_rect)


def draw(mx, my):
    global show_hitboxes

    if dayTime:
        screen.fill(YELLOW)
    else:
        screen.fill(BLACK)
    screen.blit(map1, map1.get_rect())

    pygame.draw.rect(screen, YELLOW, upgrade_area, 1)

    for item in items:
        item.draw()

    player.draw()

    if show_hitboxes:
        pygame.draw.rect(screen, RED, player.hitbox, 1)

    for enemy in enemies:
        enemy.draw()

        if show_hitboxes:
            pygame.draw.rect(screen, RED, enemy.hitbox, 1)
            pygame.draw.line(screen, YELLOW, player.hitbox.center, enemy.hitbox.center)

    for obj in objects:
        obj.draw()
        if show_hitboxes:
            pygame.draw.rect(screen, RED, obj.hitbox, 1)

    for enemy in enemies:
        enemy.draw_hp_bar()

    for bullet in bullets:
        bullet.draw()

    if upgrade_area.collidepoint((player.hitbox.centerx, player.hitbox.centery)) and not shop.opened:
        if dayTime:
            text = font24.render("press E for shop", True, YELLOW)
        else:
            text = font24.render("shop closed", True, YELLOW)

        text_rect = text.get_rect()
        screen.blit(text, pygame.Rect(550, 110, text_rect.width, text_rect.height))
    elif shop.opened:
        shop.draw(mx, my)

    values = [0.1, 0.2, 0.5, 0.8]
    images = [dmg_image_4, dmg_image_3, dmg_image_2, dmg_image_1]
    for x in range(4):
        if player.hp < player.maxHP * values[x]:
            screen.blit(images[x], pygame.Rect(0, 0, WINDOW_W, WINDOW_H))
            break

    drawUI()


def run():
    drawInterval = 1_000_000_000 / targetFPS
    delta = 0
    lastTime = time.time_ns()

    playing = True

    mx, my = (0, 0)

    while playing:
        currentTime = time.time_ns()

        delta += (currentTime - lastTime) / drawInterval

        lastTIme = currentTime

        if delta >= 1:
            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        playing = False

                    case pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            player.holdingLeftMouse = True

                    case pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            player.holdingLeftMouse = False
                            shop.click(mx, my)
                    case pygame.KEYUP:
                        if event.key == pygame.K_f:
                            global show_hitboxes
                            if show_hitboxes:
                                show_hitboxes = False
                            else:
                                show_hitboxes = True

            spawnZombies()

            update(mx, my)
            draw(mx, my)

            pygame.display.flip()
            pygame.display.update()

            if player.hp <= 0:
                playing = False

                draw(mx, my)
                x = WINDOW_W / 2 - (gameover.get_width() / 2)
                y = WINDOW_H / 2 - (gameover.get_height() / 2)
                screen.blit(gameover, pygame.Rect(x, y, gameover.get_width(), gameover.get_height()))

                pygame.display.flip()
                pygame.display.update()

                while True:
                    for event in pygame.event.get():
                        match event.type:
                            case pygame.QUIT:
                                break


pistol = Pistol()
revolver = Revolver()
smg = SMG()

player = Player((WINDOW_W / 2), (WINDOW_H / 2), tileSize)
shop = Shop()

placeObjects()
run()
pygame.quit()
