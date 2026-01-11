<template>
  <div class="task-item">
    <div class="task-main">
      <div class="task-header">
        <span class="task-status" :class="statusClass">
          {{ statusText }}
        </span>
      </div>

      <h2>{{ task.title }}</h2>
      <p>{{ task.description }}</p>
    </div>

    <div class="task-buttons">
      <button class="pill-btn done" @click="$emit('toggle', task)">
        {{ task.completed ? 'Undo' : 'Mark done' }}
      </button>

      <button class="pill-btn edit" @click="$emit('edit', task)">
        Edit
      </button>

      <button class="pill-btn delete" @click="$emit('delete', task.id)">
        Delete
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  task: {
    type: Object,
    required: true
  }
})

defineEmits(['delete', 'toggle', 'edit'])

const statusText = computed(() =>
  props.task.completed ? 'done' : 'pending'
)

const statusClass = computed(() =>
  props.task.completed ? 'done' : 'pending'
)
</script>

<style scoped>
.task-item {
  background: white;
  padding: 28px;
  border-radius: 24px;
  border: 1px solid #eee;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all 0.3s ease;
  font-family: system-ui, -apple-system, sans-serif;
}

.task-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.04);
}

.task-main h2 {
  font-size: 22px;
  font-weight: 800;
  color: #0b0b0b;
  margin: 15px 0 10px;
  line-height: 1.2;
}

.task-main p {
  font-size: 16px;
  color: #6c7a89;
  line-height: 1.5;
  margin-bottom: 25px;
}

.task-status {
  font-size: 11px;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 4px 12px;
  border-radius: 1000px;
  display: inline-block;
}

.task-status.pending {
  background: #fff0eb;
  color: #ff4500;
}

.task-status.done {
  background: #f0fdf4;
  color: #16a34a;
}

.task-buttons {
  display: flex;
  gap: 12px;
}

.pill-btn {
  flex: 1;
  padding: 12px;
  border-radius: 1000px;
  font-weight: 700;
  font-size: 14px;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 1px solid #0b0b0b;
  background: white;
  color: #0b0b0b;
}

.pill-btn.done:hover {
  background: #ff4500;
  color: white;
  border-color: #ff4500;
  box-shadow: 0 4px 12px rgba(255, 69, 0, 0.2);
}

.pill-btn.edit {
  border-color: #0b0b0b;
  color: #0b0b0b;
}

.pill-btn.edit:hover {
  background: #0b0b0b;
  color: white;
  border-color: #0b0b0b;
}

.pill-btn.delete {
  border-color: transparent;
  color: #6c7a89;
}

.pill-btn.delete:hover {
  background: #fee2e2;
  color: #dc2626;
}
</style>