import pyglet

window = pyglet.window.Window(resizable=True)
pyglet.lib.load_library('avbin')
pyglet.have_avbin=True

@window.event
def on_draw():
    player.get_texture().blit(0, 0)

if __name__ == "__main__":
    try:
        player = pyglet.media.Player()
        source = pyglet.media.load("C:\\Users\\Administrator\\desktop\\video.mp4")
        player.queue(source)
        player.play

        pyglet.app.run()
    except Exception as e:
        print (e)