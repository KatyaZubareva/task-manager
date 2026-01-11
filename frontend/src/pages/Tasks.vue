<template>
  
  <div class="calendar-wrapper">
      <div class="calendar-container">
        <div class="hero-main hero-section">

        <h1>
          Where planning feels<br />
          <span>effortless</span>
        </h1>

        <p class="hero-description">
          Plan your tasks, track progress, and clear your mind from daily chaos.
          Everything in its place, every day under control.
        </p>

        <router-link to="/login">
          <button class="cta-button">Try now</button>
        </router-link>
      </div>
      <header class="calendar-header">
        <div class="header-left">
          <h1 class="calendar-title">January 2026</h1>
          <span class="calendar-subtitle">
            <span class="dot"></span> 12 active tasks
          </span>
        </div>
        <div class="header-actions">
          <div class="view-switches">
            <button class="btn-view active">Month</button>
            <button class="btn-view">Week</button>
          </div>
          <button class="btn-today">Today</button>
        </div>
      </header>

      <div class="calendar-grid">
        <div 
          v-for="d in dayNames" 
          :key="d" 
          class="day-name"
          :class="{ 'is-weekend': d === 'Sat' || d === 'Sun' }"
        >
          {{ d }}
        </div>

        <div v-for="empty in startOffset" :key="'empty-'+empty" class="day-cell empty"></div>

        <div 
          v-for="n in 31" 
          :key="n" 
          class="day-cell"
          :class="{ 
            'is-today': n === 10, 
            'is-weekend': isWeekend(n) 
          }"
        >
          <div class="day-header">
            <span class="day-number">{{ n }}</span>
            <button class="add-task-btn">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                <line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line>
              </svg>
            </button>
          </div>

          <div class="day-content">
            <div v-if="n % 4 === 0" class="task-card">
              <div class="task-info">
                <span class="task-dot"></span>
                <span class="task-text">Design review</span>
              </div>
              <div class="mini-progress">
                <div class="mini-progress-fill" :style="{ width: '70%' }"></div>
              </div>
            </div>
            
            <div v-if="n === 10" class="task-card meeting">
              <span class="task-text">📞 Daily Standup</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const dayNames = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
const startOffset = 0;

const isWeekend = (day) => {
  const dayOfWeek = (day + startOffset - 1) % 7;
  return dayOfWeek === 5 || dayOfWeek === 6;
};
</script>

<style scoped>

h1 {
  font-size: 48px;
}

h2 {
  font-size: 24px;
}

p {
  font-size: 16px;
}

.hero-section {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 80px 20px;
  margin-top: 2em;
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
  margin: 2em 0 2em 0;
}

.hero-section h1 {
  font-weight: 800;
  line-height: 1.15;
  margin: 0 0 10px;
}

.hero-section span {
  color: #ff4500;
}

.hero-description {
  max-width: 600px;
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
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;

  transition: background-color 0.3s ease, transform 0.2s ease;
}

.cta-button:hover {
  background-color: #0d0d0d;
  transform: translateY(-2px);
}

.calendar-wrapper {
  padding-top: 100px;
  min-height: 100vh;
  background-color: #f9fafb;
  font-family: system-ui, -apple-system, sans-serif;
}

.calendar-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px 40px;
}

.calendar-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 24px;
}

.calendar-title {
  font-size: 32px;
  font-weight: 800;
  margin: 0;
  color: #000;
}

.calendar-subtitle {
  color: #666;
  font-size: 14px;
  display: flex;
  align-items: center;
  gap: 6px;
  margin-top: 4px;
}

.dot {
  width: 8px;
  height: 8px;
  background: #ff4500;
  border-radius: 50%;
}

.header-actions {
  display: flex;
  gap: 12px;
}

.view-switches {
  background: #eee;
  padding: 4px;
  border-radius: 12px;
  display: flex;
}

.btn-view {
  border: none;
  background: none;
  padding: 6px 16px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  color: #666;
}

.btn-view.active {
  background: white;
  color: black;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.btn-today {
  padding: 10px 20px;
  border-radius: 12px;
  border: 1px solid #e8e8e8;
  background: white;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.btn-today:hover {
  border-color: #ff4500;
  color: #ff4500;
}

.calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 1px; 
  background: #e8e8e8;
  border: 1px solid #e8e8e8;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0,0,0,0.03);
}

.day-name {
  background: #fff;
  padding: 16px 0;
  text-align: center;
  font-weight: 700;
  font-size: 12px;
  color: #999;
  text-transform: uppercase;
}

.day-cell {
  background: #fff;
  min-height: 140px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  transition: background 0.2s;
}

.day-cell.empty { background: #fdfdfd; }

.day-cell:hover:not(.empty) {
  background: #fffcfb;
}

.day-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
}

.day-number {
  font-weight: 600;
  font-size: 16px;
}

.is-today {
  background: #fff5f2 !important;
}

.is-today .day-number {
  color: #ff4500;
  background: white;
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  box-shadow: 0 2px 6px rgba(255, 69, 0, 0.2);
}

.is-weekend { color: #ff4500; }
.day-cell.is-weekend { background: #fafafa; }

.add-task-btn {
  opacity: 0;
  width: 28px;
  height: 28px;
  border-radius: 8px;
  border: none;
  background: #000;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: 0.2s;
}

.day-cell:hover .add-task-btn {
  opacity: 1;
}

.add-task-btn:hover {
  background: #ff4500;
  transform: scale(1.1);
}

.task-card {
  background: white;
  border: 1px solid #eee;
  padding: 8px;
  border-radius: 10px;
  margin-bottom: 6px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.02);
  cursor: pointer;
}

.task-card.meeting {
  border-left: 3px solid #ff4500;
  background: #fff9f7;
}

.task-info {
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 4px;
}

.task-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #4caf50;
}

.task-text {
  font-size: 11px;
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.mini-progress {
  height: 3px;
  background: #eee;
  border-radius: 10px;
}

.mini-progress-fill {
  height: 100%;
  background: #4caf50;
  border-radius: 10px;
}

@media (max-width: 800px) {
  .calendar-grid { grid-template-columns: repeat(1, 1fr); }
  .day-name { display: none; }
  .day-cell { min-height: auto; border-bottom: 1px solid #eee; }
  .calendar-header { flex-direction: column; align-items: flex-start; gap: 16px; }
}
</style>