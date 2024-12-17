from .plot_settings import *
import numpy as np

def plot_sxy_vs_gxy(ax, data, stop_idx, xmin='auto', xmax='auto', ymin='auto', ymax='auto'):
    """
    Plots shear stress (τ_xy) versus shear strain (γ_xy) on the provided Matplotlib Axes.

    Parameters:
    - ax: Matplotlib Axes
        The Axes object where the plot will be drawn.
    - data: pandas.DataFrame
        A DataFrame containing the data to be plotted. Must include the columns:
        'gamxy' (shear strain, γ_xy) and 'sxy' (shear stress, τ_xy).
    - stop_idx: int
        The index in the data where the plot should stop.
    - xmin: float or 'auto', optional
        Minimum x-axis limit. Default is 'auto', which calculates the limit from the data.
    - xmax: float or 'auto', optional
        Maximum x-axis limit. Default is 'auto', which calculates the limit from the data.
    - ymin: float or 'auto', optional
        Minimum y-axis limit. Default is 'auto', which calculates the limit from the data.
    - ymax: float or 'auto', optional
        Maximum y-axis limit. Default is 'auto', which calculates the limit from the data.

    Returns:
    - None
        The function modifies the provided Axes object in place.
    """

    # Set axis labels
    ax.set_xlabel('Shear strain, $\\gamma_{xy}$ [%]')
    ax.set_ylabel('Shear stress, $\\tau_{xy}$ [kPa]')

    # Add horizontal and vertical dotted lines at zero
    ax.axhline(0, color='k', linestyle='dotted')
    ax.axvline(0, color='k', linestyle='dotted')

    # Add grid lines with low opacity
    ax.grid(color='gray', alpha=0.2)

    # Calculate axis limits
    xmin, xmax = set_limit(xmin, xmax, data,['gamxy'])
    ymin, ymax = set_limit(ymin, ymax, data,['sxy'])

    # Apply calculated or provided limits to the plot
    ax.set_ylim(ymin, ymax)
    ax.set_xlim(xmin * 100, xmax * 100)  # Convert x-axis limits to percentage

    # Plot the data up to the stop index
    ax.plot(data['gamxy'].values[:stop_idx] * 100, data['sxy'].values[:stop_idx], color='k')

    # Highlight the final point with a scatter plot
    ax.scatter(data['gamxy'].values[stop_idx - 1] * 100, data['sxy'].values[stop_idx - 1], color='k')

def plot_sxy_vs_sy(ax, data, stop_idx, xmin='auto', xmax='auto', ymin='auto', ymax='auto'):
    """
    Plots shear stress (τ_xy) versus vertical effective stress (σ'_y) on the provided Matplotlib Axes.

    Parameters:
    - ax: Matplotlib Axes
        The Axes object where the plot will be drawn.
    - data: pandas.DataFrame
        A DataFrame containing the data to be plotted. Must include the following columns:
        'sy' (vertical effective stress, σ'_y) and 'sxy' (shear stress, τ_xy).
    - stop_idx: int
        The index in the data up to which the plot should be drawn.
    - xmin: float or 'auto', optional
        Minimum x-axis limit. If 'auto', it is calculated based on the data in the 'sy' column.
    - xmax: float or 'auto', optional
        Maximum x-axis limit. If 'auto', it is calculated based on the data in the 'sy' column.
    - ymin: float or 'auto', optional
        Minimum y-axis limit. If 'auto', it is calculated based on the data in the 'sxy' column.
    - ymax: float or 'auto', optional
        Maximum y-axis limit. If 'auto', it is calculated based on the data in the 'sxy' column.

    Returns:
    - None
        The function modifies the provided Axes object in place.
    """

    # Set axis labels
    ax.set_xlabel('Vertical effective stress, $\\sigma\'_{y}$ [kPa]')
    ax.set_ylabel('Shear stress, $\\tau_{xy}$ [kPa]')

    # Add a horizontal line at τ_xy = 0 for reference
    ax.axhline(0, color='k', linestyle='dotted')

    # Add grid lines for better visualization
    ax.grid(color='gray', alpha=0.2)

    # Calculate axis limits using the helper function set_limit
    xmin, xmax = set_limit(xmin, xmax, data,['sy'])
    ymin, ymax = set_limit(ymin, ymax, data,['sxy'])

    # Apply axis limits
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    # Plot the data from the start to the stop index
    ax.plot(data['sy'].values[:stop_idx], data['sxy'].values[:stop_idx], color='k')

    # Highlight the last point in the plot
    ax.scatter(data['sy'].values[stop_idx - 1], data['sxy'].values[stop_idx - 1], color='k')


def plot_alpha_vs_N(ax, data, stop_idx, xmin='auto', xmax='auto', ymin='auto', ymax='auto'):
    """
    Plots back stress ratio (\u03b1) versus the number of uniform cycles (N) on the provided Matplotlib Axes.

    Parameters:
    - ax: Matplotlib Axes
        The Axes object where the plot will be drawn.
    - data: pandas.DataFrame
        A DataFrame containing the data to be plotted. Must include the following columns:
        'N', 'alphaxx', 'alphayy', and 'alphaxy'.
    - stop_idx: int
        The index in the data up to which the plot should be drawn.
    - xmin: float or 'auto', optional
        Minimum x-axis limit. If 'auto', it is calculated based on the data in the 'N' column.
    - xmax: float or 'auto', optional
        Maximum x-axis limit. If 'auto', it is calculated based on the data in the 'N' column.
    - ymin: float or 'auto', optional
        Minimum y-axis limit. If 'auto', it is calculated based on the data in the columns 'alphaxx', 'alphayy', and 'alphaxy'.
    - ymax: float or 'auto', optional
        Maximum y-axis limit. If 'auto', it is calculated based on the data in the columns 'alphaxx', 'alphayy', and 'alphaxy'.

    Returns:
    - None
        The function modifies the provided Axes object in place.
    """

    # Set axis labels
    ax.set_xlabel('Number of uniform cycles, $N$ [-]')  # Label for the x-axis
    ax.set_ylabel('Back stress ratio, $\\alpha_{ii}$ [-]')  # Label for the y-axis

    # Add a horizontal reference line at \u03c4_xy = 0
    ax.axhline(0, color='k', linestyle='dotted')

    # Add grid lines for better visualization
    ax.grid(color='gray', alpha=0.2)

    # Helper function to calculate axis limits
    xmin, xmax = set_limit(xmin, xmax, data, ['N'])  # Set x-axis limits based on the 'N' column
    ymin, ymax = set_limit(ymin, ymax, data, ['alphaxx', 'alphaxy', 'alphayy'])  # Set y-axis limits based on the back stress ratio columns

    # Apply the calculated axis limits
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    # Define colors and labels for the variables
    colors = {
        'alphaxx': 'b',           # Blue for \u03b1_xx
        'alphayy': 'r',           # Red for \u03b1_yy
        'alphaxy': 'forestgreen'  # Green for \u03b1_xy
    }
    sims = {
        'alphaxx': '$\\alpha_{xx}$',
        'alphayy': '$\\alpha_{yy}$',
        'alphaxy': '$\\alpha_{xy}$'
    }

    # Loop through each variable to plot
    for var in colors.keys():
        # Plot the data up to the specified stop index
        ax.plot(
            data['N'].values[:stop_idx],  # X-axis: Number of uniform cycles
            data[var].values[:stop_idx],  # Y-axis: Back stress ratio
            color=colors[var]             # Line color
        )

        # Highlight the last point plotted
        ax.scatter(
            data['N'].values[stop_idx - 1],  # X-coordinate of the last point
            data[var].values[stop_idx - 1],  # Y-coordinate of the last point
            color=colors[var]                # Marker color
        )

        # Add a legend entry for the variable
        ax.plot([], [], color=colors[var], label=sims[var], marker='o')

    # Add the legend to the plot
    ax.legend(loc='upper left', ncol=3)

    


def plot_q_vs_p(ax, data, params, stop_idx, xmin='auto', xmax='auto', ymin='auto', ymax='auto'):
    """
    Plots back stress ratio (\u03b1) versus the number of uniform cycles (N) on the provided Matplotlib Axes.

    Parameters:
    - ax: Matplotlib Axes
        The Axes object where the plot will be drawn.
    - data: pandas.DataFrame
        A DataFrame containing the data to be plotted. Must include the following columns:
        'N', 'alphaxx', 'alphayy', and 'alphaxy'.
    - stop_idx: int
        The index in the data up to which the plot should be drawn.
    - xmin: float or 'auto', optional
        Minimum x-axis limit. If 'auto', it is calculated based on the data in the 'N' column.
    - xmax: float or 'auto', optional
        Maximum x-axis limit. If 'auto', it is calculated based on the data in the 'N' column.
    - ymin: float or 'auto', optional
        Minimum y-axis limit. If 'auto', it is calculated based on the data in the columns 'alphaxx', 'alphayy', and 'alphaxy'.
    - ymax: float or 'auto', optional
        Maximum y-axis limit. If 'auto', it is calculated based on the data in the columns 'alphaxx', 'alphayy', and 'alphaxy'.

    Returns:
    - None
        The function modifies the provided Axes object in place.
    """

    # Set axis labels
    ax.set_xlabel('Mid stress, $p^{*} = \dfrac{\sigma_{x}+\sigma_{y}}{2}$ [kPa]')
    ax.set_ylabel('Deviatoric stress, $q^{*} = \\sqrt{2} \\cdot |\\sigma-pI|$ [kPa]')
    

    # Add grid lines for better visualization
    ax.grid(color='gray', alpha=0.2)

    # Helper function to calculate axis limits
    xmin, xmax = set_limit(xmin, xmax, data, ['p_ast'])  # Set x-axis limits based on the 'N' column
    ymin, ymax = set_limit(ymin, ymax, data, ['q_ast'])  # Set y-axis limits based on the back stress ratio columns

    xmin = 0
    ymin = 0

    # Apply the calculated axis limits
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)


    pbs = np.linspace(0,xmax,10000)

    M = calculate_M(params)
    ax.plot([0,xmax],[0,xmax*M],color='r',label='$M$')

    Mb = calculate_Mb(pbs,params,data,stop_idx)
    ax.plot(pbs,pbs*Mb,color='b',label='$M_{b}$')

    Md = calculate_Md(pbs,params,data,stop_idx)
    ax.plot(pbs,pbs*Md,color='forestgreen',label='$M_{d}$')


    # TO IMPROVE
    m = 0.01
    ax.plot([0,10000],[0,10000*data['q_ast'].values[stop_idx-1]/data['p_ast'].values[stop_idx-1]],color='gray')
    ax.plot([0,10000],[0,10000*(data['q_ast'].values[stop_idx-1]/data['p_ast'].values[stop_idx-1]-2*m)],color='gray',
             label='Yield surface')
    


    ax.plot(data['p_ast'].values[:stop_idx],data['q_ast'].values[:stop_idx],color='k')
    ax.scatter(data['p_ast'].values[stop_idx-1],data['q_ast'].values[stop_idx-1],color='k')

    ax.legend(loc='upper left')



def plot_e_vs_logp(ax, data, params, stop_idx, xmin='auto', xmax='auto', ymin='auto', ymax='auto',log_scale=True):
    """
    Plots back stress ratio (\u03b1) versus the number of uniform cycles (N) on the provided Matplotlib Axes.

    Parameters:
    - ax: Matplotlib Axes
        The Axes object where the plot will be drawn.
    - data: pandas.DataFrame
        A DataFrame containing the data to be plotted. Must include the following columns:
        'N', 'alphaxx', 'alphayy', and 'alphaxy'.
    - stop_idx: int
        The index in the data up to which the plot should be drawn.
    - xmin: float or 'auto', optional
        Minimum x-axis limit. If 'auto', it is calculated based on the data in the 'N' column.
    - xmax: float or 'auto', optional
        Maximum x-axis limit. If 'auto', it is calculated based on the data in the 'N' column.
    - ymin: float or 'auto', optional
        Minimum y-axis limit. If 'auto', it is calculated based on the data in the columns 'alphaxx', 'alphayy', and 'alphaxy'.
    - ymax: float or 'auto', optional
        Maximum y-axis limit. If 'auto', it is calculated based on the data in the columns 'alphaxx', 'alphayy', and 'alphaxy'.

    Returns:
    - None
        The function modifies the provided Axes object in place.
    """

    # Set axis labels
    ax.set_xlabel('Mid stress, $p^{*} = \dfrac{\sigma_{x}+\sigma_{y}}{2}$ [kPa]')
    ax.set_ylabel('Void ratio, e [-]')

    # Add grid lines for better visualization
    ax.grid(color='gray', alpha=0.2)

    # Helper function to calculate axis limits
    xmin, xmax = set_limit(xmin, xmax, data, ['p_ast'])  # Set x-axis limits based on the 'N' column
    ymin, ymax = set_limit(ymin, ymax, data, ['e'])  # Set y-axis limits based on the back stress ratio columns


    # Apply the calculated axis limits
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    if log_scale == True:
        ax.set_xscale('log')
    
    ax.plot([1,100000],[data['Gamma'].values[stop_idx-1],
                         data['Gamma'].values[-1]-params['lambda'].values[0]*np.log(100000)],
                         color='r',label='Critical state')
    

    ax.plot(data['p_ast'].values[:stop_idx],data['e'].values[:stop_idx],color='k')
    ax.scatter(data['p_ast'].values[stop_idx-1],data['e'].values[stop_idx-1],color='k')
    

    if data['xi'].values[stop_idx-1]>0:
        colorstate = 'limegreen'
    else:
        colorstate ='firebrick'

    p_ast_value = data['p_ast'].values[stop_idx-1]
    e_value = data['e'].values[stop_idx-1]
    ecs_value = data['e'].values[stop_idx-1]-data['xi'].values[stop_idx-1]
    ax.plot([p_ast_value,p_ast_value],[e_value,ecs_value],color=colorstate,zorder=1,
             label='$\\xi =$ '+str(np.round(data['xi'].values[stop_idx-1],decimals=2)))

    ax.legend(loc='lower left')

