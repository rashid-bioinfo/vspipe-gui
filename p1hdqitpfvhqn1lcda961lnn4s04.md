VSpipe -- GUI Installation Guide for Mac

Accessing and downloading VSpipe-GUI repository

-   Access the GitHub repository

-   Clone or go to the path or Executables/Mac/, and download the repo
    containing following files

    -   *vspipe-gui-mac-app* (executable file and can be run either
        through terminal or directly by double clicking on the app)

    -   *vspipe-tools/* (directory containing all required files to run
        vspipe-gui-mac-app application)

-   Clone or download *vspipe-libraries.zip* file. It contains already
    minimized libraries provided by vspipe-gui

Installation of dependencies needed to run VSpipe-GUI

1.  Python (<https://www.python.org/downloads/macos/>)

2.  MGL Tools (<https://ccsb.scripps.edu/mgltools/downloads/>)

3.  Rscript (<https://cran.r-project.org/bin/macosx/>)

Step-by-Step guide

Once you have downloaded above mentioned files/directories from the
repo, do the following steps:

**Note:** You need to have administrative privileges to install
vspipe-gui

1.  You will need to locate the path of MGL tools and find out the path
    of a file '**pythonsh**'

    -   For example, in current machine, this path is:

*/Users/lydiatabernero/Downloads/mgltools_1.5.7_MacOS-X/bin/pythonsh*

(This path will be changed depends on where you have installed MGL
tools)

2\. Give following commands.

-   cd vspipe-tools/

-   open -a TextEdit prepare_receptor4.py

> (Change the header as shown in figure below)

-   open -a TextEdit prepare_ligand4.py

> (Change the header as shown in figure below)

-   open -a TextEdit prepare_dpf4.py

> (Change the header as shown in figure below)

-   open -a TextEdit prepare_gpf4.py

> (Change the header as shown in figure below)

-   open -a TextEdit summarize_results4.py

> (Change the header as shown in figure below)

-   sudo cp \* /usr/local/bin/

-   sudo chmod 777 -R /usr/local/bin/

-   unzip vspipe-libraries.zip

-   sudo cp -r minimised_libs /usr/local/lib/

-   sudo chmod 777 -R /usr/local/lib/minimised_libs/

Launching Vspipe-GUI

> Once you have followed the instructions above, double click on the
> **vspipe-gui-mac-app** icon to launch the VSpipe
> GUI.![](./image1.png){width="4.0in"
> height="2.375in"}![](./image2.png){width="4.572916666666667in"
> height="2.2916666666666665in"}
