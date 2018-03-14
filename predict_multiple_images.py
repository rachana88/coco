import os
#data_file = 'cfg/cocoped.data'
#data_file = 'cocoped_store_model_files/cocoped.data'
data_file = 'cfg/coco.data'


#cfg_file = 'cocoped_store_model_files/cocoped_yolo.cfg' 
#cfg_file = 'cfg/cocoped_yolo.cfg'
cfg_file = 'cfg/yolo.cfg'
#cfg_file = 'tiny_yolo_add_more_layers.cfg'
#cfg_file = 'newTopologies/tiny_yolo_cocoped.cfg'



#weight_file = 'backup/cocoped_yolo_18000.weights'
#weight_file = 'yolo_cocoped_final.weights'
#weight_file = 'cocoped_store_model_files/cocoped_store.weights'
#weight_file = 'cocoped_store_enhanced.weights'
weight_file = 'yolo.weights'
#weight_file = 'cocoped_compress.weights'
#weight_file = 'tiny_yolo_cocoped_13000.weights'

thresh = 0.5
#image_folder =  '/home/deepfusion/Desktop/yolo_v2_copy/v2/yolov2_training/PedVehiclesTraining/GroundTruthImages/JPEGImages/'
#image_folder = '/home/deepfusion/Desktop/yolo_v2_copy/v2/yolov2_training/StoreTraining/ValidationData_recent/JPEGImages/'
#image_folder = '/home/deepfusion/Desktop/yolo_v2_copy/v2/yolov2_training/StoreTraining/ValidationData/JPEGImages/'
#image_folder = '/home/deepfusion/Desktop/yolo_v2_copy/v2/yolov2_training/test_video_images/test_videos/test_2_video/JPEGImages'
image_folder = '/home/deepfusion/Desktop/yolo_v2_copy/v2/yolov2_training/StoreTraining/training_data_testing_demo/JPEGImages'
curpath = os.path.abspath(__file__)
dname = os.path.dirname(curpath)
os.chdir(dname)

n = 1
print 'here'
for subdir, dirs, files in os.walk(image_folder):
    for file in files:

	image_file =  os.path.join(subdir, file)
	command = ['./darknet detector test ', data_file, cfg_file, weight_file, image_file, ' -thresh', str(thresh)]
	print file
	command = ' '.join(command)
	os.system(command)
	image_file_name = os.path.splitext(os.path.basename(image_file))[0]
	if not os.path.exists('./predictions'):
		os.system('mkdir predictions')
	print(os.getcwd())
	os.system('mv predictions.jpg ./predictions/' +  image_file_name + '_pred.jpg')



