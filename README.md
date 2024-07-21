# USB2VFD-Deck
A desktop notification panel based on the AIDA64 compatible 40x2 USB2VFD serial display.

Special thanks to [Upir on YouTube](https://youtu.be/g7SOxzKatCc) who made me aware of this display and who's reverse engineering of the protocol this display uses.

## Bill of Materials
- 1x USB2VFD 40x20 Display. This USB serial display can be found from various sellers on ebay and AliExpress. I purchased mine from [this seller](https://www.ebay.ca/itm/165920311390).
- 4x 2cm M3 screws
- Roughly 150 Grams of 3d printer filiment. (if you plan to print an enclosure)
- 1x Arduino Nano
- 1x USB Hub Adapter
- 5x Momentary buttons with LEDs

## Instructions
1. Copy the .env-example file and rename the copy to .env this file will contain all the settings. 
2. The most important setting to getting this working is the *COMPORT_NUMBER*. You can get this by checking device manager provided you are on  and looking for the device marked *USB-SERIAL CH340*.
3. Set your WEATHER_LATITUDE and WEATHER_LONGITUDE to get your weather local weather. This uses weather data from Environment Canada so you may need to reimpliment the function *get_current_weather* in weather.py to use a different weather service for accurate weather in your country.
4. Set your RSS_URL and RSS_POST_COUNT to see posts from your news source / blog of choice .

## WIP
Currently only the code to display data on the display is working.