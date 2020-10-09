# Video-streamer
Simple video streamer from Raspberry pi and simple object detection with processing on the server (on your pc)
# Just stream
## Ru Guide 
Первое, скачайте репозиторий и откройте папку "just stream". Второе, загрузите на raspberry pi файл `client.py`. 
На пк первым делом запустите файл `server.py` . Далее на raspberry pi запустите файл `client.py` с параметром `-s <server ip>`. Где `<server ip>` должен быть ip вашего сервера на котором УЖЕ запущен server.py . Пример: `python3 client.py -s 192.168.1.11` Через некоторое время вы увидите окно с картинкой с вашей камеры. 
<br>
## En Guide
First, download the repository and open the "just stream" folder. Second, upload the `client.py` file to the raspberry pi.
On your pc, run the `server.py` file first. Next on the raspberry pi run the file `client.py` with the parameter` -s <server ip> `. Where `<server ip>` should be the ip of your server on which server.py is ALREADY running. Example: `python3 client.py -s 192.168.1.11` After a while you will see a window with a picture from your camera.
<br>
# Stream with object detection

## Ru Guide
Скачайте репозиторий. Откройте папку `with detection` и загрузите на raspberry pi папку `raspberry pi` и установите зависимости `pip3 install -r requirements.txt`. После этого откройте папку `pc` и установите зависимости `pip3 install -r requirements.txt` 
После этого запустите файл `server.py` с параметрами `--prototxt MobileNetSSD_deploy.prototxt --model MobileNetSSD_deploy.caffemodel --montageW 2 --montageH 2 ` и подождите пока прогрузится .
На raspberry pi запустите файл `client.py` с параметрами `- s <your server ip>` 
Через некоторое время вы увидите окно с картинкой с вашей камеры и распознованием вас. 
## En Guide 
Download the repository. Open the folder `with detection` and upload the folder` raspberry pi` to the raspberry pi and install the dependencies `pip3 install -r requirements.txt`. After that open the `pc` folder and install the dependencies` pip3 install -r requirements.txt`
Then run the file `server.py` with the parameters` --prototxt MobileNetSSD_deploy.prototxt --model MobileNetSSD_deploy.caffemodel --montageW 2 --montageH 2 `and wait while it loads.
On raspberry pi, run the `client.py` file with the parameters` - s <your server ip> `
After a while, you will see a window with a picture from your camera and recognition of you.
