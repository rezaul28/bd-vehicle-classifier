sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
python --version
sudo apt install python3-opencv
pip install opencv-python-headless==4.5.5.62
pip uninstall opencv-python-headless -y
pip install opencv-python --upgrade
sudo chmod a+rx ./run.sh
./run.sh