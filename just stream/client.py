import socket
import time
from imutils.video import VideoStream
import imagezmq
ap = argparse.ArgumentParser()
ap.add_argument("-s", required=True,
	help="ip address of the server to which the client will connect")
args = vars(ap.parse_args())

sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format(args["server_ip"]))# your ip and port

rpi_name = socket.gethostname() # send RPi hostname with each image
picam = VideoStream(usePiCamera=True).start()
time.sleep(2.0)  # allow camera sensor to warm up
while True:  # send images as stream until Ctrl-C
	image = picam.read()
	sender.send_image(rpi_name, image)