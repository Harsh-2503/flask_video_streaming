How To setup
pip install -r requirements.txt
python run.py

Api Documentation

/test
this endpoint has soceket connection (a connection is created for every user) and is responsible for calling the generate frames function which emit's frame in img format

/get-user
this endpoint is responsible to get user along with it's previous provided url and overlays

curl 'http://localhost:4999/get-user' \
 -H 'Accept: _/_' \
 -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
 -H 'Connection: keep-alive' \
 -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundary1MlNZXqGQ0A7mS40' \
 -H 'Origin: http://localhost:5173' \
 -H 'Referer: http://localhost:5173/' \
 -H 'Sec-Fetch-Dest: empty' \
 -H 'Sec-Fetch-Mode: cors' \
 -H 'Sec-Fetch-Site: same-site' \
 -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36' \
 -H 'sec-ch-ua: "Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"' \
 -H 'sec-ch-ua-mobile: ?0' \
 -H 'sec-ch-ua-platform: "macOS"' \
 --data-raw $'------WebKitFormBoundary1MlNZXqGQ0A7mS40\r\nContent-Disposition: form-data; name="user_name"\r\n\r\ntest3\r\n------WebKitFormBoundary1MlNZXqGQ0A7mS40--\r\n' \
 --compressed

/add-user
this endpoint is responsible to create user and user needs to provide a url as well

curl 'http://localhost:4999/add-user' \
 -H 'Accept: _/_' \
 -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
 -H 'Connection: keep-alive' \
 -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundarytRTInjf1LAtozygS' \
 -H 'Origin: http://localhost:5173' \
 -H 'Referer: http://localhost:5173/' \
 -H 'Sec-Fetch-Dest: empty' \
 -H 'Sec-Fetch-Mode: cors' \
 -H 'Sec-Fetch-Site: same-site' \
 -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36' \
 -H 'sec-ch-ua: "Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"' \
 -H 'sec-ch-ua-mobile: ?0' \
 -H 'sec-ch-ua-platform: "macOS"' \
 --data-raw $'------WebKitFormBoundarytRTInjf1LAtozygS\r\nContent-Disposition: form-data; name="user_name"\r\n\r\ntest4\r\n------WebKitFormBoundarytRTInjf1LAtozygS\r\nContent-Disposition: form-data; name="rtsp_url"\r\n\r\nrtsp://8.devline.ru:9784/cameras/6/streaming/sub?authorization=Basic%20YWRtaW46&audio=0\r\n------WebKitFormBoundarytRTInjf1LAtozygS--\r\n' \
 --compressed

/pause
this endpoint is used to pause the stream of the current users

curl 'http://127.0.0.1:4999/pause' \
 -H 'Accept: _/_' \
 -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
 -H 'Connection: keep-alive' \
 -H 'Content-Type: application/json' \
 -H 'Origin: http://localhost:5173' \
 -H 'Referer: http://localhost:5173/' \
 -H 'Sec-Fetch-Dest: empty' \
 -H 'Sec-Fetch-Mode: cors' \
 -H 'Sec-Fetch-Site: cross-site' \
 -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36' \
 -H 'sec-ch-ua: "Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"' \
 -H 'sec-ch-ua-mobile: ?0' \
 -H 'sec-ch-ua-platform: "macOS"' \
 --data-raw '{"sid":"eljdEgmtHmV2BPPdAAAF"}' \
 --compressed

/play
this endpoint is used to resume the stream of the current users

curl 'http://127.0.0.1:4999/play' \
 -H 'Accept: _/_' \
 -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
 -H 'Connection: keep-alive' \
 -H 'Content-Type: application/json' \
 -H 'Origin: http://localhost:5173' \
 -H 'Referer: http://localhost:5173/' \
 -H 'Sec-Fetch-Dest: empty' \
 -H 'Sec-Fetch-Mode: cors' \
 -H 'Sec-Fetch-Site: cross-site' \
 -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36' \
 -H 'sec-ch-ua: "Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"' \
 -H 'sec-ch-ua-mobile: ?0' \
 -H 'sec-ch-ua-platform: "macOS"' \
 --data-raw '{"sid":"eljdEgmtHmV2BPPdAAAF"}' \
 --compressed

/overlays
this endpoint is used to update, create, delete overlays

curl 'http://localhost:4999/overlays' \
 -X 'PUT' \
 -H 'Accept: _/_' \
 -H 'Accept-Language: en-GB,en-US;q=0.9,en;q=0.8' \
 -H 'Connection: keep-alive' \
 -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryWqB3fWTGORTqcahY' \
 -H 'Origin: http://localhost:5173' \
 -H 'Referer: http://localhost:5173/' \
 -H 'Sec-Fetch-Dest: empty' \
 -H 'Sec-Fetch-Mode: cors' \
 -H 'Sec-Fetch-Site: same-site' \
 -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36' \
 -H 'sec-ch-ua: "Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"' \
 -H 'sec-ch-ua-mobile: ?0' \
 -H 'sec-ch-ua-platform: "macOS"' \
 --data-raw $'------WebKitFormBoundaryWqB3fWTGORTqcahY\r\nContent-Disposition: form-data; name="user_name"\r\n\r\ntest4\r\n------WebKitFormBoundaryWqB3fWTGORTqcahY\r\nContent-Disposition: form-data; name="overlays"\r\n\r\n{"type":"text","content":"dsfasdf","dragX":101,"dragY":37,"resizeW":100,"resizeH":100}\r\n------WebKitFormBoundaryWqB3fWTGORTqcahY--\r\n' \
 --compressed

The current solution is not the best one I admit it but due to laptop's batter faliure I was already late on the submission of the assignment so, I just got this build up ASAP,

ideally the overlays should have a seperate collection in Monogodb with user unique id's foreign keys and the project should be more structured as well

Even the frontend is not fully optimized, with best react principles and proper typescript usage.
