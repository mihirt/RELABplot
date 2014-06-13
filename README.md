RELABplot
=========

For plotting data from the Brown University RELAB database. 
Requires Matplotlib library on Python 2.7 (will not run on 3.x)
Matplotlib: http://matplotlib.org/
Python (2.7x): https://www.python.org/downloads/
If you have no previous experience with python, read below to understand how to use this software.

First, if you do not have python already on your computer, install it (the 2.x version). 
Once installed, go to the matplotlib page and install it as a library for python.

If you have not already done so, go to the RELAB database webpage and download the zip file. http://www.planetary.brown.edu/relabdata/ (Download the .zip file.)

Once done downloading, unzip the file (usually done by double clicking) and place it wherever you would like.
Now, go to the main page of this repository (https://github.com/iluvplanes/RELABplot) and on the right hand side click "Download as zip")

Double click on the .zip file, and locate the python program. It should be named RELAB_Plotter or something similar.
Now open the Relab Database file you downloaded earlier. You should see three items. Catalogue, Data, and ReadMeFirst.txt.
Place or paste the python file into this folder.

Now, go to the "catalogues" folder, and locate Sample_Catalogue.xls. This should open in Excel or a similar program. Locate the name of the Sample you would like to see data for. To the left of it, there should be an ID in the form of XX-XXX-000. Copy or remember this ID.

Now, open go back to the python file and open it. On windows, this should directly open into a command line interface. For Mac, right click (ctr+click) the file, navigate to "Open With..." and click python launcher. If two are given, click on the one that says 2.7.

Enter the ID number, and watch your plot be magically graphed!
