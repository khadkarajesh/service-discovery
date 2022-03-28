### How to Run Application

1. [Install Requirements](#install-requirements)
2. [Setup Redis](#setup-redis)
3. [Run Application](#run-application)

#### Install Requirements

```shell
   pip install -r requirements.txt
   ```

#### Setup Redis

1. Install Redis in Mac
```shell
brew install redis
```
2. Start Redis Service
```shell
brew services start redis
```
3. Start Redis Service
```shell
redis-server
```
4. Redis Worker
Start redis worker from project directory as:
```shell
rq worker --with-scheduler
```

#### Run Application
```shell
python app.py
```

### Monitor Background Task
[Redis Dashboard](http://127.0.0.1:5000/rq)

### Service Discovery
#### Find Available Network
```
Request
-------------------------------
Method: GET
URL: /discover?q=Vitry-sur-Seine

Response, 200
-------------------------------
{
	"SFR": {
		"2G": false,
		"3G": true,
		"4G": true
	},
	"Orange": {
		"2G": true,
		"3G": true,
		"4G": true
	},
	"Free mobile": {
		"2G": false,
		"3G": true,
		"4G": true
	},
	"Bouygues Telecom": {
		"2G": true,
		"3G": false,
		"4G": false
	}
}
```

### Background Job
This background jobs extracts data and generates necessary files to discover the available networks on respective location.
Redis worker must run before starting this job. 

```
Request
-------------------------------
Method: GET
URL: /extract

Response, 200
-------------------------------
{
	"message": "job initiated to fetch city for networks"
}
```



