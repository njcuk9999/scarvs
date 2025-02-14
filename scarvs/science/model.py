# filepath: /mnt/g/Mon disque/École/Université/Maîtrise/scarvs/scarvs/scarvs/science/radial_velocity.py
import jax
import jax.numpy as jnp
import jaxoplanet
from jaxoplanet.orbits import keplerian
from jaxoplanet.units import unit_registry as ureg

def keplerian_model(time, params):
    
    # Define the central star
    star_params = params['star']
    star = keplerian.Central(mass=star_params['mass'], radius=star_params['radius'])
    
    # Define the planetary system
    system = keplerian.System(star)
    for planet_params in params['planets']:
        system = system.add_body(
            radial_velocity_semiamplitude=planet_params['k'] * ureg.m / ureg.s, 
            period=planet_params['per'] * ureg.days, 
            time_transit=planet_params['tc'] * ureg.days,
            eccentricity=planet_params['e'],
            omega_peri=planet_params['w']
        )
    
    # Calculate radial velocities for all bodies in one call
    signals = system.radial_velocity(time)

    # Sum contributions from all planets and return
    return signals.to(ureg.m / ureg.s).magnitude.sum(axis=0)