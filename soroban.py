from cadquery import *

# All measurements are in mm

# General measurements
thickness   = 1

base             = 10           # The base number system it will use
beads_per_column = base / 2
beads_above_bar  = 1
columns          = 3            # Determines the amount of digits

# Bead measurements
bead_height = 2
bead_dmaj   = 2                 # Large diameter of the bead
bead_dmin   = bead_dmaj / 1.66  # Small diameter of the bead

column_hole = bead_dmin / 1.66

# Vertical spacing for beads below and above the bar
bead_vspace_below = 3
bead_vspace_above = 2

# Horizontal spacing for the beads
bead_hspace = 1

# Bar measurements
bar_height  = 1
bar_pos_y   = (
    thickness
  + (bead_height * (beads_per_column - 1))
  + bead_vspace_below
  + (bar_height / 2)
)

# Calculate the dimensions of the soroban
# These measurements were figured out on paper, I am not figuring them out in
# real time here.
soroban_height = (
    bar_height
  + (2 * thickness)
  + (bead_height * beads_per_column)
  + bead_vspace_below
  + bead_vspace_above
)

soroban_width = (
  thickness
  + bead_hspace
  + ((bead_dmaj + bead_hspace) * columns)
  + thickness
)

soroban_depth = 1

# Start to model the soroban

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

column_holes = [
  (
    thickness + bead_dmaj / 2 + bead_hspace + (bead_dmaj + bead_hspace) * n,
    0
  )
  for n in range(columns)
]

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

# At this point the whole soroban is defined and modelled.
# Now you can assemble the soroban pieces to see if it all goes together.

soroban = (
  Assembly()
  .add(frame, name="frame")
)

for c in range(int(columns)):
  soroban.add(rod, name="r{}".format(c))
  soroban.constrain(
    "r{}".format(c),
    rod.faces(">Y").val(),
    "frame",
    frame.faces(">Y").edges("%CIRCLE").vals()[c],
    "Plane"
  )

for c in range(int(columns)):
  for b in range(int(beads_per_column - beads_above_bar)):
    bead_n = (beads_per_column * c) + b
    soroban.add(bead, name="b{}".format(bead_n))
    soroban.constrain(
      "b{}".format(bead_n),
      bead.faces("<Z").val(),
      "r{}".format(c),
      rod.faces("<Y").val(),
      "Axis"
    )
    soroban.constrain(
      "b{}".format(bead_n),
      bead.faces(">Z").val(),
      "r{}".format(c),
      Vertex.makeVertex(0, -soroban_height + (b * bead_height) + thickness, 0),
      "Point"
    )

for c in range(int(columns)):
  for b in range(int(beads_per_column)):
    bead_n = (beads_per_column * c) + b
    if b != beads_per_column - 1:
      continue
    soroban.add(bead, name="b{}".format(bead_n))
    soroban.constrain(
      "b{}".format(bead_n),
      bead.faces(">Z").val(),
      "r{}".format(c),
      rod.faces("<Y").val(),
      "Axis"
    )
    soroban.constrain(
      "b{}".format(bead_n),
      bead.faces(">Z").val(),
      "r{}".format(c),
      Vertex.makeVertex(0, -thickness, 0),
      "Point"
    )

soroban.solve()

show_object(soroban)
