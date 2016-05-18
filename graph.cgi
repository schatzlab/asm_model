#!/bin/bash

## Get the genome size to model
###############################################################################

g=1234567

if [ $# -gt 0 ]
then
  g=$1
fi


# Generate data given genome length, and predict
###############################################################################

rm ./dat/test.dat
rm ./dat/test.idx

for l in 3700 7500 15000 30000 60000 120000 240000 480000; do 
  for c in 5 10 20 40; do 
    echo $g $l $c |  awk '{printf "0 1:%f 2:%f\n", (log($1)/log($2))/2.6924, log($3)/3.6889}' >> ./dat/test.dat
    echo $l $c >> ./dat/test.idx
  done;
done;

/var/libsvm-3.21/svm-predict -q ./dat/test.dat ./model/model.all.f2.rbf.mdl ./dat/test.prd


# Create plot data file and render with gnuplot
###############################################################################

paste ./dat/test.idx ./dat/test.prd | sed 's/\t/ /g' | awk '{if($3<0) print $1, $2, 0; else if($3>100) print $1, $2, 100 ; else printf "%d %d %.2f\n", $1, $2, $3}' > ./dat/test.plt

echo 'Content-Type: image/png'
echo 

/usr/bin/gnuplot << EOF

set terminal png size 640, 1080 enhanced font ",20"  

set style line 1 lt 2 lc rgb "red" lw 2 
set style line 2 lt 2 lc rgb "orange" lw 2
set style line 3 lt 2 lc rgb "yellow" lw 2
set style line 4 lt 2 lc rgb "green" lw 2
set style line 5 lt 2 lc rgb "blue" lw 2

set style line 6 lt 2 lc rgb "#ffd700" lw 2
set style line 7 lt 2 lc rgb "#9acd32" lw 2
set style line 8 lt 2 lc rgb "#6b8e23" lw 2
set style line 9 lt 2 lc rgb "#006400" lw 2

set multiplot layout 1,2 

#settitle "Assembly Prediction of Genome Size $g" font ",20" 

#change background of all subgraph
set object 1 rectangle from graph 0, graph 0 to graph 1, graph 1 behind fc rgbcolor '#E0E0E0' fs noborder
set size 1, 0.45
set origin 0.01, 0.5

#set xtics font "arial, 9"
#set ytics font "arial, 9"
set xtics font ", 12"
set ytics font ", 12"
set yrange[0:101]
set key box
set key right bottom
set key spacing 2.5 
#set key font "arial,9" 
set key font ",10" 
set grid ytics lt 1 lw 2 lc rgb "#ffffff"
set grid xtics lt 1 lw 2 lc rgb "#ffffff"
#set ylabel "Performance(%)" font "arial, 10"
#set ylabel "Performance(%)" font ", 12"

### first graph

set xrange[0:45]
set title "Assembly Performance by Coverage " font ",20" 
set xlabel "Coverage" font ", 12"
set ylabel "Performance" font ", 12"

set object 2 rect from 33.9,2 to 44.4,19.5 behind fc rgb "white" fs solid border lw 0 

plot 'dat/test.plt' every ::12::15 using 2:3 with linespoints ls 5 ti " mean 30,000", \
     'dat/test.plt' every ::8::11 using 2:3 with linespoints ls 4 ti " mean 15,000", \
     'dat/test.plt' every ::4::7 using 2:3 with linespoints ls 2 ti " mean 7,500", \
     'dat/test.plt' every ::0::3 using 2:3 with linespoints ls 1 ti " mean 3,700"

### second graph

set size 1, 0.45
set origin 0.01, 0

set xrange[0:31000]
set title "Assembly Performance By Read Length" font ", 20"
set xlabel "Read Length" font ", 12"

set object 3 rect from 25230,2 to 30600,19.5 behind fc rgb "white" fs solid border lw 0 

plot 'dat/test.plt' every 4::3 using 1:3 with linespoints ls 6 ti " cov 40", \
     'dat/test.plt' every 4::2 using 1:3 with linespoints ls 7 ti " cov 20", \
     'dat/test.plt' every 4::1 using 1:3 with linespoints ls 8 ti " cov 10", \
     'dat/test.plt' every 4::0 using 1:3 with linespoints ls 9 ti " cov 5"

EOF

