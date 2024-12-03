#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:59:35 2024

@author: elliott
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors as mcolors
import numpy as np
from scipy.stats import linregress
import pandas as pd
import datetime as dt
import math
import cartopy.crs as ccrs
import netCDF4
import numpy as np

'''
Read in our datasets
'''

        
def getIBTRACS(file):
    #Read in IBTRACS
    ibtracs_full  = '/Users/elliott/Documents/Grad Research/dataset_readers/dataset_files/ibtracs.since1980.list.v04r01.csv'
    ibtracs_array   = pd.read_csv(ibtracs_full)
    #read in storm IDs into array
    IBTRACSID = ibtracs_array.loc[:,'SID']


    #read in storm years into array
    year = ibtracs_array.loc[:,'SEASON']



    #read in storm number (XXX) into array
    number = ibtracs_array.loc[:,'NUMBER']



    #read in storm basin into array
    basin = ibtracs_array.loc[:,'BASIN']



    #read in storm name into array
    stormname = ibtracs_array.loc[:,'NAME']

    #read in storm timestamp into array
    timestamp = ibtracs_array.loc[:,'ISO_TIME']
    #let's make this into a datetime array
    timestampList = list(timestamp)
    DTYear = [val[0:4] for val in timestampList]
    DTPrefix = [val[0:2] for val in timestampList]
    DTMonth = [val[5:7] for val in timestampList]
    DTDay = [val[8:10] for val in timestampList]
    DTHour = [val[11:13] for val in timestampList]
    DTMinute = [val[14:16] for val in timestampList]
    DTSecond = [val[17:19] for val in timestampList]


    stormDT = []
    for i in range(len(timestamp)):
        if(DTPrefix[i] == '19' or DTPrefix[i] == '20'):
            DTIndividual = dt.datetime(int(DTYear[i]),int(DTMonth[i]),int(DTDay[i]),int(DTHour[i]),int(DTMinute[i]),int(DTSecond[i]))
            stormDT.append(DTIndividual)
        else:
            stormDT.append(dt.datetime(1979,12,31,23,59,59))
        



    #read in storm nature into array
    stormNature = ibtracs_array.loc[:,'NATURE']

    #so we're going to be using the NHC or JTWC best track data
    #Regarding the JTWC's poor analysis for the SHem in the 80s and 90s, we'll be using Neumann for that

    #first read in the USA lat/lon. This is the base JTWC/NHC analysis
    lat = ibtracs_array.loc[:,'USA_LAT']

    lon = ibtracs_array.loc[:,'USA_LON']


    #Similarly, read in the windspeed and conditionally use Neumann
    vmax = ibtracs_array.loc[:,'USA_WIND']
    
    #read in pressure into array
    pressure = ibtracs_array.loc[:,'WMO_PRES']

    #read in distance to land into array
    disttoland = ibtracs_array.loc[:,'DIST2LAND']

    #read in distance to landfall into array
    disttolandfall = ibtracs_array.loc[:,'LANDFALL']

    #read in ATCF ID into array
    ATCFID = ibtracs_array.loc[:,'USA_ATCF_ID']

    #read in SSHWS type into array
    SSHWS = ibtracs_array.loc[:,'USA_SSHS']
    
    #read in RMW into array
    rmw = ibtracs_array.loc[:,'USA_RMW']




    #create unique array of all ATCF IDs
    alluniqueATCFID = np.unique(ATCFID)
    alluniqueATCFID = alluniqueATCFID[1:]
    
    orderedUniqueATCFID = []
    for i in range(len(ATCFID)-1):
        if ((ATCFID[i+1] != ATCFID[i]) and (ATCFID[i+1] != ' ')):
            thisATCFID = ATCFID[i+1]
            orderedUniqueATCFID.append(thisATCFID)

    
    return(ibtracs_array, IBTRACSID, year, number, basin, stormname, timestamp, stormDT, stormNature,
           lat, lon, vmax, pressure, disttoland, disttolandfall, ATCFID, SSHWS, rmw,
           alluniqueATCFID, orderedUniqueATCFID)
    

#after all variables read in, delete the first row of each array
'''
Example Usage

ibtracs_filename = '/Users/elliott/Documents/Grad Research/dataset_readers/dataset_files/ibtracs.since1980.list.v04r01.csv'
ibtracs_data = getIBTRACS(ibtracs_filename)
'''

def getTCPointsOnly(file):
    #Read in IBTRACS
    ibtracs_full  = '/Users/elliott/Documents/Grad Research/dataset_readers/dataset_files/ibtracs.since1980.list.v04r01.csv'
    ibtracs_array   = pd.read_csv(ibtracs_full)
    #read in storm IDs into array
    IBTRACSID = ibtracs_array.loc[:,'SID']


    #read in storm years into array
    year = ibtracs_array.loc[:,'SEASON']



    #read in storm number (XXX) into array
    number = ibtracs_array.loc[:,'NUMBER']



    #read in storm basin into array
    basin = ibtracs_array.loc[:,'BASIN']



    #read in storm name into array
    stormname = ibtracs_array.loc[:,'NAME']

    #read in storm timestamp into array
    timestamp = ibtracs_array.loc[:,'ISO_TIME']
    #let's make this into a datetime array
    timestampList = list(timestamp)
    DTYear = [val[0:4] for val in timestampList]
    DTPrefix = [val[0:2] for val in timestampList]
    DTMonth = [val[5:7] for val in timestampList]
    DTDay = [val[8:10] for val in timestampList]
    DTHour = [val[11:13] for val in timestampList]
    DTMinute = [val[14:16] for val in timestampList]
    DTSecond = [val[17:19] for val in timestampList]


    stormDT = []
    for i in range(len(timestamp)):
        if(DTPrefix[i] == '19' or DTPrefix[i] == '20'):
            DTIndividual = dt.datetime(int(DTYear[i]),int(DTMonth[i]),int(DTDay[i]),int(DTHour[i]),int(DTMinute[i]),int(DTSecond[i]))
            stormDT.append(DTIndividual)
        else:
            stormDT.append(dt.datetime(1979,12,31,23,59,59))
        



    #read in storm nature into array
    stormNature = ibtracs_array.loc[:,'NATURE']

    #so we're going to be using the NHC or JTWC best track data
    #Regarding the JTWC's poor analysis for the SHem in the 80s and 90s, we'll be using Neumann for that

    #first read in the USA lat/lon. This is the base JTWC/NHC analysis
    lat = ibtracs_array.loc[:,'USA_LAT']

    lon = ibtracs_array.loc[:,'USA_LON']


    #Similarly, read in the windspeed and conditionally use Neumann
    vmax = ibtracs_array.loc[:,'USA_WIND']
    
    #read in pressure into array
    pressure = ibtracs_array.loc[:,'WMO_PRES']

    #read in distance to land into array
    disttoland = ibtracs_array.loc[:,'DIST2LAND']

    #read in distance to landfall into array
    disttolandfall = ibtracs_array.loc[:,'LANDFALL']

    #read in ATCF ID into array
    ATCFID = ibtracs_array.loc[:,'USA_ATCF_ID']

    #read in SSHWS type into array
    SSHWS = ibtracs_array.loc[:,'USA_SSHS']
    
    #read in RMW into array
    rmw = ibtracs_array.loc[:,'USA_RMW']




    #create unique array of all ATCF IDs
    alluniqueATCFID = np.unique(ATCFID)
    alluniqueATCFID = alluniqueATCFID[1:]
    
    orderedUniqueATCFID = []
    for i in range(len(ATCFID)-1):
        if ((ATCFID[i+1] != ATCFID[i]) and (ATCFID[i+1] != ' ')):
            thisATCFID = ATCFID[i+1]
            orderedUniqueATCFID.append(thisATCFID)
            
            
    tcIBTRACSID = []
    tcyear = []
    tcnumber = []
    tcbasin = []
    tcstormname = []
    tctimestamp = []
    tcstormDT = []
    tcstormNature = []
    tclat = []
    tclon = []
    tcvmax = []
    tcpressure = []
    tcdisttoland = []
    tcdisttolandfall = []
    tcATCFID = []
    tcSSHWS = []
    tcrmw = []
    
    for i in range(len(IBTRACSID)):
        if (((SSHWS[i] >= -2)) and vmax[i] != ' ' and vmax[i] != 'kts' and ((DTHour[i] == '00') or (DTHour[i] == '06') or (DTHour[i] == '12') or (DTHour[i] == '18'))):
            tcIBTRACSID.append(IBTRACSID[i])
            tcyear.append(year[i])
            tcnumber.append(number[i])
            tcbasin.append(basin[i])
            tcstormname.append(stormname[i])
            tctimestamp.append(timestamp[i])
            tcstormDT.append(stormDT[i])
            tcstormNature.append(stormNature[i])
            tclat.append(float(lat[i]))
            tclon.append(float(lon[i]))
            tcvmax.append(int(vmax[i]))
            tcpressure.append(pressure[i])
            tcdisttoland.append(disttoland[i])
            tcdisttolandfall.append(disttolandfall[i])
            tcATCFID.append(ATCFID[i])
            tcSSHWS.append(SSHWS[i])
            tcrmw.append(rmw[i])
            
            
    return(tcIBTRACSID, tcyear, tcnumber, tcbasin, tcstormname, tctimestamp, tcstormDT, tcstormNature,
           tclat, tclon, tcvmax, tcpressure, tcdisttoland, tcdisttolandfall, tcATCFID, tcSSHWS, tcrmw,
           alluniqueATCFID, orderedUniqueATCFID)
    
'''
Example usage

tconlyibtracs_data = getTCPointsOnly(ibtracs_filename)
'''

'''
To get all variables:

IBTRACSID = ibtracs_data[0]
year = ibtracs_data[1]
number = ibtracs_data[2]
basin = ibtracs_data[3]
stormname = ibtracs_data[4]
timestamp = ibtracs_data[5]
stormDT = ibtracs_data[6]
stormNature = ibtracs_data[7]
lat = ibtracs_data[8]
lon = ibtracs_data[9]
vmax = ibtracs_data[10]
pressure = ibtracs_data[11]
disttoland = ibtracs_data[12]
disttolandfall = ibtracs_data[13]
ATCFID = ibtracs_data[14]
SSHWS = ibtracs_data[15]
rmw = ibtracs_data[16]
alluniqueATCFID = ibtracs_data[17]
orderedUniqueATCFID = ibtracs_data[18]
'''
