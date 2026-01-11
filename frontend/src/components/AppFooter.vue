<template>
  <footer class="app-footer">
    <div class="footer-content">
      <div class="footer-section">
        <h3>ClearBoard</h3>
        <p>Your task management solution</p>
      </div>
      
      <div class="footer-section">
        <h4>Links</h4>
        <router-link to="/">Home</router-link>
        <router-link to="/tasks/workspace">Tasks</router-link>
        <router-link to="/subscription">Subscription</router-link>
      </div>
      
      <div class="footer-section">
        <h4>About</h4>
        <p>&copy; 2026 ClearBoard. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
</script>

<style scoped>
.app-footer {
  background-color: #0b0b0b;
  color: white;
  padding: 40px 20px;
  margin-top: 60px;
  font-family: system-ui;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 40px;
}

.footer-section h3 {
  font-size: 24px;
  margin-bottom: 10px;
  color: #ff4500;
}

.footer-section h4 {
  font-size: 18px;
  margin-bottom: 15px;
}

.footer-section p {
  color: #999;
  font-size: 14px;
  line-height: 1.6;
}

.footer-section a {
  display: block;
  color: #ccc;
  text-decoration: none;
  margin-bottom: 8px;
  font-size: 14px;
  transition: color 0.2s;
}

.footer-section a:hover {
  color: #ff4500;
}

@media (max-width: 600px) {
  .footer-content {
    grid-template-columns: 1fr;
    gap: 30px;
  }
}
</style>
