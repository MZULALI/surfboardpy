Surfline API Application

This application uses the Surfline API to retrieve wave, wind, and tide data for a specific beach and make recommendations on the surfboard and skill level based on the conditions.

Getting started

Clone or download the repository
Install the required dependencies: pip install -r requirements.txt
Obtain an API key from Surfline (instructions can be found on the Surfline API documentation)
Set the SURFLINE_API_KEY environment variable to your API key
Run the application: python app.py
The application will be available at http://localhost:5000 in your web browser
File structure

api: Contains the scripts that make API requests to Surfline to retrieve wave, wind, and tide data
data: Contains JSON files with sample data for different surf spots and surfboards
recommendations: Contains the script that makes recommendations on surfboards and skill levels based on the conditions
templates: Contains the HTML template for the application
app.py: The main script that runs the application
requirements.txt: Lists the required Python packages to run the application