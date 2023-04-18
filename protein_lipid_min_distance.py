import MDAnalysis as mda
import pandas as pd
import argparse
from MDAnalysis.analysis import distances

def get_lipid_candidates(universe):
    protein = universe.select_atoms("protein")
    water = universe.select_atoms("resname SOL or resname TIP3")
    ions = universe.select_atoms("resname NA or resname CL")
    not_lipid = protein + water + ions
    lipid_candidates = set(universe.atoms.resnames) - set(not_lipid.resnames)
    return lipid_candidates

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--topology", required=True, help="Path to the topology file.")
parser.add_argument("-f", "--trajectory", required=True, help="Path to the trajectory file.")
args = parser.parse_args()

u = mda.Universe(args.topology, args.trajectory)

lipid_candidates = get_lipid_candidates(u)
print("Lipid candidates: ", ", ".join(sorted(lipid_candidates)))

selected_lipids = input("Select lipids (comma-separated): ").split(",")

for lipid in selected_lipids:
    lipid = lipid.strip()
    protein = u.select_atoms("protein")
    lipid_residues = u.select_atoms(f"resname {lipid}").residues

    data = {
        "time (ps)": [],
        "lipid_resid": [],
        f"min_distance_protein_{lipid} (nm)": []
    }

    for ts in u.trajectory:
        for residue in lipid_residues:
            lipid_atoms = residue.atoms
            distances_array = distances.distance_array(protein.positions, lipid_atoms.positions, box=u.dimensions)
            min_distance = distances_array.min()
            data["time (ps)"].append(ts.time)
            data["lipid_resid"].append(residue.resid)
            data[f"min_distance_protein_{lipid} (nm)"].append(min_distance)

    df = pd.DataFrame(data)
    df.to_csv(f"protein_{lipid}_distance.csv", index=False)
    print(f"Output saved to protein_{lipid}_distance.csv")
