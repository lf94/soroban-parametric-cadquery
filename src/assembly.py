from cadquery import *
from measurements import *
from parts import *

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
