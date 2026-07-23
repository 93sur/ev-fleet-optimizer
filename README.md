# EV Fleet Optimizer

**Master's Project | FAU Erlangen-Nürnberg | M.Sc. Electromobility**

A Python-based computational tool for electric vehicle fleet management optimization, 
integrating electrical engineering principles with data science and machine learning.

## Overview

This project addresses key challenges in EV fleet operations:
- **Energy efficiency analysis** across vehicle fleets
- **Charging cycle optimization** for infrastructure planning
- **Battery performance monitoring** and predictive modeling
- **Thermal management** based on caloric state variables

## Features

| Feature | Description |
| Fleet Data Processing | Import and analyze technical EV parameters from CSV datasets |
| Optimization Engine | Computational strategies for charging infrastructure allocation |
| Predictive Analytics | ML-based forecasting of battery performance and degradation |
| Interactive Dashboard | Streamlit web interface for real-time visualization |
| Thermal Analysis | Circuit modeling and AC analysis for thermal management |

## Tech Stack

- **Language:** Python 3.10+
- **ML/AI:** TensorFlow, Scikit-learn
- **Data:** NumPy, Pandas
- **Visualization:** Matplotlib, Plotly, Streamlit
- **Development:** VS Code, Anaconda

## Project Structure
ev-fleet-optimizer/
├── main_app.py              # Main Streamlit application
├── calc.py                  # Core calculations module
├── data_gen.py              # Synthetic data generation
├── optimizer.py             # Optimization algorithms
├── fleet_data.csv           # Sample fleet dataset
├── fleet_data_optimized.csv # Optimized output
├── data/                    # Additional datasets
├── requirements.txt         # Python dependencies
└── README.md               # This file
plain
## AI Fleet Assistant

Natural language interface for fleet queries, powered by Groq API.
*Note: Requires Groq API key for full functionality.*
## Academic Context

Developed as part of the **Master's program in Electromobility** at 
[Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU)](https://www.fau.de).

The project incorporates:
- Thermal management analysis based on caloric state variables
- Electrical circuit modeling and AC analysis
- Machine learning architectures for predictive analytics

## Installation

```bash
# Clone repository
git clone https://github.com/93sur/ev-fleet-optimizer.git
cd ev-fleet-optimizer

# Install dependencies
pip install -r requirements.txt

# Run application
python main_app.py
Author
Nilufar Yuldashova (@93sur)
M.Sc. Student in Electromobility
FAU Erlangen-Nürnberg, Germany
This project is developed for academic purposes as part of Master's studies
in Electromobility at FAU Erlangen-Nürnberg.
