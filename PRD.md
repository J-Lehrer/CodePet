# CodePet MVP - Product Requirements Document

**Project:** CodePet  
**Branch:** main  
**Description:** Gamified task tracker with evolving pixel pet

---

## User Stories

### US-001: Project scaffolding and app window
**Priority:** 1
**Status:** ✅ Complete

**Description:**  
As a user, I can launch CodePet and see the main application window.

**Acceptance Criteria:**
- [x] Python project structure with requirements.txt
- [x] CustomTkinter app launches with 900x700 window
- [x] Dark theme enabled by default
- [x] Window has title 'CodePet' and minimum size constraints
- [x] App runs without errors: `python main.py`

**Notes:**  
_None_

---

### US-002: SQLite database and schema
**Priority:** 2
**Status:** ✅ Complete

**Description:**
As a developer, I need persistent storage for tasks, user profile, and pet state.

**Acceptance Criteria:**
- [x] Database created in user data directory (platformdirs)
- [x] Tables: tasks, user_profile, pet_state
- [x] Tasks table supports parent_id for subtasks
- [x] Database singleton pattern with WAL mode
- [x] App runs without errors

**Notes:**  
_None_

---

### US-003: Main layout with sidebar and content area
**Priority:** 3
**Status:** ✅ Complete

**Description:**
As a user, I see a clean layout with pet display area and task list.

**Acceptance Criteria:**
- [x] Left sidebar (200px) for pet display and stats
- [x] Main content area for task list
- [x] Responsive grid layout that handles window resize
- [x] Visual separation between sections
- [x] App runs without errors

**Notes:**  
_None_

---

### US-004: Pet display with placeholder sprite
**Priority:** 4
**Status:** ✅ Complete

**Description:**
As a user, I see my pet displayed in the sidebar.

**Acceptance Criteria:**
- [x] Canvas widget in sidebar displays pet sprite
- [x] Placeholder pixel art (can be simple colored rectangle initially)
- [x] Pet name displayed below sprite
- [x] Current level and XP bar shown
- [x] App runs without errors

**Notes:**  
_None_

---

### US-005: Task list display
**Priority:** 5
**Status:** ✅ Complete

**Description:**
As a user, I can see my tasks in a scrollable list.

**Acceptance Criteria:**
- [x] Scrollable frame showing all tasks
- [x] Each task shows title and completion status
- [x] Completed tasks visually distinguished (strikethrough or dimmed)
- [x] Empty state message when no tasks exist
- [x] App runs without errors

**Notes:**  
_None_

---

### US-006: Add new task
**Priority:** 6  
**Status:** ❌ Not Started

**Description:**  
As a user, I can create a new task.

**Acceptance Criteria:**
- [ ] Add task button visible at top of task list
- [ ] Clicking opens input dialog or inline entry
- [ ] Task saved to database on submit
- [ ] Task list refreshes to show new task
- [ ] App runs without errors

**Notes:**  
_None_

---

### US-007: Complete task and earn XP
**Priority:** 7  
**Status:** ❌ Not Started

**Description:**  
As a user, I can mark a task complete and see XP awarded.

**Acceptance Criteria:**
- [ ] Checkbox or button to mark task complete
- [ ] Completing task awards XP (default 10)
- [ ] XP bar updates immediately
- [ ] Visual/text feedback showing XP earned
- [ ] Pet state saved to database
- [ ] App runs without errors

**Notes:**  
_None_

---

### US-008: Leveling system
**Priority:** 8  
**Status:** ❌ Not Started

**Description:**  
As a user, I level up when I earn enough XP.

**Acceptance Criteria:**
- [ ] XP threshold increases per level (polynomial curve)
- [ ] Level displayed in sidebar updates on level-up
- [ ] Visual celebration on level-up (text notification minimum)
- [ ] Level persisted to database
- [ ] App runs without errors

**Notes:**  
_None_

---

### US-009: Subtasks
**Priority:** 9  
**Status:** ❌ Not Started

**Description:**  
As a user, I can add subtasks under a parent task.

**Acceptance Criteria:**
- [ ] Tasks can be expanded to show subtasks
- [ ] Add subtask option on each task
- [ ] Subtasks indented visually under parent
- [ ] Completing subtask awards partial XP
- [ ] App runs without errors

**Notes:**  
_None_

---

### US-010: Pet evolution stages
**Priority:** 10  
**Status:** ❌ Not Started

**Description:**  
As a user, my pet evolves when I reach certain levels.

**Acceptance Criteria:**
- [ ] Pet has evolution stages: egg → baby → child → teen → adult
- [ ] Evolution triggers at levels 2, 5, 10, 20
- [ ] Pet appearance changes on evolution (placeholder graphics ok)
- [ ] Evolution celebration notification
- [ ] Evolution state persisted
- [ ] App runs without errors

**Notes:**  
_None_

---

## Progress Tracker

| US | Title | Status |
|----|-------|--------|
| US-001 | Project scaffolding and app window | ✅ |
| US-002 | SQLite database and schema | ✅ |
| US-003 | Main layout with sidebar and content area | ✅ |
| US-004 | Pet display with placeholder sprite | ✅ |
| US-005 | Task list display | ✅ |
| US-006 | Add new task | ❌ |
| US-007 | Complete task and earn XP | ❌ |
| US-008 | Leveling system | ❌ |
| US-009 | Subtasks | ❌ |
| US-010 | Pet evolution stages | ❌ |
