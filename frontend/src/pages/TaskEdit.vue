<template>
  <TaskForm :task-id="Number($route.params.id)" />
</template>

<script setup>
import TaskForm from '@/components/TaskForm.vue'
</script>
