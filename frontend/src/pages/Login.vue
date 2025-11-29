<template>
  <div class="login-page">
    <div class="login-card">
      <h2>Log In</h2>
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
  height: 100dvh;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #fcfcfc;
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
  font-weight: 600;
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

html, body {
  margin: 0;
  padding: 0;
  height: 100%;
  overflow: hidden; 
}
</style>
