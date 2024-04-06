controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    if (my_sprite.isHittingTile(CollisionDirection.Bottom)) {
        my_sprite.vy = -125
    }
    
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile
    `, function on_overlap_tile(sprite: Sprite, location: tiles.Location) {
    my_sprite.vy = -125
})
let my_sprite : Sprite = null
my_sprite = sprites.create(assets.image`
    myImage
`, SpriteKind.Player)
controller.moveSprite(my_sprite, 100, 0)
my_sprite.ay = 250
scene.cameraFollowSprite(my_sprite)
tiles.setCurrentTilemap(tilemap`level1`)
tiles.placeOnTile(my_sprite, tiles.getTileLocation(0, 14))
