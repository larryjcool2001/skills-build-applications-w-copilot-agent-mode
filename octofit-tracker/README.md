# OctoFit Tracker

## Overview

The OctoFit Tracker is a fitness application designed to help users track their activities, manage teams, and receive personalized workout suggestions. The application is built using Django for the backend and React for the frontend.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

```
octofit-tracker/
├── backend/                # Contains the Django backend application
│   ├── venv/               # Python virtual environment
│   ├── requirements.txt     # Python packages required for the backend
│   ├── manage.py            # Command-line utility for Django
│   └── octofit_tracker/     # Main Django application package
│       ├── __init__.py
│       ├── settings.py
│       ├── urls.py
│       ├── wsgi.py
│       ├── asgi.py
│       ├── apps.py
│       ├── models.py
│       └── views.py
├── frontend/               # Contains the React frontend application
│   ├── package.json         # npm configuration file
│   ├── src/                 # Source files for the React app
│   │   ├── index.jsx
│   │   └── App.jsx
│   └── public/              # Public assets for the React app
│       └── index.html
├── .gitignore               # Files and directories to ignore in Git
└── README.md                # Project documentation
```

## Setup Instructions

### Backend Setup

1. **Create a Python Virtual Environment**:
   Navigate to the `backend` directory and create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment**:
   ```bash
   source venv/bin/activate
   ```

3. **Install Required Packages**:
   Install the required Python packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**:
   Run the Django development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. **Navigate to the Frontend Directory**:
   ```bash
   cd frontend
   ```

2. **Install npm Dependencies**:
   Install the required npm packages:
   ```bash
   npm install
   ```

3. **Start the React Application**:
   Run the React development server:
   ```bash
   npm start
   ```

## Usage

Once both the backend and frontend servers are running, you can access the application in your web browser at `http://localhost:3000`.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.