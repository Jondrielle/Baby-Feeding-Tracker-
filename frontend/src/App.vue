<!-- src/App.vue -->
<template>
  <div>
    <h1>Baby Feeding Tracker</h1>
    <button @click= "createFeeding">Create Feed Entry</button>

    <!-- List of Feedings -->
    <ul>
      <li v-for="feeding in feedings" :key="feeding.id">
        {{feeding.time}} - 
        {{feeding.amount_ml !== null && feeding.amount_ml !== undefined ? feeding.amount_ml : 'N/A'}} ml 
        {{feeding.amount_oz !== null && feeding.amount_oz !== undefined ? feeding.amount_oz : 'N/A'}} oz - {{feeding.method}} - {{feeding.notes || '' }} 
      </li>
    </ul>


  </div>
</template>

<script setup>
import {ref, onMounted} from 'vue'

const feedings = ref([])

const feedingEntry = ref({
  time:'',
  amount_ml:'',
  amount_oz:'',
  method:'',
  notes:''
})

onMounted(async () => {
  const res = await fetch('http://localhost:8000/feedings')
  feedings.value = await res.json()
})

async function createFeeding(){
  const res = await fetch('http://localhost:8000/feeding', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(feedingEntry.value)
  })
  const newFeeding = await res.json()
  feedings.value.push(newFeeding)
  feedingData.value = { time: '', amount_ml: '', amount_oz: '', method: '', notes: '' }
}

</script>

<style>
/* Optional global styles */
</style>
