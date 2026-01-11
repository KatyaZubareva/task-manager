<template>
  <div class="tasks-container">
    <div class="tasks-wrapper">
      
      <header class="header">
        <div class="header-info">
          <h1>My Tasks</h1>
          <p v-if="tasks.length">You have {{ tasks.length }} active tasks</p>
        </div>
        <router-link :to="{ name: 'TaskNew' }">
          <button class="add-btn">
            <span class="plus-icon">+</span>
            New Task
          </button>
        </router-link>
      </header>

      <div class="filters-section">
        <div class="filter-group">
          <label>Filter by status:</label>
          <select v-model="statusFilter" class="filter-select">
            <option value="all">All</option>
            <option value="completed">Completed</option>
            <option value="pending">Pending</option>
          </select>
        </div>

        <div class="filter-group">
          <label>Sort by:</label>
          <select v-model="sortBy" class="filter-select">
            <option value="date">Date</option>
            <option value="alphabet">Alphabet</option>
          </select>
        </div>
      </div>

      <div v-if="filteredAndSortedTasks.length === 0" class="empty-state">
        <h3>All Clear!</h3>
        <p>No more tasks for today. Time to relax.</p>
      </div>

      <div v-else class="task-grid">
        <TransitionGroup name="list">
          <TaskItem
            v-for="task in filteredAndSortedTasks"
            :key="task.id"
            :task="task"
            @delete="deleteTask"
            @toggle="toggleTask"
            @edit="editTask"
          />
        </TransitionGroup>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import TaskItem from '@/components/TaskItem.vue'

const router = useRouter()
const tasks = ref([])
const statusFilter = ref('all')
const sortBy = ref('date')

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

const filteredTasks = computed(() => {
  if (statusFilter.value === 'all') return tasks.value
  if (statusFilter.value === 'completed') return tasks.value.filter(t => t.completed)
  return tasks.value.filter(t => !t.completed)
})

const filteredAndSortedTasks = computed(() => {
  const filtered = [...filteredTasks.value]
  
  if (sortBy.value === 'alphabet') {
    return filtered.sort((a, b) => a.title.localeCompare(b.title))
  }
  
  return filtered.sort((a, b) => {
    const dateA = a.created_at ? new Date(a.created_at) : new Date(0)
    const dateB = b.created_at ? new Date(b.created_at) : new Date(0)
    return dateB - dateA
  })
})

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

const editTask = (task) => {
  router.push(`/tasks/${task.id}/edit`)
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

.filters-section {
  display: flex;
  gap: 20px;
  margin-bottom: 30px;
  padding: 20px;
  background: white;
  border-radius: 16px;
  border: 1px solid #eee;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.filter-group label {
  font-size: 14px;
  font-weight: 600;
  color: #6c7a89;
}

.filter-select {
  padding: 10px 16px;
  padding-right: 20px;
  border-radius: 12px;
  border: 1px solid #e5e7eb;
  background: #fdfdfd;
  font-family: inherit;
  font-size: 14px;
  cursor: pointer;
  outline: none;
  transition: border-color 0.2s;
}

.filter-select:focus {
  border-color: #ff4500;
}

@media (max-width: 600px) {
  .header {
    flex-direction: column;
    align-items: flex-start;
    gap: 20px;
  }
  
  .filters-section {
    flex-direction: column;
  }
}
</style>