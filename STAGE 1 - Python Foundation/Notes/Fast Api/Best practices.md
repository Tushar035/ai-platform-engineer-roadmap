Here’s a senior-level, production-ready guide to code practices for each FastAPI phase (1–9).
This is not just theory — it’s how experienced engineers structure and write clean, scalable code.


---

🚀 FastAPI Code Practices — Phase-wise (Production Guide)


---

📌 PHASE 1 — Basics (Routing, Params, Request Body)

✅ Best Practices

1. Separate Router Logic

# ❌ Bad
app = FastAPI()

@app.get("/users")
def get_users():
    pass

# ✅ Good
# routers/user.py
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_users():
    return []

# main.py
from fastapi import FastAPI
from routers import user

app = FastAPI()
app.include_router(user.router)


---

2. Always Use Pydantic Models

# ❌ Bad
@app.post("/user")
def create_user(name: str, age: int):
    pass

# ✅ Good
class UserCreate(BaseModel):
    name: str
    age: int


---

3. Use Clear Naming

get_user

create_user

update_user


👉 Avoid:

doStuff()



---

📌 PHASE 2 — Validation & Dependency Injection

✅ Best Practices

1. Centralize Dependencies

# dependencies/db.py
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


---

2. Reusable Validators

class User(BaseModel):
    password: str

    @validator("password")
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Weak password")
        return v


---

3. Avoid Business Logic in Routes

# ❌ Bad
@app.post("/user")
def create_user(user: User):
    db.add(user)

# ✅ Good
# services/user_service.py
def create_user(db, user):
    db.add(user)


---

📌 PHASE 3 — Security

✅ Best Practices

1. Never Hardcode Secrets

# ❌ Bad
SECRET_KEY = "123"

# ✅ Good
import os
SECRET_KEY = os.getenv("SECRET_KEY")


---

2. Always Hash Passwords

hashed_password = hash_password(user.password)


---

3. Use Token Expiry

expire = datetime.utcnow() + timedelta(minutes=30)


---

4. Separate Auth Logic

# services/auth.py
def authenticate_user():
    pass


---

📌 PHASE 4 — Data Modeling

✅ Best Practices

1. Separate Models & Schemas

# models/user.py (DB)
class User(Base):
    name = Column(String)

# schemas/user.py (API)
class UserResponse(BaseModel):
    name: str


---

2. Use Strong Types

from uuid import UUID
from pydantic import EmailStr

email: EmailStr
id: UUID


---

3. Avoid Deep Nesting

👉 Break into smaller models


---

📌 PHASE 5 — Database Integration

✅ Best Practices

1. Use Repository Pattern

# repositories/user_repo.py
def get_user(db, user_id):
    return db.query(User).filter(User.id == user_id).first()


---

2. Always Handle Transactions

try:
    db.commit()
except:
    db.rollback()


---

3. Use Alembic (Never manual DB changes)


---

4. Do NOT Use SQLite in Production

👉 Use PostgreSQL


---

📌 PHASE 6 — Async & Background

✅ Best Practices

1. Use Async Only for I/O

async def fetch_data():
    await http_call()


---

2. Avoid Blocking Code

# ❌ Bad
time.sleep(5)

# ✅ Good
await asyncio.sleep(5)


---

3. Use BackgroundTasks Carefully

👉 Only for light work
👉 Heavy work → Celery


---

📌 PHASE 7 — Headers, Cookies, Forms

✅ Best Practices

1. Validate Headers

def verify_token(x_token: str = Header()):
    pass


---

2. Secure Cookies

response.set_cookie(
    key="session",
    httponly=True,
    secure=True
)


---

3. Limit File Uploads

if file.size > 2MB:
    raise Exception("Too large")


---

📌 PHASE 8 — Responses & OpenAPI

✅ Best Practices

1. Always Use response_model

@app.get("/user", response_model=UserResponse)


---

2. Use Proper Status Codes

status_code=201


---

3. Never Return Sensitive Data

# ❌ password in response


---

4. Document All APIs


---

📌 PHASE 9 — Middleware & Lifecycle

✅ Best Practices

1. Keep Middleware Lightweight

# ❌ heavy DB call


---

2. Centralized Logging

logger.info("Request received")


---

3. Global Exception Handling


---

4. Use Lifespan for Resources

@asynccontextmanager
async def lifespan(app):
    yield


---

🧱 PRODUCTION PROJECT STRUCTURE (IMPORTANT 🔥)

app/
 ├── main.py
 ├── core/
 │    ├── config.py
 │    ├── security.py
 │
 ├── models/
 ├── schemas/
 ├── routers/
 ├── services/
 ├── repositories/
 ├── dependencies/
 ├── middleware/
 ├── utils/


---

🔥 CROSS-PHASE BEST PRACTICES


---

🧠 1. Follow Clean Architecture

Router → Service → Repository → DB



---

🧠 2. Use Environment Variables

DB URL

Secret keys



---

🧠 3. Logging Everywhere

Requests

Errors

DB operations



---

🧠 4. Write Tests

Unit tests

API tests



---

🧠 5. Use Type Hints Everywhere


---

🧠 6. Keep Functions Small

👉 One function = one responsibility


---

🏁 FINAL SUMMARY

Area	Key Practice

Routing	Use routers
Validation	Use Pydantic
Security	Hash + JWT
DB	Use repository pattern
Async	Non-blocking I/O
Middleware	Logging & security
Responses	Use response_model



---

🚀 What Next (Tech Lead Level)

If you want to go next level (very important for your career 🚀):

I can create:

✅ Enterprise FastAPI Architecture (like Netflix/Uber)
✅ System Design for your SaaS idea
✅ Full-stack (React + FastAPI + Auth + Payments)
✅ DevOps setup (Docker + CI/CD + Kubernetes)

Just tell me 👍