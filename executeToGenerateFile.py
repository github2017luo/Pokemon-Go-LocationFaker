import xml.etree.cElementTree as ET
import urllib2
import json
import sys
import cherrypy

lastLat = ""
lastLng = ""

class Pokemon:
    @cherrypy.expose
    def generateXML(self, lat=0.0, lng=0.0):
        global lastLat, lastLng
        lastLat = lat
        lastLng = lng
        gpx = ET.Element("gpx", version="1.1", creator="Xcode")
        wpt = ET.SubElement(gpx, "wpt", lat=lastLat, lon=lastLng)
        ET.SubElement(wpt, "name").text = "PokemonLocation"
        ET.ElementTree(gpx).write("pokemonLocation.gpx")
        print "Location Updated!", "latitude:", lastLat, "longitude:" ,lastLng
        return "succes"

if __name__ == '__main__':
    cherrypy.server.socket_host = "0.0.0.0"
    cherrypy.server.socket_port = 80
    cherrypy.quickstart(Pokemon(), '/')
