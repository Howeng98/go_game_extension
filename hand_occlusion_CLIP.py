'''
Source Code: https://github.com/mlfoundations/open_clip

Use this code to remove redundant and hand occlusion images.
'''
import torch
from PIL import Image
import open_clip
from glob import glob
import os
import re
import shutil

# Prepare model
model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
tokenizer = open_clip.get_tokenizer('ViT-B-32')

# 
TARGET_DATA_DIR = './GO_2_pure_data'
if os.path.exists(TARGET_DATA_DIR):
    shutil.rmtree(TARGET_DATA_DIR)
os.mkdir(TARGET_DATA_DIR)

ROOT_DATA_DIR = './GO_2_frames'
IMG_PATHS = glob(os.path.join(ROOT_DATA_DIR, '*.jpg'))
IMG_PATHS.sort(key=lambda f: int(re.sub('\D', '', f)))

discard_image_path_list = []

for IMG_PATH in IMG_PATHS:
    
    image = preprocess(Image.open(IMG_PATH)).unsqueeze(0)
    text = tokenizer([
        "An image of go board with player hand",
        "An image of go board without player hand",
        # "An image of go board with noise",
    ])

    with torch.no_grad(), torch.cuda.amp.autocast():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)

        text_probs = (10000.0 * image_features @ text_features.T).softmax(dim=-1)        
        
        print("Path: {}  Label probs{}".format(IMG_PATH, text_probs))
        # print("Path: {}  Label probs{}".format(IMG_PATH, text_probs))            
        if text_probs[0][0] != 0.0:            
            discard_image_path_list.append(os.path.basename(IMG_PATH))
        else:
            shutil.copy(IMG_PATH, os.path.join(TARGET_DATA_DIR, os.path.basename(IMG_PATH)))


print("Orignal total images:{} | Deleted images: {} | Remain images: {}".format(
    len(IMG_PATHS),
    len(discard_image_path_list),
    len(IMG_PATHS)-len(discard_image_path_list),
))

    
