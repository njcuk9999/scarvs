# filepath: /mnt/g/Mon disque/École/Université/Maîtrise/scarvs/scarvs/scarvs/plotting/plot_results.py
import os

import matplotlib.pyplot as plt
import numpy as np

from scarvs.science.model import keplerian_model

def plot_results(params):
    # Load the samples
    samples_file = params['samples_file']
    samples = np.load(samples_file, allow_pickle=True).item()
    
    # Extract data
    time = params['data']['rjd']
    vrad = params['data']['vrad']
    svrad = params['data']['svrad']
    priors = params['priors']
    param_names = list(priors.keys())
    
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.errorbar(time, vrad, yerr=svrad, fmt='o', label='Data')
    for i in range(100):
        sample_params = {name: samples[name][i] for name in param_names}
        rv_model = keplerian_model(time, sample_params)
        plt.plot(time, rv_model, color='gray', alpha=0.1)
    plt.xlabel('Time (BJD)')
    plt.ylabel('Radial Velocity (m/s)')
    plt.legend()
    
    # Save the plot
    plot_file = os.path.join(params['PATHS']['PLOT_PATH'], 'rv_fit_results.png')
    plt.savefig(plot_file)
    plt.close()
    
    return plot_file