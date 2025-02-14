# filepath: /mnt/g/Mon disque/École/Université/Maîtrise/scarvs/scarvs/scarvs/science/radial_velocity.py
import jax
import jax.numpy as jnp
import numpy as np
import numpyro
import numpyro.distributions as dist
from numpyro import infer
import matplotlib.pyplot as plt
import yaml
import os
from scarvs.science.model import keplerian_model
from scarvs.science.sampling import numpyro_model, run_sampler

def fit_keplerian_only(params):
    # Extract data and priors from params
    time = params['data']['rjd']
    vrad = params['data']['vrad']
    svrad = params['data']['svrad']
    priors = params['priors']
    
    # Define the parameter names and initial values
    param_names = list(priors.keys())
    init_values = {name: priors[name]['guess'] for name in param_names}
    
    # Define the numpyro model
    def model(x, param_dict):
        return keplerian_model(x, param_dict)
    
    # Run the sampler
    samples = run_sampler(numpyro_model, init_values, time, vrad, yerr=svrad, model=model, param_names=param_names, priors=priors)
    
    # Ensure the plot directory exists
    results_path = params['PATHS']['RESULTS_PATH']
    samples_path = os.path.join(results_path, 'samples')
    os.makedirs(samples_path, exist_ok=True)
    
    # Store the samples as a .npy file
    samples_file = os.path.join(samples_path, 'samples.npy')
    np.save(samples_file, samples)
    
    return samples