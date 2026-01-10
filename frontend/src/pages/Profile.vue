<template>
  <div class="profile-page">
    <div class="profile-card">
      
      <div class="profile-header">
        <div class="avatar-container">
          <img :src="user.avatar" alt="Avatar" class="avatar-img" />
          <button class="edit-avatar-btn" title="Change photo">
            <span>+</span>
          </button>
        </div>
        <h2>{{ user.name }}</h2>
        <p class="user-email">{{ user.email }}</p>
      </div>

      <hr class="divider" />

      <div class="profile-content">
        <div class="info-row">
          <label>Full Name</label>
          <div class="info-value">{{ user.name }}</div>
        </div>

        <div class="info-row">
          <label>Bio</label>
          <p class="info-text">{{ user.bio }}</p>
        </div>
      </div>

      <div class="profile-actions">
        <button class="edit-btn">Edit Profile</button>
        <button class="logout-btn" @click="handleLogout">Log Out</button>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const user = ref({
  name: 'Alex Johnson',
  email: 'alex.j@example.com',
  bio: 'Product Designer & Task Master. Helping people organize their lives more efficiently.',
  avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=Alex' // Генерация стильного аватара
})

const handleLogout = () => {
  console.log('Logging out...')
  // Логика выхода
}
</script>

<style scoped>
.profile-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #fcfcfc;
  font-family: system-ui, -apple-system, sans-serif;
  padding: 20px;
}

.profile-card {
  background: white;
  padding: 40px 35px;
  border-radius: 20px;
  width: 100%;
  max-width: 450px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.06);
  text-align: center;
}

.profile-header {
  margin-bottom: 25px;
}

.avatar-container {
  position: relative;
  width: 110px;
  height: 110px;
  margin: 0 auto 15px;
}

.avatar-img {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid #fff;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}

.edit-avatar-btn {
  position: absolute;
  bottom: 0;
  right: 0;
  background: #ff4500;
  color: white;
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  box-shadow: 0 2px 8px rgba(255, 69, 0, 0.4);
}

.profile-header h2 {
  margin: 10px 0 5px;
  font-size: 1.6em;
  color: #222;
}

.user-email {
  color: #888;
  font-size: 0.95em;
}

.divider {
  border: 0;
  border-top: 1px solid #eee;
  margin: 25px 0;
}

/* Контентная часть */
.profile-content {
  text-align: left;
}

.info-row {
  margin-bottom: 20px;
}

.info-row label {
  font-size: 0.85em;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  display: block;
  margin-bottom: 5px;
}

.info-value {
  font-weight: 500;
  color: #333;
}

.info-text {
  font-size: 0.95em;
  color: #555;
  line-height: 1.5;
}

.profile-actions {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 30px;
}

.edit-btn {
  width: 100%;
  padding: 14px;
  font-size: 1em;
  font-weight: 600;
  border-radius: 100px;
  border: none;
  color: white;
  background-color: #ff4500;
  cursor: pointer;
  transition: all 0.25s;
}

.edit-btn:hover {
  background-color: #e43f00;
  transform: translateY(-1px);
}

.logout-btn {
  width: 100%;
  padding: 12px;
  font-size: 1em;
  font-weight: 600;
  border-radius: 100px;
  border: 1px solid #ddd;
  color: #666;
  background-color: transparent;
  cursor: pointer;
  transition: all 0.2s;
}

.logout-btn:hover {
  background-color: #f5f5f5;
  color: #333;
}
</style>