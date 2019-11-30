# Import SDK packages
from time import sleep
import boto3
from twilio.rest import Client
from picamera import PiCamera
camera = PiCamera()
account_sid = '<accountSid>'
auth_token = '<AuthToken>'
client = Client(account_sid, auth_token)
def detect_labels_local_file(photo):


    client=boto3.client('rekognition')
   
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
        
    print('Detected labels in ' + photo)    
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))

    return len(response['Labels'])
def send_message():
	message = client.messages \
                .create(
                     body="SMS Sent!  Hey, Jenny looks a bit upset",
                     from_='+12029198699',
                     to='+6593660520'
                 )
def main():
    camera.capture('/home/pi/Desktop/image.jpg')
	photo='image.jpg'
    label_count=detect_labels_local_file(photo)
    print("Labels detected: " + str(label_count))
	if "phubbing" in label_count :
		print(message.sid)


if __name__ == "__main__":
    while True:
		main()
		sleep(10)