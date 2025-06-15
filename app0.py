import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Function to run query and return DataFrame
def query_to_dataframe(query, db_url):
    try:
        engine = create_engine(db_url)
        df = pd.read_sql_query(query, con=engine)
        return df
    except Exception as e:
        st.error(f"Error executing query: {e}")
        return pd.DataFrame()

# Streamlit UI
st.title("Hello, world!")
st.write("This app connects to a PostgreSQL database and fetches some data.")

# Run query on button click
if st.button("Run Query"):
    # Read secrets
    DBU = st.secrets["DBU"]
    DBP = st.secrets["DBP"]

    # Construct DB URL
    db_url = f"postgresql://{DBU}:{DBP}"

    # Query
    query = "SELECT * FROM table_0 LIMIT 100;"

    # Run and show result
    df = query_to_dataframe(query, db_url)
    st.write(f"Returned {len(df)} rows.")
    st.dataframe(df)

