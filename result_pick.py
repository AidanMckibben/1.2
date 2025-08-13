import pandas as pd

# I need to make a function that takes the dictionary of user inputs and returns the correct result
# This should use existing_window_lookup.py, new_window_lookup.py, wall_rvalue_lookup.py, and airtightness code (which I have not written yet)

def previous_result_picker(user_input_dict, result_path):


    # first we grab all the classes that we'll be using
    from existing_window_lookup import ExistingWindowLookup
    from previous_wall_rvalue_lookup import PreviousWallRValueLookup

    # and we grab all the values that we'll be running in the batch tool
    existing_window_code = ExistingWindowLookup('existing_window_table.csv').get_window_code(user_input_dict)
    existing_door_code = ExistingWindowLookup('existing_window_table.csv').get_door_code(user_input_dict)
    previous_wall_rvalue = PreviousWallRValueLookup('wall_rvalue_table.csv').get_r_value(user_input_dict)

    print(existing_window_code)
    # the airtightness rate is mock until Maddy shows me something
    airtightness_rate = "0.15"

    # these are the results
    results = pd.read_csv(result_path)

    # build mask for matching all parameters
    mask = (
        (results['Window Type'] == existing_window_code)) #&
        #(results['Sliding Door Type'] == existing_door_code) &
        #(results['Airtightness'] == airtightness_rate) &
        #(results['Wall R-Value'] == previous_wall_rvalue)
    #)

    # Find the matched output
    tedi = results.loc[mask, "Overheating Hours in Worst Suite"]
    if not tedi.empty:
        return tedi.iloc[0]
    else:
        return None

def new_result_picker(user_input_dict, lookup_result_path):
        
    # set up the user inputs variable that is used for each class
    user_inputs = user_input_dict

    # first we grab all the classes that we'll be using
    from new_window_lookup import NewWindowLookup
    from new_wall_rvalue_lookup import NewWallRValueLookup

    # and we grab all the values that we'll be running in the batch tool
    new_window_code = NewWindowLookup('new_window_table.csv')
    new_wall_rvalue = NewWallRValueLookup('wall_rvalue_table.csv')




if __name__ == "__main__":
    input_1 = {
        'Building Type': 'Townhouses',
        'Building Structure': 'Wood Frame',
        'WWR': 'Low (<20%)',
        'Heating System': 'Electric baseboards',
        'DHW System': 'Electric',
        'Walls': 'Wood',
        'Frame Type': 'Vinyl',
        'Glazing': 'Single',
        'Airspace': 'n/a',
        'Thermal Bridging': 'Bad',
        'Airtightness': 'Bad',
    }
   
    print(input_1)

    print(previous_result_picker(input_1, 'mock_results.csv'))