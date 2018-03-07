polar2sporstracker-sync
=

Python app and also macOS Launch Agent to import activites from Polar Flow to Sports Tracker


Getting Started
-

	$ pip install -r requirements.txt
	$ python prepare-agent.py -o com.synchronizer.plist
	$ mv com.synchronizer.plist ~/Library/LaunchAgents/
	$ launchctl load ~/Library/LaunchAgents/com.synchronizer.plist