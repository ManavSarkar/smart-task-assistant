# Smart Task Assistant 
A modular, Python-based personal assistant powered by LLM agents. It lets you search and scrape the web for information, manage your to‑do list, and orchestrate these capabilities through a root agent interface.

---

## Features

- **Web Researcher Agent**: Perform Google searches via the Serper API, extract page titles, text, and links, then summarize results.
- **To‑Do Manager Agent**: Store, add, and list to‑do items in a SQLite database.
- **Root Agent**: Coordinates sub‑agents (`web_researcher` and `todo_manager`) to provide a seamless, multi‑task assistant.

---

## Directory Structure

```text
manavsarkar-smart-task-assistant/
├── __init__.py          # Package initialization
├── agent.py             # Defines LLM agents and orchestration
└── mytools/             # Custom tool implementations
    ├── __init__.py
    ├── scrapper.py      # HTML parsing with BeautifulSoup
    ├── todo.py          # SQLite to‑do list management
    ├── web_scrapper.py  # Combines search and scraping
    └── web_search.py    # Serper API wrapper for Google Search
```

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/manavsarkar-smart-task-assistant.git
   cd manavsarkar-smart-task-assistant
   ```
2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate     # Windows
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   > **Note:** You may need to create `requirements.txt` listing: `google-adk`, `requests`, `beautifulsoup4`, `python-dotenv`.

---

## Configuration

1. **Environment Variables**:  
   Create a `.env` file in the project root:
   ```dotenv
   SERPER_API_KEY=your_serper_api_key_here
   ```
2. **Database**:  
   The to‑do agent uses an SQLite database file named `todos.db` created automatically in the working directory.

---

## Usage

Run from the parent directory of the project:

```bash
adk web
```

---

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add new tool'`).
4. Push to your branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
