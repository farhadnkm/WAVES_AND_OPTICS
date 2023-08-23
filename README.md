# Waves and Optics - code base
This repository is made for the course <b>Waves and Optics</b>, department of physics and technology, UiT - the arctic university of Norway.

## For Beginners

<span style="color:pink"><b>In case you don't remember how to setup Python and git:</b></span> 
* Install Anaconda https://www.anaconda.com/
* Install git https://git-scm.com/downloads
* To check whether git and Python are recognized, open the Anaconda prompt and execute:
    - <span style="color:gray">Check python installation </span> ``` python --version ```
    - <span style="color:gray">check git command in acanconda prompt</span> ``` git --version ```
    - (you should see versions as results)

<span style="color:pink"><b>Now follow these steps in your command prompt/terminal:</b></span> 
* <span style="color:gray">Make a new environment </span> ``` conda create --name PROJECT_NAME ```
* <span style="color:gray">Activate the environment </span> ``` conda activate PROJECT_NAME ```
* <span style="color:gray">Make a new folder and give it a name. </span>
* <span style="color:gray">Go back to the terminal and change the directory to the new folder by typing </span> ``` cd PATH_TO_THE_NEW_FOLDER ```
* <span style="color:gray">Make sure that the last name of the path shown in the terminal is the new folder's name. </span>
* <span style="color:gray">Now download the repository by typing </span> ``` git clone https://github.com/farhadnkm/WAVES_AND_OPTICS.git ```
* <span style="color:gray">Then install the requirements </span> ``` pip install -r requirements.txt ```
* <span style="color:gray">Eventually, execute the code </span> ``` python test.py ```

This must run without any errors. You should see some printed statements in the terminal and figures popping up.
You can read more details about test.py [here](https://github.com/farhadnkm/WAVES_AND_OPTICS/blob/main/01-introduction.ipynb).

### <span style="color:yellow"> Note:</span> Having VScode or an IDE on your machine is recommended

VScode has an internal interpretor for jupyter.
If VScode or any sort of IDE is not available:
* To install VScode: https://code.visualstudio.com/download
* Working without VScode
    - <span style="color:gray">install jupyter </span> ``` conda install jupyter ```
    - <span style="color:gray">Change directory to the project folder </span> ``` cd .../SOME_ROOT_DIRECTORY/FOLDER_NAME/WAVES_AND_OPTICS ```
    - <span style="color:gray">in command prompt run </span> ``` jupyter notebook ```

## Following the Sessions
For each chapter, a separate jupyter notebook is made. They are being updated in an ongoing manner.

## Syncing your local copy
If changes are made here, you can directly update your copy of this repository by following these steps:
1. Open the terminal window
2. Navigate to the project folder
3. Type ``` git pull ```
