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
    <v-layout align-start justify-space-around row fill-height wrap>
    <v-flex md2>
     <v-card>
        <img src="../assets/ACVLogo.jpg" height="160" width="160"/>
        <v-card-actions>
          <v-btn flat color="black">Go to Survey</v-btn>
        </v-card-actions>
    </v-card>
    </v-flex>
     <v-flex md2>
       <v-card>
        <img src="../assets/constellationLogo.jpg" height="160" width="160"/>
        <v-card-actions>
          <v-btn flat color="black">Go to Survey</v-btn>
        </v-card-actions>
      </v-card>
      </v-flex>
       <v-flex md2>
       <v-card>
        <img src="../assets/dattoLogo.jpg" height="160" width="160"/>
        <v-card-actions>
          <v-btn flat color="black">Go to Survey</v-btn>
        </v-card-actions>
      </v-card>
      </v-flex>

      <v-flex md2>
       <v-card>
        <img src="../assets/googleLogo.jpg" height="160" width="160"/>
        <v-card-actions>
          <v-btn flat color="black">Go to Survey</v-btn>
        </v-card-actions>
      </v-card>
      </v-flex>

      <v-flex md2>
       <v-card>
        <img src="../assets/readmeLogo.jpg" height="160" width="160"/>
        <v-card-actions>
          <v-btn flat color="black">Go to Survey</v-btn>
        </v-card-actions>
      </v-card>
      </v-flex>
    </v-layout>
    
    
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