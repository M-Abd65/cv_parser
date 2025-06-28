# 🧠 CV Parser App

A full-stack CV parser using **FastAPI**, **LangChain**, **PostgreSQL**, and a **React frontend**. Upload a CV (PDF/DOCX), extract structured data, and view results in a modern web interface.

## 🚀 Features

- ⚡ FastAPI backend for parsing and processing CVs
- 🧠 LangChain-powered CV extraction
- 🗄️ PostgreSQL + SQLAlchemy for data storage
- 🌐 Modern React frontend (with Tailwind CSS)
- 🐳 Docker support for streamlined deployment

---

## 🧑‍💻 Setup

### 📦 Without Docker

1. **Clone the repo**
   ```bash
   git clone https://github.com/M-Abd65/cv_parser.git
   cd cv-parser
   ```

2. **Set up the backend**

   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

3. **Set up the frontend**

   ```bash
   cd ../frontend
   npm install
   npm run dev
   ```

* Backend available at: `http://localhost:8000`
* Frontend available at: `http://localhost:5173`

---

### 🐳 With Docker (Recommended)

1. Make sure Docker and Docker Compose are installed:

   * [Install Docker](https://docs.docker.com/get-docker/)

2. Clone the repo and navigate to it:

   ```bash
   git clone https://github.com/M-Abd65/cv_parser.git
   cd cv-parser
   ```

3. Run the app:

   ```bash
   docker-compose up --build
   ```

4. App URLs:

   * **FastAPI backend** → `http://localhost:8000`
   * **React frontend** → `http://localhost:3000`

---

## ⚙️ Environment Variables

In the `frontend/` folder, create a `.env` file:

```env
VITE_API_URL=http://localhost:8000
```

In the `backend/` folder, create a `.env` or `.env.dev` with:

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/postgres
```

---

## 📝 Notes

* The Docker setup includes:

  * FastAPI backend
  * PostgreSQL database
  * React frontend
* Containers and database will auto-start with `docker-compose up`.

---

## 📂 Folder Structure

```
cv-parser/
│
├── backend/
│   ├── main.py              # FastAPI app
│   └── ...
│
├── frontend/
│   ├── src/
│   │   └── components/   # React components
│   ├── public/
│   ├── .env
│   └── ...
│
├── docker-compose.yml
└── README.md
```

---

## 📬 Contributing

Feel free to open issues or submit pull requests. Contributions are welcome!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).