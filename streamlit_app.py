import streamlit as st
import pandas as pd
import io

def main():
    st.title("File Upload and Download Application")

    # File upload
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "xlsx"])

    if uploaded_file is not None:
        # Read the file based on its type
        if uploaded_file.type == "text/csv":
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.type == "text/plain":
            df = pd.read_csv(uploaded_file, delimiter="\t")
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file type.")
            return

        st.write("Data Preview:")
        st.dataframe(df)

        # Process the data (for demonstration, we'll just return the same data)
        processed_data = df  # You can add your processing logic here

        # Convert DataFrame to CSV for download
        csv = processed_data.to_csv(index=False)
        st.download_button(
            label="Download Processed File",
            data=csv,
            file_name='processed_data.csv',
            mime='text/csv'
        )

if __name__ == "__main__":
    main()
