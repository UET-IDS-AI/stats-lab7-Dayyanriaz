"""
AI_stats_lab.py

Lab: Uniform Random Variable Analysis
"""

import numpy as np


def uniform_analysis(a, n_samples=10000):
    """
    Returns:
    (
        theoretical_mean,
        theoretical_variance,
        sample_mean,
        sample_variance,
        mean_error,
        variance_error,
        transformed_mean,
        transformed_variance
    )
    """

    samples = np.random.uniform(low=0, high=a, size=n_samples)

    theoretical_mean = a / 2.0
    theoretical_variance = a * a / 12.0

    sample_mean = np.mean(samples)
    sample_variance = np.var(samples)

    mean_error = abs(theoretical_mean - sample_mean)
    variance_error = abs(theoretical_variance - sample_variance)

    transformed_mean = (2 * theoretical_mean) + 1
    transformed_variance = (2 ** 2) * theoretical_variance

    return (
        theoretical_mean,
        theoretical_variance,
        sample_mean,
        sample_variance,
        mean_error,
        variance_error,
        transformed_mean,
        transformed_variance
    )


if __name__ == "__main__":
    print(uniform_analysis(6))
