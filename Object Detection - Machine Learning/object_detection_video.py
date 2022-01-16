"""
Reference : 'https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10'

The program uses a TensorFlow-trained object detector (classifier) to perform object detection. 
It loads the model (classifier) and uses it to perform object detection on a video.
It draws boxes, scores, and labels around the objects detected in each frame of the video and writes it into a video of mp4 format.

"""

# Import packages
import time
from imutils.video import FileVideoStream
from imutils.video import FPS
from utils import visualization_utils as vis_util
from utils import label_map_util
import os
import cv2
import numpy as np
import tensorflow as tf
import sys

# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")

# Name of the directory containing the object detection model used
#MODEL_NAME = 'ssd_mobilenet_v2_coco_2018_03_29' # To use pre-trained model of choice

MODEL_NAME = 'inference_graph'  # To use custom-trained model

# Input video data on which object detection is performed
VIDEO_NAME = 'v1.mp4'

# Path to current working directory
CWD_PATH = os.getcwd()

# Path to frozen detection graph .pb file of model used for object detection
PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_NAME, 'frozen_inference_graph.pb')

# Path to label map file
# PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt') # For pre-trained model
PATH_TO_LABELS = os.path.join(CWD_PATH, 'training', 'labelmap.pbtxt') # For custom-trained model
# Path to video
PATH_TO_VIDEO = os.path.join(CWD_PATH, VIDEO_NAME)

# Number of classes the object detector can identify
NUM_CLASSES = 1

# Loading label map.
# Label map maps indices to category names.
# Here we use internal utility functions, but anything that returns a
# dictionary mapping integers to appropriate string labels would be fine.
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(
    label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# Loading Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)

# Defining input and output tensors (i.e. data) for the object detection classifier

# Input tensor is the image
image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

# Output tensors are the detection boxes, scores, and classes
# Each box representing a part of the image where a particular object is detected
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

# Each score representing level of confidence for each of the objects.
# The score is shown on the result image, together with the class label.
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

# Number of objects detected
num_detections = detection_graph.get_tensor_by_name('num_detections:0')

# Open video file
video = cv2.VideoCapture(PATH_TO_VIDEO)

# Start counter to calculate FPS
fps = FPS().start()

# Initialize video writer
outputFile = 'v_out.avi'

# Selecting format type of video using codec code
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')


writer = cv2.VideoWriter(outputFile, fourcc, 30, (round(video.get(
    cv2.CAP_PROP_FRAME_WIDTH)), round(video.get(cv2.CAP_PROP_FRAME_HEIGHT))), True)

while(video.isOpened()):
    # Acquiring frame and expanding frame dimensions to have shape: [1, None, None, 3]
    # i.e. a single-column array, where each item in the column has the pixel RGB value
    ret, frame = video.read()

    # Stop if end of video
    if not ret:
        break
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_expanded = np.expand_dims(frame_rgb, axis=0)

    # Performing detection by running the model with the image as input
    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: frame_expanded})

    # Drawing results of the detection
    vis_util.visualize_boxes_and_labels_on_image_array(
        frame,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=5,
        min_score_thresh=0.60)

    # write video
    writer.write(frame.astype(np.uint8))

    # Displaying results
    cv2.imshow('Object detector', frame)

    # Update counter to calculate FPS
    fps.update()

    # Press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break

# Stop FPS counter
fps.stop()

# Printing total time elapsed and FPS for object detection
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# Cleaning up
video.release()
cv2.destroyAllWindows()
