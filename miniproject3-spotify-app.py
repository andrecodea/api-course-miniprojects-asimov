import os
from pprint import pprint
import sys
import streamlit as st
import dotenv
import requests
from requests.auth import HTTPBasicAuth

# Load environment variables from .env file
dotenv.load_dotenv(dotenv.find_dotenv())

# Spotify token endpoint URL
url = "https://accounts.spotify.com/api/token"

# Request body for client credentials flow
body = {
    'grant_type': 'client_credentials',
}


def authenticate():
    """
    Authenticates with Spotify API using client credentials flow.
    
    Retrieves client_id and client_secret from environment variables,
    encodes them using HTTPBasicAuth, and obtains an access token.
    
    Returns:
        str: Access token for Spotify API requests
        
    Raises:
        SystemExit: If authentication fails or token cannot be obtained
    """
    # Get Spotify credentials from environment variables
    client_id = os.environ['SPOTIFY_CLIENT_ID']
    client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
    
    # Create HTTP Basic Authentication object
    auth = HTTPBasicAuth(username=client_id, password=client_secret)
    
    # Make POST request to get access token
    response = requests.post(url=url, data=body, auth=auth)
    
    try:
        response.raise_for_status()  # Raise exception for HTTP errors
    except requests.HTTPError as e:
        print(f"Request error: {e}")
        token = None
    else:
        # Extract access token from response
        token = response.json()['access_token']
        print('Token obtained successfully!')
    
    # Exit application if token acquisition failed
    if not token:
        sys.exit()
    
    return token


def search_artist(artist_name, headers):
    """
    Searches for an artist by name using Spotify's search API.
    
    Args:
        artist_name (str): Name of the artist to search for
        headers (dict): HTTP headers containing authorization token
    
    Returns:
        dict or None: First artist result from search, None if no results found
    """
    # Spotify search API endpoint
    url = "https://api.spotify.com/v1/search"
    
    # Search parameters
    params = {
        'q': artist_name,    # Query string (artist name)
        'type': 'artist'     # Search type (artist only)
    }
    
    # Make GET request to search API
    response = requests.get(url, params=params, headers=headers)
    
    try:
        # Get first artist from search results
        first_result = response.json()['artists']['items'][0]
    except IndexError:
        # Return None if no artists found
        first_result = None
    
    return first_result


def get_top_tracks(artist_id, headers):
    """
    Retrieves the top tracks for a specific artist using their Spotify ID.
    
    Args:
        artist_id (str): Spotify ID of the artist
        headers (dict): HTTP headers containing authorization token
    
    Returns:
        list: List of top tracks for the artist
    """
    # Spotify top tracks API endpoint
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    
    # Make GET request to get top tracks
    response = requests.get(url, headers=headers)
    
    # Return tracks list from response
    return response.json()['tracks']


def main():
    """
    Main function that creates the Streamlit web interface for the Spotify app.
    Allows users to search for artists and displays their top tracks with popularity scores.
    """
    # App title and API documentation reference
    st.title('Spotify Web App')
    st.write('Spotify Web API data (https://developer.spotify.com/documentation/web-api)')
    
    # Authenticate and get access token
    token = authenticate()
    
    # Create authorization headers for API requests
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    # User input for artist search
    artist_name = st.text_input('Search for an artist:')
    
    # Stop execution if no artist name is provided
    if not artist_name:
        st.stop()
    
    # Search for artist using Spotify API
    artist = search_artist(artist_name=artist_name, headers=headers)
    
    # Handle case when no artist is found
    if not artist:
        st.warning(f'No artist found with the name {artist_name}.')
        st.stop()
    
    # Extract artist information
    artist_id = artist['id']                    # Spotify artist ID
    artist_name = artist['name']                # Official artist name
    artist_popularity = artist['popularity']     # Artist popularity score
    
    # Get top tracks for the artist
    top_tracks = get_top_tracks(artist_id=artist_id, headers=headers)
    
    # Display artist information header
    st.subheader(f'Artist: {artist_name} (popularity: {artist_popularity})')
    
    # Display each top track with popularity and Spotify link
    for track in top_tracks:
        track_name = track['name']                           # Track name
        track_popularity = track['popularity']               # Track popularity score
        track_link = track['external_urls']['spotify']      # Spotify track URL
        
        # Create markdown link for the track
        markdown_link = f'[{track_name}]({track_link})'
        
        # Display track information
        st.write(f"{markdown_link}, popularity: {track_popularity}")


if __name__ == "__main__":
    main()