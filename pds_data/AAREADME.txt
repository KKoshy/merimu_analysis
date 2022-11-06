PDS_VERSION_ID        = PDS3                                                  
RECORD_TYPE           = FIXED_LENGTH                                          
RECORD_BYTES          = 80                                                    
OBJECT                = TEXT                                                  
  INTERCHANGE_FORMAT    = ASCII                                               
  PUBLICATION_DATE      = 2004-08-24                                          
  NOTE                  = "N/A"                                               
END_OBJECT            = TEXT                                                  
                                                                              
END                                                                           
                                                                              
                            Mars Exploration Rover                            
                 Inertial Measurement Unit (IMU) Data Archive                 
                         (MER1/MER2-M-IMU-4-EDL-V1.0)                         
                                                                              
                              AAREADME.TXT                                    
                              26 July 2004                                    
                               J.R. Murphy                                    
                       New Mexico State University                            
                                                                              
 This compact disc contains archival inertial measurement unit (IMU) results  
from the Mars Exploration Rover mission(s). This volume includes reduced      
data from Entry, Descent, and Landing (EDL) phases of each rover mission,     
specifically measurements from the accelerometers and gyros within the two    
inertial measurement units (IMUs), one each within the rover and within the   
backshell, on each of the two Mars Exploration Rovers.                        
                                                                              
                                                                              
==============================================================================
VOLUME SET INFORMATION                                                        
==============================================================================
                                                                              
     The diagram below shows the organization of this volume, starting from   
the root of the compact disc.                                                 
                                                                              
            |- VOLDESC.CAT           A description of the contents of this    
            |                        CD_ROM volume in a format readable by    
            |                        both humans and computers.               
            |                                                                 
            |                                                                 
            |- [CATALOG]             A directory containing information       
            |     |                  about the data set                       
            |     |                                                           
            |     |- CATINFO.TXT     Description of files in this directory.  
            |     |                                                           
            |     |- DATASET.CAT     Description of the TRANSFORMED & HIGHRATE
            |     |                  data files and the data processing       
            |     |                                                           
            |     |- INSTHOST.CAT    Description of the Rovers themselves.    
            |     |                                                           
            |     |- INST.CAT        Description of the IMUs & their operation
            |     |                  during Entry, Descent, and Landing (EDL) 
            |     |                                                           
            |     |- MISSION.CAT     Description of the MER mission.          
            |     |                                                           
            |     |- PERSON.CAT      A listing of the people involved in the  
            |     |                  production of this data set and          
            |     |                  this CD-ROM.                             
            |     |                                                           
            |     |- REF.CAT         A list of pertinent references.          
            |                                                                 
            |- [INDEX]               A directory containing an index of data  
            |     |                  files on this volume                     
            |     |                                                           
            |     |- INDXINFO.TXT    Description of files in this directory.  
            |     |                                                           
            |     |- INDEX.TAB       An index of data files on this volume.   
            |     |                                                           
            |     |- INDEX.LBL       The PDS label describing INDEX.TAB.      
            |     |                                                           
            |                                                                 
            |- [DATA]                A directory containing the data files    
            |     |                  and PDS labels describing the contents   
            |     |                  of those files.                          
            |     |                                                           
            |     |- *TRANSFORMED.TAB Data tables containing the transformed  
            |     |                  measurements from the IMUs during EDL    
            |     |                                                           
            |     |- *HIGHRATE.TAB    Data tables containing the high rate    
            |     |                  measurements from the IMUs during EDL    
            |     |                                                           
            |     |- *TRANSFORMED.LBL A file describing the structure of the  
            |     |                  *TRANSFORMED.TAB files.                  
            |     |                                                           
            |     |- *HIGHRATE.LBL    A file describing the structure of the  
            |     |                  *HIGHRATE.TAB file.                      
                                                                              
                                                                              
==============================================================================
DISC FORMAT                                                                   
==============================================================================
                                                                              
     The disc is organized according to the PDS standard for "one data set,   
one volume."  This file (AAREADME.TXT), a PDS volume object definition        
(VOLDESC.CAT), and the listing of errors and changes (ERRATA.TXT) are         
included at the root level.  The following directories of descriptive         
material are also at the root level:                                          
                                                                              
          CATALOG   contains descriptive files for cataloging the data        
                    on this disc.                                             
                                                                              
          INDEX     contains index information (table of contents) on each of 
                    the data files included in this disc.                     
                                                                              
     Text files, including data files of ASCII text and all labels (*.LBL     
files) and tables (*.TAB files), are delimited with carriage-return (ASCII 13)
line-feed (ASCII 10) pairs at the end of each line.  Detached labels and text 
files (*.TXT file names) have fixed length records of 80 bytes to facilitate  
their use as either fixed-length record files or as stream files with         
carriage-return line-feed delimiters.                                         
                                                                              
                                                                              
============================================================================= 
PEER REVIEW                                                                   
==============================================================================
                                                                              
   This volume has not yet undergone a Peer Review as of 26 July, 2004.       
                                                                              
                                                                              
==============================================================================
CITATION INFORMATION                                                          
==============================================================================
                                                                              
                                                                              
    Users wishing to cite this volume in publications should adopt the        
following as the method of citation:                                          
                                                                              
          D.M. Kass, J.T. Schofield, J. Crisp, E.S. Bailey, E.H. Konefat,     
          W.J. Lee, E.C. Litty, R.M. Manning, A.M. San Martin, J.R. Willis,   
          R.F. Beebe, J.R. Murphy and L.F. Huber,                             
          MER1/MER2-M-IMU-4-EDL-V1.0, NASA Planetary Data System, 2004.       
                                                                              
                                                                              
==============================================================================
DISCLAIMER                                                                    
==============================================================================
                                                                              
     Although care has gone into making this volume set, errors are possible. 
Reports of errors or difficulties would be appreciated. Please report any     
errors you detect to:                                                         
                                                                              
James R. Murphy                                                               
New Mexico State University                                                   
Department of Astronomy                                                       
P.O. Box 30001/MSC 4500                                                       
Las Cruces, NM 88003                                                          
Tel: 505-646-5333                                                             
FAX: 505-646-1602                                                             
murphy@nmsu.edu                                                               
                                                                              
