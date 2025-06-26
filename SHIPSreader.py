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

#Function designed to retrieve variables that have different identifiers throughout the dataset. Example: NOHC and RHCN for oceanic heat content.
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


#Example usage:
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



'''

