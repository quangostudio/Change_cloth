# Change_cloth
change_cloth use model GMM, CVPTON and JPPNET write to api use flask
# How to run
1.Dowload 3 <a href="https://drive.google.com/file/d/125UtOS4T4RBji8lXtm9WEwD1KcHG4F1g/view">pretrain model</a> and copy to `checkpoint`
2.Install [packages](#packages)
3.Run api `python3 run.py`
# packages
tensorflow==1.12.0 or tensorflow == 1.15
torch==1.2.0  
torchvision==0.2.0  
run code with cpu: `Model(.., use_cuda=False)
# Docker
build image `docker build -t quangostudio\changecloth`
run docker `docker-compose up`
# Input
input api `image` and `image2`
return image base64 decode
convert image base64 decode to `.png` in path `/result/`
# Test with Postman
<img src="" title="Test api with inpurt and result return"> 

## GMM
<a href="https://arxiv.org/abs/1711.08447v1"> VITON: An Image-based Virtual Try-on Network </a>

## CVPTON
<a href="https://arxiv.org/abs/1807.07688"> Toward Characteristic-Preserving Image-based Virtual Try-On Network </a>

## JPPNET
<a href="https://arxiv.org/abs/1804.01984"> Look into Person: Joint Body Parsing & Pose Estimation Network and A New Benchmark </a> 

*Powered By **ducquan***
