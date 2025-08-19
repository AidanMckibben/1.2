import pandas as pd
from typing import Dict, Optional

class AirtightnessLookup:
    def __init__(self, csv_path: str):
        """
        """
        self.df = pd.read_csv(csv_path, dtype=str)
        # strip whitespace from all relevant columns
        for col in ['Window-to-Wall-Ratio', 'Airtightness', 'Wall Exterior Insulation', 'Leakage Rate']:
            self.df[col] = self.df[col].astype(str).str.strip()

    def get_leakage_rate(self, user_inputs: Dict[str, str]) -> Optional[str]:
        """
        """
        wwr = user_inputs.get('Window-to-Wall-Ratio', '').strip()
        airtightness = user_inputs.get('Airtightness', '').strip()
        ext_ins = user_inputs.get('Wall Exterior Insulation', '').strip()

        matches = self.df[
            (self.df['Window-to-Wall-Ratio'] == wwr) & 
            (self.df['Airtightness'] == airtightness) &
            (self.df['Wall Exterior Insulation'] == ext_ins)
        ]

        if not matches.empty:
            return matches.iloc[0]['Leakage Rate']
        return 'Error getting Leakage Rate'

# for testing
if __name__ == "__main__":
    lookup = AirtightnessLookup("airtightness_table.csv")
    input_1 = {
        'Window-to-Wall-Ratio': 'Low (<20%)',
        'Airtightness': 'Average',
        'Wall Exterior Insulation': 'No ext. ins',
    }

    print(input_1)
    leakage_rate = lookup.get_leakage_rate(input_1)
    print(leakage_rate)