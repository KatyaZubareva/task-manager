<template>
  <div class="hero-main hero-section">
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
</template>

<style scoped>

.hero-section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 80px 20px;
  margin-top: 5em;
  font-family: system-ui;
  color: #0b0b0b;
}

@media screen and (width < 750px) {
  .hero-section {
    margin-top: 2em;
  }

  .hero-cta-button {
    width: 20em;
  }
}

.hero-icon {
  height: 8em;
  width: 8em;
}

.hero-section h1 {
  font-size: 3.5em;
  font-weight: 800;
  line-height: 1.15;
  margin: 0 0 20px;
}

.hero-section span {
  color: #ff4500;
}

.hero-description {
  max-width: 600px;
  font-size: 1.2em;
  color: #6c7a89;
  margin-bottom: 30px;
  line-height: 1.5;
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
  font-size: 1.1em;
  font-weight: bold;
  cursor: pointer;

  transition: background-color 0.3s ease, transform 0.2s ease;
}

.cta-button:hover {
  background-color: #0d0d0d;
  transform: translateY(-2px);
}

</style>
