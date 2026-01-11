<template>
  <div class="layout-card">
    <!-- Обычный слот -->
    <div class="card-header">
      <slot name="header">
        <h2>Default Header</h2>
      </slot>
    </div>

    <!-- Именованный слот -->
    <div class="card-content">
      <slot name="content">
        <p>Default content</p>
      </slot>
    </div>

    <!-- Слот с ограниченной областью видимости (scoped slot) -->
    <div class="card-footer">
      <slot name="footer" :message="footerMessage" :count="itemCount">
        <p>Default footer: {{ footerMessage }}</p>
      </slot>
    </div>

    <!-- Обычный слот без имени (default) -->
    <div class="card-body">
      <slot>
        <p>Default body content</p>
      </slot>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const footerMessage = ref('Task Manager Footer')
const itemCount = ref(0)
</script>

<style scoped>
.layout-card {
  background: white;
  border-radius: 16px;
  padding: 24px;
  border: 1px solid #eee;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.card-header {
  margin-bottom: 16px;
  padding-bottom: 16px;
  border-bottom: 1px solid #eee;
}

.card-content {
  margin-bottom: 16px;
}

.card-footer {
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid #eee;
  font-size: 14px;
  color: #6c7a89;
}

.card-body {
  margin: 16px 0;
}
</style>
