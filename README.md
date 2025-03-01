# MorningToMe
An autmation script I created aimed to remove the need to look at different applications. Currently, this script grabs the latest news and weather for your current set location.
## Installation
To use, clone the repository. Navigate to install folder:
### Create a python virtual environment. 
``` python
python3 -m venv venv
```
### Activate the venv
#### Windows
``` shell
venv/Scripts/activate
```
#### MacOS
``` shell
source venv/bin/activate
```

After cloning, create a <code>.env</code> file and put in the information required by the API's. <br>
You will need to create API keys for:
<ul>
<li>OpenWeather</li>
<li>NewsAPIv2</li>
<li>OpenCage API</li>

After obtaining the API keys, make sure to put them in your <code>.env</code> file.

Execute within IDE.
I still need to work on the automation part, the idea is to run the script on a raspberry pi or similar.                             
