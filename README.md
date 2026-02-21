# VSpipe-GUI – Interactive Graphical User Interface for Virtual Screening and Hit Selection

![License: CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)

## Overview

VSpipe-GUI is a cross platform, open source Python toolkit that provides a user friendly graphical interface for structure based virtual screening. The original VSpipe pipeline was a command line tool (VSpipe CLI). VSpipe-GUI builds on that workflow, adds spatial filtering of docked poses, and helps users select hit compounds based on binding site interactions while reducing unnecessary computation.

For background and performance benchmarks, see:

Hussain, R.; Hackett, A. S.; Álvarez-Carretero, S.; Tabernero, L. (2024).  
**VSpipe-GUI, an Interactive Graphical User Interface for Virtual Screening and Hit Selection.**  
*International Journal of Molecular Sciences* 25, 2002.  
https://doi.org/10.3390/ijms25042002

---

## Authors and affiliations

- **Rashid Hussain (R.H.)**  
  School of Biological Sciences, Faculty of Biology Medicine and Health  
  University of Manchester, Manchester Academic Health Science Centre  
  Manchester M13 9PT, UK  
  Email: rashid.bioinfo@gmail.com  

- **Andrew Scott Hackett (A.S.H.)**  
  School of Biological Sciences, Faculty of Biology Medicine and Health  
  University of Manchester, Manchester Academic Health Science Centre  
  Manchester M13 9PT, UK  
  Email: andrew.hackett-2@postgrad.manchester.ac.uk  

- **Sandra Álvarez-Carretero (S. Á. C.)**  
  Bristol Palaeobiology Group, School of Earth Sciences  
  University of Bristol, Life Sciences Building, Tyndall Avenue  
  Bristol BS8 1TH, UK  
  Email: sandra.ac93@gmail.com or s.alvarez-carretero@bristol.ac.uk  

- **Lydia Tabernero (L.T.)**  
  School of Biological Sciences, Faculty of Biology Medicine and Health  
  University of Manchester, Manchester Academic Health Science Centre  
  Manchester M13 9PT, UK  
  Email: lydia.tabernero@manchester.ac.uk  

---

## Installation guide

VSpipe-GUI can be run from source on Linux or via the bundled macOS app. The steps below give a complete, self contained recipe for both.

> You will need administrative privileges for the copy steps that install tools into `/usr/local/bin` and `/usr/local/lib`.

---

## 1. Linux and Ubuntu (from source)

These steps follow the layout used on the development machine, where everything is first placed in a working folder such as `~/0_vspipe/`.

### 1.1. Prepare source and tool files

Create a working directory and place the following items inside it:

- `vspipe-gui-linux_v002.py`  
  Main VSpipe-GUI Python script for Linux (v002).

- `vspipe-tools_mac/`  
  Folder containing the helper scripts used by VSpipe-GUI  
  (used on Linux as well despite the folder name).

- `sdf_add_code.py`  
  Helper script for SDF handling (if not already in `vspipe-tools_mac`).

- `minimised_libs/`  
  Folder with pre minimised compound libraries  
  (unzipped from `vspipe-libraries.zip` or distributed separately).

Typical layout:

```text
~/0_vspipe/
    vspipe-gui-linux_v002.py
    vspipe-tools_mac/
    sdf_add_code.py
    minimised_libs/
```

### 1.2. Step 1 – copy helper scripts and libraries

From inside your working directory:

```bash
cd ~/0_vspipe

# copy all VSpipe helper tools into /usr/local/bin
sudo cp -r vspipe-tools_mac/* /usr/local/bin/

# copy the SDF helper script if needed
sudo cp sdf_add_code.py /usr/local/bin/

# copy pre minimised libraries into /usr/local/lib
sudo cp -r minimised_libs /usr/local/lib/

# make sure everything is executable and readable
sudo chmod 755 /usr/local/bin/*.py
sudo chmod -R 755 /usr/local/lib/minimised_libs
```

After this step, all VSpipe helper scripts should be available system wide and the minimised libraries accessible to the GUI.

### 1.3. Step 2 – install required system dependencies

The following components are crucial for a working installation.

#### 1.3.1. Python

- System Python 3 (for the GUI itself):

  ```bash
  sudo apt update
  sudo apt install -y python3 python3-tk python3-pip
  ```

- Python 2.7 (for legacy helper scripts such as `datasheet.py`, `atom_deletion.py`, `pdbs_rename.py`):

  On newer Ubuntu releases Python 2.7 is not shipped by default. If your system does not provide `python2.7`, you have two options:

  1. Install Python 2.7 from source and ensure `/usr/local/bin/python2.7` exists.

  2. Port the legacy helper scripts to Python 3 and update the calls inside `vspipe-gui-linux_v002.py` from `python2.7` to `python3`.

  The current pipeline assumes that `python2.7` is available unless you have ported the tools.

#### 1.3.2. MGLTools and AutoDockTools scripts

VSpipe-GUI uses AutoDockTools scripts for receptor and ligand preparation:

- `prepare_receptor4.py`
- `prepare_ligand4.py`
- `prepare_gpf4.py`
- `prepare_dpf4.py`
- `summarize_results4.py`

Steps:

1. Download and install MGLTools from Scripps.

2. Locate the `pythonsh` executable from your MGLTools installation, for example:

   ```text
   /opt/mgltools_x.y.z/bin/pythonsh
   ```

3. Open each of the above scripts that you copied into `/usr/local/bin` and update the first line (shebang) so that it points to your `pythonsh` path. For example:

   ```python
   #! /opt/mgltools_x.y.z/bin/pythonsh
   ```

This allows the AutoDockTools preparation scripts to run correctly from within the GUI.

#### 1.3.3. R and Rscript

VSpipe-GUI uses an R script for filtering and scoring:

```bash
sudo apt install -y r-base
```

Check that `Rscript` is available:

```bash
Rscript --version
```

Any additional R packages required by `filtering.R` should be installed from within R using `install.packages()`.

#### 1.3.4. Open Babel

Open Babel is used for ligand preparation and format conversion:

```bash
sudo apt install -y openbabel
```

Confirm that `obabel` is on your path:

```bash
obabel -V
```

#### 1.3.5. Docking engines

VSpipe-GUI uses both AutoDock Vina and AutoDock 4.

- AutoDock Vina:

  ```bash
  sudo apt install -y autodock-vina
  vina --version
  ```

- AutoDock 4 and Autogrid 4:

  Download the AutoDock 4 distribution from Scripps and place `autodock4` and `autogrid4` in your path, for example `/usr/local/bin`:

  ```bash
  sudo cp autodock4 autogrid4 /usr/local/bin/
  sudo chmod 755 /usr/local/bin/autodock4 /usr/local/bin/autogrid4
  ```

### 1.4. Step 3 – install Python libraries

Inside a Python 3 environment (system Python or a virtual environment), install the libraries used by the GUI:

```bash
python3 -m pip install     numpy     pandas     scikit-spatial     openpyxl     biopython     pdb-tools
```

Additional libraries can be installed later if the GUI reports that something is missing.

### 1.5. Launching VSpipe-GUI on Linux

From your working directory:

```bash
cd ~/0_vspipe
python3 vspipe-gui-linux_v002.py
```

If all dependencies and tools are correctly installed, the VSpipe-GUI window should open and you can configure your project folders, receptor, libraries, and docking settings from the interface.

---

## 2. macOS (bundled app, v002)

For macOS users a bundled application is provided together with the same tool scripts and libraries.

### 2.1. Clone or download the repository

```bash
git clone https://github.com/rashid-bioinfo/vspipe-gui.git
cd vspipe-gui
```

Inside the repository (master branch) you will find:

- `vspipe-gui-mac_v002.py`  
  macOS launcher script for VSpipe-GUI.

- `vspipe-tools_mac/`  
  Folder containing the helper scripts used by the macOS app.

- `minimised_libs/`  
  Folder containing the pre minimised compound libraries.

### 2.2. Copy helper tools and libraries

Unzip the libraries if they were provided as an archive, then copy tools and libraries to standard locations:

```bash
# copy VSpipe helper tools
cd /path/to/vspipe-gui
sudo cp -r vspipe-tools_mac/* /usr/local/bin/
sudo chmod 755 /usr/local/bin/*

# copy minimised libraries
sudo cp -r minimised_libs /usr/local/lib/
sudo chmod -R 755 /usr/local/lib/minimised_libs
```

### 2.3. Install dependencies on macOS

You need the same core dependencies as on Linux:

1. **Python 3**

   Install via Homebrew or your preferred method:

   ```bash
   brew install python
   ```

2. **MGLTools**

   Install MGLTools, then locate the `pythonsh` executable. Update the shebang line in the following scripts in `/usr/local/bin`:

   - `prepare_receptor4.py`
   - `prepare_ligand4.py`
   - `prepare_gpf4.py`
   - `prepare_dpf4.py`
   - `summarize_results4.py`

   so that the first line points to your `pythonsh` path.

3. **R and Rscript**

   Install R:

   ```bash
   brew install --cask r
   ```

   Then install any additional packages used by `filtering.R` via `install.packages()` from within R.

4. **Open Babel**

   ```bash
   brew install open-babel
   ```

5. **AutoDock Vina and AutoDock 4**

   - Install AutoDock Vina via Homebrew or manually from Scripps and ensure `vina` is on your path.
   - Download AutoDock 4, then copy `autodock4` and `autogrid4` to `/usr/local/bin` and mark them executable.

6. **Python libraries**

   ```bash
   python3 -m pip install        numpy        pandas        scikit-spatial        openpyxl        biopython        pdb-tools
   ```

### 2.4. Launching VSpipe-GUI on macOS

From Terminal:

```bash
cd /path/to/vspipe-gui
python3 vspipe-gui-mac_v002.py
```

If the required tools are installed and on the path, the GUI should open and behave identically to the Linux version.

---

## 3. Legacy versions and additional materials

Older versions of VSpipe-GUI (including the original `Installation_Guide` and `Source_Files` folders) are preserved in the `legacy-old-version` branch of this repository. If you need legacy executables, example projects, or the original CLI pipeline, switch to that branch on GitHub or via:

```bash
git checkout legacy-old-version
```

---

## Citation

If you use VSpipe-GUI in your work, please cite:

> Hussain, R.; Hackett, A. S.; Álvarez-Carretero, S.; Tabernero, L. (2024).  
> VSpipe-GUI, an Interactive Graphical User Interface for Virtual Screening and Hit Selection.  
> *International Journal of Molecular Sciences* 25, 2002.  
> https://doi.org/10.3390/ijms25042002

---

## Contact

For questions, bug reports, or suggestions, please open an issue on GitHub or contact:

- rashid.bioinfo@gmail.com
