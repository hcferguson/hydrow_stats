hydrow_stats
=============

hydrow_stats.py is a simple python script to fetch a hydrow workout from the
URL that hydrow provides, extract the workout data and reformat it into a string
of tab-separated values. An alternate specified can be provided.

Usage::

python hydrow_stats.py https://members.hydrow.com/shared/workouts/kVMWXYMnEYXd8Ko 

or, to separate with commas:: 

python hydrow_stats.py https://members.hydrow.com/shared/workouts/kVMWXYMnEYXd8Ko --sep ', '

Output of the comma-separated version::

2020-12-26T15:28:41.421Z, HarryF, 1228.25, 300.000, 122.2, 26, 199, 82, 104, Aquil Abdullah, Assessment Row


