import streamlit as st

from oh_oui_try_me.lib import try_me

quote = try_me()

f"{quote}"

st.button(next, on_click=st.experimental_rerun())
