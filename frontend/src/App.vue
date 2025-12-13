<script setup>
import { useCookies } from 'vue3-cookies';
import { ref } from 'vue';

const { cookies } = useCookies()

const acceptCookies = () => {
  cookies.set('cookies_accepted', true)
  showBanner.value = false
}

const rejectCookies = () => {
  cookies.set('cookies_accepted', false)
  showBanner.value = false
}

const showBanner = ref(!cookies.get('cookies_accepted'))
</script>

<template>
  <nav class="header">
    <div class="header-content">
      <div class="logo">
        <img src="./assets/logo_header.png" class="logo-header">
        <h2>ClearBoard</h2>
      </div>

      <div class="navigation">
        <h3><router-link to="/">Home</router-link></h3>
        <h3><router-link to="/tasks">Tasks</router-link></h3>
        <h3><router-link to="/subscription">Subscription</router-link></h3>
      </div>

      <div class="auth-buttons">
        <router-link to="/login">
          <button class="btn login-nav-btn">Login</button>
        </router-link>

        <router-link to="/register">
          <button class="btn register-btn">Create account</button>
        </router-link>
      </div>
    </div>
  </nav>

  <div class="cookie-banner" v-if="showBanner">
    <div>
      <h4 class="cookie-header">We use cookies!</h4>
      <p class="cookie-text">
        We use cookies to enhance your experience and improve our service.
        By continuing to browse, you agree to our use of cookies.
      </p>
    </div>

    <button class="cookie-button reject" @click="rejectCookies">Reject</button>
    <button class="cookie-button" @click="acceptCookies">Agree</button>
  </div>

  <router-view />
</template>

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

nav {
  font-family: system-ui;
}

.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  padding: 15px 30px;
  background-color: #ffffff;
  border-bottom: #e8e8e8 solid 1px;
  color: black;
  z-index: 1000;
}

.header-content {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.logo h2 {
  margin: 0;
  padding-left: 0.5em;
  font-size: 18px;
}

.logo-header {
  width: 2em;
  height: 2em;
}

.navigation {
  display: flex;
  gap: 2em;
  align-items: center;
}

.navigation h3 {
  margin: 0;
}

.navigation a.router-link-active {
  color: #ff4500;
  font-weight: 600;
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
  font-size: 14px;
  border-radius: 100px;
  border: none;
  cursor: pointer;
  transition: 0.2s;
  font-weight: 600;
  font-family: system-ui;
  line-height: 1.2;
}

.login-nav-btn {
  background: none;
  color: rgb(0, 0, 0);
  padding: 10px 25px;
  border-radius: 50px;
  border: none;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
}

.login-nav-btn:hover {
  transform: translateY(-2px);
  color: #e03f00;
}


.register-btn {
  background-color: black;
  color: white;
}

.register-btn:hover {
  background-color: #ff4500;
}

.cookie-banner {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  width: 90%;
  max-width: 850px;
  background: #ffffff;
  color: rgb(0, 0, 0);
  padding: 10px 25px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  font-family: system-ui;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.167);
  z-index: 2000;
  animation: fadeInUp 0.4s ease;
}

.cookie-header {
  margin-bottom: 0.5em;
}

.cookie-text {
  flex: 1;
  font-family: system-ui;
  font-size: 14px;
  line-height: 1.45;
  opacity: 0.9;
}

.cookie-button {
  background: #ff4500;
  color: white;
  border: none;
  padding: 12px 25px;
  border-radius: 50px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.25s ease, transform 0.2s ease;
}

.cookie-button:hover {
  background: #e03f00;
  transform: translateY(-1px);
}

.reject {
  background: none;
  border: #e03f00 solid 1px;
  color: #e03f00;
}

.reject:hover {
  background: rgba(224, 63, 0, 0.1);
  color: #e03f00;
  border-color: #e03f00;
  transform: translateY(-1px);
}

@media (max-width: 600px) {
  .cookie-banner {
    flex-direction: column;
    text-align: center;
    padding: 20px;
  }

  .cookie-button {
    width: 100%;
  }
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translate(-50%, 20px);
  }
  to {
    opacity: 1;
    transform: translate(-50%, 0);
  }
}
</style>
