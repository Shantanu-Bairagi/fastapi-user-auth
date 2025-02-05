## Project Structure

<pre>
fastapi-user-auth/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   ├── models/
│   │   └── user.py
│   ├── schemas/
│   │   └── user.py
│   ├── routers/
│   │   └── auth.py
│   └── services/
│       └── auth.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
</pre>

## File Descriptions

- `app/main.py`: The main entry point of the application. It initializes the FastAPI app and includes the router.
- `app/database.py`: Handles the database connection to MongoDB.
- `app/config.py`: Contains configuration settings loaded from the .env file.
- `app/models/user.py`: Defines the User model for interacting with the database.
- `app/schemas/user.py`: Contains Pydantic models for request/response validation.
- `app/routers/auth.py`: Defines the API endpoints for user registration, login, and profile retrieval.
- `app/services/auth.py`: Implements authentication-related functions like password hashing and token generation.
- `.env`: Contains environment variables (not tracked by Git).
- `.gitignore`: Specifies files and directories that Git should ignore.
- `requirements.txt`: Lists all Python dependencies for the project.

## Run the application using the command: 
uvicorn app.main:app --reload

## API Endpoints

- `POST /register`: Register a new user
- `POST /token`: Login and receive an access token
- `GET /profile`: Retrieve the current user's profile (protected route)

