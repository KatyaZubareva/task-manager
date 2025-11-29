<template>
  <div class="tasks-page">

    <div class="tasks-header">
      <h1>Today's Tasks</h1>
      <p class="subtitle">Stay focused and track your progress</p>

      <input class="task-input" placeholder="Add a new task..." />
    </div>

    <div class="tasks-list">
      <div class="task-item" v-for="task in tasks" :key="task.id">
        
        <div class="task-main">
          <span class="task-status" :class="task.statusClass">{{ task.status }}</span>

          <h2>{{ task.title }}</h2>
          <p>{{ task.description }}</p>
        </div>

        <div class="task-buttons">
          <button class="pill-btn done">✓ Mark done</button>
          <button class="pill-btn delete">✕ Delete</button>
        </div>

      </div>
    </div>

  </div>
</template>

<script setup>
const tasks = [
  { id: 1, title: "Create UI layout", description: "Design the main components for the task manager.", status: "Pending", statusClass: "pending" },
  { id: 2, title: "Add authentication", description: "Implement secure login system.", status: "In Progress", statusClass: "progress" },
  { id: 3, title: "Fix routing bug", description: "Switch between pages without reload.", status: "Review", statusClass: "review" },
  { id: 4, title: "Connect database", description: "Link backend API to the database.", status: "Blocked", statusClass: "blocked" },
  { id: 5, title: "Write documentation", description: "Explain how everything works.", status: "Done", statusClass: "done" }
];
</script>

<style scoped>
/* Layout */
.tasks-page {
  max-width: 800px;
  margin: 0 auto;
  padding: 50px 20px;
  font-family: system-ui;
}

/* Header */
.tasks-header {
  text-align: center;
  margin-bottom: 30px;
}

.tasks-header h1 {
  font-size: 2.6em;
  margin-bottom: 5px;
  color: #1c1c1c;
}

.subtitle {
  color: #6b6b6b;
  font-size: 1.1em;
  margin-bottom: 20px;
}

.task-input {
  padding: 14px 20px;
  width: 100%;
  max-width: 480px;
  border-radius: 50px;
  border: 1px solid #ddd;
  outline: none;
  font-size: 1em;
  margin-top: 10px;
  transition: 0.2s;
  box-sizing: border-box;
}

.task-input:focus {
  border-color: #ff4500;
  box-shadow: 0 0 0 3px rgba(255,69,0,0.15);
}

/* Tasks list */
.tasks-list {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

/* Task card */
.task-item {
  background: #ffffff;
  padding: 25px;
  border-radius: 18px;
  box-shadow: 0 6px 22px rgba(0,0,0,0.06);
  transition: 0.25s ease;
}

.task-item:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 28px rgba(0,0,0,0.08);
}

.task-main h2 {
  margin: 6px 0 8px;
}

.task-main p {
  color: #606b75;
}

/* Status styles */
.task-status {
  display: inline-block;
  padding: 5px 14px;
  border-radius: 50px;
  font-size: 0.8em;
  font-weight: 600;
  margin-bottom: 8px;
}

.pending { background: #ffe1cd; color: #b53800; }
.progress { background: #cfe7ff; color: #0054b8; }
.review { background: #fff3c9; color: #a88a00; }
.blocked { background: #ffd2d2; color: #9f1e1e; }
.done { background: #dff5d8; color: #1e7c22; }

/* Buttons */
.task-buttons {
  margin-top: 18px;
  display: flex;
  gap: 12px;
}

.pill-btn {
  border: none;
  padding: 10px 22px;
  border-radius: 50px;
  font-size: 0.95em;
  cursor: pointer;
  transition: 0.2s;
  font-weight: 500;
  color: white;
}

.pill-btn.done {
  background: #ff4500;
}
.pill-btn.done:hover {
  background: #e03f00;
}

.pill-btn.delete {
  background: #d9534f;
}
.pill-btn.delete:hover {
  background: #c74745;
}
</style>
