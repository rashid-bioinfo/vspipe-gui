# VSpipe-GUI, an Interactive Graphical User Interface for Virtual Screening and Hit Selection

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)

## Overview

VSpipe-GUI is a cross-platform, open-source Python toolkit that brings a user-friendly graphical interface to structure-based virtual screening. Originally developed as a command-line pipeline (VSpipe-CLI), VSpipe-GUI streamlines the virtual screening process, introduces spatial filtering to select hit compounds based on binding site interactions, and reduces computational overhead. For detailed background and performance benchmarks, please refer to our publication:

**Hussain, R.; Hackett, A.S.; Álvarez-Carretero, S.; Tabernero, L. (2024).**  
*VSpipe-GUI, an Interactive Graphical User Interface for Virtual Screening and Hit Selection.*  
International Journal of Molecular Sciences, **25**, 2002.  
[https://doi.org/10.3390/ijms25042002](https://doi.org/10.3390/ijms25042002)

## Installation Guide

To get started with VSpipe-GUI, follow these installation steps:

### Prerequisites
- **Operating System:**  
  VSpipe-GUI has been tested on Ubuntu 20.04, Windows 10 (via Windows Subsystem for Linux), and macOS (High Sierra and later).
- **Python:**  
  Ensure you have Python 3 installed.
- **Dependencies:**  
  Required Python libraries and third-party tools (e.g., AutoDock Vina, Open Babel) are detailed in the [Installation Guide](https://github.com/rashid-bioinfo/vspipe-gui/tree/master/Installation_Guide).

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/rashid-bioinfo/vspipe-gui.git
   cd vspipe-gui


   # VSpipe – GUI Installation Guide for Mac

## Accessing and Downloading VSpipe-GUI Repository

- **Access the GitHub repository**
- **Clone or navigate to the `Executables/Mac/` directory** and download the repository containing the following files:
  - `vspipe-gui-mac-app` (executable file; can be run either through Terminal or directly by double-clicking on the app)
  - `vspipe-tools/` (directory containing all required files to run the `vspipe-gui-mac-app` application)
- **Clone or download** the `vspipe-libraries.zip` file. It contains already minimized libraries provided by VSpipe-GUI.

## Installation of Dependencies Needed to Run VSpipe-GUI

1. [Python](https://www.python.org/downloads/macos/)
2. [MGL Tools](https://ccsb.scripps.edu/mgltools/downloads/)
3. [Rscript](https://cran.r-project.org/bin/macosx/)

## Step-by-Step Guide

*Note: You need to have administrative privileges to install VSpipe-GUI.*

1. **Locate the Path of MGL Tools**

   You will need to locate the path of MGL Tools and find out the path of the file `pythonsh`.

   - For example, on the current machine, this path is:
     ```
     /Users/lydiatabernero/Downloads/mgltools_1.5.7_MacOS-X/bin/pythonsh
     ```
     *(This path will change depending on where you have installed MGL Tools.)*

2. **Execute the Following Commands**

   - Change directory to `vspipe-tools/`:
     ```bash
     cd vspipe-tools/
     ```
   - Open the following Python scripts with TextEdit to update their header lines with the correct path to `pythonsh`:
     - `prepare_receptor4.py`:
       ```bash
       open -a TextEdit prepare_receptor4.py
       ```
     - `prepare_ligand4.py`:
       ```bash
       open -a TextEdit prepare_ligand4.py
       ```
     - `prepare_dpf4.py`:
       ```bash
       open -a TextEdit prepare_dpf4.py
       ```
     - `prepare_gpf4.py`:
       ```bash
       open -a TextEdit prepare_gpf4.py
       ```
     - `summarize_results4.py`:
       ```bash
       open -a TextEdit summarize_results4.py
       ```
   - Then, execute the following commands in Terminal:
     ```bash
     sudo cp * /usr/local/bin/
     sudo chmod 777 -R /usr/local/bin/
     unzip vspipe-libraries.zip
     sudo cp -r minimised_libs /usr/local/lib/
     sudo chmod 777 -R /usr/local/lib/minimised_libs/
     ```

## Launching VSpipe-GUI

- Once you have followed the instructions above, double-click on the `vspipe-gui-mac-app` icon to launch the VSpipe GUI.
- **Important:** Change the header line in each script with the correct path (as defined in Step 1), then update and save the file.

