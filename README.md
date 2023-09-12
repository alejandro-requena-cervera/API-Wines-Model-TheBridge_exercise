|Developed Using Python|Built Using Flask|
|--|--|
|<img alt="Python Logo" src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg" width="200">|<img alt="Python Logo" src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-ar21.svg" width="200">|

|App is deployed in [Fl0](https://www.fl0.com)|Database is deployed on [AWS RDS](https://aws.amazon.com/rds/)|
|--|--|
|<img alt="fl0 Logo" src="https://avatars.githubusercontent.com/u/118862654?s=200&v=4" width="200">|<img alt="AWS Logo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/1024px-Amazon_Web_Services_Logo.svg.png" width="200">|


# Python Flask App Exercise
This is a [Flask](https://flask.palletsprojects.com/en/1.1.x/) app that take predictions with a modified [wine model from Sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html).

This application is an exercise to test the knowledge acquired in class.


## Home Page
<div style="overflow: auto;">
    <img align="right" width="300" src="./templates/img/HomePage.png" alt="Home Page" />
    The homepage has an index with a short explanation of what each API does. The result is returned as JSON in version 0. Version 1 collects information via a form. The result is displayed in HTML.
</div>


## Take Predictions
<div style="overflow: auto;">
    <img align="right" width="300" src="./templates/img/TakePredictions.png" alt="Take Predictions" />
    Once the variables have been entered, they are passed to the trained model to make a prediction. Displays the result of the prediction and the inputs entered.
</div>


## View Database
<div style="overflow: auto;">
    <img align="right" width="300" src="./templates/img/ViewDatabase.png" alt="View Database" />
    It is necessary to specify the database to be viewed. This is returned as JSON or HTML depending on the version. The database containing the samples and their predictions can be deleted from the same page (v1).
</div>


## Delete Database
<div style="overflow: auto;">
    <img align="right" width="300" src="./templates/img/DeleteDatabase.png" alt="Delete Database" />
    You must enter the database you wish to delete. The application will ask for confirmation before deleting (version 1 only).
</div>


<div style="color:gold;">
<h1> 🤚⚠️ APPLICATION STATUS UPDATE</h1>
</div>
Database and application are currently <span style="color: red;">disconnected</span> from their servers.
