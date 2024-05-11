"""
MAIN PYTHON SCRIPT
stereo-vision.py
Homework 11: Sparse 3D reconstruction using stereo vision.

Authors:  Ana Bárbara Quintero 544073
Organisation: UDEM
Due date: Thursday, May 16th, 2024

EXAMPLE TERMINAL CODE: 
$ python stereo-vision.py --l_img left-image.png --r_img right-image.png

MY TERMINAL CODE:
python -u "/Users/anabi/Documents/GitHub/stereo-vision/ stereo-vision.py" --l_img "/Users/anabi/Documents/GitHub/stereo-vision/left_infrared_image.png" --r_img "/Users/anabi/Documents/GitHub/stereo-vision/right_infrared_image.png"

"""
# Importing the necessary libraries
import cv2 as cv
import numpy as np
import open3d as o3d
import json
import argparse


def parse_args():
    """
    Parse command line arguments for image paths.
    
    This function parses the command line arguments for the paths to the image file for object detection
    and the video file. The function returns a Namespace object containing the parsed arguments.

    Returns:
        Namespace: Parsed command line arguments with paths to the images.
    """

    parser = argparse.ArgumentParser(description='Stereo Calibration')
    parser.add_argument('--l_img', type=str, default="/Users/anabi/Documents/GitHub/stereo-vision/left_infrared_image.png", help='Path to the left image')
    parser.add_argument('--r_img', type=str, default="/Users/anabi/Documents/GitHub/stereo-vision/right_infrared_image.png", help='Path to the right image')
    args = parser.parse_args()


    return args

def run_pipeline(video_path, img_obj_path):
  



    return 

def load_parameters(file_path):
    """
    Load camera calibration parameters from a JSON-like text file.

    Args:
        file_path (str): Path to the JSON-like text file containing calibration parameters.

    Returns:
        dict: Dictionary containing the loaded calibration parameters.
    """
    # Load camera calibration parameters from the file
    with open(file_path, 'r') as f:
        calibration_data = json.load(f)


    # Extract relevant parameters
    baseline = float(parameters["baseline"])
    rectified_fx = float(parameters["rectified_fx"])
    rectified_fy = float(parameters["rectified_fy"])
    rectified_cx = float(parameters["rectified_cx"])
    rectified_cy = float(parameters["rectified_cy"])
    rectified_width = int(parameters["rectified_width"])
    rectified_height = int(parameters["rectified_height"])

    # Print the loaded parameters (optional)
    print("Baseline:", baseline)
    print("Rectified fx:", rectified_fx)
    print("Rectified fy:", rectified_fy)
    print("Rectified cx:", rectified_cx)
    print("Rectified cy:", rectified_cy)
    print("Rectified width:", rectified_width)
    print("Rectified height:", rectified_height)

    return parameters


def get_coordinates(event, x, y, param):
    """
    Callback function to get coordinates of selected pixel.
    """
    global uL, uR, v
    if event == cv.EVENT_LBUTTONDOWN:
        if param == 'left':
            uL, v = x, y
        elif param == 'right':
            uR = x

def calculate_coordinates(uL, uR, v, parameters):
    """
    Calculate X, Y, and Z coordinates of selected pixel.
    """
    # Calculate disparity
    disparity = abs(uL - uR)
    
    # Calculate depth
    depth = parameters["baseline"] * parameters["rectified_fx"] / disparity
    
    # Convert pixel coordinates to Cartesian coordinates
    X = (uL - parameters["rectified_cx"]) * depth / parameters["rectified_fx"]
    Y = (v - parameters["rectified_cy"]) * depth / parameters["rectified_fy"]
    Z = depth
    
    return X, Y, Z




def display_images(left_image, right_image):
   
    # Load rectified left and right infrared images
    left_image = cv.imread('left_infrared_image.png', cv.IMREAD_GRAYSCALE)
    right_image = cv.imread('right_infrared_image.png', cv.IMREAD_GRAYSCALE)

    # Display images and allow user to select pixels
    cv.namedWindow('Left Infrared Image')
    cv.setMouseCallback('Left Infrared Image', get_coordinates, param='left')
    cv.imshow('Left Infrared Image', left_image)
    cv.waitKey(0)

    cv.namedWindow('Right Infrared Image')
    cv.setMouseCallback('Right Infrared Image', get_coordinates, param='right')
    cv.imshow('Right Infrared Image', right_image)
    cv.waitKey(0)


if __name__ == '__main__':
    # Parse command line arguments
    args = parse_args()

    # Load left and right images
    left_image = cv.imread(args.l_img)
    right_image = cv.imread(args.r_img)

    # LOAD PATH TO CALIBRATION PARAMETERS
    calibration_file = "/Users/anabi/Documents/GitHub/stereo-vision/calibration-parameters.txt"
    parameters = load_parameters(calibration_file)

    


