"""
CS230:      Section HB1
Name:       Evan DiMambro
Data:       McDonald's Locations - mcdonalds_clean1.csv
Description:
This program begins by showing the user a table of all the McDonald's locations provided. It then shows
a map of every location below this. After that, the user can select from the dropdown menu what region
they want to see McDonald's locations for, and tables will show up with the result. Additionally, the
locations will be divided by division within each region (like New England within Northeast).
Finally, a bar graph is shown to visualize how many of each type of store there is (freestanding, etc).

I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student.
URL: Link to your web application online (see extra credit)
"""
import pandas as pd
import streamlit as st

McDonaldsCLEANFILE = "mcdonalds_clean1.csv"
st.title("Evan DiMambro's Final Project")

dfStores = pd.read_csv(McDonaldsCLEANFILE)
dfStores.columns=['lon', 'lat', 'storeNumber', 'storeType', 'address', 'city', 'state', 'zip', 'phone', 'playplace', 'driveThru', 'archCard', 'freeWifi', 'storeUrl']
FILTERS = ('storeType', 'address', 'city', 'state', 'zip', 'phone', 'driveThru', 'storeUrl', 'lon', 'lat')
dfStores = dfStores.filter(FILTERS)

#Drop-down menu on the side to organize data better
add_selectbox = st.sidebar.selectbox(
    "Select what page to navigate to.",
    ("Home", "All Locations", "Map", "Locations by Region", "Graphs")
)

def homePage():
    st.header("Welcome to my project!\n"
              "Please select a page to view from the side menu.")
    from PIL import Image
    logo = Image.open('mcdonaldslogo.png')
    st.image(logo)

def allLocations():
    st.header("All McDonald's Locations")
    print(dfStores)
    st.write(dfStores)
    st.write("This is a table of every McDonald's location from the dataset. You can also sort by whichever "
             "category you prefer.")

def mapLocations():
    st.header("Map of Locations")
    st.map(dfStores)
    st.write("Here's a map of all the locations.")

def graphStores():
    st.header("Bar Graph of Store Types")
    dfStoreChart = dfStores['storeType'].value_counts()
    print(dfStoreChart)
    st.bar_chart(dfStoreChart)
    st.write("For this visualization, I wanted to show how many of each store type there is. "
             "Unsurprisingly, the most common is freestanding, but I think it's interesting to "
             "see that there are other ones as well that people may not think of!")

    st.header("Line Graph of Locations")
    dfStoreLine = dfStores['state'].value_counts()
    print(dfStoreLine)
    st.line_chart(dfStoreLine)
    st.write("Here is a line graph of the locations by state to show which states have a larger amount "
             "of McDonald's locations.")

def northeastOption():
    #Also will distinct by division within regions using subheaders
    st.subheader("New England states:")
    ct = dfStores[(dfStores.state == 'CT')]
    me = dfStores[(dfStores.state == 'ME')]
    mass = dfStores[(dfStores.state == 'MA')]
    nh = dfStores[(dfStores.state == 'NH')]
    ri = dfStores[(dfStores.state == 'RI')]
    vt = dfStores[(dfStores.state == 'VT')]
    st.write(ct)
    st.write(me)
    st.write(mass)
    st.write(nh)
    st.write(ri)
    st.write(vt)

    st.subheader("Mid-Atlantic states:")
    nj = dfStores[(dfStores.state == 'NJ')]
    ny = dfStores[(dfStores.state == 'NY')]
    pa = dfStores[(dfStores.state == 'PA')]
    st.write(nj)
    st.write(ny)
    st.write(pa)

def midwestOption():
    st.subheader("East North Central states:")
    il = dfStores[(dfStores.state == 'IL')]
    indiana = dfStores[(dfStores.state == 'IN')]
    mi = dfStores[(dfStores.state == 'MI')]
    oh = dfStores[(dfStores.state == 'OH')]
    wi = dfStores[(dfStores.state == 'WI')]
    st.write(il)
    st.write(indiana)
    st.write(mi)
    st.write(oh)
    st.write(wi)

    st.subheader("West North Central states:")
    ia = dfStores[(dfStores.state == 'IA')]
    ks = dfStores[(dfStores.state == 'KS')]
    mn = dfStores[(dfStores.state == 'MN')]
    mo = dfStores[(dfStores.state == 'MO')]
    ne = dfStores[(dfStores.state == 'NE')]
    nd = dfStores[(dfStores.state == 'ND')]
    sd = dfStores[(dfStores.state == 'SD')]
    st.write(ia)
    st.write(ks)
    st.write(mn)
    st.write(mo)
    st.write(ne)
    st.write(nd)
    st.write(sd)

def southOption():
    st.subheader("South Atlantic states:")
    de = dfStores[(dfStores.state == 'DE')]
    fl = dfStores[(dfStores.state == 'FL')]
    ga = dfStores[(dfStores.state == 'GA')]
    md = dfStores[(dfStores.state == 'MD')]
    nc = dfStores[(dfStores.state == 'NC')]
    sc = dfStores[(dfStores.state == 'SC')]
    va = dfStores[(dfStores.state == 'VA')]
    dc = dfStores[(dfStores.state == 'DC')]
    wv = dfStores[(dfStores.state == 'WV')]
    st.write(de)
    st.write(fl)
    st.write(ga)
    st.write(md)
    st.write(nc)
    st.write(sc)
    st.write(va)
    st.write(dc)
    st.write(wv)

    st.subheader("East South Central states:")
    al = dfStores[(dfStores.state == 'AL')]
    ky = dfStores[(dfStores.state == 'KY')]
    ms = dfStores[(dfStores.state == 'MS')]
    tn = dfStores[(dfStores.state == 'TN')]
    st.write(al)
    st.write(ky)
    st.write(ms)
    st.write(tn)

    st.subheader("West South Central states:")
    ar = dfStores[(dfStores.state == 'AR')]
    la = dfStores[(dfStores.state == 'LA')]
    ok = dfStores[(dfStores.state == 'OK')]
    tx = dfStores[(dfStores.state == 'TX')]
    st.write(ar)
    st.write(la)
    st.write(ok)
    st.write(tx)

def westOption():
    st.subheader("Mountain states:")
    az = dfStores[(dfStores.state == 'AZ')]
    co = dfStores[(dfStores.state == 'CO')]
    id = dfStores[(dfStores.state == 'ID')]
    mt = dfStores[(dfStores.state == 'MT')]
    nv = dfStores[(dfStores.state == 'NV')]
    nm = dfStores[(dfStores.state == 'NM')]
    ut = dfStores[(dfStores.state == 'UT')]
    wy = dfStores[(dfStores.state == 'WY')]
    st.write(az)
    st.write(co)
    st.write(id)
    st.write(mt)
    st.write(nv)
    st.write(nm)
    st.write(ut)
    st.write(wy)

    st.subheader("Pacific states:")
    ak = dfStores[(dfStores.state == 'AK')]
    ca = dfStores[(dfStores.state == 'CA')]
    hi = dfStores[(dfStores.state == 'HI')]
    oreg = dfStores[(dfStores.state == 'OR')]
    wa = dfStores[(dfStores.state == 'WA')]
    st.write(ak)
    st.write(ca)
    st.write(hi)
    st.write(oreg)
    st.write(wa)

if add_selectbox == "Home":
    homePage()

if add_selectbox == "All Locations":
    allLocations()

if add_selectbox == "Map":
    mapLocations()

if add_selectbox == "Locations by Region":
    st.header("Locations by Region")
    option = st.selectbox(
        "Please pick a region to display locations for.",
        ('Northeast', 'Midwest', 'South', 'West'))
    if option == 'Northeast':
        northeastOption()
    if option == 'Midwest':
        midwestOption()
    if option == 'South':
        southOption()
    if option == 'West':
        westOption()

if add_selectbox == "Graphs":
    graphStores()


