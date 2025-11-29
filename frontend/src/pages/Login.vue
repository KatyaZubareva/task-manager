<template>
  <div class="login-page">
    <div class="login-card">

      <h1>Log In</h1>
      <p class="subtitle">Welcome back! Enter your credentials to continue.</p>

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
import { ref } from 'vue'

const email = ref('')
const password = ref('')

const login = () => {
  console.log('Logged in with:', email.value)
}
</script>

<style scoped>
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #fcfcfc;
  font-family: system-ui;
  padding: 20px;
  height: 100vh;
  overflow: hidden;
}

.login-card input,
.login-card button {
  box-sizing: border-box;
}

.login-card {
  background: white;
  padding: 40px 35px;
  border-radius: 14px;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 8px 30px rgba(0,0,0,0.08);
  text-align: center;
}

.login-card h1 {
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
}

.input-group input:focus {
  border-color: #ff4500;
}

/* Кнопка логина */
.login-btn {
  width: 100%;
  background-color: #ff4500;
  color: white;
  border: none;
  padding: 14px;
  font-size: 1.1em;
  border-radius: 100px;
  cursor: pointer;
  transition: 0.25s;
  margin-top: 10px;
}

.login-btn:hover {
  background-color: #e43f00;
  transform: translateY(-2px);
}

.register-text {
  margin-top: 20px;
  font-size: 0.95em;
  color: #555;
}

.register-text a {
  color: #ff4500;
  font-weight: 600;
  text-decoration: none;
}

.register-text a:hover {
  text-decoration: underline;
}
</style>
