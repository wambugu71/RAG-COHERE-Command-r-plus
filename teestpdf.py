import base64
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(layout="wide")
# Function to display the PDF
def show_pdf():
    file  = st.file_uploader("upload pdf", type=["pdf"])
    if  file != None:
    #with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(file.getvalue()).decode('utf-8')
        pdf_display = f"""
        <embed src="data:application/pdf;base64,{base64_pdf}#toolbar=0s" width="100%" height="1000px" type="application/pdf">
        """
        st.markdown(pdf_display,unsafe_allow_html=True)
    else:
        st.write("Upload to continue")

# Path to your PDF file
path = "example.pdf"
show_pdf()
