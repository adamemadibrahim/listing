import requests

# URL of the webpage
url = "https://www.yellowpages.com.au/vic/shepparton/diverse-support-empowerment-1000002904806-listing.html"

try:
    # Send a GET request to the webpage
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Save the HTML content to a file
        with open("yellowpages_listing.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("HTML content saved to yellowpages_listing.html")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")
