# All measurements are in mm

# General measurements
thickness   = 1

base             = 10           # The base number system it will use
beads_per_column = base / 2
beads_above_bar  = 1
columns          = 10           # Determines the amount of digits

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

