<template>
  <div class="home-center">

    <!-- Large intro text -->
    <div class="font-weight-medium display-1" style="margin-top: 30px">Experience the Simplicity of Poster AI</div>
    <div class="font-weight-thin headline">General User Experience:</div>
    <div class="font-weight-thin headline">1. Choose a company below</div>
    <div class="font-weight-thin headline">2. Complete their survey</div>
    <div class="font-weight-thin headline">3. Collect your cash</div>
    
    <br>
    <br>

    <v-layout align-start justify-space-around row wrap>
      <v-card  v-for="url in urls" style="width: 240px; height: 240px; margin: auto; margin-bottom: 30px;">
        <v-card-media style="height: 160px; display: flex; justify-content: center; align-items: center">
          <img :src="url" style="max-height: 160px; max-width: 160px"/>
        </v-card-media>
        <v-card-actions>
          <v-btn flat color="black" style="margin: auto">Start Survey</v-btn>
        </v-card-actions>
      </v-card>
    </v-layout>
    
    <!-- Solutions -->
    <div class="font-weight-medium display-1" style="margin-top: 30px; margin-bottom: 5px">Opportunities and Solutions</div>
    <div v-for="item in solutions" class="font-weight-thin headline" style="text-align: center">
      {{item}}
    </div>
    
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
        ],
        solutions: [
          'Supplement the results of your cognitive walkthroughs and end-user testing with automated '
          + 'quantitative data gathering, backed by cutting edge AI.',
          'Explore new avenues of data gathering and user testing.',
          'Quickly view and share the results of your tests with any major web browser.',
          'Interactive data visualization available without any extra work.'
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
  margin: 15px;
  margin-top: 10px;
}
</style>