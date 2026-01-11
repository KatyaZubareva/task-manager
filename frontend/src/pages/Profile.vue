<template>
  <div class="profile-page">
    <div class="profile-card">
      
      <div class="profile-header">
        <h2>{{ user.name || 'User' }}</h2>
        <p class="user-email">{{ user.email }}</p>
      </div>

      <hr class="divider" />

      <div v-if="!isEditing" class="profile-content">
        <div class="info-row">
          <label>Full Name</label>
          <div class="info-value">{{ user.name || 'Not set' }}</div>
        </div>

        <div class="info-row">
          <label>Email</label>
          <div class="info-value">{{ user.email }}</div>
        </div>

        <div class="info-row">
          <label>Bio</label>
          <p class="info-text">{{ user.bio || 'No bio yet' }}</p>
        </div>
      </div>

      <div v-else class="profile-edit">
        <form @submit.prevent="saveProfile">
          <div class="input-group">
            <label>Full Name</label>
            <input 
              type="text" 
              v-model="editForm.name" 
              placeholder="Enter your name"
              class="form-input"
            />
          </div>

          <div class="input-group">
            <label>Bio</label>
            <textarea 
              v-model="editForm.bio" 
              placeholder="Tell us about yourself"
              class="form-textarea"
              rows="4"
            ></textarea>
          </div>

          <div class="form-actions">
            <button type="button" class="cancel-btn" @click="cancelEdit">Cancel</button>
            <button type="submit" class="save-btn">Save Changes</button>
          </div>
        </form>
      </div>

      <div v-if="!isEditing" class="profile-actions">
        <button class="edit-btn" @click="startEdit">Edit Profile</button>
        <button class="logout-btn" @click="handleLogout">Log Out</button>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const user = ref({
  name: '',
  email: '',
  bio: ''
})

const isEditing = ref(false)
const editForm = ref({
  name: '',
  bio: ''
})

const loadProfile = async () => {
  const token = localStorage.getItem('token')
  if (!token) {
    router.push('/login')
    return
  }

  try {
    const res = await fetch('http://localhost:8000/api/user/me', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    if (!res.ok) {
      throw new Error('Failed to load profile')
    }

    const data = await res.json()
    user.value = {
      name: data.name || '',
      email: data.email || '',
      bio: data.bio || ''
    }
  } catch (error) {
    console.error('Error loading profile:', error)
    const email = localStorage.getItem('email')
    user.value = {
      name: 'User',
      email: email || '',
      bio: ''
    }
  }
}

const startEdit = () => {
  editForm.value = {
    name: user.value.name || '',
    bio: user.value.bio || ''
  }
  isEditing.value = true
}

const cancelEdit = () => {
  isEditing.value = false
  editForm.value = {
    name: '',
    bio: ''
  }
}

const saveProfile = async () => {
  const token = localStorage.getItem('token')
  if (!token) {
    router.push('/login')
    return
  }

  try {
    const res = await fetch('http://localhost:8000/api/user/me', {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`
      },
      body: JSON.stringify({
        name: editForm.value.name || null,
        bio: editForm.value.bio || null
      })
    })

    if (!res.ok) {
      throw new Error('Failed to update profile')
    }

    await loadProfile()
    isEditing.value = false
  } catch (error) {
    console.error('Error saving profile:', error)
    alert('Failed to save profile. Please try again.')
  }
}

const handleLogout = () => {
  localStorage.removeItem('token')
  localStorage.removeItem('email')
  router.push('/login')
}

onMounted(() => {
  loadProfile()
})
</script>


<style scoped>
.profile-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #f9fafb;
  font-family: system-ui, -apple-system, sans-serif;
  padding: 20px;
  margin-top: 5em;
}

.profile-card {
  background: white;
  padding: 40px 35px;
  border-radius: 20px;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.06);
  text-align: center;
}

.profile-header {
  margin-bottom: 25px;
}

.profile-header h2 {
  margin: 0 0 5px;
  font-size: 24px;
  color: #222;
  font-weight: 700;
}

.user-email {
  color: #888;
  font-size: 16px;
  margin: 0;
}

.divider {
  border: 0;
  border-top: 1px solid #eee;
  margin: 25px 0;
}

.profile-content {
  text-align: left;
}

.info-row {
  margin-bottom: 20px;
}

.info-row label {
  font-size: 14px;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
}

.info-value {
  font-weight: 500;
  color: #333;
  font-size: 16px;
}

.info-text {
  font-size: 16px;
  color: #555;
  line-height: 1.5;
  margin: 0;
}

.profile-edit {
  text-align: left;
}

.input-group {
  margin-bottom: 20px;
}

.input-group label {
  display: block;
  margin-bottom: 8px;
  color: #333;
  font-weight: 600;
  font-size: 14px;
}

.form-input,
.form-textarea {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 16px;
  font-family: inherit;
  outline: none;
  transition: border-color 0.2s;
  box-sizing: border-box;
}

.form-input:focus,
.form-textarea:focus {
  border-color: #ff4500;
}

.form-textarea {
  resize: vertical;
  min-height: 100px;
}

.form-actions {
  display: flex;
  gap: 12px;
  margin-top: 25px;
}

.cancel-btn,
.save-btn {
  flex: 1;
  padding: 12px;
  border-radius: 100px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.25s;
  border: none;
}

.cancel-btn {
  background-color: #f5f5f5;
  color: #666;
}

.cancel-btn:hover {
  background-color: #e8e8e8;
}

.save-btn {
  background-color: #ff4500;
  color: white;
}

.save-btn:hover {
  background-color: #e43f00;
  transform: translateY(-1px);
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
  font-size: 16px;
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
  font-size: 16px;
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