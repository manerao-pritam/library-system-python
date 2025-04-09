### Stack for undo/redo
Stack for undo/redo actions of borrowing/returning item

⸻

🔄 Basic idea

You can think of undo/redo as two stacks:
	•	Undo stack: stores actions that have been done and can be undone.
	•	Redo stack: stores actions that have been undone and can be redone.

⸻

	•	undo_stacks: Dict[MemberID, Stack[Action]]
	•	redo_stacks: Dict[MemberID, Stack[Action]]

⸻

📚 For your library system:

Let’s say you’re tracking actions like:
	•	Member borrows a book
	•	Member returns a book

Every time a member performs an action, you push a record of that action onto the undo stack. If the user then hits Undo, you:
	1.	Pop from the undo stack
	2.	Reverse the action (e.g., if they borrowed a book, you “return” it)
	3.	Push that reversed action onto the redo stack

Similarly, if the user hits Redo:
	1.	Pop from the redo stack
	2.	Re-apply the action
	3.	Push it back onto the undo stack

⸻

🧠 What goes in the stack?

Each stack element could be a small object or tuple that describes:
	•	The type of action: borrow or return
	•	The member ID
	•	The book ID
	•	Maybe a timestamp, if needed

This way, you know what happened and how to reverse it.

⸻

🔄 Resetting Redo Stack

Important detail: anytime the user performs a new action (not a redo), you should clear the redo stack—because the future changed.

⸻

✅ Benefits of using stacks:
	•	Easy LIFO (last-in, first-out) behavior for undo/redo.
	•	You can limit the size of stacks if you want to cap history.
	•	Very intuitive, matches user mental model.

⸻

### Queue to maintaining borrow requests for unavailable items

⸻

📕 Scenario:

Let’s say a book or magazine is currently checked out. Other members still want it, so you want to let them “wait in line”—classic queue behavior.

⸻

🧾 Why a queue?
	•	First-come, first-served: whoever requested the book first should get it first.
	•	A queue gives you that perfect FIFO (first-in, first-out) behavior.

⸻

🧠 How it works:
	1.	Book is checked out → not available.
	2.	Member requests it → you add their member ID to the wait queue for that book.
	3.	When the book is returned:
	•	You check if the wait queue for that book is non-empty.
	•	If it is, you dequeue the next member and notify them (or auto-assign depending on your flow).

⸻

📚 Data structure-wise:

You can have a waitlist map:

book_id → queue of member_ids

Each unavailable book has its own queue of members waiting for it.

⸻

Bonus thoughts:
	•	You could even add timestamps to each entry if you need more detailed logs or for debugging fairness.
	•	Want to let someone give up their spot? Just remove them from the queue.
	•	If you allow holds to expire, you could combine a queue with a timer or scheduling system.

⸻
