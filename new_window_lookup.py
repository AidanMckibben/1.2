import pandas as pd
from typing import Dict, Optional

class NewWindowLookup:
    def __init__(self, csv_path: str):
        """
        Loads the CSV into a pandas DataFrame for fast lookup.
        Expects columns: Frame Type, Glazing, Code.
        """
        self.df = pd.read_csv(csv_path, dtype=str)
        # Strip whitespace from all relevant columns
        for col in ['Frame Type', 'Glazing', 'Code']:
            self.df[col] = self.df[col].astype(str).str.strip()

    def get_code(self, user_inputs: Dict[str, str]) -> Optional[str]:
        """
        Looks up the code based on user input dictionary.
        Keys should include 'Frame Type' and 'Glazing'.
        Returns None if no match is found.
        """
        frame_type = user_inputs.get('Frame Type', '').strip()
        glazing = user_inputs.get('Glazing', '').strip()

        matches = self.df[
            (self.df['Frame Type'] == frame_type) &
            (self.df['Glazing'] == glazing)
        ]


        if not matches.empty:
            return matches.iloc[0]["Window Code"]
        return None

    def get_code(self, user_inputs: Dict[str, str]) -> Optional[str]:
        """
        Looks up the code based on user input dictionary.
        Keys should include 'Frame Type' and 'Glazing'.
        Returns None if no match is found.
        """
        frame_type = user_inputs.get('Frame Type', '').strip()
        glazing = user_inputs.get('Glazing', '').strip()

        matches = self.df[
            (self.df['Frame Type'] == frame_type) &
            (self.df['Glazing'] == glazing)
        ]


        if not matches.empty:
            return matches.iloc[0]["Door Code"]
        return None
# Example usage:
# lookup = WindowCodeLookup('window_codes.csv')
# user_inputs = {
#     'Frame Type': 'Fiberglass',
#     'Glazing': 'Triple, typical'
# }
# code = lookup.get_code(user_inputs)
# print(code)  # Should print: New2