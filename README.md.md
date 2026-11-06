# MotoPulse 🏍️

> **Motorcycle Maintenance Tracker and Alert System**  
> *Final Project for Data Structures (IT252) — Asia Pacific College*

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**MotoPulse** is a robust, console-based Python application designed to automate motorcycle maintenance tracking, log vehicle mileage, track historical expenses, and surface prioritized service alerts. Built around efficiency and strict algorithmic data structure principles, MotoPulse ensures motorcycle owners keep their vehicles road-worthy while mitigating mechanical failures.

---

## 📌 Context & Problem Statement

Motorcycles serve as a primary mode of transportation in the Philippines due to their affordability and maneuverability. However, many riders rely on memory or informal logs to manage maintenance routines (e.g., engine oil changes, brake inspections, drive belt/chain replacements). This disorganization leads to missed service intervals, premature component degradation, and increased road safety hazards.

### 🌐 UN Sustainable Development Goals (SDGs) Alignment
* **SDG 3 (Good Health & Well-Being):** Reduces preventable road accidents caused by poorly maintained components.
* **SDG 12 (Responsible Consumption & Production):** Promotes resource efficiency, extends vehicle lifespans, and minimizes waste.

---

## 🏗️ Architecture & Data Structures Breakdown

MotoPulse avoids inefficient list-traversals ($O(n)$) in critical paths by leveraging optimized core data structures:

| Data Structure | Code Location / Implementation | Operational Purpose | Complexity |
| :--- | :--- | :--- | :--- |
| **Hash Table (Dictionary)** | `AppState.users`, `User.motorcycles`, `Motorcycle.custom_intervals` | Instantaneous $O(1)$ lookup and retrieval of user accounts, registered vehicle records, and customized task intervals. | **Lookup:** $O(1)$<br>**Insert:** $O(1)$ |
| **Priority Queue (Heap)** | `Motorcycle.get_tasks_by_priority()` using Python's `heapq` | Dynamically surfaces the most urgent overdue maintenance task without re-sorting the entire list. | **Push/Pop:** $O(\log n)$ |
| **Stack (LIFO Array)** | `AppState.action_stack`, `undo_last_action()` | Captures state snapshots after critical operations to enable state reversal and user error correction. | **Push/Pop:** $O(1)$ |
| **Dynamic Array / List** | `Motorcycle.service_history` | Sequential historical record storage for servicing logs and total expense tracking. | **Traversal:** $O(n)$<br>**Sort:** $O(n \log n)$ |

---

## ⚡ Core Algorithm: Task Prioritization

Rather than executing standard array sorting algorithms ($O(n \log n)$) every time alerts are rendered, MotoPulse dynamically computes an **Urgency Score** for scheduled tasks and maintains a Min-Heap.

### Formula:
$$\text{Urgency Score} = (\text{Current Mileage} - \text{Due Mileage}) + \text{Days Overdue}$$

* Tasks with higher urgency scores surface immediately at the top of the Min-Heap queue.
* **Date Normalization:** Employs an intelligent date parsing algorithm (`standardize_date`) handling varied input patterns (e.g., `SEPT 15 2026`, `09/15/2026`).

---

## ✨ Features

- 🔑 **Secure Authentication:** User registration and login utilizing hashed credential management.
- 🛵 **Multi-Vehicle Registry:** Support for managing multiple motorcycles under a single user profile.
- 🚨 **Priority-Based Alerts:** Algorithmic task surface engine driven by urgency scores.
- 💵 **Expense Tracking:** Historical cost computation and service log management.
- ↩️ **Global Undo Mechanism:** Stack-backed action snapshots to revert erroneous entries seamlessly.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.8 or higher installed on your machine.

### Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/motopulse.git
   cd motopulse
   ```

2. **Run the Application:**
   ```bash
   python main.py
   ```

---

## 🛠️ Usage Flow

```text
[ Login / Register ] ──► [ Dashboard ] ──► [ Add Motorcycle ]
                                  │
      ┌───────────────────────────┴───────────────────────────┐
      ▼                                                       ▼
[ Schedule Task / Log Mileage ]                    [ View Prioritized Alerts ]
      │                                                       │
      └───────────────────────────┬───────────────────────────┘
                                  ▼
                    [ Log Completed Maintenance ]
                                  │
                                  ▼
                   [ Undo Action (Stack Reversal) ]
```

---

## 🧪 Testing & Edge Cases Handled

* **Intelligent Date Parsing:** Tested against diverse formats (`09/15/2026`, `SEPT 15 2026`, `2026-09-15`) with full fallback protection.
* **Empty Stack Handling:** Safe bounds-checking on the Undo functionality prevents application crashes when stack history is empty.
* **Data Persistence:** Robust structured JSON persistence preventing file corruption during state rewrites.

---

## 👥 Authors & Acknowledgments

**Proponents (NCTN - IT252):**
* **Evan Prens P. Exanes**
* **Rhona-Mae P. Prudenciado**

**Instructor:**
* Roselle Wednesday L. Gardon

*Asia Pacific College — June 2026*

---

## 📄 AI Transparency & Ethics Declaration

AI tools (ChatGPT, Claude, Gemini, Copilot) were strictly used for enhancing documentation clarity, optimizing CLI formatting, and standardizing code structure. All underlying algorithm logic, heap prioritization mechanics, and data structure selection were independently designed and verified by the authors.