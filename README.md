# Virtual-Photo-Booth
Virtual photo booth made with Python. It uses the opencv library to access the user's camera. Through simple face detection, it places props on faces in view of the camera. It also changes the background and adds a foreground. This project was made in IDLE, and I cannot guarantee it will work elsewhere.

The props, backgrounds and foregrounds are for the scenario this was developed for, which is a celebration of the 15th anniversaary of the School of Science and Technology. 

In order to run this program, you need to first download the facial landmarks model [here](https://github.com/italojs/facial-landmarks-recognition).

After that, create a virtual environment with Terminal.
```
cd [Folder with the virtual photo booth]
```
Choose a name for your CV environment, e.g. cvenv. Then type:
```
python3 -m venv cvenv
```
When the virtual environment is created, activate it: 
```
source cvenv/bin/activate
```
Install the required packages using pip3:
```
pip3 install opencv-python dlib imutils
```
You also need to install cvzone.
```
pip install cvzone
```
When you are ready, open IDLE with:
```
python -m idlelib
```


