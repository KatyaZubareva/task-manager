<template>
    <div class="task-item" v-for="task in tasks" :key="task.id">
          
        <div class="task-main">
            <span class="task-status" :class="task.statusClass">{{ statusbar }}</span>
  
            <h2>{{ header }}</h2>
            <p>{{ description }}</p>
        </div>
  
        <div class="task-buttons">
            <button class="pill-btn done">Mark done</button>
            <button class="pill-btn delete">Delete</button>
        </div>
  
    </div>
</template>
  
<script setup>

const props = defineProps({
    statusbar: 'pending',
    header: String,
    description: String
})
  
</script>
  
<style scoped>

.task-item {
    background: #ffffff;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 6px 22px rgba(0,0,0,0.06);
    transition: 0.25s ease;
}
  
.task-item:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 28px rgba(0,0,0,0.08);
}
  
.task-main h2 {
    margin: 6px 0 8px;
}
  
.task-main p {
    color: #606b75;
}
  
.task-status {
    display: inline-block;
    padding: 5px 14px;
    border-radius: 50px;
    font-size: 0.8em;
    font-weight: 600;
    margin-bottom: 8px;
}
  
.pending { background: #ffe1cd; color: #b53800; }
.progress { background: #cfe7ff; color: #0054b8; }
.review { background: #fff3c9; color: #a88a00; }
.blocked { background: #ffd2d2; color: #9f1e1e; }
.done { background: #dff5d8; color: #1e7c22; }
  
.task-buttons {
    margin-top: 18px;
    display: flex;
    gap: 12px;
}
  
.pill-btn {
    border: none;
    padding: 10px 22px;
    border-radius: 50px;
    font-size: 0.95em;
    cursor: pointer;
    transition: 0.2s;
    font-weight: 500;
    color: white;
}
  
.pill-btn.done {
    background: #ff4500;
}
.pill-btn.done:hover {
    background: #e03f00;
}
  
.pill-btn.delete {
    background: #d9534f;
}

.pill-btn.delete:hover {
    background: #c74745;
}

</style>
  