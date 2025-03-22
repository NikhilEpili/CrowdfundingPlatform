crowdfunding-platform/
│── backend/                  # Backend (Flask API)
│   ├── migrations/           # Database migrations (Flask-Migrate)
│   ├── models.py             # Database models (SQLAlchemy)
│   ├── config.py             # App configurations (Database, API keys)
│   ├── payments.py           # Razorpay integration
│   ├── routes.py             # API routes (Users, Donations, Campaigns)
│   ├── app.py                # Main Flask application
│   ├── auth.py               # User authentication (JWT)
│   ├── database.py           # Database initialization
│   ├── utils.py              # Helper functions (email notifications, etc.)
│   ├── .env                  # Environment variables (API keys, secrets)
│   └── requirements.txt      # Dependencies
│
│── frontend/                 # Frontend (React or Flask templates)
│   ├── public/               # Public assets (Images, logos)
│   ├── src/                  # Source code
│   │   ├── components/       # Reusable UI components
│   │   ├── pages/            # Pages (Home, Campaigns, Donations)
│   │   ├── services/         # API calls to backend
│   │   ├── App.js            # Main React App
│   │   ├── index.js          # React entry point
│   ├── package.json          # Node.js dependencies
│
│── docs/                     # Documentation
│   ├── README.md             # Project overview
│   ├── API.md                # API documentation
│
│── scripts/                  # Deployment & automation scripts
│
│── .gitignore                # Ignore unnecessary files in Git
│── README.md                 # Main project readme
│── venv/                     # Virtual environment (Python)
