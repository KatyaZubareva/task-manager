<template>
  <div class="calendar-preview">

    <h1 class="title">Monthly Planner</h1>

    <div class="calendar-grid">

      <!-- Подписи дней недели -->
      <div class="day-name" v-for="d in dayNames" :key="d">{{ d }}</div>

      <!-- Дни месяца -->
      <div class="day-cell" v-for="n in 30" :key="n">
        <div class="day-number">{{ n }}</div>

        <!-- Превью статусов задач -->
        <div class="tasks-status">
          <span class="status pending"></span>
          <span class="status progress"></span>
          <span class="status done"></span>
        </div>

        <!-- Место для заметок -->
        <div class="day-note">
          <p>Write your notes here...</p>
        </div>
      </div>

    </div>

  </div>
</template>

<style scoped>
.calendar-preview {
  max-width: 1000px;
  margin: 0 auto;
  padding: 40px;
  font-family: system-ui;
}

/* Заголовок */
.title {
  text-align: center;
  font-size: 2.4em;
  margin-bottom: 25px;
  font-weight: 700;
  color: #2b2b2b;
}

/* GRID */
.calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 15px;
}

/* Подписи дней недели */
.day-name {
  text-align: center;
  font-weight: 600;
  color: #6b6b6b;
  padding-bottom: 8px;
  font-size: 0.95em;
  border-bottom: 1px solid #ddd;
}

/* Ячейка дня */
.day-cell {
  background: #ffffff;
  border-radius: 16px;
  padding: 12px;
  min-height: 140px;
  display: flex;
  flex-direction: column;
  border: 1px solid #e5e5e5;
  transition: 0.2s;
}

.day-cell:hover {
  border-color: #ff8a4c;
  box-shadow: 0 4px 18px rgba(255,140,78,0.15);
}

/* Номер дня */
.day-number {
  font-weight: 700;
  color: #3a3a3a;
  font-size: 1.1em;
  margin-bottom: 8px;
}

/* Статусы задач */
.tasks-status {
  display: flex;
  gap: 5px;
  margin-bottom: 8px;
}

.status {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  display: inline-block;
}

.pending { background: #ffe1cd; }
.progress { background: #cfe7ff; }
.done { background: #dff5d8; }

/* Заметка */
.day-note {
  flex-grow: 1;
  font-size: 0.85em;
  color: #666;
  overflow: hidden;
}

.day-note p {
  margin: 0;
  line-height: 1.2em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Адаптив */
@media (max-width: 900px) {
  .calendar-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

@media (max-width: 600px) {
  .calendar-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>

<script setup>
const dayNames = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"];
</script>
