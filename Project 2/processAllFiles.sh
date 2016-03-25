#!/bin/bash
# If the file results exists from a previous
# execution of the script, remove it.
if [ -f results ]; then
  rm results
fi
# If the file summary exists from a previous
# execution of the script, remove it.
if [ -f summary ]; then
  rm summary
fi
# For all the files, execute the python script
# that finds the min and max degree for every file
# Store the results in the file results
for i in {0..1043}
do
    python MaxMinDegrees.py f$i >> results
done
# Now summarize the results in a file called summary
awk ' { sum[$1][$2] = sum[$1][$2]+1}  \
END {for (i in sum) for (j in sum[i]) print i,j,sum[i][j]} ' \
results | sort -n > summary
