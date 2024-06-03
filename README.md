# Virtual-Photo-Booth
Virtual photo booth made with Python. It uses the opencv library to access the user's camera. Through simple face detection, it places props on faces in view of the camera. It also changes the background and adds a foreground.

In order to run this program, you need to first download the facial landmarks model [here](https://github.com/italojs/facial-landmarks-recognition).

After that, create a virtual environment with Terminal.
```
cd [Folder with the virtual photo booth]
python3 -m venv cvenv
source cvenv/bin/activate
pip3 install opencv-python dlib imutils
python -m idlelib
```

You also need to install cvzone.
```
pip install cvzone
```
