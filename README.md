# Circuit Breaker - Electrician Exam Prep

A comprehensive application to help electricians prepare for their licensing exams, featuring study materials for electrical theory, NEC articles, licensing requirements by state, and interactive practice quizzes.

## Features

- State-by-state licensing requirements
- NEC article summaries and explanations
- Electrical theory topics
- Calculation tutorials
- Practice quizzes with explanations

## Deployment to Vercel

This repository includes a serverless-compatible version for Vercel deployment.

### Deployment Steps

1. Push this repository to GitHub
2. Connect your GitHub repository to Vercel:
   - Create an account on Vercel if you don't have one
   - Click "New Project" and import this repository
   - Configure the project:
     - Framework Preset: Other
     - Build Command: (leave empty)
     - Output Directory: (leave as default)
     - Install Command: `pip install -r requirements.txt`
   - Add environment variables if needed:
     - `PYTHON_VERSION`: 3.9
   - Click "Deploy"

### How the Vercel Deployment Works

The Vercel deployment is configured to run as a read-only version of the site, with these key differences:

- No user authentication required
- Quiz results aren't saved to a database
- Uses an in-memory SQLite database with sample data

The key files for Vercel deployment are:

- `vercel.json`: Configuration for Vercel
- `api/index.py`: Serverless function entry point
- `api/init_db.py`: Database initialization for serverless environment
- `vercel_app.py`: Modified Flask application for Vercel
- Templates with `vercel_` prefix: Simplified templates for Vercel deployment

## Local Development

To run the application locally:

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`

For the read-only Vercel version:

```
python vercel_app.py
```

## License

All rights reserved.
