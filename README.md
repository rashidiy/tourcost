# TourCost

TourCost is a Python project built using the aiogram library for creating a Telegram bot. It helps users manage tour costs and provides localization support through the use of locales.

## Dependencies
- Python >= 3.11
- aiogram >= 3.2.0
- python-dotenv >= 1.0.0
- sqlalchemy (with asyncio support) >= 2.0.23
- aiosqlite >= 0.19.0
- alembic >= 1.13.1

## Project Structure
```
tourcost/
├── database/
│   └── models/
├── db_versions/
│   └── versions/
├── handlers/
├── locales/
│   ├── ru/
│   │   └── LC_MESSAGES/
│   └── uz/
│       └── LC_MESSAGES/
└── utils/
```

## Description
- **database/**: Houses database-related functionalities and models.
- **db_versions/**: Contains database migration scripts.
- **handlers/**: Implements Telegram bot message handlers.
- **locales/**: Stores localization files for different languages.
- **utils/**: Holds utility functions used throughout the project.

## Usage
1. Clone the repository.
2. Install dependencies using `poetry install`.
3. Set up your Telegram bot token and other configurations in a `.env.copy` file (you should clone .env.copy to .env).
4. Run the bot using `python app.py`.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
