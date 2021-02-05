import numpy as np
import progressbar
import cv2
import time
import argparse 
import sys
import os

#using argprase to do saving,giving animal and habitat model and to give arena pic
parser = argparse.ArgumentParser( usage="""python myscript.py {vid}""",description='''Description.''',epilog="""Epilog.""")
parser.add_argument("vid", help="input path")
parser.add_argument('-f',help="folder path for saving")
parser.add_argument('-s',help="no of frames to be skipped")
parser.add_argument('-p',help="fintune the threshold percentage(0-1 float values)")
args = parser.parse_args()
if(args.vid==None or args.f==None):
	print("ERROR:no input/output path specified")
	exit()
input_location=args.vid
output_location=args.f
perc=0.15
ch=5
if(args.s!=None):
    ch=int(args.skip)
if(args.p!=None):
    perc=float(args.skip)

current_directory = os.getcwd()
final_directory = os.path.join(current_directory,output_location)
if not os.path.exists(final_directory):
   os.makedirs(final_directory)

cap = cv2.VideoCapture(input_location)

if cap.isOpened()==False:
	print("ERROR:Failed to open video file")
	exit()
os.chdir(final_directory)
count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
n=cap.get(cv2.CAP_PROP_FRAME_WIDTH)*cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
old_frame = None
f=0
i=0
sl_count=1

bar = progressbar.ProgressBar(maxval=count, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()

while i<count:

    ret, frame = cap.read()
    f=f+1
    if ret == True and f==ch:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if old_frame is not None:
            diff_frame = cv2.absdiff(frame, old_frame)
            diff_per=float(cv2.countNonZero(cv2.cvtColor(diff_frame, cv2.COLOR_BGR2GRAY))/n)
            frame_blank=float(cv2.countNonZero(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))/n)
            if diff_per>perc and frame_blank>0.40:
                name=('slide' + "% d"+'.jpg') % sl_count
                cv2.imwrite(name,frame)
                sl_count=sl_count+1
                old_frame = frame
        else:
            old_frame = frame
        f=0
    bar.update(i+1)
    i=i+1

bar.finish()
cap.release()

