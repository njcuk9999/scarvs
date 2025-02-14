import jax
import jax.numpy as jnp

import numpyro
from numpyro import distributions as dist, infer

def numpyro_model(x, model, param_names, priors, y=None, yerr=None):
    param_dict = {}
    
    # Define the priors for each parameter
    for param_name, prior in zip(param_names, priors):
        if prior["distribution"] == "uniform":
            param_dict[param_name] = numpyro.sample(param_name, dist.Uniform(prior["min"], prior["max"]))
        elif prior["distribution"] == "normal":
            param_dict[param_name] = numpyro.sample(param_name, dist.Normal(prior["mean"], prior["std"]))
        elif prior["distribution"] == "loguniform":
            param_dict[param_name] = numpyro.sample(param_name, dist.LogUniform(prior["min"], prior["max"]))
        else:
            raise ValueError(f"Unsupported distribution type: {prior['distribution']}")
    
    # White noise
    error = numpyro.sample("error", dist.LogUniform(jnp.median(yerr)/100.0, jnp.median(yerr)*100.0))
    
    # Offset
    offset = numpyro.sample("offset", dist.Normal(jnp.median(y), jnp.std(y)))

    # Compute RV model from planetary signals
    rv_planet = model(x, param_dict)
    
    # the likelihood function
    numpyro.sample("y", dist.Normal(rv_planet, jnp.sqrt(error**2 + yerr.magnitude**2)), obs=y-offset)
    
def run_sampler(numpyro_model, init_values, x, y, verbose=True, seed_id=42):
    # Define the number of warm-up steps, samples, and chains
    ndim = len(init_values)
    
    # Set the number of samples and chains based on the number of parameters 
    # TODO: Make this more flexible
    num_warmup = ndim * 1000
    num_samples = ndim * 2000
    num_chains = ndim

    # Use NUTS sampler with initialization strategy set to predefined values
    nuts_model = infer.NUTS(numpyro_model,
                            dense_mass=True,
                            regularize_mass_matrix=False,
                            init_strategy=infer.init_to_value(values=init_values))
    sampler = infer.MCMC(
        nuts_model,  # Initialize with the defined initial values
        num_warmup=num_warmup,
        num_samples=num_samples,
        num_chains=num_chains,
        progress_bar=verbose,
    )

    # Ensure random seed is provided and compatible with JAX
    seed = jax.random.PRNGKey(seed_id)

    # Run the sampler on the model with time and observed RV data
    if not verbose:
        print("Sampling in progress...")
    else:    
        sampler.run(seed, x, y=y)

    # Summarize the results
    if verbose:
        sampler.print_summary()
    else: 
        print("Sampling complete.")
    
    return sampler.get_samples()