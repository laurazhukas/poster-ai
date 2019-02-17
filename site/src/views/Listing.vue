<template>
  <div>
    <div  v-for="id in IDs">
      <v-btn :to="`/results/${id}`">View Previous Survey</v-btn>
      <div>{{id}}</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'listing',
  mounted() {
    // Get list of all things
    axios.get('http://34.73.42.130:8000/face').then(response => {
      let data = response.data;
      
      // Collate into list of all IDs
      for(let pt of data) { //pt.session_id
        if(!this.IDs.includes(pt.session_id)) {
          this.IDs.push(pt.session_id);
        }
      }
      // console.log(data);
      this.ready = true;
    });


  },
  data() {
    return {
      IDs: [],
      ready: false
    };
  }
}
</script>

<style>

</style>
