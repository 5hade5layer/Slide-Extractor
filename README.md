# Slide-Extractor
Extracts slides from a video of a ppt presentation
## How to run
1. navigate to the file directory through terminal or cmd
2. Run the requirements.txt
```
pip install -r requirements.txt
```
3.run the program in the below format
```
python slides.py <videopath> -f <output folder name> 
```
4. optionaly if you want to adjust the number of frames skipped to speed up the process(default is 5) you can use
```
python slides.py <videopath> -f <output folder name> -s <number of frames to be skipped>
```
5. optionaly if you want to adjust the simalirity threshold which is a float value ranging from 0-1 and higher the value is the code will only detect more dissimilar frames to adjust this value you can use
```
python slides.py <videopath> -f <output folder name> -p <a float value b/w 0-1>
```
