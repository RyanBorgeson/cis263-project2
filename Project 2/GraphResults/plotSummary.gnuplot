#
set key off
set xlabel 'Diameter'
set ylabel 'Size Max Clique'
splot 'summary' using 1:2:3 with points
pause -1
