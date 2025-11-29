<script setup>
</script>

<template>
  <nav class="header">
    <div class="logo">
      <h2>ClearBoard</h2>
    </div>

    <div class="navigation">
      <h3><router-link to="/">Home</router-link></h3>
      <h3><router-link to="/tasks">Tasks</router-link></h3>
    </div>

    <div class="auth-buttons">
      <router-link to="/login">
        <button class="btn login-nav-btn">Login</button>
      </router-link>

      <router-link to="/register">
        <button class="btn register-btn">Create account</button>
      </router-link>
    </div>
  </nav>

  <div class="nav-spacer"></div>

  <router-view />
</template>

<style scoped>

nav {
  font-family: system-ui;
}

.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;

  display: flex;
  justify-content: space-between;
  align-items: center;

  padding: 15px 30px;
  background-color: #ffffff;
  border-bottom: #e8e8e8 solid 1px;
  color: black;

  z-index: 1000;
}

.nav-spacer {
  height: 80px;
}

.logo h2 {
  margin: 0;
  padding-left: 0.5em;
}

.navigation {
  display: flex;
  gap: 2em;
  align-items: center;
}

.navigation h3 {
  margin: 0;
}

a {
  text-decoration: none;
  color: black;
}

a:hover {
  color: #ff4500;
}

.auth-buttons {
  display: flex;
  gap: 10px;
  align-items: center;
  margin-right: 4em;
}

.btn {
  padding: 10px 20px;
  font-size: 0.95em;
  border-radius: 100px;
  border: none;
  cursor: pointer;
  transition: 0.2s;
  font-weight: 600;
  font-family: system-ui;
  line-height: 1.2;
}

.login-nav-btn {
  color: black;
}

.login-nav-btn:hover {
  color: #ff4500;
}

.register-btn {
  background-color: black;
  color: white;
}

.register-btn:hover {
  background-color: #ff4500;
}
</style>
