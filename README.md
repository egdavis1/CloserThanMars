# CloserThanMars
Made for the 2018 Spaceapps hackathon Exploring Mars Challenge.

The code accesses the NASA Mars Rover API (https://data.nasa.gov/Space-Science/Mars-Rover-Photos-API/929k-jizu) to get and proccess
information about the pictures and sends it to an image proccessing code.

The image proccessing uses Microsoft Azure Image proccessing open source code that has been edited for the use of this program.
Origonal code from: https://github.com/Azure-Samples/cognitive-services-java-computer-vision-tutorial.git

The information about the tags of each picture is stored in a database which is then used to search pictures of Mars using key words
that the image proccessing software produced.

