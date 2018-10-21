Made for the 2018 Spaceapps hackathon Exploring Mars Challenge.

The code accesses the NASA Mars Rover API (https://data.nasa.gov/Space-Science/Mars-Rover-Photos-API/929k-jizu) to get and proccess information about the pictures and sends it to an image proccessing code.

The image proccessing uses Microsoft Azure Image proccessing open source code that has been edited for the use of this program. Origonal code from: https://github.com/Azure-Samples/cognitive-services-java-computer-vision-tutorial.git

The information about the tags of each picture is stored in a database which is then used to search pictures of Mars using key words that the image proccessing software produced.

The software can be run using the bash script found under: CloserThanMars/ComputerVision/src/runMarsPhotos.sh
To run the software you need a key from the NASA website. A key can be obtained from this website: https://api.nasa.gov/index.html#apply-for-an-api-key
Also needed is a key for the Image proccessing which can be found at:
Included with the for image proccessing will be a region.

The date should also be changed to specify the date of when the pictures were taken.
Change the appropriate data in the bash script to run the code.

Other than the code from Microsoft Azure, the code was written by: Emma Davis, Sam Dugan, Felix Lawson, Matthew Nielsen, Andrew Gamble, and Justin Drapeau.
