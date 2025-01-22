# Project: Driving Safety Analysis

## Overview
This project focuses on analyzing road safety data to identify trends, patterns, and areas of improvement for reducing accidents. Using Python and Miniconda, we set up a structured environment for data analysis and visualization.

---

## Getting Started

### Environment Setup
1. **Install Miniconda**: Ensure you have Miniconda installed on your system.
 
2. **Create a Conda Environment**:
   **Creating env in miniconda folder.**
   ```bash
   conda create -n my_project_env python=3.9
   Activate the env.
   conda activate my_project_env
   ```
3. **Install Required Libraries**:
   Install the following libraries:
   ```bash
   conda install pandas numpy matplotlib seaborn
   conda install jupyter 
   ```

4. **Export Environment**:
   Export the environment to share with others:
   ```bash
   conda env export > environment.yml
   ```
---

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

## Sharing with Teammates
1. Share the `environment.yml` file to recreate the Conda environment:
   ```bash
   conda env create -f environment.yml
   ```
2. Use Git for version control and collaboration.

---
## By me
- check for the env name :
conda info --envs



