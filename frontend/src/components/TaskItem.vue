<template>
  <div class="task-item">
    <div class="task-main">
      <span class="task-status" :class="statusClass">
        {{ statusText }}
      </span>

      <h2>{{ task.title }}</h2>
      <p>{{ task.description }}</p>
    </div>

    <div class="task-buttons">
      <button class="pill-btn done" @click="$emit('toggle', task)">
        {{ task.completed ? 'Undo' : 'Mark done' }}
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

defineEmits(['delete', 'toggle'])

const statusText = computed(() =>
  props.task.completed ? 'done' : 'pending'
)

const statusClass = computed(() =>
  props.task.completed ? 'done' : 'pending'
)
</script>
