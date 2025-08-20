import pandas as pd
from typing import Dict, Optional

# this class is only need to look up the new leakage rate, not needed for the existing leakage rate
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
        else:
            raise Exception('Existing window code could not be selected')

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
            else:
                raise Exception('Existing door code could not be selected')

class PreviousWallRValueLookup:
    def __init__(self, csv_path: str):
        """
        Loads the CSV into a pandas DataFrame for fast lookup.
        Expects columns: Thermal Bridging Performance, Walls, Wall Exterior Insulation, R-Value.
        """
        self.df = pd.read_csv(csv_path, dtype=str)
        # Strip whitespace from all relevant columns
        for col in ['Thermal Bridging Performance', 'Walls', 'Wall Exterior Insulation', 'R-Value']:
            self.df[col] = self.df[col].astype(str).str.strip()

    def get_rvalue(self, user_inputs: Dict[str, str]) -> Optional[str]:
        """
        Looks up the R-Value based on user input dictionary.
        Keys should include 'Thermal Bridging Performance', 'Walls', 'Wall Exterior Insulation'.
        Returns None if no match is found.
        """
        tb_perf = user_inputs.get('Thermal Bridging Performance', '').strip()
        walls = user_inputs.get('Walls', '').strip()
        # for the previous runs, we never have an insulation upgrade. Thus, we will only take options with no exterior insulation
        ext_ins = "No ext. ins"

        matches = self.df[
            (self.df['Thermal Bridging Performance'] == tb_perf) &
            (self.df['Walls'] == walls) &
            (self.df['Wall Exterior Insulation'] == ext_ins)
        ]
        
        if not matches.empty:
            return matches.iloc[0]['R-Value']
        else:
            raise Exception("A wall R-Value was not obtained")

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
        else:
            raise Exception('New window code could not be selected')

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
        else:
            raise Exception('New door code could not be selected')

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

    def get_rvalue(self, user_inputs: Dict[str, str]) -> Optional[str]:
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
    df_airtightness = AirtightnessLookup('airtightness_table.csv')
    df_existing_window = ExistingWindowLookup('existing_window_table.csv')
    df_previous_wall = PreviousWallRValueLookup('wall_rvalue_table.csv')
    df_new_window = NewWindowLookup('new_window_table.csv')
    df_new_wall = NewWallRValueLookup('wall_rvalue_table.csv')

    input = {
        'Window-to-Wall-Ratio': 'High (>30%)',
        'Walls': 'Uninsulated',
        'Frame Type': 'Aluminum (no thermal break)',
        'Glazing': 'Single Glazing',
        'Glazing Cavity': 'none',
        'Thermal Bridging Performance': 'High TB',
        'Airtightness': 'Average',
        'Retrofit Window Frame': 'Aluminum',
        'Retrofit Window Glazing': 'Double',
        'Wall Exterior Insulation': 'No ext. ins',
        'Roof Upgrade': 'None'
    }

    print(input)
    leakage_rate = df_airtightness.get_leakage_rate(input)
    existing_window_code = df_existing_window.get_window_code(input)
    previous_rvalue = df_previous_wall.get_rvalue(input)
    new_window_code = df_new_window.get_window_code(input)
    new_rvalue = df_new_wall.get_rvalue(input)
