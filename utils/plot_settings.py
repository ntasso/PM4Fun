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
