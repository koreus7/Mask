#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals

import pi3d
import time

# Setup display and initialise pi3d
DISPLAY = pi3d.Display.create(x=0, y=0, w=-100, h=-100,
#                          background = (1, 1, 1, 1))
                         background = (0.0, 0.0, 0.0, 1))

shader = pi3d.Shader('shaders/custom')
#========================================

# load model_loadmodel
mymodel = pi3d.Model(file_string='models/faceModel.obj',
                name='face', x=0, y=-1, z=40,
                sx=2.5, sy=2.5, sz=2.5)
                #sx=0.005, sy=0.005, sz=0.005)
mymodel.set_shader(shader)

# Fetch key presses
mykeys = pi3d.Keyboard()

start_time = time.time()
es = 0
delta = 1
noiseTex = pi3d.Texture("textures/cnoise1.jpg")
post = pi3d.PostProcess("shaders/filter_paint", add_tex=[noiseTex], scale=0.5)
post1 = pi3d.PostProcess("shaders/filter_hatch")


while True:  
  newes = (time.time() - start_time)
  delta = newes - es
  es = newes

  DISPLAY.clear()

  post.sprite.set_custom_data(48, [es])
  post.start_capture()##<<<<<<<<<<<<<<
  mymodel.draw()
  post.end_capture()##>>>>>>>>>>>>>>
  post1.start_capture()
  post.draw()
  
  post1.end_capture()
  post1.draw()

  mymodel.rotateIncY(0.21)

  mymodel.set_custom_data(48, [es])

  k = mykeys.read()
  if k >-1:
    if k==112: pi3d.screenshot('screen.jpg')
    elif k==27:
      mykeys.close()
      DISPLAY.destroy()
      break
    else:
      print(k)

  DISPLAY.swap_buffers()
