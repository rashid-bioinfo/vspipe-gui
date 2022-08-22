#----------------------#
# 0. CLEAN ENVIRONMENT #
#----------------------#
rm( list = ls( ) )


#-------------#
# 1. GET ARGS #
#-------------#
args <- commandArgs(TRUE)
res.dir      <- args[1] # Name for results directory -- make sure we add abs.path
par.order    <- as.numeric( args[2] )# Order for par to filter
choice       <- args[3] # Filtering choice, e.g., " <-6.0"
filt         <- as.numeric( args[4])# 1=Filtering yes | 0=Filtering no
fil.dir.name <- args[5] # Name for filtered_results directory -- make sure we add abs.path

#------------#
# 2. SET WD  # 
#------------#
setwd( res.dir )


#----------------------#
# 3. DECLARE FUNCTIONS #
#----------------------#

# ------------------------------------------------------------------------#
# Function to generate several plots that inform the user about 
# different different chemical properties
#
#   infile = Data frame. This is the object "inp.output", in which the 
#            "output.csv" file has been saved
#   
#   savedir = Path to where the filtered ligands will be saved
#
# ----------------------------------------------------------------------- #
# Send questions to: Sandra Alvarez-Carretero <sandra.ac93@gmail.com>     #
# ----------------------------------------------------------------------- #
plots_func <- function( infile, savedir ){
  
  # Plot NSEI vs NBEI 
  pdf( paste( savedir, "NSEI-NBEI.pdf", sep = "" ), paper = "a4" ) 
  plot( x = infile$NSEI, y = infile$NBEI, main = "NSEI vs NBEI",
        xlab = "NSEI", ylab = "NBEI", cex.axis = 0.8 )
  text( infile$NSEI, infile$NBEI, labels = infile[,2], pos = 4, cex = 0.3 )
  
  dev.off()
  
  # Plot SEI vs BEI 
  pdf( paste( savedir, "SEI-BEI.pdf", sep = "" ), paper = "a4" )
  plot( x = infile$SEI, y = infile$BEI, main = "SEI vs BEI",
        xlab = "SEI", ylab = "BEI", cex.axis = 0.8 )
  text( infile$SEI, infile$BEI, labels = infile[,2], pos = 4, cex = 0.3 )
  dev.off()
  
  # Plot MW vs Num. compounds 
  range100 <- length( which( infile$MolecularWeight < 100 ) )
  range200 <- length( which( infile$MolecularWeight >= 100 & infile$MolecularWeight < 200 ) )
  range300 <- length( which( infile$MolecularWeight >= 200 & infile$MolecularWeight < 300 ) )
  range400 <- length( which( infile$MolecularWeight >= 300 & infile$MolecularWeight < 400 ) )
  range500 <- length( which( infile$MolecularWeight >= 400 & infile$MolecularWeight < 500 ) )
  rangeEX  <- length( which( infile$MolecularWeight >= 500 ) )
  
  MWvals.bplot <- c( range100, range200, range300, range400, range500, rangeEX )
  #MW.labels    <- c( "MW<100", "100=<MW<200", "200=<MW<300", "300=<MW<400", "400=<MW<500", "MW=<500" )
  MW.labels    <- c( "<100", "[100-200)", "[200-300)", "[300-400)", "[400-500)", "=<500" )
  
  pdf( paste( savedir, "MW-numComp.pdf", sep = "" ), paper = "a4" )
  barplot( height = MWvals.bplot, names.arg = MW.labels, xlab = "MW range",
           ylab = "Number of compounds", main = "MW frequency" )
           #xaxt = 'n' )
  #axis(1, at = 1:length(MW.labels), labels = MW.labels, las = 1, cex.axis = 0.4 )
  dev.off()
  
  # Plot PSA vs Num. compounds 
  psa50  <- length( which( infile$PSA < 50 ) )
  psa100 <- length( which( infile$PSA >= 50 & infile$PSA < 100 ) )
  psa150 <- length( which( infile$PSA >= 100 & infile$PSA < 150 ) )
  psa200 <- length( which( infile$PSA >= 150 & infile$PSA < 200 ) )
  psaEX  <- length( which( infile$PSA >=200 ) )

  PSAvals.bplot <- c( psa50, psa100, psa150, psa200,psaEX )
  PSA.labels    <- c( "<50", "[50-100)", "[100-150)", "[150-200)", "=<200" )
  
  pdf( paste( savedir, "PSA-numComp.pdf", sep = "" ), paper = "a4" )
  barplot( height = PSAvals.bplot, names.arg = PSA.labels, xlab = "MW range",
           ylab = "Number of compounds", main = "PSA frequency" )
  dev.off()
  
  # Plot logP vs Num. compounds 
  clogP1  <- length( which( infile$cLogP < 1 ) )
  clogP2  <- length( which( infile$cLogP >= 1 & infile$cLogP < 2 ) )
  clogP3  <- length( which( infile$cLogP >= 2 & infile$cLogP < 3 ) )
  clogP4  <- length( which( infile$cLogP >= 3 & infile$cLogP < 4 ) )
  clogP5  <- length( which( infile$cLogP >= 4 & infile$cLogP < 5 ) )
  clogP6  <- length( which( infile$cLogP >= 5 & infile$cLogP < 6 ) )
  clogPEX <- length( which( infile$cLogP >=6 ) )
  
  clogPvals.bplot <- c( clogP1, clogP2, clogP3, clogP4, clogP5, clogP6, clogPEX )
  clogP.labels    <- c( "<1", "[1-2)", "[2-3)", "[3-4)", 
                        "[4-5)", "[5-6)", "=<6" )
  
  pdf( paste( savedir, "clogP-NumComp.pdf", sep = "" ), paper = "a4" )
  barplot( height = clogPvals.bplot, names.arg = clogP.labels, xlab = "cLogP",
           ylab = "Number of compounds", main = "cLogP frequency" )
  dev.off()
  
  # Plot HBA vs Num. compounds 
  HBA0  <- length( which( infile$HBA == 0 ) )
  HBA1  <- length( which( infile$HBA == 1 ) )
  HBA2  <- length( which( infile$HBA == 2  ) )
  HBA3  <- length( which( infile$HBA == 3 ) )
  HBA4  <- length( which( infile$HBA == 4 ) )
  HBA5  <- length( which( infile$HBA == 5  ) )
  HBA6  <- length( which( infile$HBA == 6  ) )
  HBA7  <- length( which( infile$HBA == 7  ) )
  HBA8  <- length( which( infile$HBA == 8  ) )
  HBA9  <- length( which( infile$HBA == 9  ) )
  HBAEX <- length( which( infile$HBA >= 10 ) )
  
  HBAvals.bplot <- c( HBA0, HBA1, HBA2, HBA3, HBA4, HBA5, 
                      HBA6, HBA7, HBA8, HBA9, HBAEX )
  HBA.labels <- c( "0", "1", "2", "3", "4", "5",
                   "6", "7", "8", "9", "=<10" )
  
  pdf( paste( savedir, "NumHBA-NumComp.pdf", sep = "" ), paper = "a4" )
  barplot( height = HBAvals.bplot, names.arg = HBA.labels,
           xlab = "Number of HBA",
           ylab = "Number of compounds", main = "Frequency of HBA" )
  dev.off()
  
}


# ------------------------------------------------------------------------#
# Function to filter the data set according to the user's choice
# It takes the following arguments
#
#   infile = Data frame. This is the object "inp.output", in which the 
#            "output.csv" file has been saved
#   
#   choice = Character. This is the filtering choice introduced by 
#            the user. There are three possibilities:
#              a) Greater than a value, e.g,. 5: ">5.0"
#              b) Lower than a value, e.g., 5: "<5.0"
#              c) In a range, e.g., 4 to 8: "4,8"
#
#   par.order = Numeric. The parameter (column) used to filter according
#               to user's choice:
#               1: Molecular Weight    9:  Ki
#               2: cLogS               10: ligand efficiency
#               3: cLogP               11: BEI
#               4: HBD                 12: SEI
#               5: HBA                 13: NSEI
#               6: PSA                 14: NBEI
#               7: rotatable bonds     15: nBEI
#               8: δG                 16: mBEI
#
#   filt = Boolean. 0: no filtering | 1: filtering takes place
#
#   out = Path to where the filtered ligands will be saved
#
# ----------------------------------------------------------------------- #
# Send questions to: Sandra Alvarez-Carretero <sandra.ac93@gmail.com>     #
# ----------------------------------------------------------------------- #
filtering <- function( infile, choice, par.order, filt, out ){
  
  if( filt == 0 ){
    # No filtering -- By default order by 8) δG
    # E.g., par.order = 1 --> 1 + 2 == col3 == MW)
    
    # Get column to filter and order the file according to
    # increasing dG
    val.to.filt <- par.order + 2
    ord.df.filt <- infile[order( infile[,val.to.filt] ),]
    cat( "You have not applied any filters. By default, the\n" )
    cat( "output file has been ordered according to increasing dG\n" )
    
    # Write output ordered and filtered output files and save them 
    # in the main "results" directory
    write.table( ord.df.filt, file = paste( res.dir, "ordered_output.csv", sep = "" ),
                 quote = FALSE, row.names = F, sep = "," )
    write.table( ord.df.filt, file = paste( res.dir, "ordered_output.tsv", sep = "" ),
                 quote = FALSE, row.names = F, sep = "\t" )
    
    # Write output for ATLAS
    ki.list <- rep( "Ki", dim( ord.df.filt )[1] )
    atlas.df <- cbind( as.character( ord.df.filt[,2] ),
                       as.character( ord.df.filt[,1] ),
                       ki.list,
                       as.numeric( ord.df.filt[,11] ) )
    write.table( atlas.df, file = paste( res.dir, "ordered_output_ATLAS.txt", sep = "" ),
                 quote = FALSE, row.names = F, col.names = F, 
                 sep = ";" )
    
    # Generate plots 
    plots_func( infile = ord.df.filt, savedir = res.dir )
  }
  else if( filt == 1 ){
    # Filtering ( According to user )
    # E.g., par.order = 1 --> 1 + 2 == col3 == MW)

    # Get column to filter 
    val.to.filt <- par.order + 2
    
    # Get if choice is to keep ">" or "<" threshod
    split.choice <- strsplit( x = choice, split = "" )
    
    # Check if the split.choice object has ",", ">", or "<"
    inrange <- "," %in% split.choice[[1]]
    greater <- ">" %in% split.choice[[1]]
    lower   <- "<" %in% split.choice[[1]]
    
    if ( greater == TRUE ){
      val.choice <- as.numeric( strsplit( x = choice, split = ">" )[[1]][2] )
      row.ind    <- which( infile[,val.to.filt] > val.choice )
      num.rows   <- length( row.ind ) 
    }
    if ( lower == TRUE ){
      val.choice <- as.numeric( strsplit( x = choice, split = "<" )[[1]][2] )
      row.ind    <- which( infile[,val.to.filt] < val.choice )
      num.rows   <- length( row.ind ) 
    }
    if ( inrange == TRUE ){
      val.choice <- as.numeric( strsplit( x = choice, split = "," )[[1]] )
      row.ind    <- which( infile[,val.to.filt] > min( val.choice ) & infile[,val.to.filt] < max( val.choice ) )
      num.rows   <- length( row.ind )
    }

    # Create data frame according to filtering
    df.filt <- as.matrix( rep(0), nrow = num.rows, ncol = dim( infile )[2] )
    df.filt <- infile[row.ind,]
    
    # Order according to the specified filtering
    ord.df.filt <- df.filt[order( df.filt[,val.to.filt] ),]
    
    # Copy only files that have been filtered in the "filtered" dir
    # We first get the corresponding names from column 2. Then, we 
    # use these names to copy the corresponding file from one dir 
    # to another
    counter <- 0 
    name_ord_filt_mols <- as.character( ord.df.filt[,2] )
    for( i in seq( 1:length( name_ord_filt_mols ) ) ){
      counter = counter + 1
      file.copy( paste( res.dir, "lowest_energy_pdb/", name_ord_filt_mols[i], ".pdb", sep = "" ),
                 out )
    }
    
    # Write output ordered and filtered output files and save them 
    # in "lowest_energy_pdb"
    write.table( ord.df.filt, file = paste( out, "ordered_filt_output.csv", sep = "" ),
                 quote = FALSE, row.names = F, sep = "," )
    write.table( ord.df.filt, file = paste( out, "ordered_filt_output.tsv", sep = "" ),
                 quote = FALSE, row.names = F, sep = "\t" )    
    
    # Write output for ATLAS
    ki.list <- rep( "Ki", dim( ord.df.filt )[1] )
    atlas.df <- cbind( as.character( ord.df.filt[,2] ),
                       as.character( ord.df.filt[,1] ),
                       ki.list,
                       as.numeric( ord.df.filt[,11] ) )
    write.table( atlas.df, file = paste( out, "ordered_output_ATLAS.txt", sep = "" ),
                 quote = FALSE, row.names = F, col.names = F, 
                 sep = ";" )
    
    # Generate plots 
    plots_func( infile = ord.df.filt, savedir = out )

  }

}


#-----------------#
# 4. READ INFILE  # 
#-----------------#
inp.output <- read.csv( file = paste( res.dir, "output.csv", sep = "" ), header = T )


#------------------#
# 5. RUN FILTERING #
#------------------#
filtering( infile = inp.output, par.order = par.order, choice = choice,
           filt = filt, out = fil.dir.name )
