# pointwisepy

Python library for the Pointwise Glyph API. Not fully tested or documented yet.

To download:

	python -m pip install --upgrade pointwisepy

To run in batch mode, add following path to environment variables (System Properties > Advanced > Environment Variables > User Variables > Path > Edit > New)
	
 	"C:\Program Files\Cadence\PointwiseV18.6R3\win64\bin" (check correct location/version)
	
To test batch mode, in command line/powershell: 
	
	python
	
 	from pointwisepy import *

	pw,glf = connectPort(0)

To connect to open GUI instance via command line/powershell: 

in Pointwise GUI: 
	
 	Script > Glyph Server > Active & port=2807
	
 	end journalling

 	close any open function panels

in cmd line/.py file:

	python
	
 	from pointwisepy import *

	pw,glf = connectPort(2807)
	
To run example, download Examples folder and run:

	python ./Downloads/Examples/01_example.py

http://www.pointwise.com/glyph2/ - Glyph documentation, lists all functions and options

https://github.com/pointwise/GlyphClientPython - API source code
