<!-- src/App.vue -->
<template>
  <div>
    <h1>Baby Feeding Tracker</h1>
    <button @click= "fetchItem">Create Feed Entry</button>
  </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'

const items = ref([])

onMounted(async () => {
  const res = await fetch('http://localhost:8000/feedings')
  items.value = await res.json()
})

async function fetchItem(){
  const res = await fetch('http://localhost:8000/feeding/')
  items.value = await res.json()
}


</script>

<style>
/* Optional global styles */
</style>
