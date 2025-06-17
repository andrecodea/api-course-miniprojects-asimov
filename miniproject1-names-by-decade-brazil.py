import requests
import pandas as pd
import streamlit as st
from pprint import pprint  # Pretty print for debugging


def make_request(uri, params=None):
    """
    Makes an HTTP GET request to the specified URI with optional parameters.
    
    Args:
        uri (str): The URI to make the request to
        params (dict, optional): Query parameters for the request
    
    Returns:
        dict or None: JSON response data if successful, None if error occurs
    """
    response = requests.get(uri, params=params)
    try:
        response.raise_for_status()  # Raises HTTPError for bad responses
    except requests.HTTPError as e:
        print(f"Request error --> {e}")
        result = None
    else:
        result = response.json()  # Parse JSON response
    return result


def get_name_by_decade(name):
    """
    Retrieves name frequency data by decade from IBGE (Brazilian Institute of Geography and Statistics).
    
    Args:
        name (str): The name to search for in the IBGE database
    
    Returns:
        dict: Dictionary with decades as keys and frequency counts as values
              Empty dictionary if no data found or error occurs
    """
    # IBGE API endpoint for name statistics
    uri = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}"
    
    # Make API request to get name data
    decade_data = make_request(uri=uri)
    
    # Initialize dictionary to store decade frequency data
    decade_dict = {}
    
    # Return empty dict if no data received
    if not decade_data:
        return {}
    
    # Process each decade's data from the API response
    for data in decade_data[0]['res']:
        decade = data['periodo']      # Time period (decade)
        frequency = data['frequencia'] # Frequency count for that decade
        decade_dict[decade] = frequency
    
    return decade_dict


def main():
    """
    Main function that creates the Streamlit web interface for the names by decade app.
    Displays name frequency data in both tabular and chart format.
    """
    # App title and data source information
    st.title('Names by Decade in Brazil Web App')
    st.write('IBGE data (source: https://servicodados.ibge.gov.br/api/docs/nomes?versao=2)')
    
    # User input for name search
    name = st.text_input('Search for a name:')
    
    # Stop execution if no name is provided
    if not name:
        st.stop()
    
    # Get decade frequency data for the specified name
    decade_dict = get_name_by_decade(name)
    
    # Handle case when no data is found
    if not decade_dict:
        st.warning(f'No data found for the name {name}')
        st.stop()
    
    # Convert dictionary to pandas DataFrame for display and visualization
    # orient='index' uses dictionary keys as DataFrame index
    df = pd.DataFrame.from_dict(decade_dict, orient='index')
    
    # Create two columns with different widths (30% and 70%)
    col1, col2 = st.columns([0.3, 0.7])
    
    # Left column: Display frequency data table
    with col1:
        st.write('Frequency by decade')
        st.dataframe(df)  # Interactive data table
    
    # Right column: Display line chart showing evolution over time
    with col2:
        st.write('Evolution over time')
        st.line_chart(df)  # Line chart visualization


if __name__ == '__main__':
    main()