from asyncio import sleep
import time
import cv2
import webbrowser

print("initializing camera...")
cap = cv2.VideoCapture(0)

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
n=0
while True:
    print("scanning...")
    while True:
        # extract the image from camera
        _, img = cap.read()
        # detect and decode, if any
        data, bbox, _ = detector.detectAndDecode(img)
        # check if there is a QRCode in the image
        if data:
            qr_code=data
            break
        else:
            n=n+1
            print("looking...", n)
            time.sleep(0.25)

    print("code detected:", qr_code)

    # cv2.imshow("QRCODEscanner", img)
    # msgShown = False
    # while True:
    #     if cv2.waitKey(1) == ord("q"):
    #         cap.release()
    #         cv2.destroyAllWindows()
    #         break
    #     else:
    #         if not msgShown:
    #             print("waiting for q key...")
    #             msgShown=True

    # b=webbrowser.open(str(qr_code))

    bb=webbrowser.open_new(str(qr_code))
    time.sleep(5)
