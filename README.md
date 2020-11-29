# dronenet-plotter

Create an xy plot of Ingress portals to plan a dronenet flight. See how to get the furthest distance from start point.

This is a rough and ready Python exercise based on a question - How do I get the furthest from a start point with my dronenet drone in Ingress? The game is to hop from portal to portal and your distance is measured as the crow flies from the drone's point of origin. Ideally it's where you live but can be anywhere you recall the drone to and start a new set of hops. 

The big limitation is that the drone can only hop to the portals on your scanner which tends to be up to 500 (and a bit)m away from the drone's current location. The ultimate distance does depend on which S2 cells the scanner viewing area touches. (article here: https://pokemongohub.net/post/article/comprehensive-guide-s2-cells-pokemon-go/). 

We need to do several things:
- Get a load of portal latitudes and longitudes from your area of interest - pullback.py
- Clean up the file so it's proper json format. (like I said, rough and ready :-) e.g. portals.json
- Read in a file of these points & project them onto a flat surface. I use UTM - dronenetutm.py
- Matplotlib viewer then allows you to zoom in and examine your oute options in greater detail. 

To use this you'll need to know your own latitude and longitude plus the area coordinates you're interested in. 
Don't pullback a massive area with pullback.py - the webservice it calls only delivers 1000 portals which is why the script lops. Choose a smallish area. 
Be prepared to edit Python for this to work in your area. I can help if you have questions. 

Each dot has a radius of 250m which gives you the 500m scanner range. Adjust if you think you can jump further. If, on the plot, you have touching dots then you should be able to make the hop in Ingress. this way you can see routes of contiguous dots that will allow a long series of hops if that's your thing.  A nice enhancement would be to polt the home UTM and also town and cities to help orientate. 

If none of this makes sense then move along, there's nothing to see here. None of this is real life but it's a useful programming exercise that allowed me to use Matplotlib and mapping which I've been intending to do for a while.
