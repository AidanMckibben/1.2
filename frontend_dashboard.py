import streamlit as st

# set page config
st.set_page_config(page_title="Window Tool", layout="wide")

# Helper to get current value or default for dropdowns
def get_dropdown_value(key, options):
    val = st.session_state.get(key, "Select...")
    return val if val in options else "Select..."

#Initialize session state for page
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# Temporary key to store navigation intent
if "nav" not in st.session_state:
    st.session_state["nav"] = None

# Home page navigation buttons
if st.session_state["page"] == "Home":
    col_logo, col_title = st.columns([1,6]) # Adjust ratio as needed
    with col_logo:
        st.image("static/RDH logo.jpg", width=200)
    with col_title:
        st.title("Deep Energy Retrofit Window Replacement Tool")
    st.write("Use the buttons below or the sidebar to navigate the tool. Once the Building Info, Assembly Info, and Retrofit Info has been filled in, data can be pulled from the appropriate energy model run to estimate the energy savings.")

    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        if st.button("Building Info", key="home_building_info"):
            st.session_state["nav"] = "Building Info"

    with col2:
        if st.button("Assembly Info", key="home_assembly_info"):
            st.session_state["nav"] = "Assembly Info"

    with col3:
        if st.button("Retrofit Info", key="home_retrofit_info"):
            st.session_state["nav"] = "Retrofit Info"


# Back to Home buttons
elif st.session_state["page"] in ["Building Info", "Assembly Info", "Retrofit Info"]:
    if st.button("Back to Home"):
        st.session_state["nav"] = "Home"

# Apply navigation
if st.session_state["nav"]:
    st.session_state["page"] = st.session_state["nav"]
    st.session_state["nav"] = None
    st.rerun()

# Sidebar navigation (now uses session state)
page = st.sidebar.radio(
    "Go to",
    ("Home", "Building Info", "Assembly Info", "Retrofit Info", "Summary"),
    key="page"
)

# Display content based on st.session_state["page"]
# Each content gets svaed into its own session state if it is not Select...

if st.session_state["page"] == "Building Info":
    st.title("Building Info")
    st.write("This is the Building Info page.")
    # Dropdowns for Building Info
    # Define options for each dropdown
    building_type_options = [
        "Select...",
        "Townhouses",
        "Up to 6 stories",
        "More than 6 stories"
    ]
    building_structure_options = [
        "Select...",
        "Townhouses",
        "up to 6 stories (low-mid rise)",
        "more than 6 stories"
    ]
    building_structure_options = [
        "Select...",
        "Concrete",
        "Wood Frame"
    ]
    heating_system_options = [
        "Select...",
        "Electric Baseboards",
        "Natural Gas Baseboards"
    ]
    dhw_system_options = [
        "Select...",
        "Electric",
        "Natural Gas"
    ]
    window_to_wall_ratio_options = [
        "Select...",
        "Low (<20%)",
        "Medium (20%<x<30%)",
        "High (>30%)"
    ]

    # Render selectboxes with value from session_state
    building_type = st.selectbox(
        "Building Type",
        building_type_options,
        index=building_type_options.index(get_dropdown_value("building_type", building_type_options)),
        key="building_type_selectbox"
    )
    if building_type != "Select...":
        st.session_state["building_type"] = building_type
    
    building_structure = st.selectbox(
        "Building Structure",
        building_structure_options,
        index=building_structure_options.index(get_dropdown_value("building_structure", building_structure_options)),
        key="building_structure_selectbox"
    )
    if building_structure != "Select...":
        st.session_state["building_structure"] = building_structure

    heating_system = st.selectbox(
        "Heating System",
        heating_system_options,
        index=heating_system_options.index(get_dropdown_value("heating_system", heating_system_options)),
        key="heating_system_selectbox"
    )
    if heating_system != "Select...":
        st.session_state["heating_system"] = heating_system

    dhw_system = st.selectbox(
        "DHW System",
        dhw_system_options,
        index=dhw_system_options.index(get_dropdown_value("dhw_system", dhw_system_options)),
        key="dhw_system_selectbox"
    )
    st.session_state["dhw_system"] = dhw_system

    window_to_wall_ratio = st.selectbox(
        "Window-to-Wall-Ratio",
        window_to_wall_ratio_options,
        index=window_to_wall_ratio_options.index(get_dropdown_value("window_to_wall_ratio", window_to_wall_ratio_options)),
    )
    st.session_state["window_to_wall_ratio"] = window_to_wall_ratio

elif st.session_state["page"] == "Assembly Info":
    st.title("Assembly Info")
    st.write("This is the Assembly Info page.")
    # Dropdowns for Assembly Info
    # Define options for each dropdown
    window_door_frame_options = [
        "Select...",
        "Aluminum (no thermal break)",
        "Aluminum (w/ thermal break)",
        "Fiberglass",
        "Vinyl"
    ]
    assembly_window_glazing_options = [
        "Select...",
        "Single Glazing",
        "Double (no low-e)",
        "Double (low-e)"
    ]
    thermal_bridging_options = ["Select...", "Low TB", "Average TB", "High TB"]
    airtightness_options = ["Select...", "Average", "Poor"]

    # Specific Logic for Walls
    # Get Building Structure selection from session state if available
    building_structure = st.session_state.get("building_structure", None)

    # Determine Walls dropdown label and options
    if building_structure == "Wood Frame":
        walls_label = "Walls (wood)"
        walls_options = ["Select...", "2x4 studs w/ batt", "2x6 studs w/ batt"]
    elif building_structure == "Concrete":
        walls_label = "Walls (concrete)"
        walls_options = ["Select...", "Interior stud wall w/ batt", "Continuous rigid insulation", "Uninsulated"]
    else:
        walls_label = "Walls"
        walls_options = ["Please select building structure first"]
    
    # Ensure the session stat value is always valid for the current options
    current_walls_value = st.session_state.get("assembly_walls", walls_options[0])
    if current_walls_value not in walls_options:
        if "Assembly_walls" in st.session_state:
            del st.session_state["assembly_walls"]
        current_walls_value = walls_options[0]

    # wall selectbox render
    walls = st.selectbox(
        walls_label,
        walls_options,
        index=walls_options.index(current_walls_value),
        key="assembly_walls_selectbox"
    )
    st.session_state["assembly_walls"] = walls

    # Render select boxes for each dropdown
    window_door_frame = st.selectbox(
        "Frame Type",
        window_door_frame_options,
        index=window_door_frame_options.index(get_dropdown_value("window_door_frame", window_door_frame_options)),
        key="window_door_frame_selectbox"
    )
    st.session_state["window_door_frame"] = window_door_frame

    window_glazing = st.selectbox(
        "Glazing",
        assembly_window_glazing_options,
        index=assembly_window_glazing_options.index(get_dropdown_value("window_glazing", assembly_window_glazing_options)),
    key="window_glazing_selectbox"
    )
    st.session_state["window_glazing"] = window_glazing

    # glazing cavity only appears for certain glazing types
    if window_glazing in ["Double (no low-e)", "Double (low-e)"]:
        glazing_cavity_options = ["Select...", "1/4", "1/8"]
        glazing_cavity = st.selectbox(
            "Glazing Cavity",
            glazing_cavity_options,
            index=glazing_cavity_options.index(get_dropdown_value("glazing_cavity", glazing_cavity_options)),
            key="glazing_cavity_selectbox"
        )
        st.session_state["glazing_cavity"] = glazing_cavity
    else:
        st.session_state["glazing_cavity"] = "none"

    thermal_bridging = st.selectbox(
            "Thermal Bridging Performance",
            thermal_bridging_options,
            index=thermal_bridging_options.index(get_dropdown_value("thermal_bridging", thermal_bridging_options)),
            key="thermal_bridging_selectbox"
        )
    st.session_state["thermal_bridging"] = thermal_bridging

    airtightness = st.selectbox(
        "Airtightness",
        airtightness_options,
        index=airtightness_options.index(get_dropdown_value("airtightness", airtightness_options)),
        key="airtightness_selectbox"
    )
    st.session_state["airtightness"] = airtightness


elif st.session_state["page"] == "Retrofit Info":
    st.title("Retrofit Info")
    st. write("This is the Retrofit Info page.")

    # Define options for each dropdown
    window_frame_options = [
        "Select...",
        "Aluminum",
        "Fiberglass",
        "Vinyl",
    ]
    window_glazing_options = [
        "Select...",
        "Double",
        "Triple, typical",
        "Triple, high performance"
    ]
    wall_exterior_insulation_options = [
        "Select...",
        "No ext. ins",
        "3 in. ext. ins",
        "5 in. ext. ins",
        "8 in. ext. ins"
    ]
    roof_upgrade_options = [
        "Select...",
        "None",
        "Improved"
    ]

    # Render each dropdown
    window_frame = st.selectbox(
        "Frame Type",
        window_frame_options,
        index=window_frame_options.index(get_dropdown_value("retrofit_window_frame", window_frame_options)),
        key="retrofit_window_frame_selectbox"
    )
    st.session_state["retrofit_window_frame"] = window_frame
    
    window_glazing = st.selectbox(
        "Glazing",
        window_glazing_options,
        index=window_glazing_options.index(get_dropdown_value("retrofit_window_glazing", window_glazing_options)),
        key="retrofit_window_glazing_selectbox"
    )
    st.session_state["retrofit_window_glazing"] = window_glazing

    wall_exterior_insulation = st.selectbox(
        "Wall Exterior Insulation",
        wall_exterior_insulation_options,
        index=wall_exterior_insulation_options.index(get_dropdown_value("retrofit_wall_exterior_insulation", wall_exterior_insulation_options)),
        key="retrofit_wall_exterior_insulation_selectbox"
    )
    st.session_state["retrofit_wall_exterior_insulation"] = wall_exterior_insulation

    roof_upgrade = st.selectbox(
        "Roof Upgrade",
        roof_upgrade_options,
        index=roof_upgrade_options.index(get_dropdown_value("retrofit_roof_upgrade", roof_upgrade_options)),
        key="retrofit_roof_upgrade_selectbox"
    )
    st.session_state["retrofit_roof_upgrade"] = roof_upgrade

elif st.session_state["page"] == "Summary":
    st.title("Summary of Selections")
    st.write("Below is a summary of all your selections. This is the data that will be entered into the calibrated energy model. When all fields are filled successfully, energy savings can be calculated.")

    import pandas as pd
    summary_data = [
        ["Building Type", st.session_state.get("building_type", "")],
        ["Building Structure", st.session_state.get("building_structure", "")],
        ["Heating System", st.session_state.get("heating_system", "")],
        ["DHW System", st.session_state.get("dhw_system", "")],
        ["Window-to-Wall-Ratio", st.session_state.get("window_to_wall_ratio", "")],
        ["Walls", st.session_state.get("assembly_walls", "")],
        ["Frame Type", st.session_state.get("window_door_frame", "")],
        ["Glazing", st.session_state.get("window_glazing", "")],
        ["Glazing Cavity", st.session_state.get("glazing_cavity", "")],
        ["Thermal Bridging Performance", st.session_state.get("thermal_bridging", "")],
        ["Airtightness", st.session_state.get("airtightness", "")],
        ["Retrofit Window Frame", st.session_state.get("retrofit_window_frame", "")],
        ["Retrofit Window Glazing", st.session_state.get("retrofit_window_glazing", "")],
        ["Wall Exterior Insulation", st.session_state.get("retrofit_wall_exterior_insulation", "")],
        ["Roof Upgrade", st.session_state.get("retrofit_roof_upgrade", "")],
    ]
    df = pd.DataFrame(summary_data, columns=["Dropdown Title", "Selection"])
    st.table(df)

    #List of required keys (including glazing cavity)
    required_keys = [
        "building_type",
        "building_structure",
        "heating_system",
        "dhw_system",
        "window_to_wall_ratio",
        "assembly_walls",
        "window_door_frame",
        "window_glazing",
        "glazing_cavity",
        "thermal_bridging",
        "airtightness",
        "retrofit_window_frame",
        "retrofit_window_glazing",
        "retrofit_wall_exterior_insulation",
        "retrofit_roof_upgrade",
    ]
    # check if all required fields are filled (not empty and not 'Select...' or 'Please select building structure first')
    all_filled = all(
        st.session_state.get(k, "").strip() not in ["", "Select...", "Please select building structure first"]
        for k in required_keys
    )

    # CSV export logic
    import io
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_data = csv_buffer.getvalue()

    st.download_button(
        label="Download CSV of Summary",
        data=csv_data,
        file_name="summary.csv",
        mime="text/csv",
        disabled=not all_filled
    )

# managing the energy model dataset
    from archetype_pick import select_building_output

    if st.button(
            label="Calculate Energy Savings",
            disabled=not all_filled
        ):
        user_input_archetype_dict = dict(summary_data[:5])
        st.write(user_input_archetype_dict)
        archetype = select_building_output(user_input_archetype_dict, 'building_combinations.csv')
        st.write(archetype)
        if archetype == 'not a feasible archetype':
            raise Exception('Program cannot continue without a feasible archetype')
        archetype_csv_path = 'Results/' + str(archetype) + '.csv'
        st.write(archetype_csv_path)
        user_input_dict = dict(summary_data)
        st.write(user_input_dict)

        from result_pick import previous_result_picker
        from result_pick import new_result_picker

        p_teui = previous_result_picker(user_input_dict, archetype_csv_path)[2]
        p_utility = previous_result_picker(user_input_dict, archetype_csv_path)[5]
        n_teui = new_result_picker(user_input_dict, archetype_csv_path)[2]
        n_utility = new_result_picker(user_input_dict, archetype_csv_path)[5]

        delta_teui = p_teui-n_teui
        delta_utility = p_utility-n_utility

        st.write(p_teui)
        st.write(n_teui)
        st.write(p_utility)
        st.write(n_utility)

        st.write('The Thermal Energy Usage Intensity will decrease by '+ str(delta_teui) + ' kWh/m\u00b2 per year')
        st.write('The Utility Cost will decrease by $' + str(delta_utility) + ' per year')




    # can debug here
    # st.write(st.session_state)
