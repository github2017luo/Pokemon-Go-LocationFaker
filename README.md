# Pokemon Fake Location for iOS

## Browser as Location Controller:

Clone this project to your computer.

Open index.html and change the Google Maps Javascript API Key by generating one [here](https://developers.google.com/maps/documentation/javascript/get-api-key)

Open your index.html file in a browser and click where to change your loction too. 

## Execute Python Script for generating a .gpx location file:

Install CherryPy for the python script(executeToGenerateFile.py): 
[http://docs.cherrypy.org/en/latest/install.html#installing](http://docs.cherrypy.org/en/latest/install.html#installing)
This python program opens a cherrypy server on port 80 which recieves the new coordinates and creates a .gpx file

When you execute the script it should look like this
![Alt text](Assets/commandLinePythonExecutable.tiff?raw=true "command line image")

## Location Faker on iOS

Create a blank new Xcode project and add the .gpx file which was generated by the python script (when adding the file select reference and do not copy it)
![Alt text](Assets/addGpxFile.png?raw=true "add .gpx file")

Run the iOS App and click on the location button and select the .gpx file everytime you changed your location in the browser map view
![Alt text](Assets/locationChanger.png?raw=true "change location using .gpx file")
