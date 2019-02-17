<template>
  <div class="home-center">
    <!-- Large intro text -->
    <div class="font-weight-medium display-3">Experince the Simplicity of Poster AI</div>
    <!-- Sub text -->
    <br>
    <div class="font-weight-thin headline">The User Experience: <br>
    1. Choose a company below<br>
    2. Complete their survey<br>
    3. Collect your cash
    </div>
    <br>
    <br>
    <br>

    <v-layout align-start justify-space-around row wrap>
      <v-card  v-for="url in urls" style="width: 240px; height: 240px; margin: auto; margin-bottom: 30px;">
        <v-card-media style="height: 160px; display: flex; justify-content: center; align-items: center">
          <img :src="url" style="max-height: 160px; max-width: 160px"/>
        </v-card-media>
        <v-card-actions>
          <v-btn flat color="black">Go to Survey</v-btn>
        </v-card-actions>
      </v-card>
    </v-layout>
    
  </div>
</template>

<script>
  export default {
    data() {
      return {
        urls: [
          require('../assets/ACVLogo.jpg'),
          require('../assets/constellationLogo.jpg'),
          require('../assets/dattoLogo.jpg'),
          require('../assets/googleLogo.jpg'),
          require('../assets/readmeLogo.jpg')
        ]
      };
    }
  }
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