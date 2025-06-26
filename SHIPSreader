#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 08:54:49 2024

@author: elliott
"""


#Start by reading in all SHIPS data.
#To save time, remember to only do this once per session. The arrays are MASSIVE and take a while to read in.
#Comment the array creation sections out once you finish reading in all the data.

#Read in Atlantic SHIPS data

def getSHIPSAtlantic():
    print('Reading North Atlantic SHIPS data...')
    SHIPS_AL_full = open('/Users/elliott/Documents/Grad Research/SHIPS Data/lsdiaga_1982_2022_sat_ts_5day.txt', 'r')
    SHIPS_AL_array = []
    for line in SHIPS_AL_full:
        row = line.split()
        if row[len(row)-1] == 'HEAD':
            rowDate = row[1]
            rowHour = int(row[2])
            rowATCFID = row[7]
        elif row[len(row)-1] == 'LAST':
            for i in range(len(row)-1):
                row[i] = int(row[i])
            rowDateList = []
            rowHourList = []
            rowATCFIDList = []
            for i in range(len(row)-1):
                rowDateList.append(rowDate)
                rowHourList.append(rowHour)
                rowATCFIDList.append(rowATCFID)
            rowDateList.append('DATE')
            rowHourList.append('HOUR')
            rowATCFIDList.append('ATCF')
            SHIPS_AL_array.append(rowDateList)
            SHIPS_AL_array.append(rowHourList)
            SHIPS_AL_array.append(rowATCFIDList)
            SHIPS_AL_array.append(row)
        elif row[len(row)-1] == ('TIME') or row[len(row)-1] == ('VMAX') or row[len(row)-1] == ('MSLP')\
        or row[len(row)-1] == ('TYPE') or row[len(row)-1] == ('DELV') or row[len(row)-1] == ('INCV')\
        or row[len(row)-1] == ('LAT') or row[len(row)-1] == ('LON') or row[len(row)-1] == ('CSST')\
        or row[len(row)-1] == ('CD20') or row[len(row)-1] == ('CD26') or row[len(row)-1] == ('COHC')\
        or row[len(row)-1] == ('DTL') or row[len(row)-1] == ('OAGE') or row[len(row)-1] == ('NAGE')\
        or row[len(row)-2] == ('RSST') or row[len(row)-2] == ('DSST') or row[len(row)-1] == ('DSTA'):
            SHIPS_AL_array.append(row[2:24])
        elif row[len(row)-2] == ('NSST') or row[len(row)-2] == ('NSTA') or row[len(row)-2] == ('NTMX')\
        or row[len(row)-2] == ('NDTX') or row[len(row)-2] == ('NDML') or row[len(row)-2] == ('ND30')\
        or row[len(row)-2] == ('ND28') or row[len(row)-2] == ('ND26') or row[len(row)-2] == ('ND24')\
        or row[len(row)-2] == ('ND22') or row[len(row)-2] == ('ND20') or row[len(row)-2] == ('ND18')\
        or row[len(row)-2] == ('ND16') or row[len(row)-2] == ('NDFR') or row[len(row)-2] == ('NTFR')\
        or row[len(row)-2] == ('NOHC') or row[len(row)-2] == ('ND20'):
            SHIPS_AL_array.append(row[0:22])
        else:
            SHIPS_AL_array.append(row)
    return(SHIPS_AL_array)

def getSHIPSEastPacific():
    #Read in Eastern Pacific SHIPS data   
    print('Reading Eastern Pacific SHIPS data...') 
    SHIPS_EP_full = open('/Users/elliott/Documents/Grad Research/SHIPS Data/lsdiage_1982_2022_sat_ts_5day.txt', 'r')
    SHIPS_EP_array = []
    for line in SHIPS_EP_full:
        row = line.split()
        if row[len(row)-1] == 'HEAD':
            rowDate = row[1]
            rowHour = int(row[2])
            rowATCFID = row[7]
        elif row[len(row)-1] == 'LAST':
            for i in range(len(row)-1):
                row[i] = int(row[i])
            rowDateList = []
            rowHourList = []
            rowATCFIDList = []
            for i in range(len(row)-1):
                rowDateList.append(rowDate)
                rowHourList.append(rowHour)
                rowATCFIDList.append(rowATCFID)
            rowDateList.append('DATE')
            rowHourList.append('HOUR')
            rowATCFIDList.append('ATCF')
            SHIPS_EP_array.append(rowDateList)
            SHIPS_EP_array.append(rowHourList)
            SHIPS_EP_array.append(rowATCFIDList)
            SHIPS_EP_array.append(row)
        elif row[len(row)-1] == ('TIME') or row[len(row)-1] == ('VMAX') or row[len(row)-1] == ('MSLP')\
        or row[len(row)-1] == ('TYPE') or row[len(row)-1] == ('DELV') or row[len(row)-1] == ('INCV')\
        or row[len(row)-1] == ('LAT') or row[len(row)-1] == ('LON') or row[len(row)-1] == ('CSST')\
        or row[len(row)-1] == ('CD20') or row[len(row)-1] == ('CD26') or row[len(row)-1] == ('COHC')\
        or row[len(row)-1] == ('DTL') or row[len(row)-1] == ('OAGE') or row[len(row)-1] == ('NAGE')\
        or row[len(row)-2] == ('RSST') or row[len(row)-2] == ('DSST') or row[len(row)-1] == ('DSTA'):
            SHIPS_EP_array.append(row[2:24])
        elif row[len(row)-2] == ('NSST') or row[len(row)-2] == ('NSTA') or row[len(row)-2] == ('NTMX')\
        or row[len(row)-2] == ('NDTX') or row[len(row)-2] == ('NDML') or row[len(row)-2] == ('ND30')\
        or row[len(row)-2] == ('ND28') or row[len(row)-2] == ('ND26') or row[len(row)-2] == ('ND24')\
        or row[len(row)-2] == ('ND22') or row[len(row)-2] == ('ND20') or row[len(row)-2] == ('ND18')\
        or row[len(row)-2] == ('ND16') or row[len(row)-2] == ('NDFR') or row[len(row)-2] == ('NTFR')\
        or row[len(row)-2] == ('NOHC') or row[len(row)-2] == ('ND20'):
            SHIPS_EP_array.append(row[0:22])
        else:
            SHIPS_EP_array.append(row)
    return(SHIPS_EP_array)

def getSHIPSCentralPacific():
    #Read in Central Pacific SHIPS data    
    print('Reading Central Pacific SHIPS data...')
    SHIPS_CP_full = open('/Users/elliott/Documents/Grad Research/SHIPS Data/lsdiagc_1982_2022_sat_ts_5day.txt', 'r')
    SHIPS_CP_array = []
    for line in SHIPS_CP_full:
        row = line.split()
        if row[len(row)-1] == 'HEAD':
            rowDate = row[1]
            rowHour = int(row[2])
            rowATCFID = row[7]
        elif row[len(row)-1] == 'LAST':
            for i in range(len(row)-1):
                row[i] = int(row[i])
            rowDateList = []
            rowHourList = []
            rowATCFIDList = []
            for i in range(len(row)-1):
                rowDateList.append(rowDate)
                rowHourList.append(rowHour)
                rowATCFIDList.append(rowATCFID)
            rowDateList.append('DATE')
            rowHourList.append('HOUR')
            rowATCFIDList.append('ATCF')
            SHIPS_CP_array.append(rowDateList)
            SHIPS_CP_array.append(rowHourList)
            SHIPS_CP_array.append(rowATCFIDList)
            SHIPS_CP_array.append(row)
        elif row[len(row)-1] == ('TIME') or row[len(row)-1] == ('VMAX') or row[len(row)-1] == ('MSLP')\
        or row[len(row)-1] == ('TYPE') or row[len(row)-1] == ('DELV') or row[len(row)-1] == ('INCV')\
        or row[len(row)-1] == ('LAT') or row[len(row)-1] == ('LON') or row[len(row)-1] == ('CSST')\
        or row[len(row)-1] == ('CD20') or row[len(row)-1] == ('CD26') or row[len(row)-1] == ('COHC')\
        or row[len(row)-1] == ('DTL') or row[len(row)-1] == ('OAGE') or row[len(row)-1] == ('NAGE')\
        or row[len(row)-2] == ('RSST') or row[len(row)-2] == ('DSST') or row[len(row)-1] == ('DSTA'):
            SHIPS_CP_array.append(row[2:24])
        elif row[len(row)-2] == ('NSST') or row[len(row)-2] == ('NSTA') or row[len(row)-2] == ('NTMX')\
        or row[len(row)-2] == ('NDTX') or row[len(row)-2] == ('NDML') or row[len(row)-2] == ('ND30')\
        or row[len(row)-2] == ('ND28') or row[len(row)-2] == ('ND26') or row[len(row)-2] == ('ND24')\
        or row[len(row)-2] == ('ND22') or row[len(row)-2] == ('ND20') or row[len(row)-2] == ('ND18')\
        or row[len(row)-2] == ('ND16') or row[len(row)-2] == ('NDFR') or row[len(row)-2] == ('NTFR')\
        or row[len(row)-2] == ('NOHC') or row[len(row)-2] == ('ND20'):
            SHIPS_CP_array.append(row[0:22])
        else:
            SHIPS_CP_array.append(row)
    return(SHIPS_CP_array)

def getSHIPSWestPacific():
    #Read in Western Pacific SHIPS data    
    print('Reading Western Pacific SHIPS data...')
    SHIPS_WP_full = open('/Users/elliott/Documents/Grad Research/SHIPS Data/lsdiagw_1990_2021_5day.txt', 'r')
    SHIPS_WP_array = []
    for line in SHIPS_WP_full:
        row = line.split()
        if row[len(row)-1] == 'HEAD':
            rowDate = row[1]
            rowHour = int(row[2])
            rowATCFID = row[7]
        elif row[len(row)-1] == 'LAST':
            for i in range(len(row)-1):
                row[i] = int(row[i])
            rowDateList = []
            rowHourList = []
            rowATCFIDList = []
            for i in range(len(row)-1):
                rowDateList.append(rowDate)
                rowHourList.append(rowHour)
                rowATCFIDList.append(rowATCFID)
            rowDateList.append('DATE')
            rowHourList.append('HOUR')
            rowATCFIDList.append('ATCF')
            SHIPS_WP_array.append(rowDateList)
            SHIPS_WP_array.append(rowHourList)
            SHIPS_WP_array.append(rowATCFIDList)
            SHIPS_WP_array.append(row)
        elif row[len(row)-1] == ('TIME') or row[len(row)-1] == ('VMAX') or row[len(row)-1] == ('MSLP')\
        or row[len(row)-1] == ('TYPE') or row[len(row)-1] == ('DELV') or row[len(row)-1] == ('INCV')\
        or row[len(row)-1] == ('LAT') or row[len(row)-1] == ('LON') or row[len(row)-1] == ('CSST')\
        or row[len(row)-1] == ('CD20') or row[len(row)-1] == ('CD26') or row[len(row)-1] == ('COHC')\
        or row[len(row)-1] == ('DTL') or row[len(row)-1] == ('OAGE') or row[len(row)-1] == ('NAGE')\
        or row[len(row)-2] == ('RSST') or row[len(row)-2] == ('DSST') or row[len(row)-1] == ('DSTA'):
            SHIPS_WP_array.append(row[2:24])
        elif row[len(row)-2] == ('NSST') or row[len(row)-2] == ('NSTA') or row[len(row)-2] == ('NTMX')\
        or row[len(row)-2] == ('NDTX') or row[len(row)-2] == ('NDML') or row[len(row)-2] == ('ND30')\
        or row[len(row)-2] == ('ND28') or row[len(row)-2] == ('ND26') or row[len(row)-2] == ('ND24')\
        or row[len(row)-2] == ('ND22') or row[len(row)-2] == ('ND20') or row[len(row)-2] == ('ND18')\
        or row[len(row)-2] == ('ND16') or row[len(row)-2] == ('NDFR') or row[len(row)-2] == ('NTFR')\
        or row[len(row)-2] == ('RHCN') or row[len(row)-2] == ('ND20'):
            SHIPS_WP_array.append(row[0:22])
        else:
            SHIPS_WP_array.append(row)
    return(SHIPS_WP_array)

def getSHIPSNorthIndian():
    #Read in North Indian Ocean SHIPS data    
    print('Reading North Indian Ocean SHIPS data...')
    SHIPS_IO_full = open('/Users/elliott/Documents/Grad Research/SHIPS Data/lsdiagi_1990_2021_5day.txt', 'r')
    SHIPS_IO_array = []
    for line in SHIPS_IO_full:
        row = line.split()
        if row[len(row)-1] == 'HEAD':
            rowDate = row[1]
            rowHour = int(row[2])
            rowATCFID = row[7]
        elif row[len(row)-1] == 'LAST':
            for i in range(len(row)-1):
                row[i] = int(row[i])
            rowDateList = []
            rowHourList = []
            rowATCFIDList = []
            for i in range(len(row)-1):
                rowDateList.append(rowDate)
                rowHourList.append(rowHour)
                rowATCFIDList.append(rowATCFID)
            rowDateList.append('DATE')
            rowHourList.append('HOUR')
            rowATCFIDList.append('ATCF')
            SHIPS_IO_array.append(rowDateList)
            SHIPS_IO_array.append(rowHourList)
            SHIPS_IO_array.append(rowATCFIDList)
            SHIPS_IO_array.append(row)
        elif row[len(row)-1] == ('TIME') or row[len(row)-1] == ('VMAX') or row[len(row)-1] == ('MSLP')\
        or row[len(row)-1] == ('TYPE') or row[len(row)-1] == ('DELV') or row[len(row)-1] == ('INCV')\
        or row[len(row)-1] == ('LAT') or row[len(row)-1] == ('LON') or row[len(row)-1] == ('CSST')\
        or row[len(row)-1] == ('CD20') or row[len(row)-1] == ('CD26') or row[len(row)-1] == ('COHC')\
        or row[len(row)-1] == ('DTL') or row[len(row)-1] == ('OAGE') or row[len(row)-1] == ('NAGE')\
        or row[len(row)-2] == ('RSST') or row[len(row)-2] == ('DSST') or row[len(row)-1] == ('DSTA'):
            SHIPS_IO_array.append(row[2:24])
        elif row[len(row)-2] == ('NSST') or row[len(row)-2] == ('NSTA') or row[len(row)-2] == ('NTMX')\
        or row[len(row)-2] == ('NDTX') or row[len(row)-2] == ('NDML') or row[len(row)-2] == ('ND30')\
        or row[len(row)-2] == ('ND28') or row[len(row)-2] == ('ND26') or row[len(row)-2] == ('ND24')\
        or row[len(row)-2] == ('ND22') or row[len(row)-2] == ('ND20') or row[len(row)-2] == ('ND18')\
        or row[len(row)-2] == ('ND16') or row[len(row)-2] == ('NDFR') or row[len(row)-2] == ('NTFR')\
        or row[len(row)-2] == ('RHCN') or row[len(row)-2] == ('ND20'):
            SHIPS_IO_array.append(row[0:22])
        else:
            SHIPS_IO_array.append(row)
    return(SHIPS_IO_array)


def getSHIPSSouthHemisphere():
    #Read in Southern Hemisphere SHIPS data    
    print('Reading Southern Hemisphere SHIPS data...')
    SHIPS_SH_full = open('/Users/elliott/Documents/Grad Research/SHIPS Data/lsdiags_1998_2021_5day.txt', 'r')
    SHIPS_SH_array = []
    for line in SHIPS_SH_full:
        row = line.split()
        if row[len(row)-1] == 'HEAD':
            rowDate = row[1]
            rowHour = int(row[2])
            rowATCFID = row[7]
        elif row[len(row)-1] == 'LAST':
            for i in range(len(row)-1):
                row[i] = int(row[i])
            rowDateList = []
            rowHourList = []
            rowATCFIDList = []
            for i in range(len(row)-1):
                rowDateList.append(rowDate)
                rowHourList.append(rowHour)
                rowATCFIDList.append(rowATCFID)
            rowDateList.append('DATE')
            rowHourList.append('HOUR')
            rowATCFIDList.append('ATCF')
            SHIPS_SH_array.append(rowDateList)
            SHIPS_SH_array.append(rowHourList)
            SHIPS_SH_array.append(rowATCFIDList)
            SHIPS_SH_array.append(row)
        elif row[len(row)-1] == ('TIME') or row[len(row)-1] == ('VMAX') or row[len(row)-1] == ('MSLP')\
        or row[len(row)-1] == ('TYPE') or row[len(row)-1] == ('DELV') or row[len(row)-1] == ('INCV')\
        or row[len(row)-1] == ('LAT') or row[len(row)-1] == ('LON') or row[len(row)-1] == ('CSST')\
        or row[len(row)-1] == ('CD20') or row[len(row)-1] == ('CD26') or row[len(row)-1] == ('COHC')\
        or row[len(row)-1] == ('DTL') or row[len(row)-1] == ('OAGE') or row[len(row)-1] == ('NAGE')\
        or row[len(row)-2] == ('RSST') or row[len(row)-2] == ('DSST') or row[len(row)-1] == ('DSTA'):
            SHIPS_SH_array.append(row[2:24])
        elif row[len(row)-2] == ('NSST') or row[len(row)-2] == ('NSTA') or row[len(row)-2] == ('NTMX')\
        or row[len(row)-2] == ('NDTX') or row[len(row)-2] == ('NDML') or row[len(row)-2] == ('ND30')\
        or row[len(row)-2] == ('ND28') or row[len(row)-2] == ('ND26') or row[len(row)-2] == ('ND24')\
        or row[len(row)-2] == ('ND22') or row[len(row)-2] == ('ND20') or row[len(row)-2] == ('ND18')\
        or row[len(row)-2] == ('ND16') or row[len(row)-2] == ('NDFR') or row[len(row)-2] == ('NTFR')\
        or row[len(row)-2] == ('RHCN') or row[len(row)-2] == ('ND20'):
            SHIPS_SH_array.append(row[0:22])
        else:
            SHIPS_SH_array.append(row)
    return(SHIPS_SH_array)
    
def getSHIPSGlobal():
    SHIPS_global_array = []
    print('Reading North Atlantic SHIPS data...')
    SHIPS_AL_full = open('/Users/elliott/Documents/Grad Research/SHIPS Data/lsdiaga_1982_2022_sat_ts_5day.txt', 'r')
    for line in SHIPS_AL_full:
        row = line.split()
        if row[len(row)-1] == 'HEAD':
            rowDate = row[1]
            rowHour = int(row[2])
            rowATCFID = row[7]
        elif row[len(row)-1] == 'LAST':
            for i in range(len(row)-1):
                row[i] = int(row[i])
            rowDateList = []
            rowHourList = []
            rowATCFIDList = []
            for i in range(len(row)-1):
                rowDateList.append(rowDate)
                rowHourList.append(rowHour)
                rowATCFIDList.append(rowATCFID)
            rowDateList.append('DATE')
            rowHourList.append('HOUR')
            rowATCFIDList.append('ATCF')
            SHIPS_global_array.append(rowDateList)
            SHIPS_global_array.append(rowHourList)
            SHIPS_global_array.append(rowATCFIDList)
            SHIPS_global_array.append(row)
        elif row[len(row)-1] == ('TIME') or row[len(row)-1] == ('VMAX') or row[len(row)-1] == ('MSLP')\
        or row[len(row)-1] == ('TYPE') or row[len(row)-1] == ('DELV') or row[len(row)-1] == ('INCV')\
        or row[len(row)-1] == ('LAT') or row[len(row)-1] == ('LON') or row[len(row)-1] == ('CSST')\
        or row[len(row)-1] == ('CD20') or row[len(row)-1] == ('CD26') or row[len(row)-1] == ('COHC')\
        or row[len(row)-1] == ('DTL') or row[len(row)-1] == ('OAGE') or row[len(row)-1] == ('NAGE')\
        or row[len(row)-2] == ('RSST') or row[len(row)-2] == ('DSST') or row[len(row)-1] == ('DSTA'):
            SHIPS_global_array.append(row[2:24])
        elif row[len(row)-2] == ('NSST') or row[len(row)-2] == ('NSTA') or row[len(row)-2] == ('NTMX')\
        or row[len(row)-2] == ('NDTX') or row[len(row)-2] == ('NDML') or row[len(row)-2] == ('ND30')\
        or row[len(row)-2] == ('ND28') or row[len(row)-2] == ('ND26') or row[len(row)-2] == ('ND24')\
        or row[len(row)-2] == ('ND22') or row[len(row)-2] == ('ND20') or row[len(row)-2] == ('ND18')\
        or row[len(row)-2] == ('ND16') or row[len(row)-2] == ('NDFR') or row[len(row)-2] == ('NTFR')\
        or row[len(row)-2] == ('NOHC') or row[len(row)-2] == ('ND20'):
            SHIPS_global_array.append(row[0:22])
        else:
            SHIPS_global_array.append(row)

    #Read in Eastern Pacific SHIPS data   
    print('Reading Eastern Pacific SHIPS data...') 
    SHIPS_EP_full = open('/Users/elliott/Documents/Grad Research/SHIPS Data/lsdiage_1982_2022_sat_ts_5day.txt', 'r')
    for line in SHIPS_EP_full:
        row = line.split()
        if row[len(row)-1] == 'HEAD':
            rowDate = row[1]
            rowHour = int(row[2])
            rowATCFID = row[7]
        elif row[len(row)-1] == 'LAST':
            for i in range(len(row)-1):
                row[i] = int(row[i])
            rowDateList = []
            rowHourList = []
            rowATCFIDList = []
            for i in range(len(row)-1):
                rowDateList.append(rowDate)
                rowHourList.append(rowHour)
                rowATCFIDList.append(rowATCFID)
            rowDateList.append('DATE')
            rowHourList.append('HOUR')
            rowATCFIDList.append('ATCF')
            SHIPS_global_array.append(rowDateList)
            SHIPS_global_array.append(rowHourList)
            SHIPS_global_array.append(rowATCFIDList)
            SHIPS_global_array.append(row)
        elif row[len(row)-1] == ('TIME') or row[len(row)-1] == ('VMAX') or row[len(row)-1] == ('MSLP')\
        or row[len(row)-1] == ('TYPE') or row[len(row)-1] == ('DELV') or row[len(row)-1] == ('INCV')\
        or row[len(row)-1] == ('LAT') or row[len(row)-1] == ('LON') or row[len(row)-1] == ('CSST')\
        or row[len(row)-1] == ('CD20') or row[len(row)-1] == ('CD26') or row[len(row)-1] == ('COHC')\
        or row[len(row)-1] == ('DTL') or row[len(row)-1] == ('OAGE') or row[len(row)-1] == ('NAGE')\
        or row[len(row)-2] == ('RSST') or row[len(row)-2] == ('DSST') or row[len(row)-1] == ('DSTA'):
            SHIPS_global_array.append(row[2:24])
        elif row[len(row)-2] == ('NSST') or row[len(row)-2] == ('NSTA') or row[len(row)-2] == ('NTMX')\
        or row[len(row)-2] == ('NDTX') or row[len(row)-2] == ('NDML') or row[len(row)-2] == ('ND30')\
        or row[len(row)-2] == ('ND28') or row[len(row)-2] == ('ND26') or row[len(row)-2] == ('ND24')\
        or row[len(row)-2] == ('ND22') or row[len(row)-2] == ('ND20') or row[len(row)-2] == ('ND18')\
        or row[len(row)-2] == ('ND16') or row[len(row)-2] == ('NDFR') or row[len(row)-2] == ('NTFR')\
        or row[len(row)-2] == ('NOHC') or row[len(row)-2] == ('ND20'):
            SHIPS_global_array.append(row[0:22])
        else:
            SHIPS_global_array.append(row)

    #Read in Central Pacific SHIPS data    
    print('Reading Central Pacific SHIPS data...')
    SHIPS_CP_full = open('/Users/elliott/Documents/Grad Research/SHIPS Data/lsdiagc_1982_2022_sat_ts_5day.txt', 'r')
    for line in SHIPS_CP_full:
        row = line.split()
        if row[len(row)-1] == 'HEAD':
            rowDate = row[1]
            rowHour = int(row[2])
            rowATCFID = row[7]
        elif row[len(row)-1] == 'LAST':
            for i in range(len(row)-1):
                row[i] = int(row[i])
            rowDateList = []
            rowHourList = []
            rowATCFIDList = []
            for i in range(len(row)-1):
                rowDateList.append(rowDate)
                rowHourList.append(rowHour)
                rowATCFIDList.append(rowATCFID)
            rowDateList.append('DATE')
            rowHourList.append('HOUR')
            rowATCFIDList.append('ATCF')
            SHIPS_global_array.append(rowDateList)
            SHIPS_global_array.append(rowHourList)
            SHIPS_global_array.append(rowATCFIDList)
            SHIPS_global_array.append(row)
        elif row[len(row)-1] == ('TIME') or row[len(row)-1] == ('VMAX') or row[len(row)-1] == ('MSLP')\
        or row[len(row)-1] == ('TYPE') or row[len(row)-1] == ('DELV') or row[len(row)-1] == ('INCV')\
        or row[len(row)-1] == ('LAT') or row[len(row)-1] == ('LON') or row[len(row)-1] == ('CSST')\
        or row[len(row)-1] == ('CD20') or row[len(row)-1] == ('CD26') or row[len(row)-1] == ('COHC')\
        or row[len(row)-1] == ('DTL') or row[len(row)-1] == ('OAGE') or row[len(row)-1] == ('NAGE')\
        or row[len(row)-2] == ('RSST') or row[len(row)-2] == ('DSST') or row[len(row)-1] == ('DSTA'):
            SHIPS_global_array.append(row[2:24])
        elif row[len(row)-2] == ('NSST') or row[len(row)-2] == ('NSTA') or row[len(row)-2] == ('NTMX')\
        or row[len(row)-2] == ('NDTX') or row[len(row)-2] == ('NDML') or row[len(row)-2] == ('ND30')\
        or row[len(row)-2] == ('ND28') or row[len(row)-2] == ('ND26') or row[len(row)-2] == ('ND24')\
        or row[len(row)-2] == ('ND22') or row[len(row)-2] == ('ND20') or row[len(row)-2] == ('ND18')\
        or row[len(row)-2] == ('ND16') or row[len(row)-2] == ('NDFR') or row[len(row)-2] == ('NTFR')\
        or row[len(row)-2] == ('NOHC') or row[len(row)-2] == ('ND20'):
            SHIPS_global_array.append(row[0:22])
        else:
            SHIPS_global_array.append(row)

    #Read in Western Pacific SHIPS data    
    print('Reading Western Pacific SHIPS data...')
    SHIPS_WP_full = open('/Users/elliott/Documents/Grad Research/SHIPS Data/lsdiagw_1990_2021_5day.txt', 'r')
    for line in SHIPS_WP_full:
        row = line.split()
        if row[len(row)-1] == 'HEAD':
            rowDate = row[1]
            rowHour = int(row[2])
            rowATCFID = row[7]
        elif row[len(row)-1] == 'LAST':
            for i in range(len(row)-1):
                row[i] = int(row[i])
            rowDateList = []
            rowHourList = []
            rowATCFIDList = []
            for i in range(len(row)-1):
                rowDateList.append(rowDate)
                rowHourList.append(rowHour)
                rowATCFIDList.append(rowATCFID)
            rowDateList.append('DATE')
            rowHourList.append('HOUR')
            rowATCFIDList.append('ATCF')
            SHIPS_global_array.append(rowDateList)
            SHIPS_global_array.append(rowHourList)
            SHIPS_global_array.append(rowATCFIDList)
            SHIPS_global_array.append(row)
        elif row[len(row)-1] == ('TIME') or row[len(row)-1] == ('VMAX') or row[len(row)-1] == ('MSLP')\
        or row[len(row)-1] == ('TYPE') or row[len(row)-1] == ('DELV') or row[len(row)-1] == ('INCV')\
        or row[len(row)-1] == ('LAT') or row[len(row)-1] == ('LON') or row[len(row)-1] == ('CSST')\
        or row[len(row)-1] == ('CD20') or row[len(row)-1] == ('CD26') or row[len(row)-1] == ('COHC')\
        or row[len(row)-1] == ('DTL') or row[len(row)-1] == ('OAGE') or row[len(row)-1] == ('NAGE')\
        or row[len(row)-2] == ('RSST') or row[len(row)-2] == ('DSST') or row[len(row)-1] == ('DSTA'):
            SHIPS_global_array.append(row[2:24])
        elif row[len(row)-2] == ('NSST') or row[len(row)-2] == ('NSTA') or row[len(row)-2] == ('NTMX')\
        or row[len(row)-2] == ('NDTX') or row[len(row)-2] == ('NDML') or row[len(row)-2] == ('ND30')\
        or row[len(row)-2] == ('ND28') or row[len(row)-2] == ('ND26') or row[len(row)-2] == ('ND24')\
        or row[len(row)-2] == ('ND22') or row[len(row)-2] == ('ND20') or row[len(row)-2] == ('ND18')\
        or row[len(row)-2] == ('ND16') or row[len(row)-2] == ('NDFR') or row[len(row)-2] == ('NTFR')\
        or row[len(row)-2] == ('RHCN') or row[len(row)-2] == ('ND20'):
            SHIPS_global_array.append(row[0:22])
        else:
            SHIPS_global_array.append(row)

    #Read in North Indian Ocean SHIPS data    
    print('Reading North Indian Ocean SHIPS data...')
    SHIPS_IO_full = open('/Users/elliott/Documents/Grad Research/SHIPS Data/lsdiagi_1990_2021_5day.txt', 'r')
    for line in SHIPS_IO_full:
        row = line.split()
        if row[len(row)-1] == 'HEAD':
            rowDate = row[1]
            rowHour = int(row[2])
            rowATCFID = row[7]
        elif row[len(row)-1] == 'LAST':
            for i in range(len(row)-1):
                row[i] = int(row[i])
            rowDateList = []
            rowHourList = []
            rowATCFIDList = []
            for i in range(len(row)-1):
                rowDateList.append(rowDate)
                rowHourList.append(rowHour)
                rowATCFIDList.append(rowATCFID)
            rowDateList.append('DATE')
            rowHourList.append('HOUR')
            rowATCFIDList.append('ATCF')
            SHIPS_global_array.append(rowDateList)
            SHIPS_global_array.append(rowHourList)
            SHIPS_global_array.append(rowATCFIDList)
            SHIPS_global_array.append(row)
        elif row[len(row)-1] == ('TIME') or row[len(row)-1] == ('VMAX') or row[len(row)-1] == ('MSLP')\
        or row[len(row)-1] == ('TYPE') or row[len(row)-1] == ('DELV') or row[len(row)-1] == ('INCV')\
        or row[len(row)-1] == ('LAT') or row[len(row)-1] == ('LON') or row[len(row)-1] == ('CSST')\
        or row[len(row)-1] == ('CD20') or row[len(row)-1] == ('CD26') or row[len(row)-1] == ('COHC')\
        or row[len(row)-1] == ('DTL') or row[len(row)-1] == ('OAGE') or row[len(row)-1] == ('NAGE')\
        or row[len(row)-2] == ('RSST') or row[len(row)-2] == ('DSST') or row[len(row)-1] == ('DSTA'):
            SHIPS_global_array.append(row[2:24])
        elif row[len(row)-2] == ('NSST') or row[len(row)-2] == ('NSTA') or row[len(row)-2] == ('NTMX')\
        or row[len(row)-2] == ('NDTX') or row[len(row)-2] == ('NDML') or row[len(row)-2] == ('ND30')\
        or row[len(row)-2] == ('ND28') or row[len(row)-2] == ('ND26') or row[len(row)-2] == ('ND24')\
        or row[len(row)-2] == ('ND22') or row[len(row)-2] == ('ND20') or row[len(row)-2] == ('ND18')\
        or row[len(row)-2] == ('ND16') or row[len(row)-2] == ('NDFR') or row[len(row)-2] == ('NTFR')\
        or row[len(row)-2] == ('RHCN') or row[len(row)-2] == ('ND20'):
            SHIPS_global_array.append(row[0:22])
        else:
            SHIPS_global_array.append(row)

    #Read in Southern Hemisphere SHIPS data    
    print('Reading Southern Hemisphere SHIPS data...')
    SHIPS_SH_full = open('/Users/elliott/Documents/Grad Research/SHIPS Data/lsdiags_1998_2021_5day.txt', 'r')
    for line in SHIPS_SH_full:
        row = line.split()
        if row[len(row)-1] == 'HEAD':
            rowDate = row[1]
            rowHour = int(row[2])
            rowATCFID = row[7]
        elif row[len(row)-1] == 'LAST':
            for i in range(len(row)-1):
                row[i] = int(row[i])
            rowDateList = []
            rowHourList = []
            rowATCFIDList = []
            for i in range(len(row)-1):
                rowDateList.append(rowDate)
                rowHourList.append(rowHour)
                rowATCFIDList.append(rowATCFID)
            rowDateList.append('DATE')
            rowHourList.append('HOUR')
            rowATCFIDList.append('ATCF')
            SHIPS_global_array.append(rowDateList)
            SHIPS_global_array.append(rowHourList)
            SHIPS_global_array.append(rowATCFIDList)
            SHIPS_global_array.append(row)
        elif row[len(row)-1] == ('TIME') or row[len(row)-1] == ('VMAX') or row[len(row)-1] == ('MSLP')\
        or row[len(row)-1] == ('TYPE') or row[len(row)-1] == ('DELV') or row[len(row)-1] == ('INCV')\
        or row[len(row)-1] == ('LAT') or row[len(row)-1] == ('LON') or row[len(row)-1] == ('CSST')\
        or row[len(row)-1] == ('CD20') or row[len(row)-1] == ('CD26') or row[len(row)-1] == ('COHC')\
        or row[len(row)-1] == ('DTL') or row[len(row)-1] == ('OAGE') or row[len(row)-1] == ('NAGE')\
        or row[len(row)-2] == ('RSST') or row[len(row)-2] == ('DSST') or row[len(row)-1] == ('DSTA'):
            SHIPS_global_array.append(row[2:24])
        elif row[len(row)-2] == ('NSST') or row[len(row)-2] == ('NSTA') or row[len(row)-2] == ('NTMX')\
        or row[len(row)-2] == ('NDTX') or row[len(row)-2] == ('NDML') or row[len(row)-2] == ('ND30')\
        or row[len(row)-2] == ('ND28') or row[len(row)-2] == ('ND26') or row[len(row)-2] == ('ND24')\
        or row[len(row)-2] == ('ND22') or row[len(row)-2] == ('ND20') or row[len(row)-2] == ('ND18')\
        or row[len(row)-2] == ('ND16') or row[len(row)-2] == ('NDFR') or row[len(row)-2] == ('NTFR')\
        or row[len(row)-2] == ('RHCN') or row[len(row)-2] == ('ND20'):
            SHIPS_global_array.append(row[0:22])
        else:
            SHIPS_global_array.append(row)
   
    return SHIPS_global_array


#Finished reading all the datasets in!
def getSHIPSVariable(array, variable):
    SHIPS_Variable_Array = []
    for i in range(len(array)):
        row = array[i]
        if row[21] == variable:
            if variable == 'LAT' or variable == 'LON' or variable == 'CSST' or variable == 'OAGE'\
            or variable == 'NAGE' or variable == 'RSST' or variable == 'DSST' or variable == 'DSTA'\
            or variable == 'U200' or variable == 'U20C' or variable == 'V20C' or variable == 'V000'\
            or variable == 'EPOS' or variable == 'ENEG' or variable == 'EPSS' or variable == 'ENSS'\
            or variable == 'T000' or variable == 'TLAT' or variable == 'TLON' or variable == 'TWAC'\
            or variable == 'TWXC' or variable == 'G150' or variable == 'G200' or variable == 'G250'\
            or variable == 'V000' or variable == 'V850' or variable == 'V500' or variable == 'V300'\
            or variable == 'SHDC' or variable == 'SHGC' or variable == 'T150' or variable == 'T200'\
            or variable == 'T250' or variable == 'SHRD' or variable == 'SHRS' or variable == 'SHRG'\
            or variable == 'HE07' or variable == 'HE05' or variable == 'PW01' or variable == 'PW02'\
            or variable == 'PW03' or variable == 'PW04' or variable == 'PW05' or variable == 'PW06'\
            or variable == 'PW07' or variable == 'PW08' or variable == 'PW09' or variable == 'PW10'\
            or variable == 'PW11' or variable == 'PW12' or variable == 'PW13' or variable == 'PW14'\
            or variable == 'PW15' or variable == 'PW16' or variable == 'PW17' or variable == 'PW18'\
            or variable == 'PW19' or variable == 'XDST' or variable == 'XNST' or variable == 'XTMX'\
            or variable == 'XTFR':
                SHIPS_Variable_Array.append((float(row[0])/10))
            elif variable == 'ATCF' or variable == 'DATE':
                SHIPS_Variable_Array.append(row[0])
            else:
                SHIPS_Variable_Array.append(int(row[0]))
    return SHIPS_Variable_Array


#Finished reading all the datasets in!
def getSHIPSVariableCombined(array, variable1, variable2):
    SHIPS_Variable_Array = []
    for i in range(len(array)):
        row = array[i]
        if row[21] == variable1 or row[21] == variable2:
            if variable1 == 'LAT' or variable1 == 'LON' or variable1 == 'CSST' or variable1 == 'OAGE'\
            or variable1 == 'NAGE' or variable1 == 'RSST' or variable1 == 'DSST' or variable1 == 'DSTA'\
            or variable1 == 'U200' or variable1 == 'U20C' or variable1 == 'V20C' or variable1 == 'V000'\
            or variable1 == 'EPOS' or variable1 == 'ENEG' or variable1 == 'EPSS' or variable1 == 'ENSS'\
            or variable1 == 'T000' or variable1 == 'TLAT' or variable1 == 'TLON' or variable1 == 'TWAC'\
            or variable1 == 'TWXC' or variable1 == 'G150' or variable1 == 'G200' or variable1 == 'G250'\
            or variable1 == 'V000' or variable1 == 'V850' or variable1 == 'V500' or variable1 == 'V300'\
            or variable1 == 'SHDC' or variable1 == 'SHGC' or variable1 == 'T150' or variable1 == 'T200'\
            or variable1 == 'T250' or variable1 == 'SHRD' or variable1 == 'SHRS' or variable1 == 'SHRG'\
            or variable1 == 'HE07' or variable1 == 'HE05' or variable1 == 'PW01' or variable1 == 'PW02'\
            or variable1 == 'PW03' or variable1 == 'PW04' or variable1 == 'PW05' or variable1 == 'PW06'\
            or variable1 == 'PW07' or variable1 == 'PW08' or variable1 == 'PW09' or variable1 == 'PW10'\
            or variable1 == 'PW11' or variable1 == 'PW12' or variable1 == 'PW13' or variable1 == 'PW14'\
            or variable1 == 'PW15' or variable1 == 'PW16' or variable1 == 'PW17' or variable1 == 'PW18'\
            or variable1 == 'PW19' or variable1 == 'XDST' or variable1 == 'XNST' or variable1 == 'XTMX'\
            or variable1 == 'XTFR'\
            or variable2 == 'LAT' or variable2 == 'LON' or variable2 == 'CSST' or variable2 == 'OAGE'\
            or variable2 == 'NAGE' or variable2 == 'RSST' or variable2 == 'DSST' or variable2 == 'DSTA'\
            or variable2 == 'U200' or variable2 == 'U20C' or variable2 == 'V20C' or variable2 == 'V000'\
            or variable2 == 'EPOS' or variable2 == 'ENEG' or variable2 == 'EPSS' or variable2 == 'ENSS'\
            or variable2 == 'T000' or variable2 == 'TLAT' or variable2 == 'TLON' or variable2 == 'TWAC'\
            or variable2 == 'TWXC' or variable2 == 'G150' or variable2 == 'G200' or variable2 == 'G250'\
            or variable2 == 'V000' or variable2 == 'V850' or variable2 == 'V500' or variable2 == 'V300'\
            or variable2 == 'SHDC' or variable2 == 'SHGC' or variable2 == 'T150' or variable2 == 'T200'\
            or variable2 == 'T250' or variable2 == 'SHRD' or variable2 == 'SHRS' or variable2 == 'SHRG'\
            or variable2 == 'HE07' or variable2 == 'HE05' or variable2 == 'PW01' or variable2 == 'PW02'\
            or variable2 == 'PW03' or variable2 == 'PW04' or variable2 == 'PW05' or variable2 == 'PW06'\
            or variable2 == 'PW07' or variable2 == 'PW08' or variable2 == 'PW09' or variable2 == 'PW10'\
            or variable2 == 'PW11' or variable2 == 'PW12' or variable2 == 'PW13' or variable2 == 'PW14'\
            or variable2 == 'PW15' or variable2 == 'PW16' or variable2 == 'PW17' or variable2 == 'PW18'\
            or variable2 == 'PW19' or variable2 == 'XDST' or variable2 == 'XNST' or variable2 == 'XTMX'\
            or variable2 == 'XTFR':
                SHIPS_Variable_Array.append((float(row[0])/10))
            elif variable1 == 'ATCF' or variable1 == 'DATE' or variable2 == 'ATCF' or variable2 == 'DATE':
                SHIPS_Variable_Array.append(row[0])
            else:
                SHIPS_Variable_Array.append(int(row[0]))
    return SHIPS_Variable_Array



'''



#MPI (Emmanuel) array for all basins
SHIPS_AllBasins_MPIE_HR000 = []

for i in range(len(SHIPS_AL_array)):
    row = SHIPS_AL_array[i]
    if row[21] == 'VMPI':
        SHIPS_AllBasins_MPIE_HR000.append(int(row[0]))

for i in range(len(SHIPS_EP_array)):
    row = SHIPS_EP_array[i]
    if row[21] == 'VMPI':
        SHIPS_AllBasins_MPIE_HR000.append(int(row[0]))
        
for i in range(len(SHIPS_CP_array)):
    row = SHIPS_CP_array[i]
    if row[21] == 'VMPI':
        SHIPS_AllBasins_MPIE_HR000.append(int(row[0]))

for i in range(len(SHIPS_WP_array)):
    row = SHIPS_WP_array[i]
    if row[21] == 'VMPI':
        SHIPS_AllBasins_MPIE_HR000.append(int(row[0]))

for i in range(len(SHIPS_IO_array)):
    row = SHIPS_IO_array[i]
    if row[21] == 'VMPI':
        SHIPS_AllBasins_MPIE_HR000.append(int(row[0]))

for i in range(len(SHIPS_SH_array)):
    row = SHIPS_SH_array[i]
    if row[21] == 'VMPI':
        SHIPS_AllBasins_MPIE_HR000.append(int(row[0]))



#Create an array of intensities as a fraction of MPI (Emmanuel)

SHIPS_AllBasins_FracMPIE_HR000 = []
for i in range(len(SHIPS_AllBasins_Vmax_HR000)):
    #if SHIPS_AllBasins_Lon_HR000[i] >= 135:
        if SHIPS_AllBasins_MPIE_HR000[i] == 0:
            SHIPS_AllBasins_FracMPIE_HR000.append(float(1))
        else:
            SHIPS_AllBasins_FracMPIE_HR000.append(float(SHIPS_AllBasins_Vmax_HR000[i]/SHIPS_AllBasins_MPIE_HR000[i]))
     
#Create an array of MPIR (Xu and Wang) (Atlantic curve)
SHIPS_AllBasins_MPIR_XWT16AL_HR000 = []
for i in range(len(SHIPS_AllBasins_Vmax_HR000)):
        SHIPS_AllBasins_MPIR_XWT16AL_HR000.append(float(27.58 + (74.03 * math.exp(0.1903 * (SHIPS_AllBasins_SST_HR000[i] - 30)))))

# create 24 hr intensification rate array

SHIPS_AllBasins_24hIR_HR000 = []
for i in range(len(SHIPS_AllBasins_Vmax_HR000)):
    #if SHIPS_AllBasins_Lon_HR000[i] <= 135:
        if (i == 0 or i == 1):
            SHIPS_AllBasins_24hIR_HR000.append(np.nan)
        elif (i == len(SHIPS_AllBasins_Vmax_HR000)-2 or i == len(SHIPS_AllBasins_Vmax_HR000)-1):
            SHIPS_AllBasins_24hIR_HR000.append(np.nan)
        elif (SHIPS_AllBasins_ATCF_HR000[i-2] != SHIPS_AllBasins_ATCF_HR000[i] or SHIPS_AllBasins_ATCF_HR000[i-1] != SHIPS_AllBasins_ATCF_HR000[i]\
              or SHIPS_AllBasins_ATCF_HR000[i+1] != SHIPS_AllBasins_ATCF_HR000[i] or SHIPS_AllBasins_ATCF_HR000[i+2] != SHIPS_AllBasins_ATCF_HR000[i]):
                SHIPS_AllBasins_24hIR_HR000.append(np.nan)
        else:
            SHIPS_AllBasins_24hIR_HR000.append(float(SHIPS_AllBasins_Vmax_HR000[i+2]) - float(SHIPS_AllBasins_Vmax_HR000[i-2]))
            
SHIPS_AllBasins_12hIR_HR000 = []
for i in range(len(SHIPS_AllBasins_Vmax_HR000)):
   # if SHIPS_AllBasins_Lon_HR000[i] <= 135:
        if (i == 0):
            SHIPS_AllBasins_12hIR_HR000.append(np.nan)
        elif (i == len(SHIPS_AllBasins_Vmax_HR000)-1):
            SHIPS_AllBasins_12hIR_HR000.append(np.nan)
        elif (SHIPS_AllBasins_ATCF_HR000[i-1] != SHIPS_AllBasins_ATCF_HR000[i]\
              or SHIPS_AllBasins_ATCF_HR000[i+1] != SHIPS_AllBasins_ATCF_HR000[i]):
                SHIPS_AllBasins_12hIR_HR000.append(np.nan)
        else:
            SHIPS_AllBasins_12hIR_HR000.append(float(SHIPS_AllBasins_Vmax_HR000[i+1]) - float(SHIPS_AllBasins_Vmax_HR000[i-1]))

SHIPS_AllBasins_6hIR_HR000 = []
SHIPS_AllBasins_6hInterpVMax_HR000 = []
SHIPS_AllBasins_6hInterpFMPI_HR000 = []


for i in range(len(SHIPS_AllBasins_Vmax_HR000)):
    #if SHIPS_AllBasins_Lon_HR000[i] <= 135:
        if (i == len(SHIPS_AllBasins_Vmax_HR000)-1):
            SHIPS_AllBasins_6hIR_HR000.append(np.nan)
        elif (SHIPS_AllBasins_ATCF_HR000[i+1] != SHIPS_AllBasins_ATCF_HR000[i]):
            SHIPS_AllBasins_6hIR_HR000.append(np.nan)
            SHIPS_AllBasins_6hInterpVMax_HR000.append(np.nan)
            SHIPS_AllBasins_6hInterpFMPI_HR000.append(np.nan)
        else:
            SHIPS_AllBasins_6hIR_HR000.append(float(SHIPS_AllBasins_Vmax_HR000[i+1]) - float(SHIPS_AllBasins_Vmax_HR000[i]))
            SHIPS_AllBasins_6hInterpVMax_HR000.append((float(SHIPS_AllBasins_Vmax_HR000[i+1]) + float(SHIPS_AllBasins_Vmax_HR000[i]))/2)
            SHIPS_AllBasins_6hInterpFMPI_HR000.append((float(SHIPS_AllBasins_FracMPIE_HR000[i+1]) + float(SHIPS_AllBasins_FracMPIE_HR000[i]))/2)


#Create array of all unique ATCF IDs
SHIPS_AllBasins_UniqueATCFIDs = []
for i in range(len(SHIPS_AllBasins_ATCF_HR000)):
    if SHIPS_AllBasins_ATCF_HR000[i] not in SHIPS_AllBasins_UniqueATCFIDs:
        SHIPS_AllBasins_UniqueATCFIDs.append(SHIPS_AllBasins_ATCF_HR000[i])





# Create plot for shear vs intensification rate
#windspeedTicks = np.arange(0, 200, 20)

fig = plt.figure(figsize=(12, 8))
plt.scatter(SHIPS_AllBasins_Shear_HR000, SHIPS_AllBasins_24hIR_HR000, marker = 'o', color = 'blue')
#plt.xticks(windspeedTicks)
plt.xlabel('Wind Shear (knots)')
plt.ylabel('Centered 24-hr intensification rate (kt/day)')
plt.title('Vertical Wind Shear vs Centered 24-hr TC Intensification Rate')
plt.show()



#Setting up for all of our other plotting needs
#Remove NaN values for both arrays
NaNRemoved_SHIPS_AllBasins_24hIR_HR000 = []
NaNRemoved_SHIPS_AllBasins_12hIR_HR000 = []
NaNRemoved_SHIPS_AllBasins_6hIR_HR000 = []
NaNRemoved_SHIPS_AllBasins_Shear_HR000 = []
NaNRemoved_SHIPS_AllBasins_SST_HR000 = []
NaNRemoved_SHIPS_AllBasins_ATCF_HR000 = []
NaNRemoved_SHIPS_AllBasins_MPIE_HR000 = []
NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000 = []
NaNRemoved_SHIPS_AllBasins_MPIR_XWT16AL_HR000 = []


nan_indices_IR = np.isnan(SHIPS_AllBasins_24hIR_HR000)

for i in range(len(SHIPS_AllBasins_24hIR_HR000)):
    if nan_indices_IR[i] == False:
        if (SHIPS_AllBasins_Lat_HR000[i] < 35 and SHIPS_AllBasins_Lat_HR000[i] > -35 and SHIPS_AllBasins_6hIR_HR000[i] > 0 and SHIPS_AllBasins_Vmax_HR000[i] > 30 and SHIPS_AllBasins_SST_HR000[i] > 25):
            NaNRemoved_SHIPS_AllBasins_24hIR_HR000.append(SHIPS_AllBasins_24hIR_HR000[i])
            NaNRemoved_SHIPS_AllBasins_12hIR_HR000.append(SHIPS_AllBasins_12hIR_HR000[i])
            NaNRemoved_SHIPS_AllBasins_6hIR_HR000.append(SHIPS_AllBasins_6hIR_HR000[i])
            NaNRemoved_SHIPS_AllBasins_Shear_HR000.append(SHIPS_AllBasins_Shear_HR000[i])
            NaNRemoved_SHIPS_AllBasins_SST_HR000.append(SHIPS_AllBasins_SST_HR000[i])
            NaNRemoved_SHIPS_AllBasins_ATCF_HR000.append(SHIPS_AllBasins_ATCF_HR000[i])
            NaNRemoved_SHIPS_AllBasins_MPIE_HR000.append(SHIPS_AllBasins_MPIE_HR000[i])
            NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000.append(SHIPS_AllBasins_6hInterpFMPI_HR000[i])
            NaNRemoved_SHIPS_AllBasins_MPIR_XWT16AL_HR000.append(SHIPS_AllBasins_MPIR_XWT16AL_HR000[i])





#Create bins of fractional MPI
FracMPIBin2030 = []
IRBin2030 = []

FracMPIBin3040 = []
IRBin3040 = []

FracMPIBin4050 = []
IRBin4050 = []

FracMPIBin5060 = []
IRBin5060 = []

FracMPIBin6070 = []
IRBin6070 = []

FracMPIBin7080 = []
IRBin7080 = []

FracMPIBin8090 = []
IRBin8090 = []

FracMPIBin90100 = []
IRBin90100 = []

for i in range(len(NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000)):
    if NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i] > 0.2 and NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i] <= 0.3 and NaNRemoved_SHIPS_AllBasins_6hIR_HR000[i] > 0:
        FracMPIBin2030.append(NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i])
        IRBin2030.append(NaNRemoved_SHIPS_AllBasins_6hIR_HR000[i])
    if NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i] > 0.3 and NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i] <= 0.4 and NaNRemoved_SHIPS_AllBasins_6hIR_HR000[i] > 0:
        FracMPIBin3040.append(NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i])
        IRBin3040.append(NaNRemoved_SHIPS_AllBasins_6hIR_HR000[i])
    if NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i] > 0.4 and NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i] <= 0.5 and NaNRemoved_SHIPS_AllBasins_6hIR_HR000[i] > 0:
        FracMPIBin4050.append(NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i])
        IRBin4050.append(NaNRemoved_SHIPS_AllBasins_6hIR_HR000[i])
    if NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i] > 0.5 and NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i] <= 0.6 and NaNRemoved_SHIPS_AllBasins_6hIR_HR000[i] > 0:
        FracMPIBin5060.append(NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i])
        IRBin5060.append(NaNRemoved_SHIPS_AllBasins_6hIR_HR000[i])
    if NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i] > 0.6 and NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i] <= 0.7 and NaNRemoved_SHIPS_AllBasins_6hIR_HR000[i] > 0:
        FracMPIBin6070.append(NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i])
        IRBin6070.append(NaNRemoved_SHIPS_AllBasins_6hIR_HR000[i])
    if NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i] > 0.7 and NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i] <= 0.8 and NaNRemoved_SHIPS_AllBasins_6hIR_HR000[i] > 0:
        FracMPIBin7080.append(NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i])
        IRBin7080.append(NaNRemoved_SHIPS_AllBasins_6hIR_HR000[i])
    if NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i] > 0.8 and NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i] <= 0.9 and NaNRemoved_SHIPS_AllBasins_6hIR_HR000[i] > 0:
        FracMPIBin8090.append(NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i])
        IRBin8090.append(NaNRemoved_SHIPS_AllBasins_6hIR_HR000[i])
    if NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i] > 0.9 and NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i] <= 1.0 and NaNRemoved_SHIPS_AllBasins_6hIR_HR000[i] > 0:
        FracMPIBin90100.append(NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[i])
        IRBin90100.append(NaNRemoved_SHIPS_AllBasins_6hIR_HR000[i])

IRBin2030.sort()
IRBin3040.sort()
IRBin4050.sort()
IRBin5060.sort()
IRBin6070.sort()
IRBin7080.sort()
IRBin8090.sort()
IRBin90100.sort()

#Create percentile values
IRBinPct80 = []

IRBinPct80.append(IRBin2030[int(len(IRBin2030)*0.80)-1])
IRBinPct80.append(IRBin3040[int(len(IRBin3040)*0.80)-1])
IRBinPct80.append(IRBin4050[int(len(IRBin4050)*0.80)-1])
IRBinPct80.append(IRBin5060[int(len(IRBin5060)*0.80)-1])
IRBinPct80.append(IRBin6070[int(len(IRBin6070)*0.80)-1])
IRBinPct80.append(IRBin7080[int(len(IRBin7080)*0.80)-1])
IRBinPct80.append(IRBin8090[int(len(IRBin8090)*0.80)-1])
IRBinPct80.append(IRBin90100[int(len(IRBin90100)*0.80)-1])

IRBinPct95 = []

IRBinPct95.append(IRBin2030[int(len(IRBin2030)*0.95)-1])
IRBinPct95.append(IRBin3040[int(len(IRBin3040)*0.95)-1])
IRBinPct95.append(IRBin4050[int(len(IRBin4050)*0.95)-1])
IRBinPct95.append(IRBin5060[int(len(IRBin5060)*0.95)-1])
IRBinPct95.append(IRBin6070[int(len(IRBin6070)*0.95)-1])
IRBinPct95.append(IRBin7080[int(len(IRBin7080)*0.95)-1])
IRBinPct95.append(IRBin8090[int(len(IRBin8090)*0.95)-1])
IRBinPct95.append(IRBin90100[int(len(IRBin90100)*0.95)-1])

IRBinPct99 = []

IRBinPct99.append(IRBin2030[int(len(IRBin2030)*0.99)-1])
IRBinPct99.append(IRBin3040[int(len(IRBin3040)*0.99)-1])
IRBinPct99.append(IRBin4050[int(len(IRBin4050)*0.99)-1])
IRBinPct99.append(IRBin5060[int(len(IRBin5060)*0.99)-1])
IRBinPct99.append(IRBin6070[int(len(IRBin6070)*0.99)-1])
IRBinPct99.append(IRBin7080[int(len(IRBin7080)*0.99)-1])
IRBinPct99.append(IRBin8090[int(len(IRBin8090)*0.99)-1])
IRBinPct99.append(IRBin90100[int(len(IRBin90100)*0.99)-1])

FracMPIBinVals =  np.arange(0.25, 1.05, 0.1)



#Create arrays of max intensification rate for each storm
SHIPS_AllBasins_MaxIR = []
SHIPS_AllBasins_ShearAtMaxIR = []
SHIPS_AllBasins_MPIEAtMaxIR = []
SHIPS_AllBasins_FracMPIEAtMaxIR = []
for i in range(len(SHIPS_AllBasins_UniqueATCFIDs)):
    thisATCFID = SHIPS_AllBasins_UniqueATCFIDs[i]
    selectedStormIRs = []
    selectedStormShears = []
    selectedStormMPIE = []
    selectedStormFracMPIE = []

    for j in range(len(NaNRemoved_SHIPS_AllBasins_ATCF_HR000)):
        if NaNRemoved_SHIPS_AllBasins_ATCF_HR000[j] == thisATCFID:
            selectedStormIRs.append(NaNRemoved_SHIPS_AllBasins_24hIR_HR000[j])
            selectedStormShears.append(NaNRemoved_SHIPS_AllBasins_Shear_HR000[j])
            selectedStormMPIE.append(NaNRemoved_SHIPS_AllBasins_MPIE_HR000[j])
            selectedStormFracMPIE.append(NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000[j])


    if len(selectedStormIRs) > 0:
        SHIPS_AllBasins_MaxIR.append(max(selectedStormIRs))
        SHIPS_AllBasins_ShearAtMaxIR.append(selectedStormShears[np.argmax(selectedStormIRs)])
        SHIPS_AllBasins_MPIEAtMaxIR.append(selectedStormMPIE[np.argmax(selectedStormIRs)])
        SHIPS_AllBasins_FracMPIEAtMaxIR.append(selectedStormFracMPIE[np.argmax(selectedStormIRs)])


SHIPS_AllBasins_Predictors_HR000 = np.zeros((len(NaNRemoved_SHIPS_AllBasins_Shear_HR000),1))
for i in range(len(NaNRemoved_SHIPS_AllBasins_Shear_HR000)):
    SHIPS_AllBasins_Predictors_HR000[i,0] = NaNRemoved_SHIPS_AllBasins_Shear_HR000[i]
regrAllBasinsShearIR = linear_model.LinearRegression()
regrAllBasinsShearIR.fit(SHIPS_AllBasins_Predictors_HR000,NaNRemoved_SHIPS_AllBasins_24hIR_HR000)
# Make predictions using the testing set
predictedIRforShearAllBasins = regrAllBasinsShearIR.predict(SHIPS_AllBasins_Predictors_HR000)

# The coefficients
print("Coefficient: \n", regrAllBasinsShearIR.coef_)
print("Intercept: \n", regrAllBasinsShearIR.intercept_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(NaNRemoved_SHIPS_AllBasins_24hIR_HR000, predictedIRforShearAllBasins))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(NaNRemoved_SHIPS_AllBasins_24hIR_HR000, predictedIRforShearAllBasins))

# Plot outputs
plt.scatter(NaNRemoved_SHIPS_AllBasins_Shear_HR000, NaNRemoved_SHIPS_AllBasins_24hIR_HR000, color="black", s = 0.1)
plt.plot(NaNRemoved_SHIPS_AllBasins_Shear_HR000, predictedIRforShearAllBasins, color="blue", linewidth=3)

#plt.xticks(windspeedTicks)
plt.xlabel('Wind Shear (knots)')
plt.ylabel('Centered 24-hr intensification rate (kt/day)')
plt.text(20,80,'Regression formula: y = -0.43x + 9.41')
plt.title('Vertical Wind Shear vs Centered 24-hr TC Intensification Rate')

plt.show()


SHIPS_AllBasins_Predictors_ShearVsMaxIR = np.zeros((len(SHIPS_AllBasins_ShearAtMaxIR),1))
for i in range(len(SHIPS_AllBasins_ShearAtMaxIR)):
    SHIPS_AllBasins_Predictors_ShearVsMaxIR[i,0] = SHIPS_AllBasins_ShearAtMaxIR[i]
regrAllBasinsShearMaxIR = linear_model.LinearRegression()
regrAllBasinsShearMaxIR.fit(SHIPS_AllBasins_Predictors_ShearVsMaxIR,SHIPS_AllBasins_MaxIR)
# Make predictions using the testing set
predictedMaxIRforShearAllBasins = regrAllBasinsShearMaxIR.predict(SHIPS_AllBasins_Predictors_ShearVsMaxIR)

# The coefficients
print("Coefficient: \n", regrAllBasinsShearMaxIR.coef_)
print("Intercept: \n", regrAllBasinsShearMaxIR.intercept_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(SHIPS_AllBasins_MaxIR, predictedMaxIRforShearAllBasins))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(SHIPS_AllBasins_MaxIR, predictedMaxIRforShearAllBasins))

# Plot outputs
plt.scatter(SHIPS_AllBasins_ShearAtMaxIR, SHIPS_AllBasins_MaxIR, color="black", s = 0.2)
plt.plot(SHIPS_AllBasins_ShearAtMaxIR, predictedMaxIRforShearAllBasins, color="blue", linewidth=3)

#plt.xticks(windspeedTicks)
plt.xlabel('Wind Shear (knots)')
plt.ylabel('Centered 24-hr intensification rate (kt/day)')
plt.text(20,80,'Regression formula: y = -0.43x + 9.41')
plt.title('Vertical Wind Shear vs Lifetime Maximum Centered 24-hr TC Intensification Rate')

plt.show()

#Let's make a histogram of fractional MPI at the maximum intensification rate
FractionBins20 = np.arange(0, 1, 0.05)
fig, ax = plt.subplots()
ax.hist(SHIPS_AllBasins_FracMPIE_HR000, bins=FractionBins20)
#ax.plot(xdata, 0*xdata, 'd')
ax.set_ylabel('Cases')
ax.set_xlabel('Vmax/MPI at maximum intensification rate')
plt.title('Distrubution of Fractional MPI at maximum intensification rate')
plt.show



#Scatterplot for fractional MPI vs MPIR
fig, ax = plt.subplots(figsize=(8, 6))

plt.scatter(NaNRemoved_SHIPS_AllBasins_FracMPIE_HR000, NaNRemoved_SHIPS_AllBasins_6hIR_HR000, color="gray", s = 4)
plt.plot(FracMPIBinVals, IRBinPct80, color="blue", linewidth=2)
plt.plot(FracMPIBinVals, IRBinPct95, color="green", linewidth=2)
plt.plot(FracMPIBinVals, IRBinPct99, color="red", linewidth=2)
ax.legend(['Individual intensification case','80th percentile IR','95th percentile IR','99th percentile IR'])
plt.xlim(0.2,1)
plt.xlabel('Fractional MPI (Emmanuel)')
plt.ylabel('24 hour IR')
plt.title('Fractional MPI vs 6-hour IR \n for all global TC intensification cases')

plt.show()

'''

