# All measurements are in mm

# General measurements
thickness   = 7

base             = 10           # The base number system it will use
beads_per_column = base / 2
beads_above_bar  = 1
columns          = 1           # Determines the amount of digits

# Bead measurements
bead_height = 8
bead_dmaj   = 8                 # Large diameter of the bead
bead_dmin   = bead_dmaj / 1.66  # Small diameter of the bead

column_hole = bead_dmin / 1.66
bead_hole = column_hole + 0.2 * 2

# Vertical spacing for beads below and above the bar
bead_vspace_below = 8
bead_vspace_above = 6

# Horizontal spacing for the beads
bead_hspace = 4

# Bar measurements
bar_height  = 4
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

soroban_depth = 7

# Where the holes will be
column_holes = [
  (
    thickness + bead_dmaj / 2 + bead_hspace + (bead_dmaj + bead_hspace) * n,
    0
  )
  for n in range(columns)
]
