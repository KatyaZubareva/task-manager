<template>
  <div class="pricing-page">

    <h1>Choose your plan</h1>
    <p class="subtitle">Flexible pricing to suit your productivity needs</p>

    <div class="plans-container">

      <div class="plan-card">
        <h2>Free</h2>
        <p class="plan-price">$0<span>/month</span></p>
        <ul>
          <li>Up to 10 tasks</li>
          <li>Basic task tracking</li>
          <li>Email support</li>
        </ul>
        <button class="cta-button">Get Started</button>
      </div>

      <div class="plan-card popular">
        <div class="badge">Most Popular</div>
        <h2>Pro</h2>
        <p class="plan-price">$9.99<span>/month</span></p>
        <ul>
          <li>Unlimited tasks</li>
          <li>Advanced analytics</li>
          <li>Priority support</li>
          <li>Team collaboration</li>
        </ul>
        <button class="cta-button">Upgrade Now</button>
      </div>

      <div class="plan-card">
        <h2>Enterprise</h2>
        <p class="plan-price">Custom<span>pricing</span></p>
        <ul>
          <li>Custom features</li>
          <li>Dedicated support</li>
          <li>Advanced security</li>
          <li>Team management tools</li>
        </ul>
        <button class="cta-button">Contact Us</button>
      </div>

    </div>

  </div>
</template>

<script setup>
</script>

<style scoped>
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

.pricing-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 80px 20px;
  font-family: system-ui;
  color: #0b0b0b;
  background: #f9f9f9;
  min-height: 100vh;
  margin-top: 0;
}

.subtitle {
  color: #6c7a89;
  margin-bottom: 50px;
  font-size: 16px;
}

.plans-container {
  display: flex;
  gap: 30px;
  flex-wrap: wrap;
  justify-content: center;
}

.plan-card {
  background: white;
  padding: 40px 30px;
  border-radius: 20px;
  width: 300px;
  position: relative;
  box-shadow: 0 10px 25px rgba(0,0,0,0.05);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.plan-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 18px 35px rgba(0,0,0,0.1);
}

.plan-card.popular {
  border: 2px solid #ff4500;
}

.badge {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: #ff4500;
  color: white;
  font-size: 12px;
  font-weight: 600;
  padding: 5px 12px;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.plan-price {
  font-size: 24px;
  font-weight: 700;
  margin: 15px 0;
  color: #0b0b0b;
}

.plan-price span {
  font-size: 16px;
  color: #6c7a89;
}

.plan-card ul {
  list-style: none;
  padding: 0;
  margin: 25px 0;
  color: #6c7a89;
}

.plan-card ul li {
  margin-bottom: 12px;
}

.cta-button {
  display: inline-block;
  text-align: center;
  background: linear-gradient(135deg, #ff4500, #ff6a2c);
  color: white;
  padding: 14px 0;
  width: 100%;
  border: none;
  border-radius: 1000px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.cta-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 15px rgba(255,69,0,0.4);
}

@media screen and (max-width: 950px) {
  .plans-container {
    flex-direction: column;
    gap: 25px;
    align-items: center;
  }
}
</style>
