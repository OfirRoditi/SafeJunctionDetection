# Project: Driving Safety Analysis

## Overview
This project focuses on analyzing road safety data to identify trends, patterns, and areas of improvement for reducing accidents. Using Python and Miniconda, we set up a structured environment for data analysis and visualization.

---

## Getting Started

### Environment Setup
1. **Install Miniconda**: Ensure you have Miniconda installed on your system.
 
2. **Create a Conda Environment**:
   ```bash
   conda create -n my_project_env python=3.9
   conda activate my_project_env
   ```
3. **Install Required Libraries**:
   Install the following libraries:
   ```bash
   conda install pandas numpy matplotlib seaborn
   conda install jupyter  # Optional, for interactive analysis
   ```

4. **Export Environment**:
   Export the environment to share with others:
   ```bash
   conda env export > environment.yml
   ```
---

### Project Structure
The project is organized as follows:
```
project_folder/
├── data/             # Raw and processed datasets
├── notebooks/        # Jupyter Notebooks for exploratory analysis
├── scripts/          # Python scripts for reusable logic
├── outputs/          # Graphs, results, and visualizations
├── environment.yml   # Conda environment configuration
└── README.md         # Project description and setup instructions
```

---

## How to Run
1. Clone the repository or download the project folder.
2. Create the Conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate my_project_env
   ```
3. Open the project in VS Code.
4. Select the Conda environment as the interpreter (via Command Palette: `Python: Select Interpreter`).
5. Run scripts or open notebooks to start analyzing data.

---

## Example Script
Here’s an example script for basic data exploration:
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data/your_dataset.csv')

# Plot accidents by day of the week
accidents_by_day = data['YOM_BASHAVUA'].value_counts()
accidents_by_day.sort_index().plot(kind='bar')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Accidents')
plt.title('Accidents by Day of the Week')
plt.show()
```

---

## Sharing with Teammates
1. Share the `environment.yml` file to recreate the Conda environment:
   ```bash
   conda env create -f environment.yml
   ```
2. Use Git for version control and collaboration.
---

## Dependencies
- Python 3.9
- pandas
- numpy
- matplotlib
- seaborn
- jupyter (optional)

---
## By me
- check for the env name :
conda info --envs

-



