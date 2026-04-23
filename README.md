<p align="center">
  <h1 align="center">VSpipe-GUI</h1>
  <p align="center">
    <b>An Interactive Graphical User Interface for Virtual Screening and Hit Selection</b><br>
    <i>Structure-based drug discovery · Molecular docking · Hit prioritisation</i>
  </p>
</p>

<p align="center">
  <a href="https://doi.org/10.3390/ijms25042002">
    <img src="https://img.shields.io/badge/DOI-10.3390%2Fijms25042002-blue?style=flat-square" alt="DOI">
  </a>
  <a href="https://www.mdpi.com/1422-0067/25/4/2002">
    <img src="https://img.shields.io/badge/Journal-Int.%20J.%20Mol.%20Sci.%202024-green?style=flat-square" alt="Journal">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/R-Filtering%20%26%20Plots-276DC3?style=flat-square&logo=r&logoColor=white" alt="R">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20macOS-lightgrey?style=flat-square" alt="Platform">
  <a href="https://creativecommons.org/licenses/by/4.0/">
    <img src="https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey?style=flat-square" alt="License">
  </a>
</p>

---

## Abstract

VSpipe-GUI is a cross-platform, open-source Python application that provides an accessible graphical interface for structure-based virtual screening. Built upon the original VSpipe command-line pipeline, it extends the workflow with spatial pose filtering and interaction-based hit selection — enabling researchers to prioritise compounds for experimental validation without requiring command-line expertise. The software integrates AutoDock Vina and AutoDock 4 docking engines, automates physicochemical property extraction and Lipinski filtering, computes nine ligand efficiency metrics per compound, and generates publication-quality diagnostic plots. It has been validated against established benchmarking datasets.

> **Published in** *International Journal of Molecular Sciences* (2024) — peer-reviewed, open access.  
> Hussain, R.; Hackett, A. S.; Álvarez-Carretero, S.; Tabernero, L. *Int. J. Mol. Sci.* **2024**, *25*, 2002. https://doi.org/10.3390/ijms25042002

---

## Table of Contents

- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [Scoring Metrics](#scoring-metrics)
- [Bundled Compound Libraries](#bundled-compound-libraries)
- [Output Files](#output-files)
- [Helper Scripts Reference](#helper-scripts-reference)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [1. Linux / Ubuntu (from source)](#1-linux--ubuntu-from-source)
  - [2. macOS (from source)](#2-macos-from-source)
  - [3. Legacy versions](#3-legacy-versions-and-additional-materials)
- [Usage](#usage)
- [Citation](#citation)
- [Authors](#authors)
- [License](#license)

---

## Key Features

| Feature | Description |
|---|---|
| **Graphical Interface** | Tkinter-based GUI — no command-line required for routine screening |
| **Dual Docking Engine Support** | Compatible with AutoDock Vina and AutoDock 4 |
| **Receptor Preparation** | Automated PDB cleaning, chain extraction, metalloprotein handling, PDBQT correction |
| **Ligand Preparation** | SDF parsing, unsupported-atom removal, Lipinski / custom Rule-of-Five filtering, PDBQT conversion |
| **Spatial Pose Filtering** | Filters docked poses by geometric proximity to a user-defined binding site |
| **Nine Ligand Efficiency Metrics** | Computes δG, Ki, LE, BEI, SEI, NSEI, NBEI, nBEI, mBEI per compound |
| **Post-docking Filtering** | Filter and rank results by any of 16 physicochemical or scoring parameters |
| **Diagnostic Plots** | Auto-generates PDF plots (NSEI–NBEI, SEI–BEI, MW, PSA, cLogP, HBA distributions) |
| **ATLAS-Compatible Output** | Exports results in ATLAS-ready format |
| **Batch Screening** | Supports screening of large compound libraries |
| **Bundled Libraries** | Ships with 10 pre-minimised fragment and natural product libraries |
| **Cross-Platform** | Runs on Linux, macOS and Windows|

---

## How It Works

VSpipe-GUI orchestrates a multi-step virtual screening pipeline through four GUI modules:

```
┌─────────────────────────────────────────────────────────────┐
│                        VSpipe-GUI                           │
│                                                             │
│  ┌──────────────────┐    ┌──────────────────┐               │
│  │ 1. Receptor Prep │    │ 2. Ligand Prep   │               │
│  │                  │    │                  │               │
│  │ • PDB cleaning   │    │ • SDF parsing    │               │
│  │ • Chain extract  │    │ • Atom filtering │               │
│  │ • Metal handling │    │ • Lipinski RO5   │               │
│  │ • PDBQT convert  │    │ • PDBQT convert  │               │
│  └────────┬─────────┘    └────────┬─────────┘               │
│           │                       │                         │
│           └──────────┬────────────┘                         │
│                      ▼                                      │
│           ┌──────────────────────┐                          │
│           │  3. Docking Engine   │                          │
│           │                      │                          │
│           │  AutoDock Vina  ──►  │  .pdbqt poses            │
│           │  AutoDock 4     ──►  │  .dlg / .pdbqt           │
│           └──────────┬───────────┘                          │
│                      ▼                                      │
│           ┌──────────────────────┐                          │
│           │  4. Results & Filter │                          │
│           │                      │                          │
│           │  • Metric extraction │  output.csv / .tsv       │
│           │  • Spatial filtering │  lowest_energy_pdb/      │
│           │  • Property filter   │  ordered_output.*        │
│           │  • PDF plots         │  NSEI-NBEI.pdf etc.      │
│           └──────────────────────┘                          │
└─────────────────────────────────────────────────────────────┘
```

### Receptor preparation pipeline

1. `clean_protein.py` — extracts the first protein chain from the input PDB, writes `*_clean.pdb`
2. `adding_metal_ion.py` — handles metalloprotein targets: extracts chain, waters, and metal ion into a clean PDB
3. `adding_metal_charge.py` — assigns correct AutoDock charge type to metal ions in the PDBQT file
4. `receptor_pdbqt_correction.py` — validates and corrects column alignment in receptor PDBQT files to prevent docking failures
5. AutoDockTools `prepare_receptor4.py` — final PDBQT preparation via MGLTools

### Ligand preparation pipeline

1. `atom_deletion.py` — scans canonical SMILES in the SDF and removes compounds containing atoms unsupported by AutoDock force fields
2. `datasheet.py` — parses SDF files, extracts physicochemical properties (MW, cLogS, cLogP, HBD, HBA, PSA, rotatable bonds), applies Lipinski Rule of Five or user-defined thresholds, outputs `output.csv` and `output.tsv`
3. `to_sdf_correction.py` — inserts compound code IDs into SDF files when not present
4. `pdbs_rename.py` — renames PDB files according to compound code IDs from the SDF
5. AutoDockTools `prepare_ligand4.py` — PDBQT preparation; `prepare_gpf4.py` / `prepare_dpf4.py` — grid and docking parameter file generation

### Docking parameter automation

- `generating_correct_dpf.py` — auto-generates docking parameter files (DPF) from the receptor GPF, resolving ligand type compatibility
- `dpf_rewrite.py` — patches receptor and ligand paths in GPF/DPF files; sets `unbound_model` to `bound`
- `creating_etc_dir.py` — builds the `docking.list` file required for multi-node AutoDock 4 runs

### Post-docking analysis

- `values_extraction_vina.py` — parses Vina log and PDBQT output; extracts lowest-energy pose; calculates δG, Ki, LE, BEI, SEI, NSEI, NBEI, nBEI, mBEI; writes lowest-energy pose to `lowest_energy_pdb/`
- `values_extraction_AD4.py` — equivalent pipeline for AutoDock 4 DLG output
- `filtering.R` — filters and ranks compounds by any of 16 parameters; generates six PDF diagnostic plots; exports filtered results in CSV, TSV, and ATLAS formats

---

## Scoring Metrics

For every docked compound, VSpipe-GUI computes the following metrics (written to `output.csv` / `output.tsv`):

| Column | Metric | Definition |
|---|---|---|
| `DG` | Free energy of binding (δG) | kcal/mol; lower is better |
| `Ki` | Inhibition constant | μmol/L; calculated from δG at 298.15 K using *R* = 1.987 × 10⁻³ kcal/mol·K |
| `LIGAND_EFFICIENCY` | Ligand efficiency (LE) | δG / number of heavy atoms |
| `BEI` | Binding efficiency index | pKi / MW (kDa) |
| `SEI` | Surface efficiency index | pKi / PSA (100 Å²) |
| `NSEI` | Normalised SEI | pKi / number of polar atoms |
| `NBEI` | Normalised BEI | pKi / number of heavy atoms |
| `nBEI` | nBEI | −log(Ki / heavy atoms) |
| `mBEI` | mBEI | −log(Ki / MW in kDa) |

**Physicochemical properties** extracted per compound from the SDF file:

`MolecularWeight` · `cLogS` · `cLogP` · `HBD` · `HBA` · `PSA` · `ROTATABLE_BONDS`

**Post-docking filtering** (`filtering.R`) supports all 16 columns above. Filtering operators: `>value`, `<value`, or `min,max` range. Results are automatically ordered by δG when no filter is applied.

**Diagnostic PDF plots** generated automatically:

| Plot file | Content |
|---|---|
| `NSEI-NBEI.pdf` | NSEI vs NBEI scatter plot with compound labels |
| `SEI-BEI.pdf` | SEI vs BEI scatter plot with compound labels |
| `MW-numComp.pdf` | Molecular weight frequency distribution |
| `PSA-numComp.pdf` | PSA frequency distribution |
| `clogP-NumComp.pdf` | cLogP frequency distribution |
| `NumHBA-NumComp.pdf` | Hydrogen bond acceptor frequency distribution |

---

## Bundled Compound Libraries

VSpipe-GUI ships with ten pre-minimised, ready-to-dock compound libraries in `minimised_libs/`:

| Library | Description |
|---|---|
| `ENAMINE_fragment_library` | Enamine fragment library |
| `Indofine_Natural_Products` | Indofine natural products collection |
| `Maybridge_Pre_Fragment_COCL_PFP` | Maybridge pre-fragment (acyl chloride / PFP ester) |
| `Maybridge_Pre_Fragment_NCO` | Maybridge pre-fragment isocyanate set |
| `Maybridge_Pre_Fragment_NCO_min` | Minimised Maybridge NCO fragments |
| `Maybridge_Pre_Fragment_NCO_min_4comp` | 4-component minimised NCO fragments |
| `Maybridge_Pre_Fragment_SO2Cl` | Maybridge pre-fragment sulfonyl chloride set |
| `Maybridge_Ro3_1000_Fragment_Library` | Maybridge Rule-of-Three 1000-compound fragment library |
| `Maybridge_Ro3_500_Fragment_Library` | Maybridge Rule-of-Three 500-compound fragment library |
| `Specs_Natural_Products` | Specs natural products collection |

Custom libraries in SDF or SMILES format can be used by loading them through the Ligand Preparation module.

---

## Output Files

After a completed screening run, the results directory contains:

| File / Directory | Description |
|---|---|
| `output.csv` / `output.tsv` | Full results table: all physicochemical properties + nine scoring metrics |
| `ordered_output.csv` / `.tsv` | Results sorted by δG (no filter applied) |
| `ordered_output_ATLAS.txt` | ATLAS-compatible output: CodeID; SMILES; Ki type; Ki value |
| `ordered_filt_output.csv` / `.tsv` | Filtered and sorted results (when a filter is applied) |
| `lowest_energy_pdb/` | Lowest-energy docked pose for each compound as a PDB file |
| `NSEI-NBEI.pdf` | Scatter plot: NSEI vs NBEI |
| `SEI-BEI.pdf` | Scatter plot: SEI vs BEI |
| `MW-numComp.pdf` | MW distribution histogram |
| `PSA-numComp.pdf` | PSA distribution histogram |
| `clogP-NumComp.pdf` | cLogP distribution histogram |
| `NumHBA-NumComp.pdf` | HBA distribution histogram |

---

## Helper Scripts Reference

All helper scripts reside in `vspipe-tools_mac/` and are called internally by the GUI.

| Script | Language | Function |
|---|---|---|
| `clean_protein.py` | Python 3 | Extracts first protein chain from PDB |
| `adding_metal_ion.py` | Python 3 | Extracts chain + waters + metal ion for metalloprotein targets |
| `adding_metal_charge.py` | Python 3 | Assigns correct AutoDock charge type to metal ions in PDBQT |
| `receptor_pdbqt_correction.py` | Python 3 | Validates and corrects PDBQT column alignment |
| `atom_deletion.py` | Python 2.7 | Removes compounds with unsupported atoms from SDF |
| `datasheet.py` | Python 2.7 | Parses SDF; extracts physicochemical properties; applies RO5 filter; writes `output.csv` / `output.tsv` |
| `to_sdf_correction.py` | Python 2.7 | Inserts compound code IDs into SDF files |
| `pdbs_rename.py` | Python 2.7 | Renames PDB files by compound code ID |
| `values_extraction_vina.py` | Python 3 | Extracts δG, Ki, LE, BEI/SEI/NBEI/nBEI/mBEI from Vina output |
| `values_extraction_AD4.py` | Python 3 | Extracts same metrics from AutoDock 4 DLG output |
| `generating_correct_dpf.py` | Python 3 | Auto-generates docking parameter file (DPF) from receptor GPF |
| `dpf_rewrite.py` | Python 3 | Patches receptor/ligand paths in GPF/DPF; sets `unbound_model` to `bound` |
| `creating_etc_dir.py` | Python 3 | Builds `docking.list` for multi-node AutoDock 4 runs |
| `filtering.R` | R | Filters ranked results; generates six PDF diagnostic plots |
| `prepare_receptor4.py` | AutoDockTools | Receptor PDBQT preparation (MGLTools) |
| `prepare_ligand4.py` | AutoDockTools | Ligand PDBQT preparation (MGLTools) |
| `prepare_gpf4.py` | AutoDockTools | Grid parameter file generation (MGLTools) |
| `prepare_dpf4.py` | AutoDockTools | Docking parameter file generation (MGLTools) |
| `summarize_results4.py` | AutoDockTools | Summarises AutoDock 4 results |

---

## Prerequisites

The following tools must be installed and available on your `PATH` before running VSpipe-GUI.

| Dependency | Version | Purpose | Verify |
|---|---|---|---|
| Python 3.x | ≥ 3.6 | GUI runtime + most helper scripts | `python3 --version` |
| Python 2.7 | 2.7.x | Legacy helper scripts (`atom_deletion.py`, `datasheet.py`, `pdbs_rename.py`) | `python2.7 --version` |
| MGLTools / AutoDockTools | ≥ 1.5.6 | Receptor & ligand PDBQT preparation | `pythonsh` path required |
| AutoDock Vina | ≥ 1.1.2 | Docking engine | `vina --version` |
| AutoDock 4 + AutoGrid 4 | ≥ 4.2 | Docking engine | binaries in `/usr/local/bin` |
| Open Babel | ≥ 2.4 | Format conversion | `obabel -V` |
| R + Rscript | ≥ 3.5 | Post-docking filtering and plots | `Rscript --version` |

**Python packages** (installed via `requirements.sh`):

```
numpy  pandas  scikit-spatial  openpyxl  biopython  pdb-tools
```

---

## Installation

> **Requirement:** Administrative privileges are needed for steps that install tools into `/usr/local/bin` and `/usr/local/lib`.

---

### 1. Linux / Ubuntu (from source)

These steps follow the layout used on the development machine, where everything is first placed in a working folder such as `~/0_vspipe/`.

#### 1.1 Prepare source and tool files

Create a working directory and place the following items inside it:

- `vspipe-gui-linux_v002.py`  
  Main VSpipe-GUI Python script for Linux (v002).

- `vspipe-tools_mac/`  
  Folder containing the helper scripts used by VSpipe-GUI  
  (used on Linux as well despite the folder name).

- `sdf_add_code.py`  
  Helper script for SDF handling (if not already in `vspipe-tools_mac`).

- `minimised_libs/`  
  Folder with pre-minimised compound libraries  
  (unzipped from `vspipe-libraries.zip` or distributed separately).

- `requirements.sh`  
  Convenience script for installing Python dependencies.

Typical layout:

```text
~/0_vspipe/
    vspipe-gui-linux_v002.py
    vspipe-tools_mac/
    sdf_add_code.py
    minimised_libs/
    requirements.sh
```

#### 1.2 Install required system and Python dependencies

Install all dependencies first, then copy the VSpipe tools and libraries.

##### 1.2.1 Python

- **System Python 3** (for the GUI itself):

  ```bash
  sudo apt update
  sudo apt install -y python3 python3-tk python3-pip
  ```

- **Python 2.7** (for legacy helper scripts: `atom_deletion.py`, `datasheet.py`, `pdbs_rename.py`):

  On newer Ubuntu releases Python 2.7 is not shipped by default. If your system does not provide `python2.7`, you have two options:

  1. Install Python 2.7 from source and ensure `/usr/local/bin/python2.7` exists.
  2. Port the legacy helper scripts to Python 3 and update the calls inside `vspipe-gui-linux_v002.py` from `python2.7` to `python3`.

  The current pipeline assumes that `python2.7` is available unless you have ported the tools.

##### 1.2.2 MGLTools and AutoDockTools scripts

VSpipe-GUI uses AutoDockTools scripts for receptor and ligand preparation:

- `prepare_receptor4.py`
- `prepare_ligand4.py`
- `prepare_gpf4.py`
- `prepare_dpf4.py`
- `summarize_results4.py`

Steps:

1. Download and install [MGLTools](https://ccsb.scripps.edu/mgltools/) from Scripps.

2. Locate the `pythonsh` executable from your MGLTools installation, for example:

   ```text
   /opt/mgltools_x.y.z/bin/pythonsh
   ```

3. After copying these scripts into `/usr/local/bin` (see Step 1.3), open each one and update the first line (shebang) so that it points to your `pythonsh` path. For example:

   ```python
   #! /opt/mgltools_x.y.z/bin/pythonsh
   ```

This allows the AutoDockTools preparation scripts to run correctly from within the GUI.

##### 1.2.3 R and Rscript

VSpipe-GUI uses an R script for post-docking filtering, ranking, and plot generation:

```bash
sudo apt install -y r-base
```

Check that `Rscript` is available:

```bash
Rscript --version
```

Any additional R packages required by `filtering.R` should be installed from within R using `install.packages()`.

##### 1.2.4 Open Babel

Open Babel is used for ligand preparation and format conversion:

```bash
sudo apt install -y openbabel
```

Confirm that `obabel` is on your path:

```bash
obabel -V
```

##### 1.2.5 Docking engines

VSpipe-GUI uses both AutoDock Vina and AutoDock 4.

- **AutoDock Vina:**

  ```bash
  sudo apt install -y autodock-vina
  vina --version
  ```

- **AutoDock 4 and AutoGrid 4:**

  Download the AutoDock 4 distribution from [Scripps](https://autodock.scripps.edu/) and place `autodock4` and `autogrid4` in your path, for example `/usr/local/bin`:

  ```bash
  sudo cp autodock4 autogrid4 /usr/local/bin/
  sudo chmod 755 /usr/local/bin/autodock4 /usr/local/bin/autogrid4
  ```

##### 1.2.6 Python libraries

**Option A – using `requirements.sh` (recommended)**

From inside your working directory:

```bash
cd ~/0_vspipe   # folder containing requirements.sh
chmod +x requirements.sh
./requirements.sh
```

This script installs all Python packages required by VSpipe-GUI. Open it in a text editor to see exactly what it installs.

**Option B – manual installation**

```bash
python3 -m pip install \
    numpy \
    pandas \
    scikit-spatial \
    openpyxl \
    biopython \
    pdb-tools
```

Additional libraries can be installed later if the GUI reports that something is missing.

#### 1.3 Copy helper scripts and libraries

Once all dependencies are in place, copy the helper scripts and minimised libraries:

```bash
# Copy all VSpipe helper tools into /usr/local/bin
sudo cp -r vspipe-tools_mac/* /usr/local/bin/

# Copy the SDF helper script
sudo cp sdf_add_code.py /usr/local/bin/

# Copy pre-minimised libraries into /usr/local/lib
sudo cp -r minimised_libs /usr/local/lib/

# Make everything executable and readable
sudo chmod 755 /usr/local/bin/*.py
sudo chmod -R 755 /usr/local/lib/minimised_libs
```

After this step, all VSpipe helper scripts are available system-wide and the minimised libraries are accessible to the GUI. You can now also adjust the shebang lines in the AutoDockTools scripts as described in Section 1.2.2.

#### 1.4 Launch VSpipe-GUI on Linux

From your working directory:

```bash
cd ~/0_vspipe
python3 vspipe-gui-linux_v002.py
```

If all dependencies and tools are correctly installed, the VSpipe-GUI window will open and you can configure your project folders, receptor, libraries, and docking settings from the interface.

---

### 2. macOS (from source)

#### 2.1 Clone or download the repository

```bash
git clone https://github.com/rashid-bioinfo/vspipe-gui.git
cd vspipe-gui
```

Inside the repository you will find:

- `vspipe-gui-mac_v002.py`  
  macOS launcher script for VSpipe-GUI.

- `vspipe-tools_mac/`  
  Folder containing the helper scripts used by the macOS app.

- `minimised_libs/`  
  Folder containing the pre-minimised compound libraries.

- `requirements.sh`  
  Script for installing Python dependencies.

#### 2.2 Install dependencies on macOS

You need the same core dependencies as on Linux:

1. **Python 3**

   Install via [Homebrew](https://brew.sh/):

   ```bash
   brew install python
   ```

2. **MGLTools**

   Download and install [MGLTools](https://ccsb.scripps.edu/mgltools/) from Scripps, then locate the `pythonsh` executable.

3. **R and Rscript**

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
   - Download AutoDock 4 from [Scripps](https://autodock.scripps.edu/), then copy `autodock4` and `autogrid4` to `/usr/local/bin` and mark them executable.

6. **Python libraries**

   Using `requirements.sh` (recommended):

   ```bash
   cd /path/to/vspipe-gui
   chmod +x requirements.sh
   ./requirements.sh
   ```

   Or manually:

   ```bash
   python3 -m pip install \
       numpy \
       pandas \
       scikit-spatial \
       openpyxl \
       biopython \
       pdb-tools
   ```

#### 2.3 Copy helper tools and libraries on macOS

Unzip the libraries if they were provided as an archive, then copy tools and libraries to standard locations:

```bash
cd /path/to/vspipe-gui

# Copy VSpipe helper tools
sudo cp -r vspipe-tools_mac/* /usr/local/bin/
sudo chmod 755 /usr/local/bin/*

# Copy minimised libraries
sudo cp -r minimised_libs /usr/local/lib/
sudo chmod -R 755 /usr/local/lib/minimised_libs
```

After copying, update the shebang line in the following scripts in `/usr/local/bin` so that the first line points to the correct `pythonsh` from your MGLTools installation:

- `prepare_receptor4.py`
- `prepare_ligand4.py`
- `prepare_gpf4.py`
- `prepare_dpf4.py`
- `summarize_results4.py`

#### 2.4 Launch VSpipe-GUI on macOS

```bash
cd /path/to/vspipe-gui
python3 vspipe-gui-mac_v002.py
```

If the required tools are installed and on the path, the GUI will open and behave identically to the Linux version.

---

### 3. Legacy versions and additional materials

Older versions of VSpipe-GUI (including the original `Installation_Guide` and `Source_Files` folders) are preserved in the `legacy-old-version` branch of this repository. If you need legacy executables, example projects, or the original CLI pipeline, switch to that branch on GitHub or via:

```bash
git checkout legacy-old-version
```

---

## Usage

Once launched, the GUI presents four sequential modules:

### Module 1 — Receptor Preparation

- Load a PDB file and define the project output directory
- Optionally fetch a PDB structure by accession ID
- Enable metalloprotein mode to retain metal ions and coordinating waters
- The GUI calls `clean_protein.py`, `adding_metal_ion.py`, `adding_metal_charge.py`, `receptor_pdbqt_correction.py`, and `prepare_receptor4.py` in sequence

### Module 2 — Ligand Preparation

- Select a bundled pre-minimised library or load a custom SDF / SMILES file
- Configure Lipinski Rule-of-Five thresholds (default: MW < 500, cLogP < 5, HBD < 5, HBA < 10, PSA < 150, RotBonds < 8) or disable filtering
- The GUI calls `atom_deletion.py`, `datasheet.py`, `to_sdf_correction.py`, `pdbs_rename.py`, and `prepare_ligand4.py`

### Module 3 — Docking

- Set the docking engine (AutoDock Vina or AutoDock 4)
- Define grid box centre coordinates and dimensions
- Configure number of runs / exhaustiveness
- The GUI generates GPF/DPF files via `prepare_gpf4.py`, `generating_correct_dpf.py`, and `dpf_rewrite.py`, then runs the docking engine

### Module 4 — Results and Filtering

- After docking, values are extracted via `values_extraction_vina.py` or `values_extraction_AD4.py`
- Apply spatial filtering to retain only poses within a user-defined distance of the binding site
- Apply property-based filtering (any of 16 parameters) via `filtering.R`
- Results exported as CSV, TSV, ATLAS format, and PDF diagnostic plots

For detailed workflow documentation and benchmarking data, refer to the published paper:  
[https://doi.org/10.3390/ijms25042002](https://doi.org/10.3390/ijms25042002)

---

## Citation

If you use VSpipe-GUI in your research, please cite:

```
Hussain, R.; Hackett, A. S.; Álvarez-Carretero, S.; Tabernero, L. (2024).
VSpipe-GUI, an Interactive Graphical User Interface for Virtual Screening and Hit Selection.
International Journal of Molecular Sciences, 25, 2002.
https://doi.org/10.3390/ijms25042002
```

**BibTeX:**

```bibtex
@article{hussain2024vspipegui,
  author    = {Hussain, Rashid and Hackett, Andrew Scott and
               {\'A}lvarez-Carretero, Sandra and Tabernero, Lydia},
  title     = {{VSpipe-GUI}, an Interactive Graphical User Interface for
               Virtual Screening and Hit Selection},
  journal   = {International Journal of Molecular Sciences},
  volume    = {25},
  pages     = {2002},
  year      = {2024},
  doi       = {10.3390/ijms25042002}
}
```

---

## Authors

- **Rashid Hussain (R.H.)**  
  School of Biological Sciences, Faculty of Biology Medicine and Health  
  University of Manchester, Manchester Academic Health Science Centre, Manchester M13 9PT, UK  
  [rashid.bioinfo@gmail.com](mailto:rashid.bioinfo@gmail.com)

- **Andrew Scott Hackett (A.S.H.)**  
  School of Biological Sciences, Faculty of Biology Medicine and Health  
  University of Manchester, Manchester Academic Health Science Centre, Manchester M13 9PT, UK  
  [andrew.hackett-2@postgrad.manchester.ac.uk](mailto:andrew.hackett-2@postgrad.manchester.ac.uk)

- **Sandra Álvarez-Carretero (S.Á.C.)**  
  Bristol Palaeobiology Group, School of Earth Sciences  
  University of Bristol, Life Sciences Building, Tyndall Avenue, Bristol BS8 1TH, UK  
  [sandra.ac93@gmail.com](mailto:sandra.ac93@gmail.com) · [s.alvarez-carretero@bristol.ac.uk](mailto:s.alvarez-carretero@bristol.ac.uk)

- **Lydia Tabernero (L.T.)**  
  School of Biological Sciences, Faculty of Biology Medicine and Health  
  University of Manchester, Manchester Academic Health Science Centre, Manchester M13 9PT, UK  
  [lydia.tabernero@manchester.ac.uk](mailto:lydia.tabernero@manchester.ac.uk)

For questions, bug reports, or feature requests, please [open an issue](https://github.com/rashid-bioinfo/vspipe-gui/issues) or contact [rashid.bioinfo@gmail.com](mailto:rashid.bioinfo@gmail.com) or [vspipe.local@gmail.com](mailto:vspipe.local@gmail.com).

---

## License

This software is released under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) licence. You are free to share and adapt the material provided appropriate credit is given.

---

<p align="center">
  <i>Developed at the University of Manchester · Published in Int. J. Mol. Sci. (2024)</i>
</p>
