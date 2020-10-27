# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 11:53:27 2020

@author: mahroua
@Description: Some useful pandas tools for ETL Processes

"""

import re, pandas as pd

def niceColumns (df,inplace=False):
    '''
    Prettify your columns. Usefull for SQL Operations
    
    Parameters
    ----------
    df : A Pandas DataFrame
    inplace : If True, will peform on the datafram in place. Default is False
    
    '''
    
    for x in df.columns:
        colName = re.sub('[^0-9a-zA-Z]+', '_', x)[:-1] \
            if '_' == re.sub('[^0-9a-zA-Z]+', '_', x)[-1] \
            else re.sub('[^0-9a-zA-Z]+', '_', x)
        df.rename(columns={x:colName},inplace=True)

def getCreateTable(df, tableName,niceColumns=True):
    '''
    Get SQL DDL that is the perfect fit for your dataframe

    Parameters
    ----------
    df : Pandas DataFrame
    tableName : Destination Table Name
    niceColumns : Boolean. Will prettify your column names to make them more SQL Friendly
        DESCRIPTION. The default is True.

    Returns
    -------
    String that you can use to create a destination table in SQL

    '''
    sqlDF = pd.DataFrame(columns=['col'])
    for x in df.columns:
        if niceColumns == True:
            colName = re.sub('[^0-9a-zA-Z]+', '_', x)[:-1] if '_' == re.sub('[^0-9a-zA-Z]+', '_', x)[-1]  else re.sub('[^0-9a-zA-Z]+', '_', x)
        if x in df.select_dtypes(include='object').columns:
            colLen = round(1.25 * (df[x].map(lambda x: len(str(x))).max()))
            sqlDF = sqlDF.append({'col': f'{colName} nvarchar({colLen})'},ignore_index=True)
        if x in df.select_dtypes(include='datetime').columns:
            sqlDF = sqlDF.append({'col': f'{colName} datetime'},ignore_index=True)
        if x in df.select_dtypes(include='float').columns:
            sqlDF = sqlDF.append({'col': f'{colName} float'},ignore_index=True)
    
    return (f'Create Table {tableName} (' + sqlDF.col.str.cat(sep=', ') + ' );')
            #