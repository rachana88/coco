import os
data_file = 'cfg/coco.data'
cfg_file = 'cfg/yolo.cfg' 
weight_file = '../yolo.weights'
thresh = 0.2
#image_folder =  '/home/deepfusion/Desktop/yolo_v2_copy/v2/yolov2_training/PedVehiclesTraining/GroundTruthImages/JPEGImages/'
image_folder = '/home/deepfusion/Desktop/yolo_v2_copy/v2/yolov2_training/StoreTraining/ValidationData/JPEGImages/'


curpath = os.path.abspath(__file__)
dname = os.path.dirname(curpath)
os.chdir(dname)

n = 1
for subdir, dirs, files in os.walk(image_folder):
    for file in files:

	image_file =  os.path.join(subdir, file)
	command = ['./darknet detector test ', data_file, cfg_file, weight_file, image_file, ' -thresh', str(thresh)]
	command = ' '.join(command)
	os.system(command)
	image_file_name = os.path.splitext(os.path.basename(image_file))[0]
	if not os.path.exists('./predictions'):
		os.system('mkdir predictions')
	print(os.getcwd())
	os.system('mv predictions.jpg ./predictions/' +  image_file_name + '_pred.jpg')



