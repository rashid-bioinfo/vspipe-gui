# Importing Modules 
from __future__ import division # Module used for spatial filtering
from distutils.log import error
from tkinter import *
# from Bio.PDB import *   #for fetching pdb file through pdb id
from tkinter import ttk
from turtle import st     # for implementation of tabs 
from tkinter import messagebox
from tkinter import filedialog
from turtle import right
# from PIL import ImageTk, Images
import os
import time

# ----
from tkinter.messagebox import showinfo
from tkinter import Button, ttk
from tkinter.messagebox import askyesno
from tkinter.messagebox import showerror, showinfo, showwarning
import tkinter.messagebox as tmsg # for dialogue box

# # Spatial Filtering Modules import
# from asyncore import write
# from cProfile import label
# from distutils.command.config import config
# from fileinput import filename
# import math as mean
# from sre_parse import State
# from turtle import clear, end_fill
# import numpy as nx
# from string import*
# from itertools import islice
# import shutil 
# import csv
# import pandas as pd
# import glob
# from skspatial.objects import Plane
# from skspatial.objects import Points
# from skspatial.plotting import plot_3d
# import math

# ==========================================



print ("\n|-------------------------------------------------------------------|")
print ("\n|          VSpipe - Graphical User Interface                        |")
print ("\n|-------------------------------------------------------------------|")
print ("\n|                      Mac version                                  |")
print ("\n|-------------------------------------------------------------------|")
print ("\n| Pipeline designed and developed by:                               |")
print ("\n| Rashid Hussain, Andrew Hackett, Sandra Alvarez-Carretero,         |")
print ("\n| Hira Khalid, and Lydia Tabernero                                  |")
print ("\n|                                                                   |")
print ("\n| Pipeline currently maintained by:                                 |")
print ("\n| Rashid Hussain & Sandra Alvarez-Carretero                         |")
print ("\n|                                                                   |")
print ("\n| School of Biological Sciences, Faculty of Biology Medicine        |")
print ("\n| and Health, The University of Manchester.                         |")
print ("\n| Manchester M13 9PT, UK                                            |")
print ("\n|                                                                   |")
print ("\n|                                                                   |")
print ("\n| You can find a tutorial and the manual for VSpipe here:           |")
print ("\n| Command line interface: https://github.com/sabifo4/VSpipe         |")
print ("\n|                                                                   |")
print ("\n| If you have further questions or need to report a bug, please     |")
print ("\n| send a message to:                                                |")
print ("\n| send a message to:                                                |")
print ("\n|    vspipe.local@gmail.com                                         |")
print ("\n|    rashid.bioinfo@gmail.com                                       |")
print ("\n|                     Happy Docking! :)                             |")
print ("\n|-------------------------------------------------------------------|\n\n")

##----------------------------------------------------------------------##
##                                                                      ##           
#                   TKINTER GUI BELOW - Main GUI                         #
##                                                                      ##
##----------------------------------------------------------------------##

class VSPipeInterface:
    def __init__(self, master):

        self.master = master 

        #------------------------------------------------------ ----##           
        #                   Creating Menu in GUI                     #
        ##----------------------------------------------------------##

        main_menu=Menu(root)

        file_menu = Menu(main_menu)
        file_menu.add_command(label="Load session", command=self.dummy)
        file_menu.add_command(label="Save session", command=self.dummy)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit)
        main_menu.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(main_menu)
        help_menu.add_command(label="Generating GPF file", command=self.dummy)
        main_menu.add_cascade(label="Help", menu=help_menu)

        main_menu.add_command(label="Cite", command=self.dummy)

        root.config(menu=main_menu)
        ##----------------------------------------------------------------------##           
        #                             Title Frame (Top)                          #
        ##----------------------------------------------------------------------##

        self.f1 = Frame(self.master, borderwidth=5, relief=SUNKEN)
        self.f1.pack(side="top", pady=10)

        self.f1_title = Label(self.f1, text="VSpipe - Virtual Screening Toolkit", font="Roman 16 bold", fg="#660099")
        self.f1_title.grid(row=1, column=5, sticky=W, padx=125)

        #----------------------------------------------------------------------##           
        #                     File Input Frame (Top down)                        #
        ##----------------------------------------------------------------------##

        self.f2 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f2.pack(anchor="nw", padx=20, pady=8, fill=X)

        ### -----   Labels for Inputing file ----- ###
        self.f2_outDir = Label(self.f2, text="Project Directory: ", font="Roman 12 bold")
        self.f2_recep = Label(self.f2, text="Receptor File: ", font="Roman 12 bold")
        self.f2_compLib = Label(self.f2, text="Library Directory: ", font="Roman 12 bold")
        self.f2_outDir.grid(row=1, sticky=W, padx=10, pady=5, ipadx=3, ipady=3)
        self.f2_recep.grid(row=2, sticky=W, padx=10, pady=5, ipadx=15, ipady=2)
        self.f2_compLib.grid(row=3, sticky=W, padx=10, pady=5, ipadx=3, ipady=3)
        
        ### -----   Entry Widgets for Inputing file ----- ###
        self.recep_value = StringVar()
        global compLib_value
        compLib_value = StringVar()
        global outDir_value
        outDir_value = StringVar()
        self.outDir_entry = Entry(self.f2, textvariable=outDir_value, width=21)
        self.recep_entry = Entry(self.f2, textvariable=self.recep_value, width=21)
        self.compLib_entry = Entry(self.f2, textvariable=compLib_value, width=21)
        self.outDir_entry.grid(row=1, column=2, padx=10, pady=5)
        self.recep_entry.grid(row=2, column=2, padx=10, pady=5)
        self.compLib_entry.grid(row=3, column=2, padx=10, pady=5)

        ### -----   Browse buttons for Inputing file (Ready)----- ###
        self.outDir_button = Button(self.f2, text="Define", font="Roman 13 bold", fg="green", command=self.output_directory)
        self.recep_button = Button(self.f2, text="Load", font="Roman 13 bold", fg="green", command=self.receptor_file)
        self.compLib_button = Button(self.f2, text="Load", font="Roman 13 bold", fg="green", command=self.compounds_library)
        self.outDir_button.grid(row=1, column=3, padx=5, pady=5, ipadx=5)
        self.recep_button.grid(row=2, column=3, padx=5, pady=5, ipadx=9)
        self.compLib_button.grid(row=3, column=3, padx=5, pady=5, ipadx=9)

        ### -----   Buttons to open modules
        filter_results = Button(self.f2, text="Filter", font="Roman 13 bold", fg="purple", command=self.FilterModule)
        recep_prep = Button(self.f2, text="Prepare", font="Roman 13 bold", fg="purple", command=self.ReceptorPrepModule)
        compLib_prep = Button(self.f2, text="Prepare", font="Roman 13 bold", fg="purple", command=self.LigandPrepModule)
        filter_results.grid(row=1, column=4, padx=5, pady=5, ipadx=11)
        recep_prep.grid(row=2, column=4, padx=5, pady=5, ipadx=2)
        compLib_prep.grid(row=3, column=4, padx=5, pady=5, ipadx=2)

        ##----------------------------------------------------------------------##           
        #                    Parameters Input Frame (Bottom up)                  #
        ##----------------------------------------------------------------------##

        self.f3 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f3.pack(anchor="nw", padx=20, pady=8, fill=X)

        ### -----   Labels for Parameters' Values ----- ###
        self.f3_xDim = Label(self.f3, text="x-Dim: ")
        self.f3_yDim = Label(self.f3, text="y-Dim: ")
        self.f3_zDim = Label(self.f3, text="z-Dim: ")
        self.f3_xCen = Label(self.f3, text="x-Cent: ")
        self.f3_yCen = Label(self.f3, text="y-Cent: ")
        self.f3_zCen = Label(self.f3, text="z-Cent: ")
        self.f3_xDim.grid(row=1, column=1, padx=7, pady=5)
        self.f3_yDim.grid(row=2, column=1, padx=3, pady=5)
        self.f3_zDim.grid(row=3, column=1, padx=3, pady=5)
        self.f3_xCen.grid(row=1, column=3, padx=3, pady=5)
        self.f3_yCen.grid(row=2, column=3, padx=3, pady=5)
        self.f3_zCen.grid(row=3, column=3, padx=3, pady=5)

        ### -----   Entry Widgets for Parameters' Values ----- ###
        self.param_file = StringVar() # *gpf requires for AD4 docking
        self.xDim_value = DoubleVar()
        self.yDim_value = DoubleVar()
        self.zDim_value = DoubleVar()
        self.xCen_value = DoubleVar()
        self.yCen_value = DoubleVar()
        self.zCen_value = DoubleVar()
        self.xDim_entry = Entry(self.f3, textvariable=self.xDim_value, width=13)
        self.yDim_entry = Entry(self.f3, textvariable=self.yDim_value, width=13)
        self.zDim_entry = Entry(self.f3, textvariable=self.zDim_value, width=13)
        self.xCen_entry = Entry(self.f3, textvariable=self.xCen_value, width=13)
        self.yCen_entry = Entry(self.f3, textvariable=self.yCen_value, width=13)
        self.zCen_entry = Entry(self.f3, textvariable=self.zCen_value, width=13)
        self.xDim_entry.grid(row=1, column=2, padx=3, pady=5)
        self.yDim_entry.grid(row=2, column=2, padx=3, pady=5)
        self.zDim_entry.grid(row=3, column=2, padx=3, pady=5)
        self.xCen_entry.grid(row=1, column=4, padx=3, pady=5)
        self.yCen_entry.grid(row=2, column=4, padx=3, pady=5)
        self.zCen_entry.grid(row=3, column=4, padx=3, pady=5)

        ### -----   Buttons for saving and loading Parameters' values ----- ###
        self.load_button = Button(self.f3, text="Load Parameters", fg="green", font="Roman 11 bold", command=self.load_parameters)
        self.save_button = Button(self.f3, text="Save Parameters", font="Roman 11 bold", command=self.save_parameters)
        self.load_button.grid(row=1,column=5, padx=10, pady=5, ipady=3)
        self.save_button.grid(row=2,column=5, padx=10, pady=5, ipady=3)

        ##----------------------------------------------------------------------##           
        #    Docking Type & Docking Metods (blind/targeted) (vina/autodock)      #
        ##----------------------------------------------------------------------##

        self.f4 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f4.pack(anchor="nw", padx=20, pady=8, fill=X)

        ### -----   Define type and method of docking (Labels) ----- ###
        self.docking_type = Label(self.f4, text="Docking Type: ", font="Roman 12 bold")
        self.docking_type.grid(row=1, sticky=W, padx=7, pady=5, ipadx=7)
        self.docking_method = Label(self.f4, text="Docking Method: ", font="Roman 12 bold")
        self.docking_method.grid(row=2, sticky=W, padx=7, pady=5)
        ### -----   Define type and method of docking (Radio Buttons - blind/targeted) ----- ###
        self.dockType_value = IntVar(value=1)
        self.blind_dock = Radiobutton(self.f4, text="Blind", bg="#999999", font="Roman 12", variable=self.dockType_value, value=1)
        self.targeted_dock = Radiobutton(self.f4, text="Targeted",  bg="#999999", font="Roman 12", variable=self.dockType_value, value=2, command=self.dummy)
        self.blind_dock.grid(row=1, column=2, sticky=W, padx=70, pady=5)
        self.targeted_dock.grid(row=1, column=3, sticky=W, padx=10, pady=5)
        ### -----   Define type and method of docking (Radio Buttons - vina/autodock) ----- ###
        self.dockMethod_value = IntVar(value=1)
        self.vina_dock = Radiobutton(self.f4, text="Vina", bg="#999999", font="Roman 12", variable=self.dockMethod_value, value=1)
        self.autodock_dock = Radiobutton(self.f4, text="Autodock",  bg="#999999", font="Roman 12", variable=self.dockMethod_value, value=2, command=self.dummy)
        self.vina_dock.grid(row=2, column=2, sticky=W, padx=70, pady=5)
        self.autodock_dock.grid(row=2, column=3, sticky=W, padx=10, pady=5)


        ##----------------------------------------------------------------------##           
        #                   Lipinski's Rule of Five (Frame - lipin (yes/no))     #
        ##----------------------------------------------------------------------##

        self.f5 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f5.pack(anchor="nw", padx=20, pady=8, fill=X) 
        # Lipinki - label
        self.lipin_label = Label(self.f5, text="Lipinski's Rule: ", font="Roman 12 bold")
        self.lipin_label.grid(row=1, sticky=W, pady=1, padx=7, ipadx=5)
        # Lipinski's radio buttons
        self.lipin_value = IntVar(value=1)
        self.lipin_no = Radiobutton(self.f5, text="No",  bg="#999999", font="Roman 12", variable=self.lipin_value, value=1, command=self.apply_lipinRules)
        self.lipin_default = Radiobutton(self.f5, text="Default",  bg="#999999", font="Roman 12", variable=self.lipin_value, value=2, command=self.apply_lipinRules)
        self.lipin_custom = Radiobutton(self.f5, text="Custom",  bg="#999999", font="Roman 12", variable=self.lipin_value, value=3, command=self.apply_lipinRules)
        self.lipin_no.grid(row=1, column=2, sticky=W, padx=30, pady=5)
        self.lipin_default.grid(row=1, column=2, sticky=W, padx=110, pady=5)
        self.lipin_custom.grid(row=1, column=2, sticky=W, padx=220, pady=1)

        ##----------------------------------------------------------------------##           
        #               Lipinski's Rule of Five (Frame - lipin (parameters))     #
        ##----------------------------------------------------------------------##

        self.f6 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f6.pack(anchor="nw", padx=20, pady=3, fill=X)
        
      
        
        # Lipinski's parameters' labels
        self.mw_label = Label(self.f6, text="MW: < ")
        self.logp_label = Label(self.f6, text="LogP: < ")
        self.tpsa_label = Label(self.f6, text="TPSA: < ")
        self.hbd_label = Label(self.f6, text="HBD: < ")
        self.hba_label = Label(self.f6, text="HBA: < ")
        self.rtb_label = Label(self.f6, text="RTB: < ")
        self.mw_label.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        self.logp_label.grid(row=1, column=3, padx=5, pady=3)
        self.tpsa_label.grid(row=1, column=5, padx=5, pady=3)
        self.hbd_label.grid(row=2, column=1, padx=5, pady=3)
        self.hba_label.grid(row=2, column=3, padx=5, pady=3)
        self.rtb_label.grid(row=2, column=5, padx=5, pady=3)

        ### Lipinski's parameters' values
        self.mw_value = DoubleVar()
        self.logp_value = DoubleVar()
        self.tpsa_value = DoubleVar()
        self.hbd_value = DoubleVar()
        self.hba_value = DoubleVar()
        self.rtb_value = DoubleVar()
        self.mw_entry = Entry(self.f6, textvariable=self.mw_value, width=9)
        self.logp_entry = Entry(self.f6, textvariable=self.logp_value, width=9)
        self.tpsa_entry = Entry(self.f6, textvariable=self.tpsa_value, width=9)
        self.hbd_entry = Entry(self.f6, textvariable=self.hbd_value, width=9)
        self.hba_entry = Entry(self.f6, textvariable=self.hba_value, width=9)
        self.rtb_entry = Entry(self.f6, textvariable=self.rtb_value, width=9)
        self.mw_entry.grid(row=1, column=2, padx=5, pady=3)
        self.logp_entry.grid(row=1, column=4, padx=5, pady=3)
        self.tpsa_entry.grid(row=1, column=6, padx=5, pady=3)
        self.hbd_entry.grid(row=2, column=2, padx=5, pady=3)
        self.hba_entry.grid(row=2, column=4, padx=5, pady=3)
        self.rtb_entry.grid(row=2, column=6, padx=5, pady=3)

        # Lipinski's properties
        self.lipin_prop = Button(self.f6, text="?", fg="black", font="Roman 10 bold", borderwidth=1, command=self.lipin_desc)
        self.lipin_prop.grid(row=1, column=8, padx=20)
            
         # Lipinski's properties fields are disabled unless YES button is pressed
        self.mw_label["state"] = "disabled"
        self.logp_label["state"] = "disabled"
        self.tpsa_label["state"] = "disabled"
        self.hbd_label["state"] = "disabled"
        self.hba_label["state"] = "disabled"
        self.rtb_label["state"] = "disabled"
        self.mw_entry["state"] = "disabled"
        self.logp_entry["state"] = "disabled"
        self.tpsa_entry["state"] = "disabled"
        self.hbd_entry["state"] = "disabled"
        self.hba_entry["state"] = "disabled"
        self.rtb_entry["state"] = "disabled"
        self.lipin_prop["state"] = "disabled"

        ##----------------------------------------------------------------------##           
        #                             Button Frame (bottom)                      #
        ##----------------------------------------------------------------------##

        self.f7 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f7.pack(side="bottom")

        ### -----   Buttons for running the script, clearing and exiting the program ----- ###
        self.run_button = Button(self.f7, text="RUN", fg="green", font="Roman 13 bold", borderwidth=2, command=self.run)
        self.exit_button = Button(self.f7, text="EXIT", fg="red", font="Roman 13", command=self.exit)
        self.clear_button = Button(self.f7, text="CLEAR", fg="blue", font="Roman 13", command=self.clear_form)
        self.run_button.grid(row=3, column=6, padx=8)
        self.exit_button.grid(row=3, column=8, padx=8)
        self.clear_button.grid(row=3, column=4, padx=8)

       
    ##----------------------------------------------------------------------##
    ##                                                                      ##           
    #             METHODS IMPLEMENTED IN THE GUI - Main GUI                  #
    ##                                                                      ##
    ##----------------------------------------------------------------------##

    ##---------------------------------------------------------------------##           
    #                         Prepare Modules Buttons                       #
    ##---------------------------------------------------------------------##

    # ### -----   for loading (Receptor Preparation Module)   ----- ###
    def ReceptorPrepModule(self):
        # Need to define project directory first in order to save receptor files inside it
        if (os.path.exists(outDir_value.get())):
            self.recepPrepWindow = Toplevel(self.master)
            self.recepPrepWindow.geometry("400x500")
            self.recepPrepWindow.resizable(False, False)
            self.recepPrepWindow.title("VSpipe - Receptor Preparation")
            self.app = RecepPrepModule(self.recepPrepWindow)
        else:
            showinfo("Project directory is needed!", "Please first define project directory to proceed.")    
    # ### -----   for loading (Ligand Preparation Module)   ----- ###
    def LigandPrepModule(self):
        # Need to define project directory first in order to save ligands files inside it
        if (os.path.exists(outDir_value.get())):
            self.ligPrepWindow = Toplevel(self.master)
            self.ligPrepWindow.geometry("500x400")
            self.ligPrepWindow.resizable(False, False)
            self.ligPrepWindow.title("VSpipe - Ligand Preparation")
            self.app = LigandPrepModule(self.ligPrepWindow)
        else:
            showinfo("Project directory is needed!", "Please first define project directory to proceed.")  

    
    # ### -----   for loading (Filtration Module)   ----- ###
    # Filtration Module
    def FilterModule(self):
        # To ensure to use this module only if the user has already run virtual screening by VSpipe
        answer = askyesno(title='Confirmation!',
                    message='This module allows you to filter VS results, Have you already run VS by VSpipe?')
        if (answer):
            conf = askyesno(title='Filtering!',
                    message='You want to filter VS results by physicochemical properties?\nPress Yes.\nOr press No for spatial filtering.')
            if (conf):
                # Filtering - VS Results Filtering
                self.filterWindow = Toplevel(self.master)
                self.filterWindow.geometry("500x515")
                self.filterWindow.resizable(False, False)
                self.filterWindow.title("VSpipe - VS Results Filtering")
                self.app = FiltrationModule(self.filterWindow)    
            else:
                # Filtering - Spatial Filtering
                self.spatialWindow = Toplevel(self.master)
                self.spatialWindow.geometry("480x615") # width x length
                self.spatialWindow.resizable(False, False)
                self.spatialWindow.title("VSpipe - Spatial Filtering")
                self.app = PdbModule(self.spatialWindow) 
        else:
            showinfo("Run VS first!", "You need to run virtual screening by VSpipe and then use this module.")     
    
    
    # dummy function 
    def dummy(self):
        pass

    #---------------------------------------------------------------------------------------##           
    #  Methods implemented for Browsing receptor file, compounds library & output directory   #
    ##---------------------------------------------------------------------------------------##
    
    ### -----   for taking RECEPTOR FILE PATH from the user ----- ###
    def receptor_file(self):   
        self.receptor_selected = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a Receptor File",
                                            filetypes = (("pdbqt file",
                                                            "*.pdbqt"),
                                                        ("all files",
                                                            "*.*")))
        self.recep_value.set(self.receptor_selected)


    ### -----   for taking COMPOUNDS LIBRARY PATH from the user ----- ###
    def compounds_library(self):
        self.compLib_selected = filedialog.askdirectory()
        compLib_value.set(self.compLib_selected)  

    ### -----   for taking OUTPUT DIRECTORY PATH from the user ----- ###
    def output_directory(self):

        self.outDir_selected = filedialog.askdirectory()
        try:
            # To ensure that the directory is empty and should be a valid path
            if os.path.exists(self.outDir_selected) and os.path.isdir(self.outDir_selected):
                if not os.listdir(self.outDir_selected):
                    outDir_value.set(self.outDir_selected)
                else:
                    showwarning("Directory is not empty!", "Please define an empty directory.")
            else:
                showerror("Path is not valid!", "Please define a valid path.")
            
        except TypeError:
            print("No directory is selected")

    ##----------------------------------------------------------------------##           
    #        Methods implemented for loading and saving parameters           #
    ##----------------------------------------------------------------------##

    ### -----   for loading PARAMETERS from GPF/config file ----- ###
    def load_parameters(self):   
        self.parameters_selected = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a Parameters File",
                                            filetypes = (("Parameters file",
                                                            "*.gpf *.txt"),
                                                        ("all files",
                                                            "*.*")))
       
        # requires *.gpf file for AD4 docking
        self.param_file.set(self.parameters_selected)
        # Setting parameters values that are retrieved from the file
        try:
            self.f = open(self.parameters_selected, "r")
            self.text = self.f.readlines()  
            # for *txt files containing search space information
            if (self.parameters_selected.endswith("txt")):
                self.temp = ''.join(self.text[3])
                self.coord = self.temp.split(' ')
                self.xDim_value.set(self.text[2][11:13])
                self.yDim_value.set(self.text[2][14:16])
                self.zDim_value.set(self.text[2][17:19])
                self.xCen_value.set(self.coord[4])
                self.yCen_value.set(self.coord[5])
                self.zCen_value.set(self.coord[6].strip()) #strip() to replace newline character at the end
                self.f.close()
            if (self.parameters_selected.endswith("gpf")):
                self.temp = ''.join(self.text[6])
                self.coord = self.temp.split(' ')
                self.xDim_value.set(self.text[0][5:7])
                self.yDim_value.set(self.text[0][8:10])
                self.zDim_value.set(self.text[0][11:13])
                self.xCen_value.set(self.coord[1])
                self.yCen_value.set(self.coord[2])
                self.zCen_value.set(self.coord[3]) 
                self.f.close()
        except (FileNotFoundError, AttributeError, TypeError):
            print("No file is selected")



    ### -----   for saving PARAMETERS file in text format ----- ###
    def save_parameters(self):
        self.docking_results_dir = (outDir_value.get())
        os.chdir(self.docking_results_dir)
        self.f= open("VSpipe_parameters_file_vina.txt", "w")
        self.f.write("\n\n")
        self.f.write("npts       ")
        self.f.write(str(int(self.xDim_value.get())))
        self.f.write(" ")
        self.f.write(str(int(self.yDim_value.get())))
        self.f.write(" ")
        self.f.write(str(int(self.zDim_value.get())))
        self.f.write("\ncenter    ")
        self.f.write(str(format(self.xCen_value.get(), ".3f")))
        self.f.write(" ")
        self.f.write(str(format(self.yCen_value.get(), ".3f")))
        self.f.write(" ")
        self.f.write(str(format(self.zCen_value.get(), ".3f")))
        self.f.close()
        showinfo("File is saved!", f"The file, VSpipe_parameters_file.txt is saved to {self.docking_results_dir}/")
    ##----------------------------------------------------------------------##           
    #           Methods implemented for Lipinski's Rule of Five              #
    ##----------------------------------------------------------------------##

     ### -----   To disable/enable lipinski's properties fields when specific buttons are pressed ----- ###
    def apply_lipinRules(self):
        # When no is selected then all lipinski's fields are disabled except yes
        if (self.lipin_value.get() == 1 or self.lipin_value.get() == 2):  
            self.mw_label["state"] = "disabled"
            self.logp_label["state"] = "disabled"
            self.tpsa_label["state"] = "disabled"
            self.hbd_label["state"] = "disabled"
            self.hba_label["state"] = "disabled"
            self.rtb_label["state"] = "disabled"
            self.mw_entry["state"] = "disabled"
            self.logp_entry["state"] = "disabled"
            self.tpsa_entry["state"] = "disabled"
            self.hbd_entry["state"] = "disabled"
            self.hba_entry["state"] = "disabled"
            self.rtb_entry["state"] = "disabled"
            self.lipin_prop["state"] = "disabled"
            if (self.lipin_value.get() == 2):
                self.mw_value.set('500.0')
                self.logp_value.set('5.0')
                self.tpsa_value.set('150.0')
                self.hbd_value.set('5.0')
                self.hba_value.set('10.0')
                self.rtb_value.set('8.0')
            elif(self.lipin_value.get() == 1):
                self.mw_value.set('0.0')
                self.logp_value.set('0.0')
                self.tpsa_value.set('0.0')
                self.hbd_value.set('0.0')
                self.hba_value.set('0.0')
                self.rtb_value.set('0.0')
            
        else:
            self.mw_label["state"] = "normal"
            self.logp_label["state"] = "normal"
            self.tpsa_label["state"] = "normal"
            self.hbd_label["state"] = "normal"
            self.hba_label["state"] = "normal"
            self.rtb_label["state"] = "normal"
            self.mw_entry["state"] = "normal"
            self.logp_entry["state"] = "normal"
            self.tpsa_entry["state"] = "normal"
            self.hbd_entry["state"] = "normal"
            self.hba_entry["state"] = "normal"
            self.rtb_entry["state"] = "normal"
            self.lipin_prop["state"] = "normal"

    # Lipinski's rules description
    def lipin_desc(self):
        tmsg.showinfo('Lipinski\'s Properties','MW: Molecular Weight\nlogp: Partition Coefficient\ntpsa: Molecular Polar Surface Area\nHBD: Hydrogen Bond Donor\nHBA: Hydrogen Bond Acceptor\nRTB: Number of Rotatable Bonds')
   
    ##----------------------------------------------------------------------##           
    #          Methods implemented for (Clear, Exit, Run Buttons)            #
    ##----------------------------------------------------------------------##

    ### -----   Method implemented for the EXIT button ----- ###
    def exit(self):
        self.master.destroy()

    ### -----   Method implemented for the CLEAR button ----- ###
    def clear_form(self):
        self.recep_entry.delete(0, 'end')
        self.compLib_entry.delete(0, 'end')
        self.outDir_entry.delete(0, 'end')
        self.xDim_entry.delete(0, 'end')
        self.yDim_entry.delete(0, 'end')
        self.zDim_entry.delete(0, 'end')
        self.xCen_entry.delete(0, 'end')
        self.yCen_entry.delete(0, 'end')
        self.zCen_entry.delete(0, 'end')

    ##=======================================================================##           
    #              Methods implemented for (((RUN Button)))                  #
    ##======================================================================##


    ### -----   for RUNNING THE SCRIPT FOR VIRTURAL SCREENING ----- ###
    ### -----   for RUNNING THE SCRIPT FOR VIRTURAL SCREENING ----- ###
    def run(self):
              
        # To ensure that all fields are defined before proceeding for running the program
        if (os.path.exists(self.recep_value.get()) and os.path.exists(compLib_value.get()) and os.path.exists(outDir_value.get())\
            and not self.xCen_value.get()==0.0 and not self.yCen_value.get()==0.0 and not self.zCen_value.get()==0.0\
            and not self.xDim_value.get()==0.0 and not self.yDim_value.get()==0.0 and not self.zDim_value.get()==0.0):
            # Taking input files paths
            self.recep_file = (self.recep_value.get()) 
            self.comp_dir_path = (compLib_value.get())
            self.comp_dir_path = self.comp_dir_path + "/" + "pdbqt/"
            self.compound_lib = os.listdir(self.comp_dir_path)
            os.system(f"mkdir {outDir_value.get()}/results")
            self.docking_results_dir = (outDir_value.get())+ "/results"
            
            os.system(f'mkdir {self.docking_results_dir}/pdbqt_lip_rules')
            self.lip_rules = self.docking_results_dir + "/pdbqt_lip_rules/"
            ##...........................................................##           
            #       RUN - (Creating Datasheet - Lipinski's rule of 5 )    #
            ##...........................................................##
            
            # Copying ligands/pdbqt to results/pdbqt_lip_rules/
            for lig in self.compound_lib:
                os.system(f'cp {self.comp_dir_path}* {self.lip_rules}')
            
            
            # datasheet.py is taking 4 parameters, defined by author ---
            # 1. ligands prepared library should have this file as: /sdf/del_atoms_properties_ligands.sdf
            # 2. choice = no, means no lipinski's rule will apply
            # 3. results directory 
            # 4. flag = 3, means file --- need to debug this variable (to me Rashid) 
            
            # 2. choice = no, means no lipinski's rule will apply
            if (self.lipin_value.get() == 1):
                os.system(f'python2.7 /usr/local/bin/datasheet.py {compLib_value.get()}/sdf/del_atoms_properties_ligands.sdf no {self.docking_results_dir} 3')
            
            # 2. choice = default, i.e., MW<500, logP<5, HBD<5, HBA<10, TPSA<150, ROT_BONDS<8
            elif (self.lipin_value.get() == 2):
                os.system(f'python2.7 /usr/local/bin/datasheet.py {compLib_value.get()}/sdf/del_atoms_properties_ligands.sdf default {self.docking_results_dir} 3')

            # 2. choice = custom properties, e.g. "550,5.3,4,11,140,7 for MW<550, logP<5.3, HBD<4, HBA<11, TPSA<140, ROT_BONDS<7.
            else:
                os.system(f'python2.7 /usr/local/bin/datasheet.py {compLib_value.get()}/sdf/del_atoms_properties_ligands.sdf {self.mw_value.get()},{self.logp_value.get()},{self.hbd_value.get()},{self.hba_value.get()},{self.tpsa_value.get()},{self.rtb_value.get()} {self.docking_results_dir} 3')
            
            # To use the updated library that is present in ../results/pdbqt_lip_rules which is shortened after applying lipinski's parameters
            self.compounds_lip_rules = os.listdir(self.lip_rules)
            # --------------------------------
            # Creating directories for keeping generated files from (Vina Docking) to their respectives directories
            if (self.dockMethod_value.get() == 1):
                # os.system(f"mkdir {self.docking_results_dir}/config_vina")
                os.system(f"mkdir {self.docking_results_dir}/vina_pdbqt")
                os.system(f"mkdir {self.docking_results_dir}/vina_log")    
                os.system(f"mkdir {self.docking_results_dir}/lowest_energy_pdb")    
            
        #     ##......................................##           
            #          RUN - (Vina Docking)          #
            ##.....................................##

            # Running vina for blind docking
            if (self.dockType_value.get() == 1 and self.dockMethod_value.get() == 1):
                for lig in self.compounds_lip_rules:
                    print(f"Running blind docking for the compound {lig}")
                    os.system(f'vina --receptor {self.recep_file} --ligand {self.lip_rules +lig} --center_x {self.xCen_value.get()} --center_y {self.yCen_value.get()} --center_z {self.zCen_value.get()} --size_x {self.xDim_value.get()}  --size_y {self.yDim_value.get()}  --size_z {self.zDim_value.get()} --out {self.docking_results_dir}/vina_pdbqt/{lig} --log {self.docking_results_dir}/vina_log/{lig} --num_modes 10')
                            
            # Running vina for targeted docking
            elif (self.dockType_value.get() == 2 and self.dockMethod_value.get() == 1):
                for lig in self.compounds_lip_rules:
                    print(f"Running target docking for the compound {lig}")
                    os.system(f'vina --receptor {self.recep_file} --ligand { self.lip_rules +lig} --center_x {self.xCen_value.get()} --center_y {self.yCen_value.get()} --center_z {self.zCen_value.get()} --size_x {self.xDim_value.get()*0.375}  --size_y {self.yDim_value.get()*0.375}  --size_z {self.zDim_value.get()*0.375} --out {self.docking_results_dir}/vina_pdbqt/{lig} --log {self.docking_results_dir}/vina_log/{lig} --num_modes 10')
            
                #  ----------------------------------
                #   Summarizing Vina Results
                #   ---------------------------------
            if (self.dockMethod_value.get() == 1):
                # For generting low energy pdbs
                self.dr_path = self.docking_results_dir + "/vina_log/"
                self.path_vina_log = os.listdir(self.dr_path)

                for lig in self.path_vina_log:
                    ligand_name = os.path.splitext(lig)[0]
                    os.system(f'python /usr/local/bin/values_extraction_vina.py {self.docking_results_dir}/ {ligand_name}')
            
                # for renaming compound_name.pdbqt to compound_name.txt 
                for lig in self.path_vina_log:
                    ligand_name = os.path.splitext(lig)[0] + '.txt'
                    os.system(f'mv {self.dr_path + lig} {self.dr_path + ligand_name}')
                
                
                
                # Pop up job completion message for docking by Vina
                tmsg.showinfo("Vina Docking is completed!", f"Please find your results in:\n {self.docking_results_dir}/vina_pdbqt/ \nand log files in:\n {self.docking_results_dir}/vina_log/")    

            ##......................................##           
            #          RUN - (AD4 Docking)          #
            ##.....................................##
            
            # For blind docking by AD4
            if (self.dockMethod_value.get() == 2):
                
                # Get path of current working directory
                os.chdir(f'{outDir_value.get()}')
                cwd=os.getcwd()
                # cwd = outDir_value.get()
                # Copying *.gpf file to current working directory
                os.system(f'cp {self.param_file.get()} {cwd}/')
                os.system(f'cp /usr/local/bin/scratch_sample.dpf {cwd}/')
                # rename the *gpf file as sample.gpf
                os.system(f'mv *gpf sample.gpf')
                # os.system(f'python ~/VSpipe_GUI/TOOLS/generating_correct_dpf.py Essential_Files/sample.gpf Essential_Files/scratch_sample.dpf Essential_Files/ {self.recep_file}')
                os.system(f'python /usr/local/bin/generating_correct_dpf.py {cwd}/sample.gpf {cwd}/scratch_sample.dpf {cwd}/ {self.recep_file}')

                print("Autodock 4.2 running ...")
                print(f"The grid boxes for each ligand are saved as {self.docking_results_dir}/gpf/ID.gpf")
                print(f"The autogrid output files are saved as {self.docking_results_dir}/glg/ID.glg")
                print(f"The parameter files for each ligand are saved as {self.docking_results_dir}/dpf/ID.dpf")
                print(f"The autodock output files are saved as {self.docking_results_dir}/dlg/ID/ID.dlg")
                print("Autodock 4.2 running ...")
                
                # Creating directories for keeping generated files from (AD4 docking) to their respectives directories
                os.system(f"mkdir {self.docking_results_dir}/dlg")
                os.system(f"mkdir {self.docking_results_dir}/gpf")
                os.system(f"mkdir {self.docking_results_dir}/dpf")
                os.system(f"mkdir {self.docking_results_dir}/glg")
                os.system(f"mkdir {self.docking_results_dir}/summary")
                os.system(f"mkdir {self.docking_results_dir}/lowest_energy_pdb")

                os.system(f"mkdir etc")
                os.system(f"python /usr/local/bin/creating_etc_dir.py {compLib_value.get()}/pdb/ etc/")

                os.system(f'cp {self.recep_file} .')
                # os.system(f'cp Essential_Files/sample.gpf .')
                os.system(f'/usr/local/bin/autogrid4 -p sample.gpf -l sample.glg')

                for lig in self.compounds_lip_rules:
                    if (lig.endswith("pdbqt")):
                        ligand_name = os.path.splitext(lig)[0]
                        print(f"\n\nAutoDock 4.2 is analysing {ligand_name} ... ...\n")
                        os.system(f'/usr/local/bin/prepare_gpf4.py -l {self.lip_rules +lig} -r {self.recep_file} -i {cwd}/sample.gpf -o {self.lip_rules}/{ligand_name}.gpf') 
                        os.system(f'/usr/local/bin/prepare_dpf4.py -l {self.lip_rules +lig} -r {self.recep_file} -i {cwd}/sample.dpf -o {self.lip_rules}/{ligand_name}.dpf') 
                        os.system(f'python /usr/local/bin/dpf_rewrite.py {self.lip_rules}/{ligand_name} {cwd}/ {self.lip_rules}/')
                    
                        os.system(f"mkdir {self.docking_results_dir}/dlg/{ligand_name}")
                        os.system(f'/usr/local/bin/autodock4 -p {self.lip_rules}/{ligand_name}.dpf -l {self.docking_results_dir}/dlg/{ligand_name}/{ligand_name}.dlg')
                        print (f"Analysis finished for {ligand_name}")

                # Moving dlg, gpf and glg files to their respective folders 
                os.system(f'mv {self.lip_rules}/*.gpf {self.docking_results_dir}/gpf')
                os.system(f'mv {self.lip_rules}/*.dpf {self.docking_results_dir}/dpf')
                os.system(f'mv *.glg {self.docking_results_dir}/glg')

                #   ----------------------------------
                #   Summarizing AD4 Results
                #   ---------------------------------

                print(" ---- ### SUMMARISING RESULTS ### ----")
                print(f"Creating summary files of the DLG files and saving them as {self.docking_results_dir}/summary/summary_ID.txt.")
                print(f"Extracting the lowest energy pdb file and saving it as {self.docking_results_dir}/lowest_energy_pdb/ID.pdb")

                self.docking_path = self.docking_results_dir + "/" + "dlg/"
                self.docking_dlg_path = os.listdir(self.docking_path)
                
                for file in self.docking_dlg_path: 
                    file_path = self.docking_path + file         
                    os.system(f'/usr/local/bin/summarize_results4.py -d {file_path} -b -o {self.docking_results_dir}/summary/summary_{file}.txt')
                    os.system(f'python /usr/local/bin/values_extraction_AD4.py {self.docking_results_dir}/ {file}')
                    print("---------------")
                        
                # Pop up job completion message for docking by Vina
                tmsg.showinfo("AD4 Docking is completed!", f"Please find your results in:\n {self.docking_results_dir}/dlg/ \nand summary in:\n {self.docking_results_dir}/summary/")   
        else:
            showerror("Something went wrong!", "Please check if you have supplied valid values to all the fields above")

# ==================================================================
# =================================================================
#  (((VSpipe - GUI --> Receptor Preparation Module)))
# =================================================================
# ===================================================================

##----------------------------------------------------------------------##
##                                                                      ##           
#        Documentation regarding extra modules import/installation        #
##                                                                      ##
##----------------------------------------------------------------------##
# 1. For giving tooltip 
# >>>  install idlelib.tooltip by following command for giving tooltip
# >>>   sudo apt install idle3

# 2. For fetching pdb structure from ProteinDataBank through its pdb id
# >>>   use from Bio.PDB import * (biopython module)

# 3. For extracting first chain of the protein 
# >>>   uses pdb-tools
# >>>   pip install pdb-tools 
# >>>   pip install --upgrade pdb-tools
# >>>   source: http://www.bonvinlab.org/pdb-tools/
  
    
##----------------------------------------------------------------------##
##                                                                      ##           
#             TKINTER GUI BELOW - Receptor Preparation                   #
##                                                                      ##
##----------------------------------------------------------------------##

class RecepPrepModule:
    def __init__(self, master):

        self.master = master
        ### -----   Title Frame (Top) ----- ###
        self.f1 = Frame(self.master, borderwidth=5, relief=SUNKEN)
        self.f1.pack(side="top", pady=10)

        self.f1_title = Label(self.f1, text="Receptor Preparation", font="Roman 15 bold", fg="#660099")
        self.f1_title.pack(padx=70)

        ##----------------------------------------------------------------------##           
        #     Frame for taking input from the user as a RECEPTOR (Top down)      #
        ##----------------------------------------------------------------------##

        ### -----    ----- ###
        self.f2 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f2.pack(anchor="nw", padx=20, pady=12, fill=X)

        ### -----   Labels for Inputing receptor ----- ###
        self.f2_pdbID = Label(self.f2, text="PDB ID: ", font="Roman 12 bold")
        self.f2_OR = Label(self.f2, text="OR", font="Roman 12 bold")
        self.f2_recep = Label(self.f2, text="Receptor: ", font="Roman 12 bold")
        self.f2_pdbID.grid(row=1, sticky=W, pady=5, ipadx=7)
        self.f2_OR.grid(row=2, column=2, padx=20, pady=5)
        self.f2_recep.grid(row=3, sticky=W, pady=5)

        ### -----   Entry Widgets for Inputing file ----- ###
        self.recep_value = StringVar()
        self.pdbID_value = StringVar()
        self.pdbID_entry = Entry(self.f2, textvariable=self.pdbID_value)
        # myTip = Hovertip(self.pdbID_entry,'e.g., 3e7a')
        self.recep_entry = Entry(self.f2, textvariable=self.recep_value)
        # myTip = Hovertip(self.recep_entry,'Enter the file path')
        self.pdbID_entry.grid(row=1, column=2, padx=10, pady=5)
        self.recep_entry.grid(row=3, column=2, padx=10, pady=5)

        ### -----   Receptor Browse Button ----- ###
        self.pdbID_button = Button(self.f2, text="Fetch", command=self.retreive_pdb)
        self.recep_button = Button(self.f2, text="Browse", command=self.receptor_file)
        self.pdbID_button.grid(row=1, column=3, padx=5, pady=5, ipadx=5)
        self.recep_button.grid(row=3, column=3, padx=5, pady=5)

        ##----------------------------------------------------------------------##           
        #  Frame for applying filters for cleaning the receptor (Radio Buttons)  #
        ##----------------------------------------------------------------------##

        self.f3 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f3.pack(anchor="nw", padx=20, pady=12, fill=X)

        ### -----   RADIO BUTTONS for clearning the receptor ----- ###
        self.radio_value = IntVar()
        self.radio_default = Radiobutton(self.f3, text="Keep the file by default", font="Roman 11", variable=self.radio_value, value=1, command=self.keep_metalIon)
        # myTip = Hovertip(self.radio_default,'Do nothing')
        self.radio_firstChain = Radiobutton(self.f3, text="Extract first chain and No metal ion", font="Roman 11", variable=self.radio_value, value=2, command=self.keep_metalIon)
        # myTip = Hovertip(self.radio_firstChain,'Remove water, ligand(s) and metal ion(s)')
        self.radio_metalIon = Radiobutton(self.f3, text="Extract first chain and keep the metal ion", font="Roman 11", variable=self.radio_value, value=3, command=self.keep_metalIon)
        # myTip = Hovertip(self.radio_metalIon,'Remove water, ligand(s) but keep specified metal ion')
        self.radio_default.grid(row=2, sticky=W, padx=1, pady=7)
        self.radio_firstChain.grid(row=3, sticky=W, padx=1, pady=7)
        self.radio_metalIon.grid(row=4, sticky=W, padx=1, pady=7)

        ##----------------------------------------------------------------------##           
        #                   Frame for handling metal ion                         #
        ##----------------------------------------------------------------------## 

        self.f4 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f4.pack(anchor="nw", padx=20, pady=12, fill=X)

        ### -----   Entry for uniqure ligands ----- ###
        self.f4_metal_ion = Label(self.f4, text="Specify Metal Ion: ", font="Roman 11")
        self.f4_metal_charge = Label(self.f4, text="Specify Metal Charge: ", font="Roman 11")
        self.f4_metal_ion.grid(row=1, sticky=W, pady=5, ipadx=11)
        self.f4_metal_charge.grid(row=2, sticky=W, pady=5)

        self.metalIon_value = StringVar()
        self.metalCharge_value = StringVar()
        self.metalIon_entry = Entry(self.f4, textvariable=self.metalIon_value)
        # myTip = Hovertip(self.metalIon_entry,'e.g., MN in case of Manganese')
        self.metalCharge_entry = Entry(self.f4, textvariable=self.metalCharge_value)
        # myTip = Hovertip(self.metalCharge_entry,'e.g., +2.000 in case of Manganese')
        self.metalIon_entry.grid(row=1, column=2, padx=10, pady=5)
        self.metalCharge_entry.grid(row=2, column=2, padx=10, pady=5)

        # Metal ions and charges are disabled unless third radio button is chosen for keeping metal ion
        self.f4_metal_ion["state"] = "disabled"
        self.f4_metal_charge["state"] = "disabled"
        self.metalIon_entry["state"] = "disabled"
        self.metalCharge_entry["state"] = "disabled"

        ##----------------------------------------------------------------------##           
        #                    Frame for RUN and Exit Buttons                      #
        ##----------------------------------------------------------------------## 

        ### -----   Button Frame (bottom) ----- ###
        self.f5 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f5.pack(side="bottom")

        ### -----   Buttons for running the script, clearing and exiting the program ----- ###
        self.run_button = Button(self.f5, text="RUN", fg="green", font="Roman 12 bold", borderwidth=2, command=self.run)
        # myTip = Hovertip(self.run_button,'To generate PDBQT')
        self.exit_button = Button(self.f5, text="EXIT", fg="red", font="Roman 12", command=self.terminate)
        self.run_button.grid(row=3, column=6, padx=8)
        self.exit_button.grid(row=3, column=8, padx=8)

    ##----------------------------------------------------------------------##
    ##                                                                      ##           
    #        METHODS IMPLEMENTED IN THE GUI - Receptor Preparation           #
    ##                                                                      ##
    ##----------------------------------------------------------------------##

    ##------------------------------------------------------------------------------##           
    #  Methods implemented for fetching pdb structure and browing the receptor       #
    ##------------------------------------------------------------------------------##

    ### -----   for fetching PDB file from ProteinDataBank ----- ###
    def retreive_pdb(self):   
        # Fetch the protein pdb file from ProteinDataBank
        self.pdbl = PDBList()
        self.pdbl.retrieve_pdb_file(self.pdbID_value.get(), pdir = '.', file_format = 'pdb')
        self.downloaded_file = 'pdb'+ self.pdbID_value.get().lower()+'.ent'

        # following global keyword will be used by receptor_pdbqt_correction.py and adding_metal_charge.py
        # global pdbid
        # pdbid = pdbID_value.get().lower()
        
        # pdbpdbid.ent file is renamed into pdbid.pdb
        self.pdb_file = self.pdbID_value.get().lower() + '.pdb'
        os.system(f'mv {self.downloaded_file} {self.pdb_file}')

        if (self.pdb_file in os.listdir()):
            print(f"The file (PDB ID: {self.pdbID_value.get()}) is present")
        else:
            print(f"The file (PDB ID: {self.pdbID_value.get()}) is not present")
        # Sets the value of pdb
        self.pdbID_value.set(self.pdb_file)

        
    ### -----   for taking RECEPTOR FILE PATH from the user ----- ###
    def receptor_file(self):   
        self.receptor_selected = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("pdb files",
                                                            "*.pdb"),
                                                        ("all files",
                                                            "*.*")))
        self.recep_value.set(self.receptor_selected) # sets the value to the entry field of receptor file

    ##----------------------------------------------------------------------##           
    #                 Methods implemented for Radio Buttons                  #
    ##----------------------------------------------------------------------##

    def keep_metalIon(self):
            # Metal ions and charges are disabled unless third radio button is chosen for keeping metal ion
            if (self.radio_value.get() == 3):  
                self.f4_metal_ion["state"] = "normal"
                self.f4_metal_charge["state"] = "normal"
                self.metalIon_entry["state"] = "normal"
                self.metalCharge_entry["state"] = "normal"
            else:
                self.f4_metal_ion["state"] = "disabled"
                self.f4_metal_charge["state"] = "disabled"
                self.metalIon_entry["state"] = "disabled"
                self.metalCharge_entry["state"] = "disabled"


    ##----------------------------------------------------------------------##           
    #               Methods implemented for Exit & Run Buttons               #
    ##----------------------------------------------------------------------##


    ### -----   Method implemented for the EXIT button ----- ###
    def terminate(self):
        self.master.destroy()

    ### -----   Handle generated pdbqt file (metalloprotein)----- ###
    def process_metallo_receptor(self, generated_file):
        self.pdbcode = self.generated_file[7:11]
        # print("@@@@@generated_file: ", generated_file)
        # print("hurrrrrahhhhdddddddd,,,pdbcode: ", pdbcode)
        # ChainA_pdbid_clean.pdbqt renamed into pdbid.pdbqt
        os.system(f'mv {self.generated_file} {self.pdbcode}.pdbqt')
        # os.system(f'gedit {pdbid}.pdbqt')
        # Correcting generated pdbqt file of metalloprotein
        os.system(f'python /usr/local/bin/receptor_pdbqt_correction.py {self.pdbcode}')
        # Adding charge in corrected pdbqt file of metalloprotein
        os.system(f'/usr/local/bin/adding_metal_charge.py {self.pdbcode} {self.metalIon_value.get()} {self.metalCharge_value.get()}')

    ### -----   for RUNNING THE SCRIPT FOR PROCESSING RECEPTOR ----- ###
    def process_receptor(self, receptor):
        print("Removing water residues.")
        print("Adding hydrogens in the receptor's pdb file.")
        print("Merging charges and removing non-polar hydrogens.")
        print(f"Saving the receptor as {self.receptor}")
        os.system(f'/usr/local/bin/prepare_receptor4.py -r {self.receptor} -A hydrogens -U nphs waters')
        
        # for correcting and adding charge in generated pdbqt file of metalloprotein
        if (self.radio_value.get() == 3): 
            self.directory = os.listdir()
            for self.generated_file in self.directory:
                if (self.generated_file.endswith('pdbqt')):
                    self.process_metallo_receptor(self.generated_file) 

    ##---------------------------------------------------------------------------##           
    #       For generating pdbqt of file according to the selected option         #
    ##---------------------------------------------------------------------------##   

    def run(self):
        
        # Creating receptor directory for saving receptor related files
        os.system(f'mkdir {outDir_value.get()}/receptor')
        # To check whether file is fetched or browsed
        if (os.path.isfile(self.pdbID_value.get())):
            self.selected_receptor = self.pdbID_value.get()
            print("Fetched: ", self.selected_receptor)
        elif (self.recep_value.get() != ""):
            print("receptor file: ", self.recep_value.get())
            # To extract the filename from the browsed file path
            self.selected_receptor = os.path.basename(f'{self.recep_value.get()}')
            # Copy the receptor file in the present working directory
            cwd = os.getcwd()
            print("Present Working Directory", cwd)
            os.system(f'cp {self.recep_value.get()} {cwd}')
        else:
            print("The file is not found")

        # Keep the file by default (Do nothing)
        if (self.radio_value.get() == 1):  
            # removing water from the receptor
            os.system(f'/usr/local/bin/prepare_receptor4.py -r {self.selected_receptor} -A hydrogens -U nphs waters')
           

            
        # Extract first chain and no metal ions (removes water, ligands, metal ions)
        if (self.radio_value.get() == 2):  
            # Extracting first chain of the protein
            # os.system(f'grep -v \'^HETATM\' {self.selected_receptor} > noHET_{self.selected_receptor}')
            # os.system(f'pdb_selchain -A noHET_{self.selected_receptor} > clean_{self.selected_receptor}')
            # os.system(f'rm noHET_{self.selected_receptor}')
            os.system(f'python /usr/local/bin/clean_protein.py {self.selected_receptor}')
            # os.system(f"awk '!/HOH/' {selected_receptor} > clean_{selected_receptor}")
            # Converting receptor to pdbqt
            os.system(f'rm {self.selected_receptor}')
            os.system(f'mv *pdb clean_{self.selected_receptor}')
            self.directory = os.listdir()
            for self.receptor in self.directory:
                if (self.receptor.startswith('clean')):
                    self.process_receptor(self.receptor)
            
        # Extract first chain and keep metal ion (Metalloprotein)
        if (self.radio_value.get() == 3):  
            # Extract the first chain
            # os.system(f"awk '!/HOH/' {self.selected_receptor} > noWater_{self.selected_receptor}")
            # os.system(f'pdb_selchain -A noWater_{self.selected_receptor} > ChainA_{self.selected_receptor}')
            # Keep metal ion in the extracted first chain of the protien
            os.system(f'mv {self.selected_receptor} ChainA_{self.selected_receptor}')
            os.system(f'/usr/local/bin/adding_metal_ion.py ChainA_{self.selected_receptor} {self.metalIon_value.get()}')
            os.system(f'rm ChainA_{self.selected_receptor}')
            # removes temporary files
            # os.system(f'rm noWater_{self.selected_receptor} ChainA_{self.selected_receptor}')
            # Converting receptor to pdbqt
            self.directory = os.listdir()
            for self.receptor in self.directory:
                if (self.receptor.startswith('ChainA')):
                    # os.system(f'gedit {receptor}')
                    self.process_receptor(self.receptor)
        
        # move all the receptor related files to receptor directory
        os.system(f'mv *pdb* {outDir_value.get()}/receptor')
        # delete obsolete directory, it is generated by default, it is not of any use
        os.system('rmdir obsolete')
        # Job done prompt message
        tmsg.showinfo("Job Done!", f"Please find your prepared receptor in:\n\n {outDir_value.get()}/receptor/")         
        
        
# ==================================================================
# =================================================================
#  (((VSpipe - GUI --> Ligand Preparation Module)))
# =================================================================
# ===================================================================



##--------------------------------------------------------------------------##
##                                                                          ##           
#               TKINTER GUI BELOW - Compounds Library Preparation            #
##                                                                          ##
##--------------------------------------------------------------------------##


class LigandPrepModule:
    def __init__(self, master):

        self.master = master
   
        ##---------------------------------------------------------------------##           
        #                           Title Frame (Top)                           #
        ##---------------------------------------------------------------------##

        self.f1 = Frame(self.master, borderwidth=5, relief=SUNKEN)
        self.f1.grid(row=1, column=3, columnspan=10, padx=70, pady=10)
        # Frame Title
        self.f1_title = Label(self.f1, text="Compounds Library Preparation", font="Roman 15 bold", fg="#660099")
        self.f1_title.grid(row=1, column=3, padx=55)

        self.rows = 0
        while self.rows < 50:
            self.master.rowconfigure(self.rows, weight=1)
            self.master.columnconfigure(self.rows, weight=1)
            self.rows += 1

        ### -----    ----- ###
        self.f2 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f2.grid(row=6, column=1, columnspan=35, rowspan=34)

        self.nb = ttk.Notebook(self.f2)
        self.nb.grid(row=6, column=1, columnspan=40, rowspan=39)

        # Detect which tab is selected (Calling function)
        self.nb.bind("<<NotebookTabChanged>>", self.whichTabIsSelected)

        ##---------------------------------------------------------------------##           
        #                           Tab 1 (Default Library)                     #
        ##---------------------------------------------------------------------##

        # Create an instance of ttk style (for tab colors)
        self.s = ttk.Style()
        self.s.theme_use('default')
        self.s.configure('TNotebook.Tab', background="#FFCC33")
        self.s.map("TNotebook", background= [("selected", "green3")])

        self.tab1 = ttk.Frame(self.nb)
        self.nb.add(self.tab1, text='Default Library')

        self.tab1_label = Label(self.tab1, text="Please select following minimized compounds library: ", font="Roman 13 bold")
        self.tab1_label.grid(row=1, column=1, sticky=W, padx=20, pady=15)

        # Scroll bar
        # scrollbar = Scrollbar(tab1)
        # scrollbar.grid(row=2, column=2, sticky='nse')




        # root.columnconfigure(0, weight=1) Removing this line fixes the sizing issue with the entry field.
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(1, weight=1)

        # Listbox
        # list_box = Listbox(tab1, width=40, yscrollcommand=scrollbar.set)
        self.list_box = Listbox(self.tab1, width=40)
        self.list_box.grid(row=2, column=1, padx=20, pady=3)
        
        # Implements the following option later on 
        self.list_box.insert(END, "AnalytiConDiscovery_NP")
        # self.list_box.insert(END, "ASINEX_BB_v123_SD")
        self.list_box.insert(END, "ASINEX_Synergy_Fragments")
        self.list_box.insert(END, "Chem_diverset")
        self.list_box.insert(END, "Chem_Fragment")
        self.list_box.insert(END, "Chem_MW_Set_1")
        # self.list_box.insert(END, "ENAMINE_Building_Blocks_reduced_price")
        self.list_box.insert(END, "ENAMINE_fragment_library")
        self.list_box.insert(END, "IB_Screen_NP")
        self.list_box.insert(END, "Indofine_Natural_Products")
        self.list_box.insert(END, "Maybridge_Building_Blocks_GBP")
        # self.list_box.insert(END, "Maybridge_Fragment_Collection")
        self.list_box.insert(END, "Maybridge_Pre_Fragment_COCl_PFP")
        self.list_box.insert(END, "Maybridge_Pre_Fragment_NCO")
        self.list_box.insert(END, "Maybridge_Pre_Fragment_NCO_min")
        self.list_box.insert(END, "Maybridge_Pre_Fragment_NCO_min_4comp")
        self.list_box.insert(END, "Maybridge_Pre_Fragment_SO2Cl")
        self.list_box.insert(END, "Maybridge_Ro3_1000_Fragment_Library")
        self.list_box.insert(END, "Maybridge_Ro3_500_Fragment_Library")
        # self.list_box.insert(END, "Princeton_NP")
        self.list_box.insert(END, "Specs_Natural_Products")
        self.list_box.insert(END, "Zenobia_352_Fragments")
        # self.list_box.insert(END, "PTP_database")

        ##---------------------------------------------------------------------##           
        #                Tab 2 (Minimization - Single File)                     #
        ##---------------------------------------------------------------------##

        self.tab2 = ttk.Frame(self.nb)
        self.nb.add(self.tab2, text='Minimization - File')

        self.tab2_label = Label(self.tab2, text="Conversion and Minimization of following file format: ", font="Roman 13 bold")
        self.tab2_label.grid(row=1, sticky=W, padx=15, pady=15)

        ### -----   Inputting compounds library file (Batch Single file in sdf/mol2 format) ----- ###

        # File Format: PDB, MOL, MOL2
        # File Format: CAN, SMI
        # SDF format - uplodaded by user
        # To choose which file type to upload (Rabiobuttons)
        self.radio_value = IntVar(value=1)
        self.radio_flag1 = Radiobutton(self.tab2, text="File Format: PDB, MOL, MOL2", font="Roman 12", variable=self.radio_value, value=1)
        self.radio_flag2 = Radiobutton(self.tab2, text="File Format: CAN, SMI", font="Roman 12", variable=self.radio_value, value=2)
        self.radio_flag3 = Radiobutton(self.tab2, text="File Format: SDF", font="Roman 12", variable=self.radio_value, value=3)
        self.radio_flag1.grid(row=2, sticky=W, padx=20, pady=7)
        self.radio_flag2.grid(row=3, sticky=W, padx=20, pady=7)
        self.radio_flag3.grid(row=4, sticky=W, padx=20, pady=7)


        self.f2_file_compLib = Label(self.tab2, text="Compounds \nLibrary File: ", font="Roman 12 bold")
        self.f2_file_compLib.grid(row=5, sticky=W, padx=12, pady=15)

        self.file_compLib_value = StringVar()
        self.file_compLib_entry = Entry(self.tab2, textvariable=self.file_compLib_value, width=23)
        self.file_compLib_entry.grid(row=5, padx=110, pady=7)
        self.file_compLib_button = Button(self.tab2, text="Browse", command=self.compounds_library_file)
        self.file_compLib_button.grid(row=5, sticky=E, padx=20, pady=7, ipady=3, ipadx=10)
       
        ##---------------------------------------------------------------------##           
        #   Tab 3 (Minimization - Folder (individual files in pdb format))      #
        ##---------------------------------------------------------------------##

        self.tab3 = ttk.Frame(self.nb)
        self.nb.add(self.tab3, text='Minimization - Folder')

        self.tab3_label = Label(self.tab3, text="Minimization of whole directory containing individual files \nin pdb format: ", font="Roman 13 bold")
        self.tab3_label.grid(row=1, sticky=W, padx=20, pady=15)

        ### -----   for Browsing compounds library directory in pdb format----- ###

        self.f4_min_compLib = Label(self.tab3, text="Compounds \nLibrary \nDirectory: ", font="Roman 12 bold")
        self.f4_min_compLib.grid(row=2, sticky=W, padx=5, pady=25)

        self.min_compLib_value = StringVar()
        self.min_compLib_entry = Entry(self.tab3, textvariable=self.min_compLib_value, width=23)
        self.min_compLib_entry.grid(row=2, padx=95, pady=7)

        self.min_compLib_button = Button(self.tab3, text="Browse", command=self.minimized_compounds_library)
        self.min_compLib_button.grid(row=2, sticky=E, padx=10, pady=7, ipady=3, ipadx=10)

        ##---------------------------------------------------------------------##           
        #                           Run and Exit Buttons                        #
        ##---------------------------------------------------------------------##
        ### -----   Button Frame (bottom) ----- ###
        self.f5 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f5.grid(row=50, column=1, padx=5, columnspan=30, rowspan=5)

        self.run_button = Button(self.f5, text="RUN", fg="green", font="Roman 12 bold", borderwidth=2, command=self.run)
        # run_button = Button(f5, text="RUN", fg="green", font="Roman 10 bold", borderwidth=2, command=run)
        self.exit_button = Button(self.f5, text="EXIT", fg="red", font="Roman 12", command=self.terminate)
        self.run_button.grid(row=80, column=6, rowspan=100, padx=10)
        self.exit_button.grid(row=80, column=7, rowspan=100, padx=10)
        
    ##--------------------------------------------------------------------------##
    ##                                                                          ##           
    #      METHODS IMPLEMENTED IN THE GUI - Compounds Library Preparation        #
    ##                                                                          ##
    ##--------------------------------------------------------------------------##
        #--------------------------------------------------------------------##           
    #    Methods implemented for Tab 1 (Default Library)       #
    ##--------------------------------------------------------------------##
    def Libaray_Selection(self):
        self.value = self.list_box.get(self.list_box.curselection())
        self.lib_path = '/usr/local/lib/minimised_libs/' + self.value
        compLib_value.set(self.lib_path)
        self.master.destroy()
  
    #--------------------------------------------------------------------##           
    #    Methods implemented for Tab 2 (Minimization - Single File)       #
    ##--------------------------------------------------------------------##

    ### -----   To browse compounds library file in ((sdf, mol2, mol, pdb format))  ----- ###
    def compounds_library_file(self):
        self.library_file_selected = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (("Compounds batch files",
                                                            "*.sdf *.mol2 *.mol *.pdb"),
                                                        ("all files",
                                                            "*.*")))
        self.file_compLib_value.set(self.library_file_selected) # sets the value to the entry field of receptor file
    
    ##............................................##           
    #   Batch file minimization ((sdf to pdbqt))   #
    ##............................................##
    
    # Minimizing batch sdf file (converting the batch sdf file into individual pdb files and then converting these pdbs into pdbqts)
    def batch_file_minimzation(self):
        # self.filepath = os.path.dirname(self.file_compLib_value.get())
        self.filepath = self.file_compLib_value.get()
        # File Format: PDB, MOL, MOL2 (option = 1)
        # File Format: SMI, CAN       (option = 2)
        if (self.radio_value.get() == 1 or self.radio_value.get() == 2):
            print("Converting the ligand file into a SDF file and saving it as /ligands/sdf/ligands.sdf")
            os.system(f'obabel {self.filepath} -O ligands/sdf/ligands.sdf')
            # print("Adding code names if necessary for each ligand in the directory /ligands/sdf/ligands.sdf")
            # os.system(f'python TOOLS/to_sdf_correction.py null null ligands/sdf')
            os.system(f'obabel ligands/sdf/ligands.sdf -O ligands/sdf/properties_ligands.sdf -b --unique --add cansmi HBA2 HBD logP TPSA MW')
        
        # File Format: SDF 
        if (self.radio_value.get() == 3):
                      
            # Producing canonical smiles and missing properties of the ligands and saving it as ligands/sdf/properties_ligands.sdf
            os.system(f'obabel {self.filepath} -O ligands/sdf/properties_ligands.sdf -b --unique --add cansmi HBA2 HBD logP TPSA MW')
            
        # ---------------------------
        # Deleting from /ligands/sdf/properties_ligands.sdf, the atoms that are not recognized by Autodock and saving it as ligands/sdf/del_atoms_properties_ligands.sdf
        os.system(f'python2.7 /usr/local/bin/atom_deletion.py ligands/sdf/properties_ligands.sdf ligands/sdf/')

        # Minimizing ligands/sdf/del_atoms_properties_ligands.sdf using openBabel
        os.system(f'obabel ligands/sdf/del_atoms_properties_ligands.sdf -O ligands/pdb/ligand.pdb --gen3d -m --conformer --nconf 50 --score energy')
        
        # Accessing the library path of /ligands/pdb/
        self.library_path= os.getcwd() + "/ligands/pdb/"
        self.library_path_sdf= os.getcwd() + "/ligands/sdf"
        # Renaming pdbs in ligands/pdb/ directory according to the code contained in sdf file
        os.system(f'python2.7 /usr/local/bin/pdbs_rename.py {self.library_path_sdf}/del_atoms_properties_ligands.sdf {self.library_path} 3') 
        # Minimizing the renamed pdbs contained in /ligands/pdb/ into pdbqts will be copied to /ligands/pqbqt/
        self.lig_path = os.listdir(self.library_path) 
        for self.lig in self.lig_path:
            print(f'Adding hydrogens in the {self.library_path}/{self.lig} files')
            print('Merging charges and removing non-polar hydrogens')
            os.system(f'/usr/local/bin/prepare_ligand4.py -l {self.library_path + self.lig} -A hydrogens -U nphs')
        # moving the generated pdbqts to /ligands/pdbqt/ directory
        os.system('mv *pdbqt ./ligands/pdbqt/')
        
        # Message dialogue for succesful minimization of the compounds library 
        self.library_path= os.getcwd() + "/ligands/"
        tmsg.showinfo("Compounds Library is minimized!", f"Please find the minimized ligands in the directory:\n\n{self.library_path}")    


      
    
    #------------------------------------------------------------------------------------------##           
    #  Methods implemented for Tab 3 (Minimization - Folder (individual files in pdb format))   #
    ##-----------------------------------------------------------------------------------------##

    ### -----   for taking COMPOUNDS LIBRARY PATH from the user ----- ###
    def minimized_compounds_library(self):
        self.compLib_selected = filedialog.askdirectory()
        self.min_compLib_value.set(self.compLib_selected)  

    ### -----   for RUNNING THE SCRIPT FOR PROCESSING RECEPTOR ----- ###
    def pdbDir_to_pdbqt(self):
        # self.library_path = self.min_compLib_value.get()
        self.filepath = self.min_compLib_value.get()
        # File Format: PDB, MOL, MOL2 (option = 1)
        # File Format: SMI, CAN       (option = 2)
        
        print("Converting the ligand file into a SDF file and saving it as /ligands/sdf/ligands.sdf")
        os.system(f'obabel {self.filepath}/* -O ligands/sdf/ligands.sdf')
        # print("Adding code names if necessary for each ligand in the directory /ligands/sdf/ligands.sdf")
        # os.system(f'python TOOLS/to_sdf_correction.py null null ligands/sdf')
        os.system(f'obabel ligands/sdf/ligands.sdf -O ligands/sdf/properties_ligands.sdf -b --unique --add cansmi HBA2 HBD logP TPSA MW')
        
                    
        # ---------------------------
        # Deleting from /ligands/sdf/properties_ligands.sdf, the atoms that are not recognized by Autodock and saving it as ligands/sdf/del_atoms_properties_ligands.sdf
        os.system(f'python2.7 /usr/local/bin/atom_deletion.py ligands/sdf/properties_ligands.sdf ligands/sdf/')

        # Minimizing ligands/sdf/del_atoms_properties_ligands.sdf using openBabel
        os.system(f'obabel ligands/sdf/del_atoms_properties_ligands.sdf -O ligands/pdb/ligand.pdb --gen3d -m --conformer --nconf 50 --score energy')
        
        # Accessing the library path of /ligands/pdb/
        self.library_path= os.getcwd() + "/ligands/pdb/"
        self.library_path_sdf= os.getcwd() + "/ligands/sdf"
        
        
       # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
        # writing code inside the sdf file - added in 2025
        os.system(f'python3 /usr/local/bin/sdf_add_code.py {self.library_path_sdf}')
        
        # Renaming pdbs in ligands/pdb/ directory according to the code contained in sdf file
        os.system(f'python2.7 /usr/local/bin/pdbs_rename.py {self.library_path_sdf}/del_atoms_properties_ligands.sdf {self.library_path} 3') 
        
        # Minimizing the renamed pdbs contained in /ligands/pdb/ into pdbqts will be copied to /ligands/pqbqt/
        self.lig_path = os.listdir(self.library_path) 
        for self.lig in self.lig_path:
            print(f'Adding hydrogens in the {self.library_path}/{self.lig} files')
            print('Merging charges and removing non-polar hydrogens')
            os.system(f'/usr/local/bin/prepare_ligand4.py -l {self.library_path + self.lig} -A hydrogens -U nphs')
        # moving the generated pdbqts to /ligands/pdbqt/ directory
        os.system('mv *pdbqt ./ligands/pdbqt/')
        
        # Message dialogue for succesful minimization of the compounds library 
        self.library_path= os.getcwd() + "/ligands/"
        tmsg.showinfo("Compounds Library is minimized!", f"Please find the minimized ligands in the directory:\n\n{self.library_path}")    




    #--------------------------------------------------------------------##           
    #              Methods implemented for (Run & Exit buttons)           #
    ##--------------------------------------------------------------------##
    
    ### -----   Method implemented for the EXIT button ----- ###
    def terminate(self):
        self.master.destroy()

    #--------------------------------------------------------------------##           
    #       All functions which executes when RUN button is pressed        #
    ##--------------------------------------------------------------------##    

    ### -----   MDetect which tab is selected (Defining function) ----- ###
    def whichTabIsSelected(self, event):
        if event.widget.index("current") == 0:    
            global tab
            self.tab = 1
            self.run_button.config(text="ADD")
        elif event.widget.index("current") == 1:    
            self.tab = 2 
            self.run_button.config(text="RUN")
        else:
            self.tab = 3 
            self.run_button.config(text="RUN")

    ##=======================================================================##           
    #              Methods implemented for (((RUN Button)))                  #
    ##======================================================================##

 
    def run(self):

                    
        ##............................................##           
        #     TAB 2 - (Batch single file to pdbqt)     #
        ##............................................##

        # Creating ligands directory to place the respective files accrodingly
        if (self.tab == 2 or self.tab == 3):
            os.chdir(f'{outDir_value.get()}')
            os.system(f'mkdir {outDir_value.get()}/ligands')
            os.system(f'mkdir {outDir_value.get()}/ligands/sdf')
            os.system(f'mkdir {outDir_value.get()}/ligands/pdb')
            os.system(f'mkdir {outDir_value.get()}/ligands/pdbqt')
        
        if (self.tab == 1):
            print("Tab 1: Default Library is selected")
            self.value = self.list_box.get(self.list_box.curselection())
            self.lib_path = '/usr/local/lib/minimised_libs/' + self.value
            compLib_value.set(self.lib_path)
            self.master.destroy()


        if (self.tab == 2):
            print("Tab 2: Minimization - File is seleced")
            self.batch_file_minimzation()
            # self.rename_pdbs_pdbqts()

            # tmsg.showinfo("Job Done!", "The compounds library is now mininimized. Please check results in directory, Compounds_Library_PDBQT")

        ##...................................................................##           
        #  TAB 3 - (multiple individual pdb files in a folder into pdbqt)     #
        ##...................................................................##

        # When Tab 3 (Minimization - Folder) is selected
        if (self.tab == 3):
            print("Tab 3: Minimization - Folder is seleced")
            self.pdbDir_to_pdbqt()
            # tmsg.showinfo("Job Done!", "The compounds library is now mininimized. Please check results in directory, Compounds_Library_PDBQT")

        # Successful completion message box
        # root.option_add('*Dialog.msg.font', 'Roman 12')
        # tmsg.showinfo("Job Done!", "Please see directory named Prepared_Library in your current working directory for minimzed library compounds")

# ==================================================================
# =================================================================
#  (((VSpipe - GUI --> Filtration Module)))
# =================================================================
# ===================================================================

class FiltrationModule:
    def __init__(self, master):

        self.master = master 
        
        ##---------------------------------------------------------------------##           
        #                           Title Frame (Top)                           #
        ##---------------------------------------------------------------------##
        
        self.f1 = Frame(self.master, borderwidth=5, relief=SUNKEN)
        self.f1.pack(side="top", padx=5, pady=10)

        self.f1_title = Label(self.f1, text="VS Results Filtering", font="Roman 15 bold", fg="#660099")
        self.f1_title.grid(row=1, column=5, sticky=W, padx=80)

        ##-----------------------------------------------------------------------------##           
        #   (Frame 2) Browsing to VS results directory and defining output directory   #
        ##----------------------------------------------------------------------------##
        
        self.f2 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f2.pack(anchor="nw", padx=20, pady=10, fill=X)

        ### -----   Labels for Inputing file ----- ###
        self.vsResults_label = Label(self.f2, text="VS Results Directory: ", font="Roman 12 bold")
        self.vsResults_label.grid(row=1, sticky=W, pady=5, ipadx=1)
        
        self.vsResults_value = StringVar()
        self.vsResults_entry = Entry(self.f2, textvariable=self.vsResults_value, width=21)
        self.vsResults_entry.grid(row=1, column=2, padx=10, pady=5)
        
        ### -----   Browse buttons for Inputing file (Ready)----- ###
        self.vsResults_button = Button(self.f2, text="Browse", font="Roman 12", command=self.browse_vsResults_dir)
        self.vsResults_button.grid(row=1, column=3, padx=5, pady=5, ipadx=10, ipady=2)

        ##---------------------------------------------------------------------------------------##           
        #   (Frame 3) Sort by (Parameters) and Define the range (Choice) for specific parameter   #
        ##---------------------------------------------------------------------------------------##

        self.f3 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f3.pack(anchor="nw", padx=20, pady=15, fill=X)

        ### -----   Labels for Inputing file ----- ###
        self.parmOrder_label = Label(self.f3, text="Sort the results by:  ", font="Roman 12 bold")
        self.parmOrder_label.grid(row=1, sticky=W, pady=5, ipadx=5)

        # Combobox dropdown menu
        self.param_value = StringVar(value=' 8. δG')
        self.param_combo = ttk.Combobox(self.f3, width = 20, textvariable = self.param_value)

        # Adding combobox drop down list
        self.param_combo['values'] = (' 1. Molecular Weight', 
                          ' 2. cLogS',
                          ' 3. cLogP',
                          ' 4. HBD',
                          ' 5. HBA',
                          ' 6. PSA',
                          ' 7. Rotatable bonds',
                          ' 8. δG',
                          ' 9. Ki',
                          ' 10. Ligand efficiency',
                          ' 11. BEI',
                          ' 12. SEI',
                          ' 13. NSEI',
                          ' 14. NBEI',
                          ' 15. nBEI',
                          ' 16. mBEI')

        self.param_combo.grid(column=2, row=1, padx=12, sticky=W, pady=10)

        ##------------------------------------------##           
        #   (Frame 3) Choice - Apply Filter Yes/No   #
        ##-----------------------------------------##

        # Yes/No Filter
        self.filter_label = Label(self.f3, text="Apply Filter:  ", font="Roman 12 bold")
        self.filter_label.grid(row=2, sticky=W, pady=20, ipadx=30)

        # Yes/No filter radio buttons
        self.filter_value = IntVar(value=1)
        self.filter_no = Radiobutton(self.f3, text="No",  bg="#999999", font="Roman 12", variable=self.filter_value, value=1, command=self.filtraton_option)
        self.filter_yes = Radiobutton(self.f3, text="Yes",  bg="#999999", font="Roman 12", variable=self.filter_value, value=2, command=self.filtraton_option)
        self.filter_no.grid(row=2, column=2, sticky=W, padx=15, pady=20)
        self.filter_yes.grid(row=2, column=2, sticky=W, padx=100, pady=20)
      
        ##----------------------------------------------------------------------##           
        #              (Frame 4) Choice filers, three types of filers            #
        ##----------------------------------------------------------------------##

        self.f4 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f4.pack(anchor="nw", padx=20, pady=5, fill=X)

        # ### --- Three types of filers - ((checkbox))
        self.choice_value = IntVar(value=1)
        self.filter_1 = Radiobutton(self.f4, text="Filter 1",  bg="#999999", font="Roman 12 bold", variable=self.choice_value, value=1, command=self.filter_choice)
        self.filter_2 = Radiobutton(self.f4, text="Filter 2",  bg="#999999", font="Roman 12 bold", variable=self.choice_value, value=2, command=self.filter_choice)
        self.filter_3 = Radiobutton(self.f4, text="Filter 3",  bg="#999999", font="Roman 12 bold", variable=self.choice_value, value=3, command=self.filter_choice)
        self.filter_1.grid(row=1, column=1, sticky=W, pady=7, ipadx=10)
        self.filter_2.grid(row=2, column=1, sticky=W, pady=7, ipadx=10)
        self.filter_3.grid(row=3, column=1, sticky=W, pady=7, ipadx=10)

      

        ### --- Three types of filers - ((Filter 2 Label & Entry))
        self.filter_1_label = Label(self.f4, text="Greater than:  ", font="Roman 12", bg="#999999")
        self.filter_1_label.grid(row=1, column=2, sticky=W, padx=80, pady=7, ipadx=5)
        self.filter_1_value = StringVar()
        self.filter_1_entry = Entry(self.f4, textvariable=self.filter_1_value, width=8)
        self.filter_1_entry.grid(row=1, column=2, padx=185, pady=7, ipadx=2)
        
        ### --- Three types of filers - ((Filter 3 Label & Entry))
        self.filter_2_label = Label(self.f4, text="Less than:  ", font="Roman 12", bg="#999999")
        self.filter_2_label.grid(row=2, column=2, sticky=W, padx=80, pady=7, ipadx=5)
        self.filter_2_value = StringVar()
        self.filter_2_entry = Entry(self.f4, textvariable=self.filter_2_value, width=8)
        self.filter_2_entry.grid(row=2, column=2, padx=185, pady=7, ipadx=2)

        # ### --- Three types of filers - ((Labels))
        self.filter_3_min = Label(self.f4, text="Range - Min:  ", font="Roman 12", bg="#999999")
        self.filter_3_max = Label(self.f4, text="Range - Max:  ", font="Roman 12", bg="#999999")
        self.filter_3_min.grid(row=3, column=2, sticky=W, padx=85, pady=3, ipadx=1)
        self.filter_3_max.grid(row=4, column=2, sticky=W, padx=80, pady=5, ipadx=5)
        # ### --- Three types of filers - ((Filter 1 Entry))
        self.filter_3_min_value = StringVar()
        self.filter_3_max_value = StringVar()
        self.filter_3_min_entry = Entry(self.f4, textvariable=self.filter_3_min_value, width=8)
        self.filter_3_max_entry = Entry(self.f4, textvariable=self.filter_3_max_value, width=8)
        self.filter_3_min_entry.grid(row=3, column=2, padx=180, pady=1, ipadx=2)
        self.filter_3_max_entry.grid(row=4, column=2, padx=180, pady=1, ipadx=2)

        # Filter option is diasabled by default
        # filter 1
        self.filter_1["state"] = "disabled"
        self.filter_1_label["state"] = "disabled"
        self.filter_1_entry["state"] = "disabled"
        # filter 2
        self.filter_2["state"] = "disabled"
        self.filter_2_label["state"] = "disabled"
        self.filter_2_entry["state"] = "disabled"
        # filter 3
        self.filter_3["state"] = "disabled"        
        self.filter_3_min["state"] = "disabled"
        self.filter_3_max["state"] = "disabled"       
        self.filter_3_min_entry["state"] = "disabled"
        self.filter_3_max_entry["state"] = "disabled"

        ##----------------------------------------------------------------------##           
        #                             Button Frame (bottom)                      #
        ##----------------------------------------------------------------------##

        self.f5 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f5.pack(side="bottom")

        ### -----   Buttons for running the script, clearing and exiting the program ----- ###
        self.run_button = Button(self.f5, text="RUN", fg="green", font="Roman 12 bold", borderwidth=2, command=self.run)
        self.exit_button = Button(self.f5, text="EXIT", fg="red", font="Roman 12", command=self.terminate)
        self.run_button.grid(row=3, column=6, padx=8)
        self.exit_button.grid(row=3, column=8, padx=8)

    ##----------------------------------------------------------------------##
    ##                                                                      ##           
    #             METHODS IMPLEMENTED IN THE GUI - Main GUI                  #
    ##                                                                      ##
    ##----------------------------------------------------------------------##

    ##-------------------------------------------------------------------------##           
    #  Browse Buttons - Browse to results folder and define output directory    #
    ##-------------------------------------------------------------------------##

    ### -----   for taking VS Results directory from the user ----- ###
    def browse_vsResults_dir(self):
        self.vs_results_dir = filedialog.askdirectory()
        self.vsResults_value.set(self.vs_results_dir)  

    ##----------------------------------------------------------------------##           
    #                When no filtration radio button in on                   #
    ##----------------------------------------------------------------------##

    def filtraton_option(self):
            # Filtrations options are disabled by default
            if (self.filter_value.get() == 1):  
                # Filter option is diasabled by default
                # filter 1
                self.filter_1["state"] = "disabled"
                self.filter_1_label["state"] = "disabled"
                self.filter_1_entry["state"] = "disabled"
                # filter 2
                self.filter_2["state"] = "disabled"
                self.filter_2_label["state"] = "disabled"
                self.filter_2_entry["state"] = "disabled"
                # filter 3
                self.filter_3["state"] = "disabled"        
                self.filter_3_min["state"] = "disabled"
                self.filter_3_max["state"] = "disabled"       
                self.filter_3_min_entry["state"] = "disabled"
                self.filter_3_max_entry["state"] = "disabled"
                
            else:
                # filter 1 option is active by default
                self.choice_value.set(1)
                # filter 1
                self.filter_1["state"] = "normal"
                self.filter_1_label["state"] = "normal"
                self.filter_1_entry["state"] = "normal"               
                # filter 2
                self.filter_2["state"] = "normal" 
                self.filter_2_label["state"] = "normal"
                self.filter_2_entry["state"] = "disabled"
                # filter 3
                self.filter_3["state"] = "normal" 
                self.filter_3_min["state"] = "normal"
                self.filter_3_max["state"] = "normal"       
                self.filter_3_min_entry["state"] = "disabled"
                self.filter_3_max_entry["state"] = "disabled"
    
    # TO enable only relevant fields in front of  
    def filter_choice(self):
        # When filter 1 is checked on 
        if (self.choice_value.get() == 1):
            # filter 1
            self.filter_1_entry["state"] = "normal"               
            # filter 2
            self.filter_2_entry["state"] = "disabled"
            # filter 3
            self.filter_3_min_entry["state"] = "disabled"
            self.filter_3_max_entry["state"] = "disabled" 
        # When filter 2 is checked on 
        if (self.choice_value.get() == 2):
            # filter 1
            self.filter_1_entry["state"] = "disabled"               
            # filter 2
            self.filter_2_entry["state"] = "normal"
            # filter 3
            self.filter_3_min_entry["state"] = "disabled"
            self.filter_3_max_entry["state"] = "disabled"         
        # When filter 3 is checked on 
        if (self.choice_value.get() == 3):
            # filter 1
            self.filter_1_entry["state"] = "disabled"               
            # filter 2
            self.filter_2_entry["state"] = "disabled"
            # filter 3
            self.filter_3_min_entry["state"] = "normal"
            self.filter_3_max_entry["state"] = "normal"                


    ### -----   Method implemented for the EXIT button ----- ###
    def terminate(self):
        self.master.destroy()
    
    ### ----

    def dummy(self):
        pass

    def run(self):
        # Getting paths
        self.results_dir = (self.vsResults_value.get()) + "/"
        # mkdir -p will update filtered_results if it already exists
        os.system(f'mkdir -p {self.results_dir}/filtered_results')
        
        # When apply filter = ((NO))
        if (self.filter_value.get() == 1):  
            # When filter is not applying, following values are taken
            #  --- param = arranged by parameter selected in the dropdown menu, for example, 8 for delta G
            #  --- choice = null - it remains null when filter option is turned off
            #  --- filter = 0, as filter is off, so its value will be 0
            
            os.system(f'Rscript /usr/local/bin/filtering.R {self.results_dir} {self.param_combo.current()+1} null 0 {self.results_dir}/filtered_results')
            
            # Move the generedted files to filtered_results/ 
            os.system(f'mv {self.results_dir}*pdf {self.results_dir}/filtered_results/')    
            os.system(f'mv {self.results_dir}order* {self.results_dir}/filtered_results/') 
                
 

        # When apply filter = ((YES))
        if (self.filter_value.get() == 2): 
            # When filter is not applying, following values are taken
            #  --- param = arranged by parameter selected in the dropdown menu, for example, 8 for delta G
            #  --- choice = There are 3 options (filters):
            #           1) > some value e.g., ">4"
            #           2) < some value e.g., "<4"
            #           3) in range e.g., "4,8"
            #  --- filter = 1, as filter is on, so its value will be 1

            os.system(f'mkdir -p {self.results_dir}/filtered_results/filtered_pdbs')

            # Filter 1: Arrange output.tsv according to the selected parameter as (values > selected choice)
            if(self.choice_value.get() == 1):
                os.system(f'Rscript /usr/local/bin/filtering.R {self.results_dir} {self.param_combo.current()+1} ">{self.filter_1_value.get()}" 1 {self.results_dir}/filtered_results/')
                
            # Filter 2: Arrange output.tsv according to the selected parameter as (values < selected choice)
            if(self.choice_value.get() == 2):
                os.system(f'Rscript /usr/local/bin/filtering.R {self.results_dir} {self.param_combo.current()+1} "<{self.filter_2_value.get()}" 1 {self.results_dir}/filtered_results/')
                
            # Filter 3: Arrange output.tsv according to the selected parameter as (range (min,max))
            if(self.choice_value.get() == 3):
                os.system(f'Rscript /usr/local/bin/filtering.R {self.results_dir} {self.param_combo.current()+1} "{self.filter_3_min_value.get()},{self.filter_3_max_value.get()}" 1 {self.results_dir}/filtered_results/')

            # Move the filtered pdbs to ../filtered_results/filtered_pdbs/ 
            os.system(f'mv {self.results_dir}/filtered_results/*pdb {self.results_dir}/filtered_results/filtered_pdbs/')  
        
        # Successful completion prompt to user
        tmsg.showinfo("Filtration run successful!", f"Please find your results in:\n\n {self.results_dir}filtered_results/") 


# ==================================================================
# =================================================================
#  (((VSpipe - GUI --> Spatial Filtering)))
# =================================================================
# ===================================================================

class PdbModule:
    def __init__(self, master):
        progress_var = DoubleVar()
        self.master = master
        
        ##---------------------------------------------------------------------##           
        #                           Title Frame (Top)                           #
        ##---------------------------------------------------------------------##

        
        self.f1 = Frame(self.master, borderwidth=5, relief=SUNKEN)
        self.f1.pack(side="top", pady=15)

        self.f1_title = Label(self.f1, text="Spatial Filtering", font="Arial 18 bold", fg="#660099")
        self.f1_title.grid(row=1, column=5, sticky=W, padx=120)

        self.f2 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f2.pack(anchor="nw", padx=20, fill=X)

        self.filter_value = IntVar(value=1)
        self.filter_no = Radiobutton(self.f2, text="Pocket Based Filtering",  bg="#999999", variable=self.filter_value, value=1, command=self.filtraton_option)
        self.filter_yes = Radiobutton(self.f2, text="Interaction Based Filtering",  bg="#999999", variable=self.filter_value, value=2, command=self.filtraton_option)
        self.filter_no.grid(row=0, column=0, sticky=W, padx=15)
        self.filter_yes.grid(row=0, column=2, sticky=E, padx=30)
        ##-----------------------------------------------------------------------------##           
        #   (Frame 2) Browsing to VS results directory and defining output directory   #
        ##----------------------------------------------------------------------------##

        
        
        self.f3 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f3.pack(anchor="nw", padx=20, pady=10, fill=X)

        ### -----   Labels for Inputing file ----- ###
        self.pdbDir_label = Label(self.f3, text="PDB Directory:")
        self.pdbDir_label.grid(row=1, sticky=W, padx=7, pady=5, ipadx=17)
        
        self.pdbDir_value = StringVar()
        self.pdbDir_entry = Entry(self.f3, textvariable=self.pdbDir_value, width=21)
        self.pdbDir_entry.grid(row=1, column=2, padx=8, pady=5)
        
        ### -----   Browse buttons for Inputing file (Ready)----- ###
        self.pdbDir_button = Button(self.f3, text="Browse", command=self.filePathClick)
        self.pdbDir_button.grid(row=1, column=3, padx=10, pady=5)

        self.filePathLabel = Label(self.f3,text="",font=('Arial',14,'bold'))
        self.filePathLabel.place()

        #------------------------------------------------------------------##           
        #             (Frame 2) Browsing to output.csv file                 #
        ##-----------------------------------------------------------------##
        
               ### -----   Labels for Inputing file ----- ###
        self.csv_label = Label(self.f3, text="Ouput.csv File:")
        self.csv_label.grid(row=2, sticky=W, padx=7, pady=5, ipadx=16)
        
        self.csv_value = StringVar()
        self.csv_entry = Entry(self.f3, textvariable=self.csv_value, width=21)
        self.csv_entry.grid(row=2, column=2, padx=8, pady=5)
        
        ### -----   Browse buttons for Inputing file (Ready)----- ###
        self.csv_button = Button(self.f3, text="Browse", command=self.ouputCSV_file)
        self.csv_button.grid(row=2, column=3, padx=5, pady=5)

        ##--------------------------------------------##           
        #      (Frame 2) Define Output directory       #
        ##-------------------------------------------##

        ### -----   Labels for Inputing file ----- ###
        self.outDir_label = Label(self.f3, text="Results Directory:")
        self.outDir_label.grid(row=3, sticky=W, padx=7, pady=5, ipadx=6)
        
        self.outDir_value = StringVar()
        self.outDir_entry = Entry(self.f3, textvariable=self.outDir_value, width=21)
        self.outDir_entry.grid(row=3, column=2, padx=8, pady=5)
        

        
        ##----------------------------------------------------------------------##           
        #             (Frame 3) Browse ligand and define coordinates            #
        ##----------------------------------------------------------------------##

        self.f4 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f4.pack(anchor="nw", padx=20, pady=5, fill=X)
        
        ### -----   Select a ligand ----- ###
        self.lig_label = Label(self.f4, text="Select a Ligand: ")
        self.lig_label.grid(row=1, column=0, sticky=W, padx=7, pady=5, ipadx=13)
        
        self.lig_value = StringVar()
        self.lig_entry = Entry(self.f4, textvariable=self.lig_value, width=12)
        self.lig_entry.grid(row=1, column=1, sticky=W, padx=5, pady=5)
        
        ### -----   Browse buttons for Inputing file (Ready)----- ###
        self.lig_button = Button(self.f4, text="Browse", command=self.ligClick)
        self.lig_button.grid(row=1, column=2, sticky=E,padx=10, pady=40)
        
        self.ligLabel = Label(self.f4,text="")
        self.ligLabel.place()

        # Label of Coordinates
        self.orDef_label = Label(self.f4, text="OR Define", bg="#999999")
        self.orDef_label.grid(row=2, sticky=W, padx=7, pady=5, ipadx=40)
        self.xyzCoord_label = Label(self.f4, text="XYZ Coordinates: ")
        self.xyzCoord_label.grid(row=3, sticky=W, padx=7, pady=5, ipadx=8)
        #self.lig_button = Button(self.f3, text="Load", command=self.coordClick)
        self.lig_button.grid(row=1, column=1, sticky=W, padx=130, pady=5)
        
        # Entry of Coordinates
        self.x_value = DoubleVar()
        self.y_value = DoubleVar()
        self.z_value = DoubleVar()
        self.x_entry = Entry(self.f4, textvariable=self.x_value, width=5)
        self.y_entry = Entry(self.f4, textvariable=self.y_value, width=5)
        self.z_entry = Entry(self.f4, textvariable=self.z_value, width=5)
        self.x_entry.grid(row=3, column=1, sticky=W, pady=7, padx=4)   
        self.y_entry.grid(row=3, column=1, sticky=W, pady=7, padx=65)   
        self.z_entry.grid(row=3, column=1, sticky=W, pady=7, padx=125) 
        
        ### -----   Button for Loading Coordinates----- ###
        # self.lowestPdbDir_button = Button(self.f3, text="Load", command=self.browse_lowestPdbDir_dir)
        # self.lowestPdbDir_button.grid(row=2, column=5, padx=5, pady=5, ipadx=5)
        
        ##----------------------------------------------------------------------##           
        #    (Frame 4) Define number of ligand files need to be separated        #
        ##----------------------------------------------------------------------##

        self.f5 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f5.pack(anchor="nw", padx=20, pady=5, fill=X)
        
        
        self.allAtom = IntVar()
        self.allCheck = Checkbutton(self.f5, text="Any Atom", variable=self.allAtom,onvalue=1, offvalue=0, command=self.allCheckCom)
        self.allCheck.grid(row=1, column=0)
        self.carbon = IntVar()
        self.carbonCheck = Checkbutton(self.f5, text="Carbon",onvalue=1, offvalue=0, variable=self.carbon)
        self.carbonCheck.grid(row=1, column=1)
        self.oxygen = IntVar()
        self.oxygenCheck = Checkbutton(self.f5, text="Oxygen",onvalue=1, offvalue=0, variable=self.oxygen)
        self.oxygenCheck.grid(row=1, column=2)
        self.nitrogen = IntVar()
        self.nitrogenCheck = Checkbutton(self.f5, text="Nitrogen",onvalue=1, offvalue=0, variable=self.nitrogen)
        self.nitrogenCheck.grid(row=1, column=3)
        self.hydrogen = IntVar()
        self.hydrogenCheck = Checkbutton(self.f5, text="Hydrogen",onvalue=1, offvalue=0, variable=self.hydrogen)
        self.hydrogenCheck.grid(row=1, column=4)


        self.f6 = Frame(self.master, borderwidth=5, relief=FLAT, bg="#999999")
        self.f6.pack(anchor="nw", padx=20, pady=5, fill=X)

        # Define Number of Ligands
        self.numLig_label = Label(self.f6, text="No. of Ligands: ")
        self.numLig_label.grid(row=1, column=1, sticky=W, padx=7, pady=7, ipadx=15)
        self.numLig_value = StringVar()
        self.numLig_entry = Entry(self.f6, textvariable=self.numLig_value, width=10)
        self.numLig_entry.grid(row=1, column=2, pady=7, padx=5)

        # All Within X
        self.distanceLabel = Label(self.f6, text="All Within X: ")
        self.distanceLabel.grid(row=2, column=1, sticky=W, padx=7, pady=7, ipadx=25)
        self.distance_value = StringVar()
        self.distanceEntry = Entry(self.f6, textvariable=self.distance_value, width=10)
        self.distanceEntry.grid(row=2, column=2, pady=7, padx=5)
        

        ##----------------------------------------------------------------------##           
        #                             Button Frame (bottom)                      #
        ##----------------------------------------------------------------------##

        self.f7 = Frame(self.master, borderwidth=5, relief=GROOVE)
        self.f7.pack(side="bottom")

        ### -----   Buttons for running the script, clearing and exiting the program ----- ###
        self.run_button = Button(self.f7, text="RUN", fg="green", font="Arial 13 bold", borderwidth=2, command=self.runClick)
        self.exit_button = Button(self.f7, text="EXIT", fg="red", font="Arial 13", command=self.exit)
        self.clear_button = Button(self.f7, text="CLEAR", fg="blue", font="Arial 13", command=self.clear_form)
        self.run_button.grid(row=3, column=6, padx=8)
        self.exit_button.grid(row=3, column=8, padx=8)
        self.clear_button.grid(row=3, column=4, padx=8)     


        self.lig_label["state"] = "normal"
        
        self.lig_button["state"] = "normal"
        self.orDef_label["state"] = "normal"
        self.numLig_entry["state"] = "normal"
        self.numLig_label["state"] = "normal"

        self.allCheck["state"] = "disable"
        self.carbonCheck["state"] = "disable"
        self.oxygenCheck["state"] = "disable"
        self.nitrogenCheck["state"] = "disable"
        self.hydrogenCheck["state"] = "disable"
    
    ##----------------------------------------------------------------------##
    ##                                                                      ##           
    #             METHODS IMPLEMENTED IN THE GUI - Main GUI                  #
    ##                                                                      ##
    ##----------------------------------------------------------------------##

    ##-------------------------------------------------------------------------##           
    #              Browse Buttons and Output directory (Frame 2)               #
    ##-------------------------------------------------------------------------##

    ### -----   for taking VS Results directory from the user ----- ###
    def filtraton_option(self):
        if (self.filter_value.get() == 1): 
            self.lig_label["state"] = "normal"
            
            self.lig_button["state"] = "normal"
            self.orDef_label["state"] = "normal"
            self.numLig_entry["state"] = "normal"
            self.numLig_label["state"] = "normal"

            self.allCheck["state"] = "disable"
            self.carbonCheck["state"] = "disable"
            self.oxygenCheck["state"] = "disable"
            self.nitrogenCheck["state"] = "disable"
            self.hydrogenCheck["state"] = "disable"
        else:
            
            self.allCheck["state"] = "normal"
            self.carbonCheck["state"] = "normal"
            self.oxygenCheck["state"] = "normal"
            self.nitrogenCheck["state"] = "normal"
            self.hydrogenCheck["state"] = "normal"

            self.lig_label["state"] = "disable"
            self.lig_button["state"] = "disable"
            self.orDef_label["state"] = "disable"
            self.numLig_entry["state"] = "disable"
            self.numLig_label["state"] = "disable"
       
    

    def allCheckCom(self):
        if self.allAtom.get()==1:
            
            self.carbonCheck.config(state=DISABLED)
            self.oxygenCheck.config(state=DISABLED)
            self.nitrogenCheck.config(state=DISABLED)
            self.hydrogenCheck.config(state=DISABLED)
        else:
            
            self.carbonCheck.config(state=ACTIVE)
            self.oxygenCheck.config(state=ACTIVE)
            self.nitrogenCheck.config(state=ACTIVE)
            self.hydrogenCheck.config(state=ACTIVE)

    def filePathClick(self):
        self.directory = filedialog.askdirectory()
        self.filePathLabel.config(text = self.directory)
        self.pdbDir_value.set(self.directory)

    ### -----   for taking output.csv file ----- ###
    def ouputCSV_file(self):   
        self.file_selected = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a Receptor File",
                                            filetypes = (("Output.csv file",
                                                            "*.csv"),
                                                        ("all files",
                                                            "*.*")))
        self.csv_value.set(self.file_selected)

    #-------------------------------------------------------------------------##           
    #            Ligands, Coordinates, number of ligands (Frame 3)             #
    ##-------------------------------------------------------------------------##

    # Function to browse ligand file
    def ligClick(self):
        self.lig = filedialog.askopenfilename()
        self.directory = self.filePathLabel.cget("text")
        self.ligname = self.lig.replace(self.directory,"").replace('.pdb','').replace('/','')
        self.ligLabel.config(text = self.ligname)
        numOrDistance = 0
        self.lig_value.set(self.ligname)

    
    def coordClick(self):
        ligOrCoords=1

    #-------------------------------------------------------------------------##           
    #            No. of ligands and all within X (Frame 4)             #
    ##-------------------------------------------------------------------------##
    # Function for All Within X
    def disClick(self):
        numOrDistance = 1
    ##-------------------------------------------------------------------------##           
    #                      Clear and Exit Buttons (Last Frame)                  #
    ##-------------------------------------------------------------------------##

    ### -----   Method implemented for the EXIT button ----- ###
    def exit(self):
        self.master.destroy()

        ### -----   Method implemented for the CLEAR button ----- ###
    def clear_form(self):
        self.pdbDir_entry.delete(0, 'end')
        self.csv_entry.delete(0, 'end')
        self.outDir_entry.delete(0, 'end')
        self.lig_entry.delete(0, 'end')
        self.x_entry.delete(0, 'end')
        self.y_entry.delete(0, 'end')
        self.z_entry.delete(0, 'end')
        self.numLig_entry.delete(0, 'end')
        self.distanceEntry.delete(0, 'end')
        
    ##=======================================================================##           
    #              Methods implemented for (((RUN Button)))                  #
    ##======================================================================##


    ### -----   for RUNNING THE SCRIPT FOR PDB Selection ----- ###
    
    def runClick(self):
        if (self.filter_value.get() == 1):  
            if (self.outDir_value.get()) and (self.lig_entry.get() or self.x_value.get()) and (self.numLig_entry.get() or self.distanceEntry.get()):
                directory = self.pdbDir_value.get()   
                ligname = self.lig_entry.get()
                nameOfFolder = self.outDir_value.get()
                listCopied = []
                excelFile = csv.reader(open(self.csv_value.get()))
                parent_Directory = directory + '/'
                resPath = os.path.join(parent_Directory,nameOfFolder) 
                os.mkdir(resPath)
                os.chdir(directory)
                averageCoords = {}
                listCoords = {}
                points=[]
                distanceToLig ={}
                dtp={}
                x=0
            
                ### -----   loads pdb data and average coords also loads the loading bar ----- ###
                k=0
                progress_var = DoubleVar()
                progressLabel = Label(root, text="Loading data")
                progressLabel.pack()
                progress_var=DoubleVar()
                MAX = len(glob.glob1(directory,"*.pdb"))
                s = ttk.Style()
                s.theme_use('clam')
                s.configure("green.Horizontal.TProgressbar", foreground='green', background='green', font="ArialF 10 bold")
                progressbar = ttk.Progressbar(root,style="green.Horizontal.TProgressbar", mode='determinate', variable=progress_var, maximum=MAX)
                progressbar.pack(fill=X, expand=1)
                for file in os.listdir(directory):
                    
                    
                    if file.endswith(".pdb"):
                        
                        allCoords = 0
                        y=0
                        numofdata =0
                        for x in range(200):
                            try:
                                fileName = file.replace('.pdb', '')
                                a = nx.genfromtxt(file, skip_header=2, skip_footer=x, usecols=[5, 6, 7])
                                arr = nx.array(a)
                                for x in range(len(a)):
                                    listCoords[fileName+'x'+str(x)] = arr[x,0]
                                    listCoords[fileName+'y'+str(x)] = arr[x,1]
                                    listCoords[fileName+'z'+str(x)] = arr[x,2]
                                
                                
                                array = a.mean(axis=0)
                                averageCoords[fileName+'x'] = array[0]
                                averageCoords[fileName+'y'] = array[1]
                                averageCoords[fileName+'z'] = array[2]
                                y=10
                                allCoords = 1 
                                numofdata = x-3
                                
                            except: pass
                            if (y == 10): break
                        
                        progress_var.set(k)
                        k += 1
                        root.update()
                        points=[]
                        num =0
                        if (allCoords==1 and len(a)>2):
                            for row in a:
                                points.append([])
                                points[num].append(a[num][0])
                                points[num].append(a[num][1])
                                points[num].append(a[num][2])
                                num=num+1
                            plane = Plane.best_fit(points)
                            planeX = plane.normal[0]
                            planeY = plane.normal[1]
                            planeZ = plane.normal[2]
                            num=0
                            atomdistance =0
                            for row in a:
                                ligandx = a[num][0]
                                ligandy = a[num][1]
                                ligandz = a[num][2]
                                num=num+1
                                planeC = (plane.normal[0]*(-plane.point[0]))+(plane.normal[1]*(-plane.point[1]))+(plane.normal[2]*(-plane.point[2]))
                                DistanceToPlane = ((abs((ligandx*planeX)+(ligandy*planeY)+(ligandz*planeZ)+(planeC)))/(math.sqrt(((planeX)**2)+((planeY)**2)+((planeZ)**2))))
                                atomdistance = atomdistance+DistanceToPlane
                            dtp[fileName] = (atomdistance/num)    
                        else:
                            dtp[fileName] = ('NA')
                    ### some work to be done
                ### -----   loads ligand xyz or coords xyz depending which option user picked ----- ###

                if self.lig_entry.get() !="":
                    xValue = averageCoords[ligname+"x"]
                    yValue = averageCoords[ligname+"y"]
                    zValue = averageCoords[ligname+"z"]
                else:
                    xValue = float(self.x_value.get())
                    yValue = float(self.y_value.get())
                    zValue = float(self.z_value.get())
                
        
                

                ### -----   gets closet ligands or those within x and copies pdb's to results folder ----- ###

                if self.numLig_entry.get() !="":
                    #Finds the Coordinates for the ligand to be copy, eventually will also acept plain coords
                    numToCopy=int(self.numLig_value.get())
                    #Finds the distance of each ligand to the chosen ligand and adds to dictonary 
                    for file in os.listdir(directory):
                        if file.endswith(".pdb"):
                            try:
                                fileName = file.replace('.pdb', '')
                                averagex = averageCoords[fileName+'x']
                                averagey = averageCoords[fileName+'y']
                                averagez = averageCoords[fileName+'z']
                                distanceox = abs(xValue-averagex)
                                distancetoy = abs(yValue-averagey)
                                distancetoz = abs(zValue-averagez)
                                overalldistance = distancetoy +distanceox +distancetoz
                                distanceToLig[fileName]=overalldistance
                            except: pass
                    #Sorts the dictonary based on the distance values
                    sorted_Values = sorted(distanceToLig.values())
                    sorted_Dict ={}
                    for i in sorted_Values:
                        for k in distanceToLig.keys():
                            if distanceToLig[k] == i:
                                sorted_Dict[k] = distanceToLig[k]
                                break
                
                    #Copys the clost x ligands to the results folder
                    y=0
                    for key, value in sorted_Dict.items():
                        ligandToCopy = key +'.pdb'
                        listCopied.append(key)
                        shutil.copy(ligandToCopy, resPath, follow_symlinks=True)
                        y=y+1
                        if (y==numToCopy):break



                else:
                    distanceToCopy = float(self.distanceEntry.get())
                    for file in os.listdir(directory):
                        if file.endswith(".pdb"):
                            try:
                                fileName = file.replace('.pdb', '')
                                averagex = averageCoords[fileName+'x']
                                averagey = averageCoords[fileName+'y']
                                averagez = averageCoords[fileName+'z']
                                distanceox = abs(xValue-averagex)
                                distancetoy = abs(yValue-averagey)
                                distancetoz = abs(zValue-averagez)
                                overalldistance = distancetoy +distanceox +distancetoz
                                if overalldistance <distanceToCopy:
                                    distanceToLig[fileName]=overalldistance
                            except: pass
                    for key, value in distanceToLig.items():
                        ligandToCopy = key +'.pdb'
                        shutil.copy(ligandToCopy, resPath, follow_symlinks=True)
                    for key, value in distanceToLig.items():
                        listCopied.append(key)
                    

                ### -----   makes new excel file  ----- ###
                columnnames = ["Smiles", "CodeID", "MolecularWeight", "cLogS", "cLogP", "HBD", "HBA", "PSA", "ROTATABLE_BONDS", 
                            "DG", "Ki", "LIGAND_EFFICIENCY", "BEI", "SEI", "NSEI", "NBEI", "nBEI", "mBEI", "AverageX", "AverageY", "AverageZ","PBF Score"]

                datatoenter=[]
                for x in excelFile:
                    try:
                        if x[1] in listCopied:
                            data ={"Smiles":x[0],
                                    "CodeID":x[1],
                                    "MolecularWeight":x[2],
                                    "cLogS":x[3],
                                    "cLogP":x[4],
                                    "HBD":x[5],
                                    "HBA":x[6],
                                    "PSA":x[7],
                                    "ROTATABLE_BONDS":x[8],
                                    "DG":x[9],
                                    "Ki":x[10],
                                    "LIGAND_EFFICIENCY":x[11],
                                    "BEI":x[12],
                                    "SEI":x[13],
                                    "NSEI":x[14],
                                    "NBEI":x[15],
                                    "nBEI":x[16],
                                    "mBEI":x[17],
                                    "AverageX":averageCoords[x[1]+'x'],
                                    "AverageY":averageCoords[x[1]+'y'],
                                    "AverageZ":averageCoords[x[1]+'z'],
                                    "PBF Score":dtp[x[1]]}
                            datatoenter.append(data)
                    except: pass
                df = pd.DataFrame(data=datatoenter)
                #convert into excel
                df.to_excel(resPath+"/"+"FilteredOutput.xlsx", index=False)
                self.outDir_entry.delete(0, 'end')
                self.lig_entry.delete(0, 'end')
                self.x_entry.delete(0, 'end')
                self.y_entry.delete(0, 'end')
                self.z_entry.delete(0, 'end')
                self.numLig_entry.delete(0, 'end')
                self.distanceEntry.delete(0, 'end')
                numcopied = len(listCopied)
                tmsg.showinfo("Done!", f"Execution is completed, \n{numcopied} PDB files copied to {nameOfFolder}")
                progressbar.destroy()
                progressLabel.destroy()

            else:
                tmsg.showinfo("Error", "Please fill in the required boxes.")
        else:
            directory = self.pdbDir_value.get()   
            
            nameOfFolder = self.outDir_value.get()
            xcoord = float(self.x_value.get())
            ycoord = float(self.y_value.get())
            zcoord = float(self.z_value.get())
            within = float(self.distanceEntry.get())
            parent_Directory = directory + '/'
            resPath = os.path.join(parent_Directory,nameOfFolder)
            os.mkdir(resPath) 
            os.chdir(directory)
            listCoords = {}
            listAtoms = {}
            listCopied =[]
            excelFile = csv.reader(open(self.csv_value.get()))
            x=0
            listb = {}
            atoms=0
            catoms=0
            natoms=0
            oatoms=0
            if self.allAtom.get() ==1:
                atoms=1
            if self.carbon.get()==1:
                catoms='C'
            if self.nitrogen.get()==1:
                natoms='N'
            if self.oxygen.get()==1:
                oatoms='O'
            if self.hydrogen.get()==1:
                hatoms='H'
            
           
            ### -----   loads pdb data and average coords also loads the loading bar ----- ###
            k=0
            progress_var = DoubleVar()
            progressLabel = Label(root, text="Loading data")
            progressLabel.pack()
            progress_var=DoubleVar()
            MAX = len(glob.glob1(directory,"*.pdb"))
            s = ttk.Style()
            s.theme_use('clam')
            s.configure("green.Horizontal.TProgressbar", foreground='green', background='green', font="ArialF 10 bold")
            progressbar = ttk.Progressbar(root,style="green.Horizontal.TProgressbar", mode='determinate', variable=progress_var, maximum=MAX)
            progressbar.pack(fill=X, expand=1)
            for file in os.listdir(directory):
                
                
                if file.endswith(".pdb"):
                    fileName = file.replace('.pdb', '')
                    listCoords[fileName] = 1000
                    z=0
                    
                    for x in range(200):
                        try:
                            a=nx.genfromtxt(file, skip_header=2, skip_footer=(x), usecols=[5, 6, 7])
                            Footers = x
                            arr = nx.array(a)
                            b=nx.genfromtxt(file, skip_header=2, skip_footer=(x), usecols=[2], dtype=str)
                               
                            for y in range(len(a)):
                                if listCoords[fileName] > math.sqrt(((xcoord-arr[y,0])**2)+((ycoord-arr[y,1])**2)+((zcoord-arr[y,2])**2)) and ((b[y]==catoms) or atoms==1 or (b[y]==natoms) or (b[y]==oatoms)or (b[y]==hatoms)):
                                    listCoords[fileName] = math.sqrt(((xcoord-arr[y,0])**2)+((ycoord-arr[y,1])**2)+((zcoord-arr[y,2])**2))
                                    listAtoms[fileName] = b[y]
                                       
                            z=10
                        except: pass
                        if (z == 10): break
                    

                    
                    progress_var.set(k)
                    k += 1
                    root.update()

                                       
            
            for key, value in listCoords.items():
                ligandToCopy = key +'.pdb'
                
                if int(listCoords[key]) < int(within):
                    shutil.copy(ligandToCopy, resPath, follow_symlinks=True)
                    listCopied.append(key)
                
            columnnames = ["Smiles", "CodeID", "MolecularWeight", "cLogS", "cLogP", "HBD", "HBA", "PSA", "ROTATABLE_BONDS", 
                        "DG", "Ki", "LIGAND_EFFICIENCY", "BEI", "SEI", "NSEI", "NBEI", "nBEI", "mBEI","Atom", "Distance to Point"]    
            datatoenter=[]
            for x in excelFile:
                try:
                    if x[1] in listCopied:
                        data ={"Smiles":x[0],
                                "CodeID":x[1],
                                "MolecularWeight":x[2],
                                "cLogS":x[3],
                                "cLogP":x[4],
                                "HBD":x[5],
                                "HBA":x[6],
                                "PSA":x[7],
                                "ROTATABLE_BONDS":x[8],
                                "DG":x[9],
                                "Ki":x[10],
                                "LIGAND_EFFICIENCY":x[11],
                                "BEI":x[12],
                                "SEI":x[13],
                                "NSEI":x[14],
                                "NBEI":x[15],
                                "nBEI":x[16],
                                "mBEI":x[17],
                                "Atom":listAtoms[x[1]],
                                "Distance to Point":listCoords[x[1]]
                                }
                        datatoenter.append(data)
                except: pass
            df = pd.DataFrame(data=datatoenter)
            #convert into excel
            df.to_excel(resPath+"/"+"FilteredOutput.xlsx", index=False)    
            progressbar.destroy()
            progressLabel.destroy()
            numcopied = len(listCopied)
            
            tmsg.showinfo("Done!", f"Execution is completed, \n{numcopied} PDB files copied to {nameOfFolder}")







# ==========================================
#  +++++++++++++++++++++++++++++++++++++++++
# ==========================================

### --- Creating object of the class 

if __name__ == '__main__':
    
    root = Tk()
    root.geometry("575x640") # width x length
    # root.resizable(False, False)
    root.resizable(True, True)
    root.title("VSpipe")
    app = VSPipeInterface(root)
    root.mainloop()
