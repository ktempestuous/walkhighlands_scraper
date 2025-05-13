Scraping walkhighlands website, a website listing walking trails in Scotland, to extract a description of the terrain as well as the numerical ratings of terrain grade and bogginess. Idea is to train a classification model to predict the ratings based off of the terrain description. 

## Installation 

Recommend a virtual environment 
python3 -m venv venv
source venv/bin/activate (for MacOS)

and install these dependencies: 

pip install -r requirements.txt

## Usage 

Follow this step:

python3 run.py

Output will be available in "walks.json" in the same directory as run.py. 
 
