import cv2
import random
import dropbox
import time

start_time=time.time()

def takeSnapShot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time()
        result=False
        print("snapshotTaken")

    return img_name
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token="sl.As0DKPQJlNf7RuXRi7MeI4SNjRYok5Nxcwy0GDHQswXCu00ldGC_LmlPOSmLijPNelIIyH1GuqqqNbGSS0tJF_rYFyRUHk0wv5iJU83mNjAb0EnpoEYY9TwfyoLLifB-6bHV6_I"
    file_from=img_name
    file_to="/newfolder/"+img_name
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overWrite)
        print("Picture Uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=30):
            name=takeSnapShot()
            upload_file(name)

main()