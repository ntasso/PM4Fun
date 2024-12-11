from .plot_settings import set_limit
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
    xmin, xmax = set_limit(xmin, xmax, data['gamxy'])
    ymin, ymax = set_limit(ymin, ymax, data['sxy'])

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
    xmin, xmax = set_limit(xmin, xmax, data['sy'])
    ymin, ymax = set_limit(ymin, ymax, data['sxy'])

    # Apply axis limits
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    # Plot the data from the start to the stop index
    ax.plot(data['sy'].values[:stop_idx], data['sxy'].values[:stop_idx], color='k')

    # Highlight the last point in the plot
    ax.scatter(data['sy'].values[stop_idx - 1], data['sxy'].values[stop_idx - 1], color='k')
