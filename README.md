# MotoPulse 🏍️

<div align="center">

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Data Structures](https://img.shields.io/badge/Data_Structures-Heaps_%7C_Stacks_%7C_HashMaps-blueviolet?style=for-the-badge)](#-architecture--data-structures-breakdown)

> **Motorcycle Maintenance Tracker and Alert System**  
> *Final Project for Data Structures and Algorithms (IT252) — Asia Pacific College*

</div>

---

**MotoPulse** is a robust, console-based Python application designed to automate motorcycle maintenance tracking, log vehicle mileage, track historical expenses, and surface prioritized service alerts. Built around computational efficiency and strict algorithmic data structure principles, MotoPulse ensures motorcycle owners keep their vehicles road-worthy while mitigating mechanical failures.

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
| **Priority Queue (Min-Heap)** | `Motorcycle.get_tasks_by_priority()` using Python's `heapq` | Dynamically surfaces the most urgent overdue maintenance task without re-sorting the entire list. | **Push/Pop:** $O(\log n)$ |
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

- 🔑 **Secure Authentication:** User registration and login utilizing hashed credential management (`hashlib.sha256`).
- 🛵 **Multi-Vehicle Registry:** Support for managing multiple motorcycles under a single user profile.
- 🚨 **Priority-Based Alerts:** Algorithmic task surface engine driven by urgency scores.
- 💵 **Expense Tracking:** Historical cost computation and service log management.
- ↩️ **Global Undo Mechanism:** Stack-backed action snapshots to revert erroneous entries seamlessly.

---

## 📁 Repository Structure

```
.
├── main.py            # Primary Application Entrypoint
├── MotoPulse_UI.py    # Console Interface & Menu Handler
├── MotoPulse_UX.py    # Core Domain Logic & Data Structures (Heap, Stack, HashMaps)
├── LICENSE            # MIT License
└── README.md          # Project Documentation
```

---

## 🚀 Getting Started

### Prerequisites
* Python 3.8 or higher installed on your machine.

### Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/rpprudenciado/Motorcycle-Maintenance-Tracker-and-Alert-System.git
   cd Motorcycle-Maintenance-Tracker-and-Alert-System
   ```

2. **Run the Application:**
   ```bash
   python main.py
   # Or directly:
   python MotoPulse_UI.py
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

**Proponents (NCTN - IT252, Asia Pacific College):**
* **Evan Prens P. Exanes**
* **Rhona-Mae P. Prudenciado** ([@rpprudenciado](https://github.com/rpprudenciado))
