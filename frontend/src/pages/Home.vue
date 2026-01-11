<template>
  <div class="hero-main">
    <div class="hero-section">
      <img class="hero-icon" src="./../assets/logo.png" />

      <h1>
        A smarter way to get<br />
        <span>things done</span>
      </h1>

      <p class="hero-description">
        Simplify your workflow, manage tasks efficiently, and achieve your goals faster.
        Start your journey to better productivity today!
      </p>

      <router-link to="/tasks">
        <button class="cta-button">Go to tasks</button>
      </router-link>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
/* Основной контейнер на весь экран */
.hero-main {
  min-height: 100vh;
  width: 100%;
  background-color: #f9fafb;
  display: flex;
  justify-content: center;
  align-items: center;
}

.hero-section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 80px 20px;
  max-width: 1200px;
  margin: 0 auto;
  font-family: system-ui;
  color: #0b0b0b;
}

h1 {
  font-size: 48px;
  font-weight: 800;
  line-height: 1.15;
  margin: 0 0 10px;
}

h2 {
  font-size: 24px;
}

p {
  font-size: 16px;
}

@media screen and (width < 750px) {
  .hero-section {
    padding: 40px 20px;
  }

  h1 {
    font-size: 36px;
  }

  .cta-button {
    width: 100%;
    max-width: 20em;
  }
}

@media screen and (max-width: 480px) {
  h1 {
    font-size: 28px;
  }
  
  .hero-section {
    padding: 30px 15px;
  }
}

.hero-icon {
  height: 8em;
  width: 8em;
  margin: 0 0 2em 0;
}

.hero-section span {
  color: #ff4500;
}

.hero-description {
  max-width: 600px;
  color: #6c7a89;
  margin-bottom: 30px;
  line-height: 1.5;
  font-size: 18px;
}

.cta-button {
  display: inline-block;
  text-align: center;
  background-color: #0b0b0b;
  color: white;
  padding: 15px 30px;
  width: 15em;
  border: none;
  border-radius: 1000px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.cta-button:hover {
  background-color: #ff4500;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 69, 0, 0.2);
}
</style>