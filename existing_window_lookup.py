import pandas as pd
from typing import Dict, Optional

class ExistingWindowLookup:
    def __init__(self, csv_path: str):
        """
        Loads the CSV into a pandas DataFrame for fast lookup.
        """
        self.df = pd.read_csv(csv_path, dtype=str, keep_default_na=False)
        # Strip whitespace from all string columns
        for col in ['Frame Type', 'Glazing Cavity', 'Glazing', 'Window Code', 'Door Code']:
            self.df[col] = self.df[col].astype(str).str.strip()

    def get_window_code(self, user_inputs: Dict[str, str]) -> Optional[str]:
        """
        Looks up the code based on user input dictionary.
        Keys should include 'Frame Type', 'Airspace', 'Glazing'.
        Returns None if no match is found.
        """
        frame_type = user_inputs.get('Frame Type', '').strip()
        airspace = user_inputs.get('Glazing Cavity', '').strip()
        glazing = user_inputs.get('Glazing', '').strip()

        matches = self.df[
            (self.df['Frame Type'] == frame_type) &
            (self.df['Glazing Cavity'] == airspace) &
            (self.df['Glazing'] == glazing)
        ]

        if not matches.empty:
            return matches.iloc[0]["Window Code"]
        return None

    def get_door_code(self, user_inputs: Dict[str, str]) -> Optional[str]:
            """
            Looks up the code based on user input dictionary.
            Keys should include 'Frame Type', 'Airspace', 'Glazing'.
            Returns None if no match is found.
            """
            frame_type = user_inputs.get('Frame Type', '').strip()
            airspace = user_inputs.get('Glazing Cavity', '').strip()
            glazing = user_inputs.get('Glazing', '').strip()

            matches = self.df[
                (self.df['Frame Type'] == frame_type) &
                (self.df['Glazing Cavity'] == str(airspace)) &
                (self.df['Glazing'] == glazing)
            ]

            if not matches.empty:
                return matches.iloc[0]["Door Code"]
            return None

if __name__ == "__main__":
    lookup = ExistingWindowLookup("existing_window_table.csv")
    user_inputs = {
        "Frame Type": "Vinyl",
        "Glazing Cavity": "none",
        "Glazing": "Single Glazing"
    }

    door_code = lookup.get_window_code(user_inputs)
    window_code = lookup.get_door_code(user_inputs)
    print(door_code)
    print(window_code)
    
    
# lookup = WindowCodeLookup('window_codes.csv')
# user_inputs = {
#     'Frame Type': 'Aluminum, no thermal break',
#     'Airspace': '1/4"',
#     'Glazing': 'Double Glazing (no low-e coating)'
# }
# code = lookup.get_code(user_inputs)
# print(code)  # Should print: Exist2