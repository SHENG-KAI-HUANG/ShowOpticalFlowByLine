# show_optical_flow_in_line
This is python3 code to show optical flow in color.<br />
If there are anything don't understand or bug, please feel free to post an issue.<br />

Coding and testing by Anaconda in Windows 10 with python 3.6.5.<br />

Please install following package before using this code:<br />
1. opencv<br />
2. numpy<br />
3. argparse<br />

## How to using this code:
In this project will have a sample .pfm and a sample .png to show how to use this code.<br />
this .pfm and .png is download from [Monkaa scene flow dataset sample pack](https://lmb.informatik.uni-freiburg.de/resources/datasets/SceneFlowDatasets.en.html)<br /> 
you can also find original code that how to read .pfm by python from the above website.<br /> 

Run with default arguments:<br />
python3 main.py <path/to/pfm> <path/to/image><br />

or you can run python3 main.py -h for more help.

It will create a windows to show the result like this.<br />
![alt text](https://github.com/SHENG-KAI-HUANG/show_optical_flow_in_color/blob/master/readme_image/flow_48.jpg)<br />
the line length means the optical flow vector magnitude and line direction means optical flow direction.

