<div align="center">

# Library Management System — Python CLI Application
### Object-Oriented Architecture, State-Machine Borrowing Lifecycle & JSON Persistence

[![Python](https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Architecture](https://img.shields.io/badge/Design-Object--Oriented%20Programming-blueviolet.svg?style=for-the-badge)](https://en.wikipedia.org/wiki/Object-oriented_programming)
[![Persistence](https://img.shields.io/badge/Storage-JSON%20Persistence%20Layer-blue.svg?style=for-the-badge)](https://docs.python.org/3/library/json.html)
[![Interface](https://img.shields.io/badge/Interface-Interactive%20CLI%20HUD-4D4D4D.svg?style=for-the-badge&logo=gnubash&logoColor=white)](https://en.wikipedia.org/wiki/Command-line_interface)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

<p align="center">
  <b>A modular, object-oriented terminal application simulating end-to-end library circulation, member registries, and inventory analytics.</b><br>
  Built with clean domain encapsulation (`Book`, `Member`, `LibrarySystem`), transaction state guards, atomic JSON disk serialization, and real-time inventory telemetry.
</p>

---

</div>

## Executive Summary

Manual book tracking and physical paper registers suffer from operational vulnerabilities: lost borrow records, untracked inventory attrition, member over-allocations, and lack of real-time utilization statistics.

**Library Management System** is an extensible Python CLI application designed to automate institutional library workflows without the operational overhead of setting up a heavy SQL database engine. Built around pure **Object-Oriented Programming (OOP)** paradigms, the system models entity relationships through clean Python classes, protects inventory integrity with borrow-status invariants (preventing double-borrowing of active copies), and automatically updates JSON storage records across books, registered patrons, and circulation logs.

---

## Object-Oriented Domain Architecture & Transaction Flow

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              TERMINAL UI & ACTION DISPATCHER                           │
└────────────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                       ┌─────────────────────────┐
                       │   LibraryController     │
                       └─────────────────────────┘
                                    │
       ┌────────────────────────────┼────────────────────────────┐
       ▼                            ▼                            ▼
┌──────────────┐             ┌──────────────┐             ┌──────────────┐
│  Book Entity │             │ Member Entity│             │ Transaction  │
│  ISBN, Title,│             │ Member ID,   │             │ Borrow Date, │
│  Author,     │             │ Name, Active │             │ Due Date,    │
│  IsBorrowed  │             │ Borrowed List│             │ Return Status│
└──────────────┘             └──────────────┘             └──────────────┘
       │                            │                            │
       └────────────────────────────┼────────────────────────────┘
                                    │
                                    ▼
                       ┌─────────────────────────┐
                       │ JSON Persistence Engine │
                       └─────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
            ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
            │ `books.json` │ │`members.json`│ │ `trans.json` │
            └──────────────┘ └──────────────┘ └──────────────┘
```

---

## Core Technical Features

| Domain Module | Implementation Pattern | Operational Benefit |
|:---|:---|:---|
| **Encapsulated Data Model** | Pure Python OOP classes with private attributes and property getters/setters. | Enforces data encapsulation and business rule invariants. |
| **Borrow State Guard** | Pre-condition verification checking book availability flag and member borrow limits. | Eliminates double-issue conflicts and inventory desynchronization. |
| **Lightweight Persistence** | Structured file serialization storing operational entities in decoupled JSON documents. | Persistent state across sessions without requiring external DBMS daemons. |
| **Inventory Analytics** | Dynamic aggregation computing total volumes, active loans, and available shelf stock. | Provides instant operational visibility into library asset circulation. |
| **Interactive Terminal HUD** | Clean numeric menus with input sanitization and descriptive status prompts. | High usability and zero cognitive friction for library operators. |

---

## Quickstart & Local Execution

```bash
# Clone the repository
git clone https://github.com/vsbeginner/LibraryManagement.git
cd LibraryManagement

# Run using standard Python 3.x runtime (Zero dependencies required)
python main.py
```

### Example Interactive Session:
```text
====================================================
           LIBRARY MANAGEMENT SYSTEM
====================================================
1. Add New Book to Catalog
2. Register New Member
3. Borrow a Book
4. Return a Book
5. Generate Inventory Analytics Report
6. Exit System
----------------------------------------------------
Select an option (1-6): 5

====================================================
           LIBRARY INVENTORY ANALYTICS
====================================================
Total Cataloged Titles : 48
Registered Patrons     : 22
Actively Borrowed      : 14
Available on Shelves   : 34
Circulation Ratio      : 29.17%
====================================================
```

---

## Candidate Profile & Institutional Details

- **Candidate Name**: Vinayak Sharma
- **Enrollment / Roll No**: 2501940012
- **GitHub Profile**: [@vsbeginner](https://github.com/vsbeginner)
- **LinkedIn Profile**: [Vinayak Sharma](https://www.linkedin.com/in/vinayak-sharma-24a8aa384/)
- **Email Contact**: vsbeginner14@gmail.com
- **Degree Program**: Master of Computer Applications (MCA)
- **Institution**: Department of Computer Science & Engineering, K.R. Mangalam University

---

<div align="center">
  <sub>Developed for academic excellence and technical portfolio showcase. Licensed under the <a href="LICENSE">MIT License</a>.</sub>
</div>
