import mrcnn.model as modellib

# Define model directory
MODEL_DIR = "./logs"

# Create Mask R-CNN model
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=None)
print("Mask R-CNN Model Initialized Successfully!")


