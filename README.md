# asm_model: Statistical Modeling and Prediction of Genome Assembly Quality
Developed by Hayan Lee and Michael Schatz

Third-generation long-range DNA sequencing and mapping technologies are
creating a renaissance in high-quality genome sequencing. Unlike
second-generation sequencing, which produces short reads a few hundred
base-pairs long, third-generation single-molecule technologies generate over
10,000 bp reads or map over 100,000 bp molecules. We analyze how increased
read lengths can be used to address long-standing problems in de novo genome
assembly, structural variation analysis and haplotype phasing.  We then
undertake a meta-analysis of the currently available 3rd generation genome
assemblies, a retrospective analysis of the development of the reference human 
genome, and simulations with dozens of species across the tree of life. From 
these data, we develop a new predictive model of genome assembly presented
as an online web-service that can accurately estimate the performance of 
a genome assembly project using different technologies

Preprint of the paper available here:
http://www.biorxiv.org/content/early/2016/04/13/048603

Online version available here:
http://qb.cshl.edu/asm_mode/


Installation directions

1. Install libsvm to /var/libsvm using the tarball in the install directory
2. Install gnuplot
3. Edit graph.sh with the paths to svm-predict and gnuplot
