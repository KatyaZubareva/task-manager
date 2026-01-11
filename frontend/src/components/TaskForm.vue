<template>
  <div class="tasks-container">
    <div class="tasks-wrapper">
      <h1>Новая задача</h1>

      <form @submit.prevent="createTask" class="form">
        <input v-model="title" placeholder="Заголовок" required />
        <textarea v-model="description" placeholder="Описание"></textarea>

        <button class="add-btn">Создать</button>
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
