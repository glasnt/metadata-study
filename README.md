# Metadata Survey

A simplish metadata parser. 

[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)

## Implementation

Allows generic querying of the metadata server accessible within a Cloud Run service to inspect itself. 

Implemented in Python using [HTTPx](https://github.com/encode/httpx), [Flask](https://flask.palletsprojects.com/). Styled with [LaTeX.css](https://latex.now.sh/)

## Local testing

A dummy metadata server is provided for local testing: 

```
LOCAL=5001
FLASK_ENV=development

FLASK_APP=dummymetadata.py flask run --port $LOCAL &
flask run
```

## Deploy

### First Deployment

Use the "Run on Google Cloud" button above. 

Alternative `gcloud` method: 

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
