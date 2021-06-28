from cadquery import *
from measurements import *
from parts import *

frame_with_crush_rib = (
  frame
)

exporters.export(frame_with_crush_rib, "frame.amf")
exporters.export(rod, "rod.amf")
exporters.export(bead, "bead.amf")

show_object(frame_with_crush_rib)
