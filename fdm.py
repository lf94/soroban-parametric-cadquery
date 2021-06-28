from cadquery import *
from measurements import *
from parts import *

frame_with_crush_rib = (
  frame
)

exporters.export(frame_with_crush_rib, "../printable/frame.amf")
exporters.export(rod, "../printable/rod.amf")
exporters.export(bead, "../printable/bead.amf")

show_object(frame_with_crush_rib)
