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
        for col in ['Retrofit Window Frame', 'Retrofit Window Glazing', 'Window Code', 'Door Code']:
            self.df[col] = self.df[col].astype(str).str.strip()

    def get_window_code(self, user_inputs: Dict[str, str]) -> Optional[str]:
        """
        Looks up the code based on user input dictionary.
        Keys should include 'Frame Type' and 'Glazing'.
        Returns None if no match is found.
        """
        frame_type = user_inputs.get('Retrofit Window Frame', '').strip()
        glazing = user_inputs.get('Retrofit Window Glazing', '').strip()

        matches = self.df[
            (self.df['Retrofit Window Frame'] == frame_type) &
            (self.df['Retrofit Window Glazing'] == glazing)
        ]


        if not matches.empty:
            return matches.iloc[0]["Window Code"]
        return None

    def get_door_code(self, user_inputs: Dict[str, str]) -> Optional[str]:
        """
        Looks up the code based on user input dictionary.
        Keys should include 'Frame Type' and 'Glazing'.
        Returns None if no match is found.
        """
        frame_type = user_inputs.get('Retrofit Window Frame', '').strip()
        glazing = user_inputs.get('Retrofit Window Glazing', '').strip()

        matches = self.df[
            (self.df['Retrofit Window Frame'] == frame_type) &
            (self.df['Retrofit Window Glazing'] == glazing)
        ]


        if not matches.empty:
            return matches.iloc[0]["Door Code"]
        return None








# for testing
if __name__ == "__main__":
    lookup = NewWindowLookup("new_window_table.csv")
    user_inputs = {
        "Retrofit Window Frame": "Vinyl",
        "Glazing Cavity": "1/8",
        "Retrofit Window Glazing": "Triple, typical"
    }

    door_code = lookup.get_window_code(user_inputs)
    window_code = lookup.get_door_code(user_inputs)
    print(door_code)
    print(window_code)

# Example usage:
# lookup = WindowCodeLookup('window_codes.csv')
# user_inputs = {
#     'Frame Type': 'Fiberglass',
#     'Glazing': 'Triple, typical'
# }
# code = lookup.get_code(user_inputs)
# print(code)  # Should print: New2