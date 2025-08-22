# Window-Tool-Web-Dashboard
Aidan Mckibben's work for MKP and SB for a window tool for the existing buildings team to estimate energy savings of various window replacements.

Aidan's contact info is:
aidan.w.mck@gmail.com
aidan.mckibben@mail.mcgill.ca
778 628 0892

To host the website on Streamlit's cloud server, create a fork of the main branch onto your own github account, and link that to streamlit. Then just deploy the "app" in streamlit.
localhosting the dashboard should be very easy as well, but right now admin blocks all localhosting from RDH laptops.

frontend_dashboard.py runs the web application. Streamlit is a simple python library to learn, but the code will still be confusing to look at if you aren't familiar with the library.

arhetype_pick.py uses the "Building Info" inputs to choose one of the result csvs in the Results folder. The final energy savings will be pulled from this set of results.

lookup.py contains all of the classes which pull window codes, rvalues, etc from the _table.csv files. These values are then used by result_pick.py to sort the result data.
