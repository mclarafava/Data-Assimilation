root
 |__ input_rainfall (don't touch it)
 |__ model (it is safe to delete the rainfall files. Keep the swmm file)

input_rainfall
==============
This folder keeps the original rainfall data values.

model
=====
This folder has the SWMM INP file. Also, when the optimiser starts, it copies
the content of the input_rainfall folder to this folder. Subsequently, these
files are replaced by the most recent optimised rainfall files.
