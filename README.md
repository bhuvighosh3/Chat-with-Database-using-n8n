# 🤖 AI SQL Chat Agent (n8n + Postgres):

This project is an **AI-powered SQL assistant built with n8n**.  
Users can ask natural-language questions in chat, and the AI Agent converts them into SQL queries executed on a **PostgreSQL retail database**.

---

## ✨ Features:

- 💬 Chat-based interface using n8n Chat Trigger.
- 🧠 AI Agent that understands natural language.
- 🧮 Automatic SQL query generation.
- 🐘 PostgreSQL database integration.
- 🔄 Easily replaceable with MySQL or SQLite.
- 📊 Optimized for retail transaction data.

---

## 🧩 Workflow Overview:

The workflow contains four main components:

1. **💬 When Chat Message Received**  
   Triggers the workflow whenever a user sends a message in chat.

2. **🧠 AI Agent**  
   Interprets the user’s question, decides whether a database query is needed, and orchestrates the response.

3. **🤖 Groq Chat Model**  
   Acts as the LLM backend for reasoning and SQL generation.

4. **🐘 PostgreSQL (executeQuery)**  
   Executes AI-generated SQL queries and returns results to the agent.

---

## 🗄️ Database Structure

**Database:** `retaildb`

**Tables:**
- `year_2009_2010`
- `year_2010_2011`

**Common Columns:**
- `Invoice`
- `StockCode`
- `Description`
- `Quantity`
- `InvoiceDate`
- `Price`
- `Customer ID`
- `Country`

---

## 💡 Example Questions

Try asking the chat agent:

- “Which tables are available?”.
- “Show total revenue by country”.
- “Top 10 products by quantity sold”.
- “How many unique customers are there?”.

---

## ⚙️ Setup & Usage

1. Run **n8n** using Docker or locally.
2. Configure the **PostgreSQL credentials** in the Postgres node.
3. Ensure the retail tables exist in the database.
4. Open the **Chat panel** in n8n.
5. Start asking questions in natural language.

---

## 🔄 Extending the Workflow:

- Replace PostgreSQL with **MySQL** or **SQLite**.
- Add authentication to the chat endpoint.
- Store chat history using a Memory node.
- Add data visualization nodes after query execution.


