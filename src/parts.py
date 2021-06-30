from cadquery import *
from measurements import *

base = (
  Workplane("XY")
  .rect(soroban_width, soroban_height)
  .extrude(soroban_depth)
)

with_base_cut = (
  base
  .faces(">Z")
  .wires()
  .toPending()
  .workplane()
  .offset2D(-thickness)
  .cutThruAll()
)

with_bar = (
  with_base_cut
  .faces(">X")
  .workplane()
  .transformed(offset=(soroban_height / -2, soroban_depth / -2, 0))
  .moveTo(bar_pos_y, 0)
  .rect(bar_height, soroban_depth)
  .extrude(-soroban_width)
)

with_holes_in_base = (
  with_bar
  .faces(">Y")
  .workplane()
  .pushPoints(column_holes)
  .hole(column_hole)
)

frame = with_holes_in_base

rod = (
  Workplane("XY")
  .transformed(rotate=(90, 0, 0))
  .circle(column_hole / 2)
  .extrude(soroban_height)
)

bead = (
  Workplane("XY")
  .circle(bead_dmaj / 2)
  .transformed(offset=(0, 0, bead_height))
  .circle(bead_dmin / 2)
  .loft()
  .faces(">Z") # Cut a hole through it for the rod to go through
  .workplane()
  .hole(column_hole)
)

