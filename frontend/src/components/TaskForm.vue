<template>
  <div class="tasks-container">
    <div class="tasks-wrapper">
      <h1>{{ isEdit ? 'Edit Task' : 'New Task' }}</h1>

      <form @submit.prevent="submitTask" class="form">
        <input 
          v-model.trim="title" 
          placeholder="Title" 
          required 
          class="form-input"
        />
        <textarea 
          v-model.trim="description" 
          placeholder="Description"
          class="form-textarea"
        ></textarea>

        <div class="form-group">
          <label>Priority:</label>
          <select v-model="priority" class="form-select">
            <option value="low">Low</option>
            <option value="medium">Medium</option>
            <option value="high">High</option>
          </select>
        </div>

        <div class="form-group">
          <label>Category:</label>
          <div class="radio-group">
            <label class="radio-label">
              <input 
                type="radio" 
                v-model="category" 
                value="work"
                class="radio-input"
              />
              <span>Work</span>
            </label>
            <label class="radio-label">
              <input 
                type="radio" 
                v-model="category" 
                value="personal"
                class="radio-input"
              />
              <span>Personal</span>
            </label>
            <label class="radio-label">
              <input 
                type="radio" 
                v-model="category" 
                value="general"
                class="radio-input"
              />
              <span>General</span>
            </label>
          </div>
        </div>

        <div class="form-group">
          <label class="checkbox-label">
            <input 
              type="checkbox" 
              v-model="important"
              class="checkbox-input"
            />
            <span>Important</span>
          </label>
        </div>

        <button type="submit" class="add-btn">
          {{ isEdit ? 'Update' : 'Create' }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const props = defineProps({
  taskId: {
    type: Number,
    default: null
  }
})

const router = useRouter()
const route = useRoute()

const title = ref('')
const description = ref('')
const priority = ref('medium')
const category = ref('general')
const important = ref(false)
const completed = ref(false)
const isEdit = ref(false)

const loadTask = async () => {
  const id = props.taskId || route.params.id
  if (!id) return
  
  isEdit.value = true
  try {
    const res = await fetch(`http://localhost:8000/api/tasks/${id}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`
      }
    })
    const task = await res.json()
    title.value = task.title
    description.value = task.description
    priority.value = task.priority || 'medium'
    category.value = task.category || 'general'
    important.value = task.important || false
    completed.value = task.completed || false
  } catch (e) {
    console.error("Loading error:", e)
  }
}

const submitTask = async () => {
  const id = props.taskId || route.params.id
  const url = isEdit.value 
    ? `http://localhost:8000/api/tasks/${id}`
    : 'http://localhost:8000/api/tasks'
  const method = isEdit.value ? 'PUT' : 'POST'
  
  await fetch(url, {
    method,
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${localStorage.getItem('token')}`
    },
    body: JSON.stringify({
      title: title.value,
      description: description.value,
      priority: priority.value,
      category: category.value,
      important: important.value,
      completed: completed.value
    })
  })

  router.push('/tasks/workspace')
}

onMounted(() => {
  if (props.taskId || route.params.id) {
    loadTask()
  }
})
</script>

<style scoped>
.tasks-container {
  min-height: 100vh;
  background-color: #f9fafb;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  font-family: system-ui;
}

.tasks-wrapper {
  background: white;
  padding: 40px;
  border-radius: 30px;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
}

h1 {
  font-size: 32px;
  font-weight: 800;
  margin-bottom: 30px;
  text-align: center;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-input, .form-textarea {
  width: 100%;
  padding: 15px 20px;
  border-radius: 16px;
  border: 1px solid #e5e7eb;
  background: #fdfdfd;
  font-family: inherit;
  font-size: 16px;
  outline: none;
  transition: border-color 0.2s;
}

.form-input:focus, .form-textarea:focus {
  border-color: #ff4500;
}

.form-textarea {
  min-height: 120px;
  resize: vertical;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 5px;
}

.form-group label {
  font-size: 14px;
  font-weight: 600;
  color: #6c7a89;
}

.form-select {
  padding: 12px 16px;
  border-radius: 12px;
  border: 1px solid #e5e7eb;
  background: #fdfdfd;
  font-family: inherit;
  font-size: 14px;
  cursor: pointer;
  outline: none;
  transition: border-color 0.2s;
}

.form-select:focus {
  border-color: #ff4500;
}

.radio-group {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}

.radio-label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  font-weight: normal;
}

.radio-input {
  width: 18px;
  height: 18px;
  cursor: pointer;
  accent-color: #ff4500;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  font-weight: normal;
}

.checkbox-input {
  width: 18px;
  height: 18px;
  cursor: pointer;
  accent-color: #ff4500;
}

.add-btn {
  margin-top: 10px;
  background-color: #0b0b0b;
  color: white;
  padding: 16px;
  border: none;
  border-radius: 1000px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
}

.add-btn:hover {
  background-color: #ff4500;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 69, 0, 0.2);
}
</style>