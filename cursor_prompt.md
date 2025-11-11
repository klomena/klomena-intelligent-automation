PROMPT FOR CURSOR: BUILDING KLOMENA
You are my senior technical cofounder and lead engineer for a new product called Klomena.
I am a non-technical founder, so I need you to:
Propose and create the project structure.
Generate code, configs, and documentation.
Explain key decisions in simple language.
Help me iterate towards a working MVP that we can test with real parents and vendors.
Please read this entire brief carefully and then:
Propose a repo structure.
Scaffold the initial codebase.
Implement the first working slice end-to-end.
1. What Klomena Is
Klomena is an intelligent automation platform for family celebrations, starting with kids’ birthdays and events.
It is not a generic chatbot.
It is:
A chat-first celebration concierge that helps parents plan kids’ events by:
Understanding their needs (age, area, budget, theme, date),
Matching them with relevant local vendors,
Suggesting add-ons (decor, entertainment, photographer, etc.),
Coordinating basic next steps (inquiries, reminders).
In later phases it will integrate with:
WhatsApp
Instagram DM
ChatGPT (Actions)
Web chat widget
For now, we will build a web + API MVP that can later power all channels.
2. MVP Scope (6–8 week style, but we want the core in this repo)
Focus on one main use case:
Parent: “I want to plan a [theme] birthday for my [age] year old in [area] with a budget of [X]. What are my options?”
The system should:
Parse that intent (age, area, budget, theme).
Look up vendors and services in a database.
Rank and return 3–6 vendor options, with:
short description
approximate price band
why they matched (age/theme/area/budget)
Suggest 2–4 relevant add-ons (e.g. face painting, balloons, backdrop, photographer).
We also want:
A simple admin-style way (for now: scripts or a minimal UI) to:
Seed vendors.
Approve/edit their capabilities.
We do not need full bookings, payments, or multi-city complexity yet.
3. Core IP: Celebration Graph™ + Vendor DNA (MVP version)
We want to start building our defensible IP in the code:
3.1 Celebration Graph™ v0.1
A lightweight domain model that encodes:
Node types (as tables or enums):
AgeGroup (e.g. 1–2, 3–5, 6–8, 9–12)
Theme (Mermaid, Unicorn, Football, Space, etc.)
Activity (Magician, Balloon Décor, Face Painting, Soft Play, Games Host)
VenueType (Home, Café, Play Area, Park)
AddOn (Photographer, Backdrop, Invitations, Favors)
BudgetTier (Low / Medium / Premium)
Area/City (e.g. Dbaye, Beirut, Dubai, Jumeirah…)
Edges (relationships) can be represented as simple tables with weights, e.g.:
SUITABLE_FOR: Activity ↔ AgeGroup (e.g. FacePainting ↔ Age 3–7)
COMPLEMENTS: Theme ↔ AddOn (e.g. Mermaid ↔ Balloon Décor)
PRICE_FIT: Activity/AddOn ↔ BudgetTier
(You can store these as rows in a graph_edges table.)
We don’t need a full graph DB yet.
A simple Postgres schema is fine for v0.1.
3.2 Vendor DNA v0.1
For each vendor, store:
id
name
areas_served[]
categories[] (e.g. Balloon Decor, Cake, Magician)
themes[] they support
price_band (1=budget, 2=mid, 3=premium)
age_min, age_max
is_verified (bool)
Optional: response_time_score, freshness_score (placeholders for later)
We should be able to:
Seed some vendors via a JSON/CSV file.
Load them into the DB.
Query them based on:
area
age
theme
budget
4. Tech Stack Preferences
Please choose a boring, reliable, well-documented stack.
Suggested stack (feel free to propose alternatives, but explain):
Backend API:
Python + FastAPI
or Node.js + NestJS
Database:
PostgreSQL (with a schema for vendors, graph edges, interactions)
Search / ranking (for now):
Simple SQL filters + scoring function in code.
Later we can add embeddings/pgvector.
Frontend:
Simple React or Next.js app with:
Parent-facing chat-like interface (even basic).
Admin/vendor list view (simple table).
LLM usage (MVP):
Use OpenAI API (or abstract via an llm_client) to:
Parse parent free-text requests into structured fields:
age
area
budget
theme
For now, we can fake or stub this with simple regex/heuristics if needed.
Environment:
.env file for secrets.
Clear README with setup instructions.
5. API Design (First Endpoints)
Please implement these endpoints first:
POST /parse-intent
Input: { "message": "I want a unicorn party for my 6 year old in Dbaye with $300 budget" }
Output:
{
  "age": 6,
  "area": "Dbaye",
  "theme": "Unicorn",
  "budget_amount": 300,
  "budget_tier": "medium"
}
POST /plans/search
Input: { "age": 6, "area": "Dbaye", "theme": "Unicorn", "budget_tier": "medium" }
Logic:
Find vendors in/near area.
Filter by age suitability.
Filter by theme/capabilities.
Score by:
capability match
area match
price band fit
Return 3–6 best vendors with a why_matched string.
Output example:
[
  {
    "vendor_id": "v_1",
    "name": "Unicorn Dreams Decor",
    "price_band": 2,
    "areas_served": ["Dbaye","Jounieh"],
    "services": ["Balloon Decor","Backdrop","Themed Table"],
    "why_matched": [
      "Serves Dbaye",
      "Specialized in Unicorn decor",
      "Mid-range pricing fits your budget"
    ]
  }
]
POST /addons/recommend
Input: { "age": 6, "theme": "Unicorn", "budget_tier": "medium" }
Use Celebration Graph edges (rules) to suggest 2–4 add-ons.
Output example:
[
  { "name": "Face Painting", "reason": "Popular for ages 4–7 with Unicorn theme" },
  { "name": "Photographer", "reason": "Helps capture the moment" }
]
GET /vendors
Simple list view for debugging/admin.
Pagination not required for now.
6. Frontend MVP
Please generate a very simple Web UI:
A single-page web app with:
A text box where a parent can type a request.
A “Plan my event” button.
On submit:
Call /parse-intent
Call /plans/search and /addons/recommend
Display:
Parsed info (age, area, theme, budget).
Vendor cards (name, summary, why_matched).
Add-on suggestions.
A basic Admin tab or route that:
Lists all vendors from /vendors.
Shows their themes, price band, areas.
(Later we can add editing; for now, view-only is OK.)
No need for fancy styling. Clean and readable is enough.
7. What I Want From You First
Propose the project structure in plain text:
Backend folder(s), frontend, shared, configs, etc.
Create the backend skeleton:
API server
DB models
Seed script to load sample vendors and graph edges.
Implement /plans/search and /addons/recommend with hard-coded/demo data first.
Then progressively:
Wire DB.
Implement /parse-intent (you can stub the LLM call; just define where it would go).
Build the simple frontend UI.
At each step:
Explain briefly (in comments or markdown) what you’re doing and why.
Use clear file and function names.
8. Style & Constraints
Code should be:
Well-organized
Commented where logic is non-trivial
Easy for a non-technical founder to follow with your guidance.
Prefer explicit logic over clever hacks.
Avoid heavy dependencies unless necessary.
First Action
Please respond by:
Proposing a repo structure.
Generating the initial backend project with:
Main server file
DB connection
Data models for:
vendors
services (if separate)
graph_edges
Add a seed script with a few sample vendors and graph edges (for 1 city, e.g. Dbaye / Beirut).
Then we will iterate from there.
