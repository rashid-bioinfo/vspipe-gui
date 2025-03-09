# VSpipe-GUI  
An Interactive Graphical User Interface for Virtual Screening and Hit Selection

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
