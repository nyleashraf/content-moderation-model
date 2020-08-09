# content-moderation-model
Building web application that can take user-uploaded image data and return classification from deep learning model trained on offensive, suggestive, and neutral image data.

Inspiration for the project comes from a demo created by Hive, a full-stack deep learning platform helping to bring companies into the AI era. Link to their demo: https://thehive.ai/hive-moderation-suite

Currently, I have a working front-end that can take image uploads and save them into a folder within my local Flask environment. This connection between the front-end and back-end will allow me to query my trained model and return the image file and its classification to the front-end web application. In addition, I have processed 98,999 image files for input into the pre-trained Resnet-34 neural network (with custom dense layers), and have trained the model on a sample of image files. Due to a class imbalance (low number of suggestive images), the model does not generalize well. Going forward, I will either: (a) look for additional sources of data to even out the class distribution, or (b) utilize data augmentation techniques to artificially increase the number of images in the suggestive class. In additon, I plan to train different model architectures -- maybe a simpler solution will suffice for this image classification problem.

Image files scraped using scripts from the following Github repository: https://github.com/alex000kim/nsfw_data_scraper

## Front-End Design

The following images outline the design of the application interface. The first image shows the landing page of the application, while the second image shows the portion of the home page that allows for user image upload. Images are saved to app/static/uploads. Currently, the url portion of the image upload block has no functionality. Additionally, the right block of the page with Class and Confidence Score is currently static and does not change based on the image on-screen.

![home page](https://github.com/nyleashraf/content-moderation-model/raw/master/img/home-screenshot.png)

![image upload block](https://github.com/nyleashraf/content-moderation-model/raw/master/img/dragndrop-screenshot.png)

## TO-DO

(1) Continue model training with different model architectures and larger training set (through either image augmentation or additional web scraping)<br>

(2) Allow for upload of images on the web with a url<br>

(3) Connect trained model to Flask application and image upload folder and update front-end to reflect classification result from queried model<br>

(4) Deploy application<br>

## How to Run Flask App Locally 

(Assuming usage of Linux or MacOS) After cloning the repository, navigate to the app folder and activate the venv with the following command:

        $ source venv/bin/activate
        
Then, activate the Flask application with the following two commands:
        
        $ export FLASK_APP=__init__.py
        
        $ flask run
