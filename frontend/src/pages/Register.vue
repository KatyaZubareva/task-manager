<template>
  <div class="register-page">
    <div class="register-card">

      <h2>Create an account</h2>
      <p class="subtitle">Start organizing your tasks smarter and faster.</p>

      <form @submit.prevent="register">

        <div class="input-group">
          <label>Email</label>
          <input type="email" v-model="email" required placeholder="you@example.com" />
        </div>

        <div class="input-group">
          <label>Password</label>
          <input type="password" v-model="password" required placeholder="••••••••" />
        </div>

        <div class="input-group">
          <label>Confirm password</label>
          <input type="password" v-model="confirm" required placeholder="••••••••" />
        </div>

        <button class="register-btn">Sign Up</button>

      </form>

      <p class="login-text">
        Already have an account?
        <router-link to="/login">Log in</router-link>
      </p>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const email = ref('')
const password = ref('')
const confirm = ref('')

const register = () => {
  if (password.value !== confirm.value) {
    alert('Passwords do not match')
    return
  }
  console.log('Registered:', email.value)
}
</script>

<style scoped>

h1 {
  font-size: 48px;
}

h2 {
  font-size: 24px;
}

h3 {
  font-size: 16px;
}

h4 {
  font-size: 18px;
}

p {
  font-size: 16px;
}

.register-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #fcfcfc;
  font-family: system-ui;
  padding: 20px;
}

.register-card {
  background: white;
  padding: 40px 35px;
  border-radius: 14px;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 8px 30px rgba(0,0,0,0.08);
  text-align: center;
}

.register-card h1 {
  font-size: 2.2em;
  margin-bottom: 10px;
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

.register-btn {
  width: 100%;
  padding: 14px;
  font-size: 1.1em;
  font-weight: bold;
  border-radius: 100px;
  border: none;
  color: white;
  background-color: #ff4500;
  cursor: pointer;
  transition: background-color 0.25s;
  box-sizing: border-box;
  margin-top: 10px;
}

.register-btn:hover {
  background-color: #e43f00;
}

.login-text {
  margin-top: 20px;
  font-size: 0.95em;
  color: #555;
}

.login-text a {
  color: #ff4500;
  font-weight: 600;
  text-decoration: none;
}

.login-text a:hover {
  text-decoration: underline;
}
</style>
