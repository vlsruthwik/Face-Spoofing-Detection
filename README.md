# Face-Spoofing-Detection

## Working
This model works on basis of eye blink. If there's a eye blink then a message "Verifed true" appears.
### Blink detection
The eye is detection with various tracking points, considering the distance between them we find two distances (vertical and horizontal), the ratio of this will be the threshold value to detect a blink.

## Libraries used:
* OpenCV
* cvzone (pre trained)
