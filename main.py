def on_up_pressed():
    if my_sprite.is_hitting_tile(CollisionDirection.BOTTOM):
        my_sprite.vy = -125
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite, location):
    my_sprite.vy = -125
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile)

my_sprite: Sprite = None
my_sprite = sprites.create(assets.image("""
    myImage
"""), SpriteKind.player)
controller.move_sprite(my_sprite, 100, 0)
my_sprite.ay = 250
scene.camera_follow_sprite(my_sprite)
tiles.set_current_tilemap(tilemap("""level1"""))
tiles.place_on_tile(my_sprite, tiles.get_tile_location(0, 14))