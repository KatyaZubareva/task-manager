<template>
  <div class="tasks-container">
    <div class="tasks-wrapper">
      <h1>New Task</h1>

      <form @submit.prevent="createTask" class="form">
        <input v-model="title" placeholder="Title" required />
        <textarea v-model="description" placeholder="Description"></textarea>

        <button class="add-btn">Create</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const title = ref('')
const description = ref('')
const router = useRouter()

const createTask = async () => {
  await fetch('http://localhost:8000/api/tasks', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${localStorage.getItem('token')}`
    },
    body: JSON.stringify({
      title: title.value,
      description: description.value,
      completed: false
    })
  })

  router.push('/tasks')
}
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
  gap: 15px;
}

input, textarea {
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

input:focus, textarea:focus {
  border-color: #ff4500;
}

textarea {
  min-height: 120px;
  resize: vertical;
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