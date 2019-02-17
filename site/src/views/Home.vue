<template>
  <div class="home-center">
    <!-- Large intro text -->
    <div class="font-weight-medium display-3"></div>
    <img src="../assets/logo_transparent.png" height=400 width=400/>
    <!-- Sub text -->
    <div class="font-weight-thin headline">Immediately gather real data on advertisements and posters!</div>

    <!-- Actions/buttons -->
    <v-btn to="/survey">Start New Survey</v-btn>
    <v-btn to="/listing">View Past Results</v-btn>
    
  </div>
</template>

<script>
  export default {}
</script>

<style>
.home-center {
  text-align: center;
}
.display-3 {
  margin-top: 15px;
}
.headline {
  margin: 20px;
}
</style>
