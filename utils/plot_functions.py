from .plot_settings import *
import numpy as np
import matplotlib.patches as patches

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

def plot_sxy_vs_sy(ax, data,params, stop_idx, xmin='auto', xmax='auto', ymin='auto', ymax='auto',
                   show_surfaces=True):
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

    if show_surfaces==True:

        deltaxy = data['sxy'].values[stop_idx-1]-data['sxy'].values[stop_idx-2]
        if deltaxy>=0:
            signo = 1
        else:
            signo = -1

        M = calculate_M(params)
        tanphi_M = calculate_tanphi(M)
        ax.plot([0,xmax],[0,xmax*tanphi_M*signo],color='r',label='$M$')
        pbs = [data['p_ast'].values[stop_idx-1]]

        Mb = calculate_Mb(pbs,params,data,stop_idx)
        tanphi_Mb = calculate_tanphi(Mb[0])
        ax.plot([0,xmax],[0,xmax*tanphi_Mb*signo],color='b',label='$M_{b}$')
        
        Md = calculate_Md(pbs,params,data,stop_idx)
        tanphi_Md = calculate_tanphi(Md[0])
        ax.plot([0,xmax],[0,xmax*tanphi_Md*signo],color='forestgreen',label='$M_{d}$')
        ax.legend(loc='lower left',ncol=3)
        

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

    


def plot_q_vs_p(ax, data, params, stop_idx, xmin='auto', xmax='auto', ymin='auto', ymax='auto',
                show_surfaces=True):
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
    ax.set_ylabel('Dev. stress, $q^{*} = \\sqrt{2} \\cdot |\\sigma-pI|$ [kPa]')
    

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


    if show_surfaces==True:
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
        ax.legend(loc='upper left')    


    ax.plot(data['p_ast'].values[:stop_idx],data['q_ast'].values[:stop_idx],color='k')
    ax.scatter(data['p_ast'].values[stop_idx-1],data['q_ast'].values[stop_idx-1],color='k')



def plot_e_vs_logp(ax, data, params, stop_idx, xmin='auto', xmax='auto', ymin='auto', ymax='auto', log_scale=True):
    """
    Plots the void ratio (e) versus the logarithm of mean effective stress (p*) on the provided Matplotlib Axes.

    Parameters:
    - ax: Matplotlib Axes
        The Axes object where the plot will be drawn.
    - data: pandas.DataFrame
        A DataFrame containing the data to be plotted. Must include the following columns:
        'p_ast' (mean effective stress), 'e' (void ratio), 'Gamma', and 'xi'.
    - params: dict
        A dictionary of parameters, including 'lambda', which represents the slope of the critical state line in log(p)-e space.
    - stop_idx: int
        The index in the data up to which the plot should be drawn.
    - xmin: float or 'auto', optional
        Minimum x-axis limit. If 'auto', it is calculated based on the data in the 'p_ast' column.
    - xmax: float or 'auto', optional
        Maximum x-axis limit. If 'auto', it is calculated based on the data in the 'p_ast' column.
    - ymin: float or 'auto', optional
        Minimum y-axis limit. If 'auto', it is calculated based on the data in the 'e' column.
    - ymax: float or 'auto', optional
        Maximum y-axis limit. If 'auto', it is calculated based on the data in the 'e' column.
    - log_scale: bool, optional
        Whether to use a logarithmic scale for the x-axis. Default is True.

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
    xmin, xmax = set_limit(xmin, xmax, data, ['p_ast'])  # Set x-axis limits based on the 'p_ast' column
    ymin, ymax = set_limit(ymin, ymax, data, ['e'])  # Set y-axis limits based on the 'e' column

    # Apply the calculated axis limits
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    if log_scale:
        ax.set_xscale('log')

    # Plot the critical state line
    ax.plot([1, 100000], [data['Gamma'].values[stop_idx-1],
                          data['Gamma'].values[-1] - params['lambda'].values[0] * np.log(100000)],
            color='r', label='Critical state')

    # Plot the data points and trajectory
    ax.plot(data['p_ast'].values[:stop_idx], data['e'].values[:stop_idx], color='k')
    ax.scatter(data['p_ast'].values[stop_idx-1], data['e'].values[stop_idx-1], color='k')

    # Determine the color for the state line based on 'xi'
    if data['xi'].values[stop_idx-1] > 0:
        colorstate = 'limegreen'
    else:
        colorstate = 'firebrick'

    # Plot the state line
    p_ast_value = data['p_ast'].values[stop_idx-1]
    e_value = data['e'].values[stop_idx-1]
    ecs_value = data['e'].values[stop_idx-1] - data['xi'].values[stop_idx-1]
    ax.plot([p_ast_value, p_ast_value], [e_value, ecs_value], color=colorstate, zorder=1,
            label='$\\xi =$ ' + str(np.round(data['xi'].values[stop_idx-1], decimals=2)))

    # Add legend
    ax.legend(loc='lower left')

def plot_ryy_vs_rxy(ax, data, params, stop_idx, xmin='auto', xmax='auto', ymin='auto', ymax='auto'):
    """
    Plots the stress ratio r_yy versus r_xy on the provided Matplotlib Axes.

    Parameters:
    - ax: Matplotlib Axes
        The Axes object where the plot will be drawn.
    - data: pandas.DataFrame
        A DataFrame containing the data to be plotted. Must include the following columns:
        'rxy', 'ryy', 'Mb', 'Md', 'alphaxy', 'alphayy'.
    - params: dict
        A dictionary of parameters, if needed for additional customization. Not directly used in this function.
    - stop_idx: int
        The index in the data up to which the plot should be drawn.
    - xmin: float or 'auto', optional
        Minimum x-axis limit. If 'auto', it is calculated based on the data in the 'rxy' column.
    - xmax: float or 'auto', optional
        Maximum x-axis limit. If 'auto', it is calculated based on the data in the 'rxy' column.
    - ymin: float or 'auto', optional
        Minimum y-axis limit. If 'auto', it is calculated based on the data in the 'ryy' column.
    - ymax: float or 'auto', optional
        Maximum y-axis limit. If 'auto', it is calculated based on the data in the 'ryy' column.

    Returns:
    - None
        The function modifies the provided Axes object in place.

    Description:
    This function visualizes the stress ratio r_yy versus r_xy as a 2D plot. It includes the following features:
    - Automatic scaling of the axes based on the provided data or manual limits.
    - Draws a trajectory of stress ratio values up to the given stop_idx.
    - Highlights the last point of the trajectory.
    - Plots circles representing specific critical stress ratios (e.g., Mb and Md).
    - Ensures equal scaling of axes for accurate stress ratio visualization.

    Additional Details:
    - The function uses helper functions `set_limit` and `circle`, which are assumed to calculate axis limits and generate circle coordinates respectively.
    - The axes are set to equal scaling to maintain the proportions of stress ratios.
    - The plot uses distinct colors (blue and forest green) to differentiate between circles associated with specific stress states.
    """

    # Set axis labels
    ax.set_xlabel('Stress ratio, $r_{xy}=\dfrac{\sigma_{xy}}{p^{*}}$')
    ax.set_ylabel('Stress ratio, $r_{yy}=\dfrac{\sigma_{yy}-p^{*}}{p^{*}}$')

    # Add grid lines for better visualization
    ax.grid(color='gray', alpha=0.2)

    # Helper function to calculate axis limits
    xmin, xmax = set_limit(xmin, xmax, data, ['rxy'], offset=0.2)  # Set x-axis limits based on the 'rxy' column
    ymin, ymax = set_limit(ymin, ymax, data, ['ryy'], offset=0.2)  # Set y-axis limits based on the 'ryy' column

    xmax = max(abs(xmin), xmax)
    ymax = max(abs(ymin), ymax)
    value_max = max(xmax, ymax)

    # Apply the calculated axis limits
    ax.set_xlim(-value_max, value_max)
    ax.set_ylim(-value_max, value_max)

    # Plot stress ratio trajectory
    ax.plot(data['rxy'].values[:stop_idx] * np.sqrt(2),
            data['ryy'].values[:stop_idx] * np.sqrt(2),
            color='k', zorder=2)

    # Highlight the last point in the trajectory
    ax.scatter(data['rxy'].values[stop_idx-1] * np.sqrt(2),
               data['ryy'].values[stop_idx-1] * np.sqrt(2),
               color='k', zorder=5)

    # Define a small margin for circle calculations
    m = 0.01

    # Plot the circle for Mb
    alphab = np.sqrt(1/2) * (data['Mb'].values[stop_idx-1] - m)
    xb, yb = circle(alphab, 0, 0)
    ax.plot(xb, yb, color='b')

    # Plot the circle for Md
    Md = data['Md'].values[stop_idx-1]
    alphad = np.sqrt(1/2) * (data['Md'].values[stop_idx-1] - m)
    xb, yb = circle(alphad, 0, 0)
    ax.plot(xb, yb, color='forestgreen')

    # Plot the final stress state circle
    xb, yb = circle(m, data['alphaxy'].values[stop_idx-1] / np.sqrt(1/2),
                    data['alphayy'].values[stop_idx-1] / np.sqrt(1/2))
    ax.plot(xb, yb, color='b')

    # Set axes to equal scaling
    ax.axis('equal')

    # Add a legend for clarity
    ax.legend(loc='best')


def plot_ru_vs_gxy(ax, data, params, stop_idx, xmin='auto', xmax='auto', ymin='auto', ymax='auto'):
    """
    Plots the pore pressure ratio (ru) versus shear strain (\u03b3_xy) on the provided Matplotlib Axes.

    Parameters:
    - ax: Matplotlib Axes
        The Axes object where the plot will be drawn.
    - data: pandas.DataFrame
        A DataFrame containing the data to be plotted. Must include the following columns:
        'gamxy' (shear strain) and 'ru' (pore pressure ratio).
    - params: dict
        A dictionary of parameters, if needed for additional customization. Not directly used in this function.
    - stop_idx: int
        The index in the data up to which the plot should be drawn.
    - xmin: float or 'auto', optional
        Minimum x-axis limit. If 'auto', it is calculated based on the data in the 'gamxy' column.
    - xmax: float or 'auto', optional
        Maximum x-axis limit. If 'auto', it is calculated based on the data in the 'gamxy' column.
    - ymin: float or 'auto', optional
        Minimum y-axis limit. If 'auto', it is calculated based on the data in the 'ru' column.
    - ymax: float or 'auto', optional
        Maximum y-axis limit. If 'auto', it is calculated based on the data in the 'ru' column.

    Returns:
    - None
        The function modifies the provided Axes object in place.

    Description:
    This function visualizes the evolution of the pore pressure ratio (ru) versus shear strain (\u03b3_xy) as a 2D plot. It includes the following features:
    - Automatic scaling of the axes based on the provided data or manual limits.
    - Draws a trajectory of ru values up to the given stop_idx.
    - Highlights the last point of the trajectory.
    - Includes horizontal reference lines at ru = 0 and ru = 1 to indicate key thresholds.

    Additional Details:
    - The function uses helper functions `set_limit`, which is assumed to calculate axis limits dynamically.
    - The x-axis represents shear strain (\u03b3_xy), and the y-axis represents the pore pressure ratio (ru).
    - The plot is intended to analyze the relationship between shear strain and pore pressure buildup.
    """

    # Set axis labels
    ax.set_xlabel('Shear strain, $\gamma_{xy}$ [-]')
    ax.set_ylabel('ru coefficient, $ru$ [-]')

    # Add grid lines for better visualization
    ax.grid(color='gray', alpha=0.2)

    # Helper function to calculate axis limits
    xmin, xmax = set_limit(xmin, xmax, data, ['gamxy'])  # Set x-axis limits based on the 'gamxy' column
    ymin, ymax = set_limit(ymin, ymax, data, ['ru'])  # Set y-axis limits based on the 'ru' column

    value_max = max(abs(ymin), ymax)

    # Apply the calculated axis limits
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(-value_max, value_max)

    # Plot ru versus gamxy trajectory
    ax.plot(data['gamxy'].values[:stop_idx], data['ru'].values[:stop_idx], color='k')

    # Highlight the last point in the trajectory
    ax.scatter(data['gamxy'].values[stop_idx-1], data['ru'].values[stop_idx-1], color='k')

    # Add horizontal reference lines
    ax.axhline(0, color='k', linestyle='dotted')
    ax.axhline(1, color='r', linestyle='dotted')

def particles_plot(ax, data, params, stop_idx, limit_move='auto'):
    """
    Plots a visualization of particle movement and force interactions on the provided Matplotlib Axes.

    Parameters:
    - ax: Matplotlib Axes
        The Axes object where the plot will be drawn.
    - data: pandas.DataFrame
        A DataFrame containing the data to be plotted. Must include the following columns:
        'zxy' (movement factor in the zxy direction) and 'sxy' (shear stress).
    - params: dict
        A dictionary of parameters, if needed for additional customization. Not directly used in this function.
    - stop_idx: int
        The index in the data up to which the plot should be drawn.
    - limit_move: float or 'auto', optional
        The maximum movement limit for the visualization. If 'auto', it defaults to 10.

    Returns:
    - None
        The function modifies the provided Axes object in place.

    Description:
    This function creates a schematic representation of particle movement, including:
    - Two stationary particles drawn as circles.
    - A third particle that moves vertically and horizontally based on the input data.
    - Arrows representing forces or displacements applied to the moving particle.

    Additional Details:
    - The stationary particles are represented as fixed circles at (-1,1) and (1,1).
    - The moving particle's position is determined by the 'zxy' value at the specified index (`stop_idx`).
      The movement is constrained by the `limit_move` parameter.
    - The force arrows are scaled and oriented based on the `sxy` value in the data.
    - The axes are turned off to emphasize the schematic representation.
    """

    # Draw stationary particles
    centro = (1, 1)
    radio = 1
    circulo = patches.Circle(centro, radio, edgecolor='darkgoldenrod', facecolor='darkgoldenrod', linewidth=2)
    ax.add_patch(circulo)

    centro = (-1, 1)
    radio = 1
    circulo = patches.Circle(centro, radio, edgecolor='darkgoldenrod', facecolor='darkgoldenrod', linewidth=2)
    ax.add_patch(circulo)

    # Set axis limits
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1, 5)

    # Determine movement limit
    if limit_move == 'auto':
        limit_move = 10

    # Calculate moving particle position
    zxy = max(min(data['zxy'].values[stop_idx - 1], limit_move), -limit_move) * -1
    dfactor = zxy / limit_move
    x = 0.5 * dfactor
    y = 2.95 - 0.2 * ((0.5 - np.abs(x)) / 0.5)

    # Draw moving particle
    centro = (x, y)
    radio = 1
    circulo = patches.Circle(centro, radio, edgecolor='darkgoldenrod', facecolor='darkgoldenrod', linewidth=2)
    ax.add_patch(circulo)

    # Add force/displacement arrows
    ax.arrow(x, y + 2, 0, -0.75, color='r', head_width=0.1)
    if x != 0:
        ax.arrow(x, y + 1.1, 0.75 / 0.5 * 0.5 * data['sxy'].values[stop_idx - 1] / data['sxy'].max(), 0, color='b', head_width=0.1)

    # Turn off the axis
    ax.axis('equal')
    ax.set_axis_off()

def plot_rxy_vs_N(ax, data,params, stop_idx, xmin='auto', xmax='auto', ymin='auto', ymax='auto'):
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
    ax.set_ylabel('Back stress ratio, $r_{ii}$ [-]')  # Label for the y-axis

    # Add a horizontal reference line at \u03c4_xy = 0
    ax.axhline(0, color='k', linestyle='dotted')

    # Add grid lines for better visualization
    ax.grid(color='gray', alpha=0.2)

    # Helper function to calculate axis limits
    xmin, xmax = set_limit(xmin, xmax, data, ['N'])  # Set x-axis limits based on the 'N' column
    ymin, ymax = set_limit(ymin, ymax, data, ['rxx', 'rxy', 'ryy'])  # Set y-axis limits based on the back stress ratio columns

    # Apply the calculated axis limits
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    # Define colors and labels for the variables
    colors = {
        'rxx': 'b',           # Blue for \u03b1_xx
        'ryy': 'r',           # Red for \u03b1_yy
        'rxy': 'forestgreen'  # Green for \u03b1_xy
    }
    sims = {
        'rxx': '$r_{xx}$',
        'ryy': '$r_{yy}$',
        'rxy': '$r_{xy}$'
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
