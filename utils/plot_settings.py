import numpy as np

def set_limit(axismin, axismax, data,vars):
    """
    Determines the axis limits for a plot based on input values or data series.

    Parameters:
    - axismin: float or 'auto'
        Minimum value for the axis. If 'auto', it is calculated based on the series.
    - axismax: float or 'auto'
        Maximum value for the axis. If 'auto', it is calculated based on the series.
    - series: pandas.Series or array-like
        The data series from which the limits are calculated if 'auto' is specified.

    Returns:
    - tuple: (axismin, axismax)
        The calculated or provided axis limits.
    """

    axismin_val = 10**6
    axismax_val = -10**6
    for var in vars:
        # Calculate minimum limit if 'auto' is specified
        series = data[var]
        if axismin == 'auto':
            max_value = series.max()
            min_value = series.min()
            axismin_i = min_value - (max_value - min_value) * 0.1
        else:
            axismin_i = axismin

        # Calculate maximum limit if 'auto' is specified
        if axismax == 'auto':
            max_value = series.max()
            min_value = series.min()
            axismax_i = max_value + (max_value - min_value) * 0.1
        else:
            axismax_i = axismax

        axismin_val = min(axismin_val,axismin_i)
        axismax_val = max(axismax_val,axismax_i)
    # Return the determined axis limits
    return axismin_val, axismax_val

def calculate_M(params):
    return 2*np.sin(np.radians(params['phicv'].values[0]))

def calculate_Mb(pbs, params,data,nidx):
    Mb = []
    for pb in pbs:
        pcs = data['pcs'].values[nidx-1]
        if pb>=pcs:
            xigamma = -np.log(data['pcs'].values[nidx-1])+np.log(pb)
            Mb.append(data['M'].values[nidx-1] * np.exp(-1*params['nbwet'].values[0]*xigamma))
        else:
            CMB = 1 / ((2*np.sin(np.radians(60))/data['M'].values[nidx-1])**(1/params['nbdry'].values[0])-1)
            Mb.append(data['M'].values[nidx-1]*((1+CMB)/(pb/data['pcs'].values[nidx-1]+CMB))**params['nbdry'].values[0])
    return Mb

def calculate_Md(pbs, params, data, nidx):
    Md = []
    for pb in pbs:
    
        xigamma = -np.log(data['pcs'].values[nidx-1])+np.log(pb)
        Md.append(data['M'].values[nidx-1] * np.exp(1*params['nd'].values[0]*xigamma))
    return Md

def calculate_phi(M):
    return np.degrees(np.arcsin(3*M/(6+M)))

def calculate_tanphi(M):
    return np.tan(np.arcsin(3*M/(6+M)))

