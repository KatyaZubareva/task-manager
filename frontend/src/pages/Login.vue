<template>
  <div class="login-page">
    <div class="login-card">
      <h2>Log In</h2>
      <p class="subtitle">Welcome back! Enter your credentials to continue.</p>

      <div v-if="showSuccessMessage" class="success-message">
        ✓ Registration successful! Please log in with your credentials.
      </div>

      <form @submit.prevent="login">
        <div class="input-group">
          <label>Email</label>
          <input type="email" v-model="email" required placeholder="you@example.com" />
        </div>

        <div class="input-group">
          <label>Password</label>
          <input type="password" v-model="password" required placeholder="••••••••" />
        </div>

        <button class="login-btn">Log In</button>
      </form>

      <p class="register-text">
        Don't have an account?
        <router-link to="/register">Sign Up</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const router = useRouter()
const showSuccessMessage = ref(false)

onMounted(() => {
  if (sessionStorage.getItem('registrationSuccess') === 'true') {
    showSuccessMessage.value = true
    sessionStorage.removeItem('registrationSuccess')
    
    setTimeout(() => {
      showSuccessMessage.value = false
    }, 5000)
  }
})

const login = async () => {
  const form = new FormData()
  form.append('username', email.value)
  form.append('password', password.value)

  const res = await fetch('http://localhost:8000/token', {
    method: 'POST',
    body: form
  })

  if (!res.ok) {
    alert('Invalid credentials')
    return
  }

  const data = await res.json()
  localStorage.setItem('token', data.access_token)

  router.push('/tasks')
}
</script>


<style scoped>

h2 {
  font-size: 24px;
}

p {
  font-size: 16px;
}

.login-page {
  height: 100dvh;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f9fafb;
  overflow: hidden;
  font-family: system-ui;
  padding: 0;
}

.login-card {
  background: white;
  width: 100%;
  max-width: 400px;

  padding: 40px 35px;
  border-radius: 14px;

  max-height: 90dvh;

  overflow-y: auto;

  box-shadow: 0 8px 30px rgba(0,0,0,0.08);
  text-align: center;
}

.login-card::-webkit-scrollbar {
  width: 0;
}

.subtitle {
  color: #6e6e6e;
  margin-bottom: 30px;
  font-size: 1.05em;
}

.input-group {
  text-align: left;
  margin-bottom: 20px;
}

.input-group label {
  display: block;
  margin-bottom: 6px;
  color: #333;
  font-weight: 500;
}

.input-group input {
  width: 100%;
  padding: 12px 14px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 1em;
  outline: none;
  transition: border 0.2s;
  box-sizing: border-box;
}

.input-group input:focus {
  border-color: #ff4500;
}

.login-btn {
  width: 100%;
  background-color: #ff4500;
  color: white;
  border: none;
  padding: 14px;
  border-radius: 100px;
  cursor: pointer;
  transition: 0.25s;
  margin-top: 10px;
  font-weight: bold;
  font-size: 1.1em;
}

.login-btn:hover {
  background-color: #e43f00;
  transform: translateY(-2px);
}

.register-text {
  margin-top: 20px;
  font-size: 14px;
  color: #555;
}

.register-text a {
  color: #ff4500;
  font-weight: 600;
}

.success-message {
  background-color: #d4edda;
  color: #155724;
  padding: 12px 16px;
  border-radius: 8px;
  margin-bottom: 20px;
  border: 1px solid #c3e6cb;
  font-size: 14px;
  text-align: left;
  animation: slideIn 0.3s ease;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow: hidden; 
}
</style>
