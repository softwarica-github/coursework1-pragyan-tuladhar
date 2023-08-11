import requests
from urllib.parse import urlparse

print("\nWeb Enumeration Tool")
print("1. Enumerate Website")
print("2. Information Gathering")
print("3. Exit")
choice = input("Select an option (1-3): ")

if choice == "1":
    url = input("Enter the URL: ")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            response_text = response.text
            # Perform desired web enumeration tasks here
            print(response_text)
        else:
            print("Unable to retrieve data from the website.")
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))

elif choice == "2":
    url = input("Enter the URL: ")
    parsed_url = urlparse(url)
    print("Information Gathering:")
    print("Scheme:", parsed_url.scheme)
    print("Netloc:", parsed_url.netloc)
    print("Path:", parsed_url.path)
    print("Params:", parsed_url.params)
    print("Query:", parsed_url.query)
    print("Fragment:", parsed_url.fragment)

elif choice == "3":
    quit()

else:
    print("Invalid choice. Please try again.")




