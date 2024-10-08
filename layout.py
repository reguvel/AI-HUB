import streamlit as st
from streamlit_option_menu import option_menu

def sidebar_layout():
    with st.sidebar:
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:  
            st.sidebar.image('assets/AI_HUB.svg')
        
        st.sidebar.markdown(
            """
            <div>
                <hr>
                <p style='margin: 0;'>Open for <a style="color:red" href='https://github.com/adityasatuluri/AI-HUB' target='_blank'>Contributions</a></p>
                <p style='margin: 0; color:#919191'>Developed by <a style="color:#b82f23" href='https://github.com/adityasatuluri' target='_blank'>Aditya Satuluri</a> and <a style="color:#b82f23" href='https://github.com/reguvel' target='_blank'>Reguvel Gnanavelu</a></p>
            </div>
            """,
            unsafe_allow_html=True
        )
