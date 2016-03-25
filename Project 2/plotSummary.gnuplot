#
set key off
set xlabel 'Min Degree'
set ylabel 'Max Degree'
splot 'summary' using 1:2:3 with points
pause -1
