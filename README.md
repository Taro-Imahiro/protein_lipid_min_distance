# Protein-Lipid Minimum Distance Calculator
A python script to calculate and output the minimum distances between a protein and selected lipid molecules from a molecular dynamics simulation using MDAnalysis with parallel processing.

## Requirement

- Python 3.6 or higher
- MDAnalysis
- Pandas
- NumPy

You can install the required packages using pip:

```{bash}
pip install MDAnalysis pandas numpy
```

# Usage

```
python protein_lipid_min_distance.py -s TOPOLOGY -f TRAJECTORY
```

After executing the script, you will be prompted to select the lipid residues you would like to calculate the distances for. The script will display a list of lipid candidates found in your topology file.

 (Molecular species other than protein, water, and ion are displayed as candidates, so ligands may be displayed.)

The script will output a CSV file for each selected lipid with the minimum distances between the protein and each lipid residue over the trajectory.

# Output
The output CSV files will have the following columns:

**time (ps)**: The time in picoseconds for each frame in the trajectory.
**lipid_resid**: The residue ID of the lipid molecule.
**min_distance_protein_{lipid} (nm)**: The minimum distance between the protein and the lipid residue in nanometers.

The CSV files will be named protein_{lipid}_distance.csv, where {lipid} is replaced with the lipid residue name.

## License
This project is licensed under the MIT License.