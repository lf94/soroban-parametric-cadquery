from cadquery import *
from measurements import *
from parts import *

nozzle_diameter = 0.2
rib_height = nozzle_diameter * 2
hole_larger_radius = (column_hole + (rib_height * 2)) / 2

hole_with_ribs = (
  Workplane("XY")
  .circle(hole_larger_radius)
  .extrude(1)
  .polarArray(hole_larger_radius, 0, 360, 3)
  .circle(rib_height)
  .cutThruAll()
  .faces(">Z")
  .wires()
  .val()
)

frame_with_crush_rib = (
  frame
  .faces(">Y")
  .workplane()
  .pushPoints(column_holes)
  .eachpoint(lambda loc: hole_with_ribs.moved(loc), True)
  .cutBlind(-soroban_height)
)

# frame_with_fillet = (
#   frame_with_crush_rib
#   .faces()
#   .edges("|Z")
#   .fillet(3.0)
# )

frame_final = frame_with_crush_rib

exporters.export(frame_final, "../printable/frame.amf")
exporters.export(rod, "../printable/rod.amf")
exporters.export(bead, "../printable/bead.amf")

show_object(frame_final)
