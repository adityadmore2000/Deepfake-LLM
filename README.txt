conda create -n deepfake_env -y

conda activate deepfake_env

conda install pip

pip install --upgrade google-api-python-client

pip install python-dotenv

pip install google-generativeai

pip install --upgrade pip

pip install --upgrade transformers sentencepiece datasets[audio]


Set up Application Default Credentials 
1) Install gcloud CLI
2) Create google cloud project there
3) Then, in enable API and services tab, search for generative language api, click enable
4) click create credentials
5) create a service account by clicking on set up credentials 

Now inside google cloud sdk shell, type: gcloud auth application-default login
It will open a window, in which you need to login with same email id you set your google cloud project with
then it will create a json file, copy that into your project root directory


Then on running main.py, additional config files will start downloading and project can be opened in browser

***
Create api key on: https://app.heygen.com/settings?nav=API



