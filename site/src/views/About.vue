<template>
  <div class="about">
    <br>
    <h1>The Developers Behind Poster AI</h1>
    <br>
    <v-layout align-start justify-space-around row wrap>
    <v-flex md2 v-for="student in team">
     <v-card style="max-width: 300px; margin: auto; margin-bottom: 20px;">
        <v-card-media>
          <img :src="student.img"/>
        </v-card-media>
        <v-card-text>
          <h3 class="headline mb-0">{{student.name}}</h3>
          <div>{{student.school}}<br>{{student.major}}<br>{{student.interests}}</div>
        </v-card-text>
      </v-card>
      </v-flex>
    </v-layout>
    
    <br>
    <h1>Our Tech Stack</h1>
    <p class="font-weight-thin title" style="margin-bottom: 35px;">We used Vue.js for the frontend to first gather data from the user. 
      Then, using Azure's cognitive services we analyzed the emotions the user displayed while looking at the posters. 
      This was integrated into a python and mongo DB backend. The results were then sent back to be processed and 
      displayed in the results section.
    </p>

    <h1>Thank you Brickhacks and Sponsors!</h1>
    <p class="font-weight-thin title">A huge thanks goes out to Brickhacks and the organizing team for putting together such a great event!
      Thanks to all the sponsors that contirbuted to the success of the event and all the mentors that took part
      and helped with our hack.
    </p>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        team: [
          {name: 'Sri K. Nellutla', img: require('../assets/sri.jpg'),
            school: 'University of Waterloo', major: '2nd Year Software Engineering Student', interests: 'Interests: Backend dev and ML'},
          { name: 'Robert Nill', img: require('../assets/robert.jpg'),
            school: 'Rochester Institute of Technology', major: '4th Year SE/CS BS/MS', interests: 'Interests: Frontend, Graphics & Rendering, AI'},
          { name: 'Sujan Sube', img: require('../assets/sujan.jpg'),
            school: 'University of Waterloo', major: '2nd Year Machine Learning Masters Student', interests: 'Interests:  ML in Healthcare'},
          { name: 'Laura Zhukas', img: require('../assets/laura.jpg'),
            school: 'University of Waterloo', major: '2nd Year Biomedical Engineering Student', interests: 'Interests:Full-stack dev and ML'},
        ]
      };
    }
  }
</script>

<style>
.about {
  text-align: center;
}
</style>

