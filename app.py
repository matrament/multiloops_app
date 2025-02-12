import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def convert_csv(path):
    df = pd.read_csv(path)
    return df.to_csv().encode("utf-8")


st.title('Multiloops 🧬')
st.divider()

path = 'data/comparison_lamiable2012_bpnet_new.csv'
df = pd.read_csv(path)


def highlight_value(val):
    if val == 'Mismatch':
        return 'background-color: red'

# Stosowanie formatowania do całej tabeli
styled_df = df.style.applymap(highlight_value)

# Wyświetlenie w Streamlit
st.dataframe(styled_df, use_container_width=True)

summary = pd.DataFrame({
    'Category': ['Match', 'Mismatch'],
    'Count': [df['Match'].eq('Match').sum(), df['Match'].eq('Mismatch').sum()]
})

st.bar_chart(summary.set_index("Category"))

st.dataframe(pd.read_csv('data/comparison_laing2009_fr3d.csv'), use_container_width=True)
st.header("Dataset sources", divider="violet")


st.info("""
**Source:**  
*Lamiable, A. (2012). Automated prediction of three-way junction topological families in RNA secondary structures.*  
DOI: [10.1016/j.compbiolchem.2011.11.001](https://doi.org/10.1016/j.compbiolchem.2011.11.001)
""")
col11, col12, = st.columns(2)

with col11:
    st.download_button(
        label="Download raw data",
        data= convert_csv('data/raw_dataset_lamiable2012.csv'),
        file_name="lamiable2012_raw.csv",
        mime="text/csv",
        key="lamiable2012_raw",
    )

with col12:
    st.download_button(
        label="Download processed data",
        data= convert_csv('data/lamiable2012.csv'),
        file_name="lamiable2012.csv",
        mime="text/csv",
        key="lamiable2012",
    )
st.divider()



st.info("""
**Source:**  
*Laing, C. (2012). Predicting coaxial helical stacking in RNA junctions.*  
DOI: [10.1093/nar/gkr629](https://doi.org/10.1093/nar/gkr629)
""")
col21, col22, = st.columns(2)

with col21:
    st.download_button(
        label="Download raw data",
        data=convert_csv('data/raw_dataset_laing2012.csv'),
        file_name="laing2012_raw.csv",
        mime="text/csv",
        key="laing2012_raw",
    )

with col22:
    st.download_button(
        label="Download processed data",
        data=convert_csv('data/laing2012.csv'),
        file_name="laing2012.csv",
        mime="text/csv",
        key="laing2012",
    )
st.divider()

st.info("""
**Source:**  
*Laing, C. (2009). Analysis of four-way junctions in RNA structures.*  
DOI: [10.1016/j.jmb.2009.04.084](https://doi.org/10.1016/j.jmb.2009.04.084)
""")


col31, col32, = st.columns(2)

with col31:
    st.download_button(
        label="Download raw data",
        data=convert_csv('data/raw_dataset_laing2009.csv'),
        file_name="laing2009.csv",
        mime="text/csv",
        key="laing2009_raw",
    )

with col32:
    st.download_button(
        label="Download processed data",
        data=convert_csv('data/laing2009.csv'),
        file_name="laing2009.csv",
        mime="text/csv",
        key="laing2009",
    )

# # Using object notation
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )