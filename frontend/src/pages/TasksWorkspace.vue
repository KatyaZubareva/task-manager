<template>
  <div class="tasks-container">
    <div class="tasks-wrapper">
      
      <header class="header">
        <div class="header-info">
          <h1>My Tasks</h1>
          <p v-if="tasks.length">You have {{ tasks.length }} active tasks</p>
        </div>
        <router-link to="/tasks/new">
          <button class="add-btn">
            <span class="plus-icon">+</span>
            New Task
          </button>
        </router-link>
      </header>

      <div v-if="tasks.length === 0" class="empty-state">
        <h3>All Clear!</h3>
        <p>No more tasks for today. Time to relax.</p>
      </div>

      <div v-else class="task-grid">
        <TransitionGroup name="list">
          <TaskItem
            v-for="task in tasks"
            :key="task.id"
            :task="task"
            @delete="deleteTask"
            @toggle="toggleTask"
          />
        </TransitionGroup>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import TaskItem from '@/components/TaskItem.vue'

const tasks = ref([])

const loadTasks = async () => {
  try {
    const res = await fetch('http://localhost:8000/api/tasks', {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    })
    tasks.value = await res.json()
  } catch (e) {
    console.error("Loading error:", e)
  }
}

const deleteTask = async (id) => {
  await fetch(`http://localhost:8000/api/tasks/${id}`, {
    method: 'DELETE',
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
  })
  loadTasks()
}

const toggleTask = async (task) => {
  await fetch(`http://localhost:8000/api/tasks/${task.id}`, {
    method: 'PUT',
    headers: { 
      'Content-Type': 'application/json',
      Authorization: `Bearer ${localStorage.getItem('token')}`
    },
    body: JSON.stringify({
      ...task,
      completed: !task.completed
    })
  })
  loadTasks()
}

onMounted(loadTasks)
</script>

<style scoped>

.tasks-container {
  min-height: 100vh;
  width: 100%;
  background-color: #f9fafb;
  font-family: system-ui, -apple-system, sans-serif;
  color: #0b0b0b;
  padding: 60px 20px;
}

.tasks-wrapper {
  max-width: 900px;
  margin: 0 auto;
  margin-top: 8em;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 40px;
}

.header h1 {
  font-size: 36px;
  font-weight: 800;
  margin: 0;
}

.header p {
  color: #6c7a89;
  font-size: 16px;
  margin: 5px 0 0;
}

a {
  text-decoration: none;
}

.add-btn {
  background-color: #0b0b0b;
  text-decoration: none;
  color: white;
  padding: 12px 24px;
  border: none;
  border-radius: 1000px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  gap: 8px;
}

.add-btn:hover {
  background-color: #ff4500;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 69, 0, 0.2);
}

.task-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.empty-state {
  text-align: center;
  padding: 80px 20px;
  background: white;
  border-radius: 24px;
  border: 1px solid #e5e7eb;
}

.empty-icon {
  font-size: 40px;
  margin-bottom: 10px;
}

@media (max-width: 600px) {
  .header {
    flex-direction: column;
    align-items: flex-start;
    gap: 20px;
  }
}
</style>