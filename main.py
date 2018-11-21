# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 20:28:33 2018

@author: mark
"""
import cv2
import numpy as np
from argparse import ArgumentParser
from to_read_pfm import readPFM

parser = ArgumentParser();

parser.add_argument("flow_path", help="where to get the optical flow");
parser.add_argument("img0_path", help="where to get the original image0 as base");

parser.add_argument("-VL", help="optical vector length", dest="length", type=int, default=1);
parser.add_argument("-LW", help="line width", dest="line_width", type=int, default=2);
parser.add_argument("-SY", help="show an optical flow between how many rows", dest="show_Y", type=int, default=50);
parser.add_argument("-SX", help="show an optical flow between how many columns", dest="show_X", type=int, default=50);
parser.add_argument("-ON", help="output name", dest="output_name", default='output.jpg');

args = parser.parse_args();

error_flag = False;

if '.pfm' in args.flow_path:
    flow, scale = readPFM(args.flow_path);#assume y direction is in dimension 0, and x in dimension 1.
elif '.npy' in args.flow_path:
    flow = np.load(args.flow_path);
else:
    print('not support optical flow file!');
    error_flag = True;

if error_flag == False:
    original_image = cv2.imread(args.img0_path);

    vector_length = args.length;
    line_width = args.line_width;
    show_interval_y = args.show_Y;#(vertical direction)
    show_interval_x = args.show_X;#(horizontal direction)

    for y in range(0, flow.shape[0]):#in for loop using the opencv coordinate system
        if y % show_interval_y == 0:
            for x in range(0, flow.shape[1]):
                if x % show_interval_x == 0:
                    vector = flow[y][x] * vector_length;#but in drawing function, using different way to understand x and y
                    cv2.line(original_image, (x, y), (int(np.round(x + vector[0])), int(np.round(y + vector[1]))), (0, 255, 0), line_width);
                    cv2.circle(original_image, (x, y), 1, (255, 255, 255), -1);#that's why using (x,y) not (y,x)

    cv2.imwrite(args.output_name, original_image);
    
    cv2.imshow("show", original_image);

    cv2.waitKey(0);
    cv2.destroyAllWindows();
else:
    print('exit with no output.');
