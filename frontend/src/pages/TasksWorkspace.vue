<template>
  <div class="tasks-container">
    <div class="tasks-wrapper">
      
      <header class="header">
        <div class="header-info">
          <h1>Мои задачи</h1>
          <p v-if="tasks.length">У вас {{ tasks.length }} активных дел</p>
        </div>
        <router-link to="/tasks/new">
          <button class="add-btn">
            <span class="plus-icon">+</span>
            Новая задача
          </button>
        </router-link>
      </header>

      <div v-if="tasks.length === 0" class="empty-state">
        <div class="empty-icon">✨</div>
        <h3>Все чисто!</h3>
        <p>На сегодня задач больше нет. Можно отдохнуть.</p>
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
    console.error("Ошибка загрузки:", e)
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
  background: radial-gradient(circle at top right, #f8fafc, #eff6ff);
  padding: 40px 20px;
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
}

.tasks-wrapper {
  max-width: 900px;
  margin: 0 auto;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 40px;
}

.header h1 {
  font-size: 2.5rem;
  font-weight: 800;
  letter-spacing: -0.02em;
  color: #1e293b;
  margin: 0;
}

.header p {
  color: #64748b;
  margin-top: 5px;
}

.add-btn {
  background: #4f46e5;
  color: white;
  border: none;
  padding: 14px 28px;
  border-radius: 16px;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.3);
}

.add-btn:hover {
  transform: translateY(-2px);
  background: #4338ca;
  box-shadow: 0 20px 25px -5px rgba(79, 70, 229, 0.4);
}

.task-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
}

.empty-state {
  text-align: center;
  padding: 100px 20px;
  background: white;
  border-radius: 30px;
  border: 2px dashed #e2e8f0;
}

.empty-icon {
  font-size: 3rem;
  margin-bottom: 15px;
}

.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}
.list-enter-from {
  opacity: 0;
  transform: translateY(30px);
}
.list-leave-to {
  opacity: 0;
  transform: scale(0.9);
}

@media (max-width: 600px) {
  .header {
    flex-direction: column;
    align-items: flex-start;
    gap: 20px;
  }
  .add-btn {
    width: 100%;
    justify-content: center;
  }
}
</style>