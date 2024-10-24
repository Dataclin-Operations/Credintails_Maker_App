import re
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from streamlit_authenticator.utilities.hasher import Hasher


# with open('../config.yaml', 'r', encoding='utf-8') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# # Creating the authenticator object
# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['pre-authorized']
# )

# hashed_passwords = Hasher(['Menna@404', 'Yasmin@992', 'Abeer@450', 'Hamza@628','Mohamed@128' ]).generate()
# st.write(hashed_passwords)





if __name__ == "__main__":
    with st.form("Make Credintails"):
        name = st.text_input("Enter Your Name", key="name")
        username = st.text_input("Enter Your User Name", key = "username")
        email = st.text_input("Enter Your User Email", key="email")
        password = st.text_input("Enter Your User password", key="passwrd")

        if st.form_submit_button("Submit"):
            if (
                not name or
                not username or
                not password or
                not email
            ):
                st.error("Please fill all cells then press submint button")
            else:
                hashed_passwords = Hasher([password]).generate()[0]
                valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
                if not valid:
                    st.error("Please Enter a vaild Email")
                else:
                    st.write(f"""{name} = {{ email = {email}, name = {name} , password = {hashed_passwords} }} """)


# Mohamed = {email = "muhammetgamal5@gmail.com", name = "Mohamed", password = "$2b$12$xemUqIn9R6N1Dczt00LPv.Z3nmEmTezqJqUND5Rvrpxs9UHrTaWxC"}
