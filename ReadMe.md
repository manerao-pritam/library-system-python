# 📚 Library System (Data Structures Practice in Python)

This project is a **practice-based library management system** built in Python, focused on implementing and applying **core data structures** such as **stacks**, **queues**, **sets**, and **dictionaries**.

The purpose of this repo is **not** to build a full-fledged library system, but to explore how different data structures can be used to manage and organize real-world logic in a clean and efficient way.

---

## 🚀 Features

- **Member Borrow/Return Logic** using `set`, `dict`, and `custom classes`
- **Undo / Redo functionality** per member using a custom `Stack` implementation
- **Waitlisting** system for unavailable books using a `Queue`
- **Action tracking** using dictionaries to encapsulate actions like `borrow`, `return`, `request`, and `cancel_request`
- Proper validation and error handling for user actions
- Clean OOP structure with extensible classes like `Library`, `Member`, `LibraryItem`, etc.

---

## 🧠 Data Structures Practiced

| Feature | Data Structure |
|--------|----------------|
| Tracking borrowed items | `set()` |
| Undo/Redo actions       | Custom `Stack` |
| Waitlist queue per item | Custom `Queue` |
| Action history/log      | `list`, `dict` |
| Members, Items lookup   | `dict` |

---

## 🔧 Technologies

- Python 3.10+
- Custom class-based data structure implementations (no external libraries)
- PyCharm IDE (for development)

---

## 📂 Project Structure (WIP)

library-system/ <br />
├── library.py <br />
├── member.py <br />
├── library_item.py <br />
├── stack.py <br />
├── queue.py <br />
├── borrow_record.py <br />
├── constants.py <br />
├── init.py <br />
└── …

---

## 📝 How to Run

1. Clone the repo:

```bash
git clone git@github.com:manerao-pritam/library-system-python.git
cd library-system
```

2.	Run from PyCharm or your preferred Python environment.
3.	This is not a packaged app — it’s meant for exploring logic and learning.

⸻

🎯 Future Ideas (Stretch Goals)
	•	Storing Borrowing History records as linked list  
	•	Some simple front-end
	•	Integrate persistent storage (SQLite or PostgreSQL)

⸻

🙌 Why This Project?

This repo started as a small practice project and evolved into a great hands-on way to learn and apply data structures in Python with real-world context. If you’re learning Python and want to go beyond LeetCode, this is a great way to see how DS concepts power real logic.

⸻

📬 Feedback / Suggestions?

Feel free to open issues or PRs if you have suggestions, improvements, or want to build on top of this!

⸻

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---