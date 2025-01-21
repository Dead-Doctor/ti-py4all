from ti_system import *
from ti_draw import *
from cmath import *
from math import log

view = 2
views = [
  (-0.5,0,1,False,1,100,100),
  (-0.8,-0.35,3,False,1,100,100),
  (-0.75,-0.1,10,False,1,100,100),
  (-0.75,-0.2,10,False,1,100,100),
  (-0.7436438870,-0.1318259042,1,True,5,400,200),
  (-0.7436438870,-0.1318259042,131072,False,1,400,100)
]

settings = views[view]
zoom = settings[2]
animate = settings[3]
speed = 2
center = complex(settings[0],settings[1])
resolution = settings[4]
max_iter = settings[5]
color_repetition = settings[6]
power = 2
r = 2
show_zoom = False
width, height = get_screen_dim()

def main():
  global zoom
  if animate: use_buffer()
  while True:
    scale = 1/(height/resolution)/zoom
    # this works without the cast on ti??? (seemingly ranges in for loops can accept floats)
    for y in range(int(height/resolution)):
      for x in range(int(width/resolution)):
        if get_key() == "esc":
          return
        re = (2*x-width/resolution)*scale
        im = (2*y-height/resolution)*scale
        offset = complex(re,im)
        pos = center + offset
        set_color(*pixel(pos))
        fill_rect(x*resolution,y*resolution,resolution,resolution)
    if show_zoom:
      set_color(255, 255, 255)
      draw_text(width-50,height - 8,zoom)
    if not animate:
      return
    paint_buffer()
    zoom *= speed

def pixel(pos):
  n = (mandelbrot(pos) % color_repetition) / color_repetition
  if n * 4 < 1:
    x = int((n*4)*255)
    return (x,0,0)
  elif n * 4 < 2:
    x = int((n*4-1)*255)
    return (255-x,x,0)
  elif n * 4 < 3:
    x = int((n*4-2)*255)
    return (0,255-x,x)
  else:
    x = int((n*4-3)*255)
    return (0,0,255-x)


def mandelbrot(c):
  z = 0
  n = 0
  while abs(z) <= r and n < max_iter:
    z = pow(z, power) + c
    n += 1
  if n == max_iter:
    return n
  return n - log(log(abs(z), r), power)

main()
