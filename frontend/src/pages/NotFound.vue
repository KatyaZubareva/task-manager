<template>
    <div class="main-info hero-section">
      <img class="error-icon" src="./../assets/404.png"></img>
  
      <h1>
        Oops! The page disappeared<br>
        <span>in a puff of smoke.</span>
      </h1>
  
      <p class="description">
        Maybe it’ll reappear later.
      </p>
  
      <router-link to="/">
        <button class="cta-button">
            Back to the real world
        </button>
      </router-link>
    </div>
</template>
<style scoped>
:root {
  --accent-color: #ff4500;
  --btn-color: #0b0b0b;
  --text-color: #0b0b0b;
  --bg-color: #fcfcfc;
}

.hero-section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 80px 20px;
  
  font-family: system-ui;
  color: var(--text-color);
}

.error-icon {
    height: 15em;
    width: 20em;
}

.hero-section h1 {
  font-size: 3.5em;
  font-weight: 800;
  line-height: 1.15;
  margin: 0 0 20px 0;
}

.hero-section span {
  color: var(--accent-color);
}

.description {
  max-width: 600px;
  font-size: 1.2em;
  color: #6c7a89;
  margin-bottom: 30px;
  line-height: 1.5;
}

.cta-button {
  background-color: var(--btn-color);
  color: white;
  border: none;
  padding: 15px 30px;
  font-size: 1.1em;
  font-weight: bold;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.cta-button:hover {
  background-color: #0d0d0d;
  transform: translateY(-2px);
}
</style>
