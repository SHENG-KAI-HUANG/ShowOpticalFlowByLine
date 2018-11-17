This is python3 code to show optical flow by line. (not arrow yet, maybe when I have more free time)<br />
If there are anything don't understand or bug, please feel free to post an issue.<br />

Coding and testing by Anaconda in Windows 10 with python 3.6.5.<br />

Please install following package before using this code:<br />
1. opencv<br />
2. numpy<br />
3. argparse<br />

## How to using this code:
In this project will have a sample .pfm and a sample .png to show how to use this code.<br />
These .pfm and .png are download from [Monkaa scene flow dataset sample pack](https://lmb.informatik.uni-freiburg.de/resources/datasets/SceneFlowDatasets.en.html)<br /> 
You can also find original code about how to read .pfm by python from the above website.<br /> 

You can run ```python3 main.py 0048.pfm 0048.png``` immediately after you download this repository.<br /> 
It will save an JPG image named 'output.jpg' and create a windows to show the result.<br />  

Run with default augments:<br />
```python3 main.py <path/to/pfm> <path/to/image>```<br />
or
Run ```python3 main.py -h``` for more help.


It will create a windows to show the result like this.<br />
![alt text](https://github.com/SHENG-KAI-HUANG/show_optical_flow_in_line/blob/master/readme_image/output.jpg)<br />
Those lines length mean optical flow vector magnitude and direction mean optical flow vectore direction.
