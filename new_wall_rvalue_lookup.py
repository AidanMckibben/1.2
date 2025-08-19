import pandas as pd
from typing import Dict, Optional

class NewWallRValueLookup:
    def __init__(self, csv_path: str):
        """
        Loads the CSV into a pandas DataFrame for fast lookup.
        Expects columns: Thermal Bridging Performance, Walls, Wall Exterior Insulation, R-Value.
        """
        self.df = pd.read_csv(csv_path, dtype=str)
        # Strip whitespace from all relevant columns
        for col in ['Thermal Bridging Performance', 'Walls', 'Wall Exterior Insulation', 'R-Value']:
            self.df[col] = self.df[col].astype(str).str.strip()

    def get_r_value(self, user_inputs: Dict[str, str]) -> Optional[str]:
        """
        Looks up the R-Value based on user input dictionary.
        Keys should include 'Thermal Bridging Performance', 'Walls', 'Wall Exterior Insulation'.
        Returns None if no match is found.
        """
        tb_perf = user_inputs.get('Thermal Bridging Performance', '').strip()
        walls = user_inputs.get('Walls', '').strip()
        ext_ins = user_inputs.get('Wall Exterior Insulation', '').strip()

        matches = self.df[
            (self.df['Thermal Bridging Performance'] == tb_perf) &
            (self.df['Walls'] == walls) &
            (self.df['Wall Exterior Insulation'] == ext_ins)
        ]

        if not matches.empty:
            return matches.iloc[0]['R-Value']
        else:
            raise Exception('New wall R-Value could not be selected')




# for testing
if __name__ == "__main__":
    lookup = NewWallRValueLookup("wall_rvalue_table.csv")
    user_inputs = {
        'Thermal Bridging Performance': 'High TB',
        'Walls': '2x4 Wood Frame Walls', 
        'Wall Exterior Insulation': 'No ext. ins.'
    }

    new_rvalue = lookup.get_r_value(user_inputs)
    print(new_rvalue)

# Example usage:
# lookup = WallRValueLookup('wall_rvalues.csv')
# user_inputs = {
#     'Thermal Bridging Performance': 'High TB',
#     'Walls': '2x4 Wood Frame Walls',
#     'Wall Exterior Insulation': '3" ext. ins'
# }
# r_value = lookup.get_r_value(user_inputs)
# print(r_value)  # Should print: 14