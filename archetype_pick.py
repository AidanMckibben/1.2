# code to grab the bilding_combinations csv and output the correct output based on input

import pandas as pd

def select_building_output(user_input, lookup_table_path):
    """
    Given user_input (dict of parameters) and path to lookup table, return the appropriate output.

    Args:
        user_input (dict): Keys should include 'BuildingType', 'BuildingStructure', 'WWR', 'HeatingSystem', 'DHWSystem'
        lookup_table_path (str): Path to the lookup table file (.xlsx or .csv)

    Returns:
        output (str or None): The matched output, or None if no match is found.
    """
    # Load the lookup table
    lookup = pd.read_csv(lookup_table_path)

    # Build mask for matching all parameters
    mask = (
        (lookup['Building Type'] == user_input['Building Type']) &
        (lookup['Building Structure'] == user_input['Building Structure']) &
        (lookup['Window-to-Wall-Ratio'] == user_input['Window-to-Wall-Ratio']) &
        (lookup['Heating System'] == user_input['Heating System']) &
        (lookup['DHW System'] == user_input['DHW System'])
    )

    # Find the matched output
    result = lookup.loc[mask, 'Archetype Model']
    if not result.empty:
        return result.iloc[0]
    else:
        return None


if __name__ == "__main__":
    input_1 = {
        'Building Type': 'Townhouses',
        'Building Structure': 'Wood Frame',
        'Window-to-Wall-Ratio': 'Low (<20%)',
        'Heating System': 'Electric Baseboards',
        'DHW System': 'Electric'
    }
    print(select_building_output(input_1, 'building_combinations.csv'))
# Example usage:
# user_input = {
#     'Building Type': 'Townhouses',
#     'Building Structure': 'Wood Frame',
#     'WWR': 'Low (<20%)',
#     'Heating System': 'Electric baseboards',
#     'DHW System': 'Electric'
# }
# output = select_building_output(user_input, 'building_combinations.csv')
# print('Output:', output)