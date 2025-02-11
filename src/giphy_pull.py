import requests
import os
import sys
from urllib.parse import urlencode

class GiphyDownloader:
    def __init__(self, api_key):
        """Initialize with your Giphy API key."""
        self.api_key = api_key
        self.base_url = "https://api.giphy.com/v1/gifs"
        
    def search_gifs(self, query, limit=5):
        """
        Search for GIFs using a query string.
        
        Args:
            query (str): Search term
            limit (int): Maximum number of results to return
            
        Returns:
            list: List of GIF data dictionaries
        """
        params = {
            'api_key': self.api_key,
            'q': query,
            'limit': limit
        }
        
        url = f"{self.base_url}/search?{urlencode(params)}"
        response = requests.get(url)
        response.raise_for_status()
        
        return response.json()['data']
    
    def download_gif(self, gif_id, save_path):
        """
        Download a specific GIF by ID.
        
        Args:
            gif_id (str): Giphy GIF ID
            save_path (str): Path where the GIF should be saved
        """
        # Get GIF details
        params = {
            'api_key': self.api_key
        }
        url = f"{self.base_url}/{gif_id}?{urlencode(params)}"
        response = requests.get(url)
        response.raise_for_status()
        
        # Get download URL
        gif_url = response.json()['data']['images']['original']['url']
        
        # Download the GIF
        gif_response = requests.get(gif_url)
        gif_response.raise_for_status()
        
        # Save the GIF
        with open(save_path, 'wb') as f:
            f.write(gif_response.content)

# Example usage
def main():

    # Replace with your actual API key
    api_key = open("giphy_api_key.txt").readline().strip()
    print(api_key)
    downloader = GiphyDownloader(api_key)
    
    # Create downloads directory if it doesn't exist
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    # Search for GIFs
    search_term = "cats"
    results = downloader.search_gifs(search_term, limit=3)
    
    # Download each GIF
    for i, gif in enumerate(results):
        gif_id = gif['id']
        save_path = f"downloads/gif_{i}.gif"
        print(f"Downloading GIF {i+1}...")
        downloader.download_gif(gif_id, save_path)
        print(f"Saved to {save_path}")

if __name__ == "__main__":
    main()