# import streamlit as st


# # Page title
# st.title("Prompt Designer 🤖😉")

# # Input 1
# assistant_id = st.text_input("Assistant ID", placeholder="assistant_id...")

# # Input 2
# thread_id = st.text_input("Thread ID", placeholder="thread_id...")

# service_base = "https://e2b6-2a02-810d-243f-efe0-e52f-ac3c-36c3-91bb.ngrok-free.app"
# endpoint_base = "/syntea-assistant/GCD-assistant/"

# user_msg_parameter = "?user_msg=${user_msg}"

# api_endpoint = service_base + endpoint_base + user_msg_parameter 

# # https://e2b6-2a02-810d-243f-efe0-e52f-ac3c-36c3-91bb.ngrok-free.app/syntea-assistant/GCD-assistant/?user_msg=${user_msg}&thread_id=thread_BesfaGurO4jLKYqV8JMMKumN&assistant_id=asst_MhZHTSuMbugY6L2aRYziTCEA

# # Create a button to submit the form
# if st.button("Submit"):

#     try:
#         api(name, description, prompt, author, str(datetime.now()))
#         st.success("Promt saved successfully!")
        
#     except requests.exceptions.RequestException as e:
#         st.error(f"Error: {e}")



import streamlit as st

def main():
    st.title("Assistant - Plugin Designer 🤖😉")

    service_base = "https://e2b6-2a02-810d-243f-efe0-e52f-ac3c-36c3-91bb.ngrok-free.app"
    endpoint_base = "/syntea-assistant/GCD-assistant/"
    
    user_msg_parameter = "?user_msg=${user_msg}"

    api_endpoint = service_base + endpoint_base + user_msg_parameter

    # Two optional text inputs
    assistant_id = st.text_input("Assistant ID (Optional):", placeholder="assistant_id")
    thread_id = st.text_input("Thread ID (Optional):", placeholder="thread_id")

    # Button to trigger the update
    if st.button("Get API URL"):
        if assistant_id:
            api_endpoint += f"&assistant_id={assistant_id}"

        if thread_id:
            api_endpoint += f"&thread_id={thread_id}"

        # Display the updated text
        st.write(api_endpoint)
        

if __name__ == "__main__":
    main()


