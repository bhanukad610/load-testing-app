# Load Testing application
A simple app to test the load for https://www.bbc.com with H2O wave framework and Locust.
#### H2O wave
<img src="https://www.h2o.ai/wp-content/uploads/2020/12/wave-type-yellow-1024x410.png" width="300">
H2O Wave is a software stack for building beautiful, low-latency, real-time, browser-based applications and dashboards entirely in Python without using HTML, Javascript, or CSS

#### Locust
<img src="https://github.com/bhanukad610/load-testing-app/blob/main/images/locust.jpeg" width="300">
Locust is an open source, easy to use, scriptable and scalable performance testing tool.

### Quickstart
#### Pre requesists : 
- You need to have Python 3.6+ in your Linux, macOS, and Windows in order to install H2O wave.
- Need git installed.

#### Steps : 
##### H2O wave installation and start the wave server
1. Download and extract the H2O Wave SDK for your platform using -
https://github.com/h2oai/wave/releases/tag/v0.19.0 
2. Move it to a convenient location. ($HOME/wave/)
3. Go to your Wave directory and open a new terminal. Start the wave server using,
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
#### Home page of the application as follows. You can press Start button to proceed to the load testing.
<img src="https://github.com/bhanukad610/load-testing-app/blob/main/images/home.png" width="600">

#### Then you will get the below page asking inputs.
1. Number of users: number of users you need Locust to simulate
2. Spawn rate:  speed at which users are created in the beginning until the specified number of concurrent users are created
3. Host: host to load test(it will be filled as 'https://www.bbc.com' for you)
<img src="https://github.com/bhanukad610/load-testing-app/blob/main/images/start%20new%20load%20test.png" width="600">

#### Then you proceed to the Locust dashboard. It has the following tabs.
1. Statistics
- This shows real-time statistics on how the server responds to the requests sent by Locust. For this 3 endpoints have been used and defined in the src/locust.py.
<img src="https://github.com/bhanukad610/load-testing-app/blob/main/images/statistics.png" width="600">

2. Charts
- This shows the charts about total requests per second, response time and the number of users with time.
<img src="https://github.com/bhanukad610/load-testing-app/blob/main/images/charts_1.png" width="600">

<img src="https://github.com/bhanukad610/load-testing-app/blob/main/images/charts_2.png" width="600">

3. Failures
- If any request got failed due to a connection error, timeout, page not found, bad request or similar reason, it will be displayed in this tab.
<img src="https://github.com/bhanukad610/load-testing-app/blob/main/images/failiures.png" width="600">

4. Exceptions
- If the code generates Exceptions, it is recorded in the Exceptions tab during execution.
<img src="https://github.com/bhanukad610/load-testing-app/blob/main/images/Exeptions.png" width="600">

5. Tasks
- Displays the tasks defined in the locustfile.
<img src="https://github.com/bhanukad610/load-testing-app/blob/main/images/tasks.png" width="600">

5. Download Data
- After finishing the test, we can download the data of statistics, failures and exceptions as CSV files and a report displayed in the web interface.
<img src="https://github.com/bhanukad610/load-testing-app/blob/main/images/downloads.png" width="600">
