# Set Up
# Anaconda
# conda activate an appropriate location with python 8 
# conda activate py38_env_tb1 (The one I have set up for this.)
# cd to the directory of this folder
# streamlit run save_confirmation.py

# Imports
import streamlit as st
from pop_up import Modal
from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import udf, col
from snowflake.snowpark.types import Variant
from snowflake.snowpark import functions as fn
from snowflake.snowpark import version
import streamlit as st
import json
# from snowflake.snowpark.context import get_active_session
# from streamlit_modal import Modal

# Connection
credentials = json.loads(open("credentials.json").read())

session = Session.builder.configs(credentials).create()

print("connection established")

snowflake_table = session.table('SHARE_TEST_AUSTIN.TESTING.TEST').collect()

edited = st.data_editor(data=snowflake_table)

print(edited)

modal = Modal(key="Demo Key", title="Submission Verification")

open_modal = st.button(label="Submit Changes")
if open_modal:
    with modal.container():
        st.text("Are you sure you wish to submit changes?")
        def save_data():
            session.create_dataframe(edited).write.mode("overwrite").save_as_table("share_test_austin.testing.tEST",table_type="transient")
        col1, col2 = st.columns(2)
        col1.button("Okay",on_click=save_data)
        col2.button("Cancel")
            