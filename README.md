# Day 29 — Introduction to pandas
**Roadmap:** 84-Day Python & Advanced Excel Mastery | Phase 2

## Overview
Introduced pandas as the primary data analysis library. Covered Series (1-D) vs DataFrame (2-D), loading multi-sheet Excel files, and all core exploration methods.

## Files
| File | Purpose |
|---|---|
| `Day29_Pandas_Practice.xlsx` | Practice dataset — 3 sheets: Stock Portfolio, Monthly Expenses, Company Financials |
| `Day29_Pandas_Intro.py` | Full practice code covering all 6 sections |

## Concepts Covered
- `pd.Series` — 1-D labeled array with index and name
- `pd.DataFrame` — 2-D table; collection of Series on a shared index
- `pd.read_excel()` — loading single sheet and all sheets (`sheet_name=None`)
- `.head()`, `.tail()` — preview rows
- `.shape`, `.columns`, `.dtypes` — structural metadata
- `.info()` — non-null counts, dtype summary, memory usage
- `.describe()` — statistical summary for numeric columns
- `.isnull().sum()` — missing value audit per column
- Column selection: single `df["col"]` → Series; multiple `df[["a","b"]]` → DataFrame
- `.unique()`, `.value_counts()` — categorical exploration

## Key Observation
Formula-only cells (Market_Value, P&L, Return_%) show NaN in pandas because `.xlsx` formula results are not cached until opened in Excel/LibreOffice. Raw input columns load correctly. This is expected behaviour.

## Portfolio Connection
Directly feeds into **Portfolio Project 1 (Day 78)** — Financial Dashboard requires reading and exploring multi-sheet Excel data before any analysis or visualization.

## Status
- [x] Practice sheet built
- [x] All 6 code sections tested and passing
- [x] Daily tasks completed (in progress)
