import requests
import json

class GetDogImages:

    def get_dog_images(self):
        URL = "https://dog.ceo/api/breeds/image/random"
        response = requests.get(URL)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.json()}")
            return None

    def extract_breed(self, image_data):
        # Assuming the API returns a dictionary with a "message" key containing the image URL
        image_url = image_data.get("message", "N/A")

        # Extract the breed from the image URL (assuming it follows the format)
        breed = image_url.split("/")[-2]
        return breed.capitalize()  # Capitalize the breed name

# Create an instance of GetDogImages
dog_images_instance = GetDogImages()

# Call the get_dog_images method
dog_image_data = dog_images_instance.get_dog_images()

# Check if the request was successful before proceeding
if dog_image_data:
    # Extract and print the breed
    breed = dog_images_instance.extract_breed(dog_image_data)
    print(f"Breed: {breed}")
else:
    print("Unable to fetch dog image data.")
