# Load Testing application
A simple app to test the load for https://www.bbc.com with H2O wave framework and Locust. 

### Quick start
#### Pre requesists : 
- You need to have Python 3.6+ in your Linux, macOS, and Windows in order to install H2O wave.
- Need git installed.

#### Steps : 
##### H2O wave installation and start the wave server
1. Download and extract the H2O Wave SDK for your platform using -
https://github.com/h2oai/wave/releases/tag/v0.19.0 
2. Move it to a convenient location. ($HOME/wave/)
3. Go to your Wave directory and start the wave server using,
  ```
./waved
```
##### Setup the application
1. Open a new terminal and create a directory for wave applications. ($HOME/wave-apps/)
  ```
mkdir $HOME/wave-apps
cd $HOME/wave-apps
```
2. Clone the repository and go inside the folder.
  ```
git clone https://github.com/bhanukad610/load-testing-app
cd load-testing-app
```
2. Set up a virtual environment
  ```
python3 -m venv venv
source venv/bin/activate
```
3. Install the dependencies
  ```
pip install -r dependencies/requirements.txt
```
4. Start the Load testing wave application
  ```
wave run src/test_app.py
```
5. Open a new terminal in the same directory and start the locust server.
  ```
./startLocust.sh
```
6. Go to http://localhost:10101/app to access the application.

### User Manual to the application
- Home page of the application as follows. You can press Start button to proceed to the load testing.
![alt text](https://github.com/bhanukad610/Sinhala-Song-Lyrics-Search-Engine/blob/master/Flask_app/IR%20-%20Rules.png?raw=true)
- 