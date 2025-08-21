import pandas as pd
# import all classes needed from lookup
from lookup import AirtightnessLookup
from lookup import ExistingWindowLookup
from lookup import PreviousWallRValueLookup
from lookup import NewWindowLookup
from lookup import NewWallRValueLookup

def previous_result_picker(user_input_dict, result_path):
    
    # these are the results that have been outputted by our equest runs
    results = pd.read_csv(result_path)
    
    # and we grab all the values that we'll be running in the batch tool
    existing_window_code = ExistingWindowLookup('existing_window_table.csv').get_window_code(user_input_dict)
    previous_wall_rvalue = PreviousWallRValueLookup('wall_rvalue_table.csv').get_rvalue(user_input_dict)
    if user_input_dict['Airtightness'] == 'Poor':
        previous_leakage_rate = 0.15
    elif user_input_dict['Airtightness'] == 'Average':
        previous_leakage_rate = 0.09
    else:
        raise ValueError('Airtightness was set as something other than Poor or Average')
    if user_input_dict['Roof Upgrade'] == 'Improved':
        filtered_results = results[results['Roof R-Value'] == 30]
    else:
        filtered_results = results[results['Roof R-Value'] != 30]

    # for the sake of testing
    print(existing_window_code)
    print(previous_wall_rvalue)
    print(previous_leakage_rate)
    
    # build mask for matching all parameters
    mask = ((filtered_results['Window Type'] == existing_window_code) &
        (filtered_results['Airtightness'] == previous_leakage_rate) &
        (filtered_results['Wall R-Value'] == float(previous_wall_rvalue))
    )

    # Find the matched output
    tedi = filtered_results.loc[mask, filtered_results.columns[7]].item()
    cedi = filtered_results.loc[mask, filtered_results.columns[8]].item()
    teui = filtered_results.loc[mask, filtered_results.columns[9]].item()
    heat_hours = filtered_results.loc[mask, filtered_results.columns[10]].item()
    max_temp = filtered_results.loc[mask, filtered_results.columns[11]].item()
    utility_cost = filtered_results.loc[mask, filtered_results.columns[12]].item()

    output_list = [tedi, cedi, teui, heat_hours, max_temp, utility_cost]

    if tedi != None :
        return output_list
    else:
        return 'Existing result not found'


def new_result_picker(user_input_dict, result_path):

    # make a dataframe of the results
    results = pd.read_csv(result_path)

    # and we grab all the values that we'll be running in the batch tool
    new_window_code = NewWindowLookup('new_window_table.csv').get_window_code(user_input_dict)
    new_wall_rvalue = NewWallRValueLookup('wall_rvalue_table.csv').get_rvalue(user_input_dict)
    new_leakage_rate = AirtightnessLookup('airtightness_table.csv').get_leakage_rate(user_input_dict)
    if user_input_dict['Roof Upgrade'] == 'Improved':
        filtered_results = results[results['Roof R-Value'] == 30]
    else:
        filtered_results = results[results['Roof R-Value'] != 30]

    # for the sake of testing
    print(new_window_code)
    print(new_wall_rvalue)
    print(new_leakage_rate)

    mask = ((filtered_results['Window Type'] == new_window_code) &
        (filtered_results['Airtightness'] == float(new_leakage_rate)) &
        (filtered_results['Wall R-Value'] == float(new_wall_rvalue))
    )
    print(filtered_results['Roof R-Value'])
    # Find the matched output
    tedi = filtered_results.loc[mask, filtered_results.columns[7]].item()
    cedi = filtered_results.loc[mask, filtered_results.columns[8]].item()
    teui = filtered_results.loc[mask, filtered_results.columns[9]].item()
    heat_hours = filtered_results.loc[mask, filtered_results.columns[10]].item()
    max_temp = filtered_results.loc[mask, filtered_results.columns[11]].item()
    utility_cost = filtered_results.loc[mask, filtered_results.columns[12]].item()

    output_list = [tedi, cedi, teui, heat_hours, max_temp, utility_cost]

    if tedi != None :
        return output_list
    else:
        return "Retrofit result not found"






# for testing
if __name__ == "__main__":
    input_1 = {
        'Building Type': 'Townhouses',
        'Building Structure': 'Wood Frame',
        'Window-to-Wall-Ratio': 'High (>30%)',
        'Heating System': 'Electric Baseboards',
        'DHW System': 'Electric',
        'Walls': '2x4 studs w/ batt',
        'Frame Type': 'Aluminum (no thermal break)',
        'Glazing': 'Single Glazing',
        'Glazing Cavity': 'none',
        'Thermal Bridging Performance': 'Average TB',
        'Airtightness': 'Average',
        'Retrofit Window Frame': 'Aluminum',
        'Retrofit Window Glazing': 'Double',
        'Wall Exterior Insulation': 'No ext. ins',
        'Roof Upgrade': 'Improved'
    }
   
    print(input_1)

    print(previous_result_picker(input_1, 'Results/Barafield.csv'))
    print(new_result_picker(input_1, 'Results/Barafield.csv'))
