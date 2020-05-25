# Metadata

A simplish metadata parser. 

Uses [HTTPx](https://github.com/encode/httpx), [Flask](https://flask.palletsprojects.com/), and [LaTeX.css](https://latex.now.sh/)

## Local testing

Given the metadata server is not available locally, you need to have an override. 

```
LOCAL=5001
FLASK_ENV=development

FLASK_APP=dummymetdata.py flask run --port $LOCAL &
flask run
```

## Deploy


### First Deployment

```
PROJECT_ID=YourProject
REGION=YourRegion

gcloud config set project $PROJECT_ID

gcloud builds submit --tag gcr.io/${PROJECT_ID}/metadata

gcloud run deploy metadata \
   --region $REGION \
   --platform managed \
   --image gcr.io/${PROJECT_ID}/metadata \
   --allow-unauthenticated
```
### Continuous Deployment

Requires [Cloud Build to have permissions to deploy Cloud Run](https://cloud.google.com/run/docs/continuous-deployment-with-cloud-build#continuous-iam)

```
gcloud builds submit
```
